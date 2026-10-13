"""app.py - Reactive marimo app for this project.

Marimo adds reactive controls.
Every function below is a marimo cell.

RUN LOCALLY:

  uv run marimo edit app.py     # edit
  uv run marimo run  app.py     # run as an app (CTRL+c quits)

WASM DEPENDENCIES:

Under WebAssembly (emscripten) the browser has no project environment.
This app uses polars in addition to marimo, so the first cell installs
polars with micropip when running under WASM.

NO LOGGING:

A browser-based WASM app has no persistent Python server to store log files,
so this notebook configures no logging.

PLAN CELLS FIRST

1. Imports (installs WASM deps, returns shared imports and constants)
2. Opening title and introduction (Markdown)
3. Load raw metrics and design signals (same cell handles local and WASM
   environments, via cintel.utils_system)
4. Column picker (which signal to inspect)
5. Show summary stats for the chosen column
6. Show the full signals table, sorted by the chosen column
7. Closing (Markdown)

Note: marimo triggers @app.cell functions automatically; we never call them.
The names starting with "_" are for our own organization; the engine ignores
them.
"""

# === ONLY THIS AT THE TOP OF THE FILE ===

import marimo

__generated_with = "0.25.0"

app = marimo.App(width="medium")

# === FIRST CELL IMPORTS AND RETURNS DEPENDENCIES TO MAKE IT SELF-CONTAINED ===


@app.cell
async def _():
    import sys

    if sys.platform == "emscripten":
        import micropip

        await micropip.install("polars")

    import marimo as mo
    import polars as pl

    from cintel.utils_system import design_signals, load_system_metrics

    return design_signals, load_system_metrics, mo, pl, sys


# === TITLE AND INTRODUCTION ===


@app.cell
def _(mo):
    mo.md(r"""
    # Signal Design

    Raw metrics (`requests`, `errors`, `total_latency_ms`) aren't always
    the most useful thing to look at. This app derives signals from them
    (`error_rate`, `avg_latency_ms`, `throughput`) and lets you inspect
    which one tells the clearest story.
    """)


# === LOAD RAW METRICS AND DESIGN SIGNALS ===


@app.cell
def _(design_signals, load_system_metrics, mo, sys):
    """Load system metrics and design signals. Two environments, one cell.

    Locally, polars reads the CSV from data/.
    Under WASM (emscripten), Pyodide's open_url() fetches the CSV from
    public/ and load_system_metrics() reads it from there instead.
    """
    notebook_location = mo.notebook_location()

    if notebook_location is None:
        raise RuntimeError("Unable to determine notebook location.")

    filename = "system_metrics.csv"

    if sys.platform == "emscripten":
        from pyodide.http import open_url  # ty: ignore[unresolved-import]

        data_url = notebook_location / "public" / filename
        df = load_system_metrics(open_url(str(data_url)))
    else:
        data_path = notebook_location.parents[1] / "data" / filename
        df = load_system_metrics(data_path)

    signals_df = design_signals(df)
    return (signals_df,)


# === COLUMN PICKER ===


@app.cell
def _(mo, signals_df):
    column_picker = mo.ui.dropdown(
        options=signals_df.columns,
        value="error_rate",
        label="Column to inspect",
    )
    column_picker  # noqa: B018 (marimo often uses standalone expressions)
    return (column_picker,)


# === SUMMARY STATS FOR THE CHOSEN COLUMN ===


@app.cell
def _(column_picker, mo, signals_df):
    col = column_picker.value
    stats = signals_df.select(col).describe()
    mo.vstack(
        [
            mo.md(f"**Summary for `{col}`:**"),
            mo.ui.table(stats),
        ]
    )


# === FULL SIGNALS TABLE, SORTED BY THE CHOSEN COLUMN ===


@app.cell
def _(column_picker, mo, signals_df):
    mo.ui.table(signals_df.sort(column_picker.value, descending=True))


# === TYPICALLY END WITH A MARKDOWN SOURCE LINK AND CLOSING ===


@app.cell
def _(mo):
    mo.md(r"""
    ---
    [😊 Learn more at marimo.io](https://marimo.io/)
    ---

    **Running locally?**
    To stop the app, click in the VS Code terminal,
    then press **CTRL** and **c** together (CTRL+c).
    When it asks "Are you sure you want to quit? (y/N)",
    type **y** and press **Enter**.
    ---
    """)


if __name__ == "__main__":
    app.run()
