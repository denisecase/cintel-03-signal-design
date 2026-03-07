"""
signal_design_case.py - Project script (example).

Author: Denise Case
Date: 2026-02

System Metrics Data

- Data is taken from a system that records operational metrics.
- The data is structured and static for this example.
- Each row represents one observation of system behavior.
- The CSV file includes these columns:
  - requests: number of requests handled
  - errors: number of failed requests
  - total_latency_ms: total response time in milliseconds

Purpose

- Read system metrics from a CSV (comma-separated values) file.
- Design useful signals from the raw measurements.
- Save the resulting signals as a new CSV artifact.
- Log the pipeline process to assist with debugging and transparency.

Questions to Consider

- What should we measure to understand system behavior?
- Which signals are more informative than the raw input values?
- How can derived signals help us detect problems more clearly?

Paths (relative to repo root)

    INPUT FILE: data/system_metrics_case.csv
    OUTPUT FILE: artifacts/signals_case.csv

Terminal command to run this file from the root project folder

    uv run python -m cintel.signal_design_case

OBS:
  Don't edit this file - it should remain a working example.
  Use as much of this code as you can when creating your own pipeline script,
  and change the logic to create signals that make sense for your project.
"""

# === DECLARE IMPORTS (packages we will use in this project) ===

# First from the Python standard library (no installation needed)
import logging
from pathlib import Path
from typing import Final

import polars as pl
from datafun_toolkit.logger import get_logger, log_header, log_path

# === CONFIGURE LOGGER ONCE PER MODULE (FILE) ===

LOG: logging.Logger = get_logger("P3", level="DEBUG")

# === DECLARE GLOBAL CONSTANTS FOR FOLDER PATHS (directories) ===

ROOT_DIR: Final[Path] = Path.cwd()
DATA_DIR: Final[Path] = ROOT_DIR / "data"
ARTIFACTS_DIR: Final[Path] = ROOT_DIR / "artifacts"

# === DECLARE GLOBAL CONSTANTS FOR FILE PATHS ===

DATA_FILE: Final[Path] = DATA_DIR / "system_metrics_case.csv"
OUTPUT_FILE: Final[Path] = ARTIFACTS_DIR / "signals_case.csv"


# === DEFINE THE MAIN FUNCTION ===

def main() -> None:
    """Run the pipeline.

    log_header() logs a standard run header.
    log_path() logs repo-relative paths (privacy-safe).
    """
    log_header(LOG, "CINTEL")

    LOG.info("========================")
    LOG.info("START main()")
    LOG.info("========================")

    # Log the constants to help with debugging and transparency.
    log_path(LOG, "ROOT_DIR", ROOT_DIR)
    log_path(LOG, "DATA_FILE", DATA_FILE)
    log_path(LOG, "OUTPUT_FILE", OUTPUT_FILE)

    # Call the mkdir() method to ensure it exists
    # The parents=True argument allows it to create any necessary parent directories.
    # The exist_ok=True argument prevents an error if the directory already exists.
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)

    log_path(LOG, "ARTIFACTS_DIR", ARTIFACTS_DIR)

    # ----------------------------------------------------
    # STEP 1: READ CSV DATA FILE INTO A POLARS DATAFRAME (TABLE)
    # ----------------------------------------------------
    # Polars is great for tabular data.
    # We will use the polars package to
    # read CSV (comma-separated values) files
    # into a two-dimensional table called a DataFrame.

    # Call the Polars library read_csv() method.
    # Pass in (provide) the DATA_FILE path of the CSV file.
    # Name the result "df" as is customary.
    df: pl.DataFrame = pl.read_csv(DATA_FILE)

    # Visually inspect the file in the data/ folder.
    # The DataFrame height attribute returns the number of rows.
    LOG.info(f"Loaded {df.height} system metric records")

    # ----------------------------------------------------
    # STEP 2: DESIGN SIGNALS FROM RAW METRICS
    # ----------------------------------------------------
    # Analysts often create derived values that are more useful than
    # the original raw columns alone.
    LOG.info("Designing signals from the raw metrics...")

    # ----------------------------------------------------
    # STEP 2.1: DEFINE A CONDITION WE CAN REUSE
    # ----------------------------------------------------
    # Only calculate per-request signals when requests > 0.
    # Use the Polars col() function to refer to a column by name.
    # This creates a boolean expression:
    # True when requests > 0, False otherwise.
    is_requests_positive: pl.Expr = pl.col("requests") > 0

    # ----------------------------------------------------
    # STEP 2.2: DEFINE THE ERROR RATE CALCULATION
    # ----------------------------------------------------
    # This creates an expression for:
    #     errors / requests
    # It is only a calculation recipe at this point.
    calculated_error_rate: pl.Expr = pl.col("errors") / pl.col("requests")

    # ----------------------------------------------------
    # STEP 2.3: DEFINE THE ERROR RATE SIGNAL RECIPE
    # ----------------------------------------------------
    # A signal recipe tells Polars how to build a new column.
    # If requests > 0, use errors / requests.
    # Otherwise, use 0.0.
    # Name the new column "error_rate".
    error_rate_signal_recipe: pl.Expr = (
        pl.when(is_requests_positive)
        .then(calculated_error_rate)
        .otherwise(0.0)
        .alias("error_rate")
    )

    # ----------------------------------------------------
    # STEP 2.4: DEFINE THE AVERAGE LATENCY CALCULATION
    # ----------------------------------------------------
    # This creates an expression for:
    #     total_latency_ms / requests
    # Again, this is only a calculation recipe so far.
    calculated_avg_latency: pl.Expr = (
        pl.col("total_latency_ms") / pl.col("requests")
    )

    # ----------------------------------------------------
    # STEP 2.5: DEFINE THE AVERAGE LATENCY SIGNAL RECIPE
    # ----------------------------------------------------
    # If is_requests_positive is true,
    # then: set to calculated_avg_latency
    # else: set to 0.0.
    # Name the new column "avg_latency_ms".
    avg_latency_signal_recipe: pl.Expr = (
        pl.when(is_requests_positive)
        .then(calculated_avg_latency)
        .otherwise(0.0)
        .alias("avg_latency_ms")
    )

    # ----------------------------------------------------
    # STEP 2.6: DEFINE THE THROUGHPUT SIGNAL RECIPE
    # ----------------------------------------------------
    # In this example, throughput is just the requests column,
    # which contains the number of requests handled in each observation.
    # This shows that a signal can be:
    # - a new calculation, or
    # - a renamed version of an existing column.
    throughput_signal_recipe: pl.Expr = (
        pl.col("requests").alias("throughput")
    )

    # ----------------------------------------------------
    # STEP 2.7: APPLY THE SIGNAL RECIPES TO THE DATAFRAME
    # ----------------------------------------------------
    # Now we use with_columns() to apply all the recipes
    # and create a new DataFrame with the added signal columns.
    df_with_signals: pl.DataFrame = df.with_columns(
        [
            error_rate_signal_recipe,
            avg_latency_signal_recipe,
            throughput_signal_recipe,
        ]
    )

    LOG.info("Created signal columns: error_rate, avg_latency_ms, throughput")

    # ----------------------------------------------------
    # STEP 3: SELECT THE COLUMNS WE WANT TO SAVE
    # ----------------------------------------------------
    # Keep the original columns and the new signal columns together.
    # And use the select() method to choose which columns
    # to include in the final output.
    signals_df = df_with_signals.select(
        [
            "requests",
            "errors",
            "total_latency_ms",
            "error_rate",
            "avg_latency_ms",
            "throughput",
        ]
    )

    LOG.info(f"Enhanced signals table has {signals_df.height} rows")

    # ----------------------------------------------------
    # STEP 4: SAVE THE SIGNALS TABLE AS AN ARTIFACT
    # ----------------------------------------------------
    # We call generated files artifacts.
    # Use the write_csv() method to save the signals_df DataFrame
    # as a CSV file at the OUTPUT_FILE path.
    signals_df.write_csv(OUTPUT_FILE)
    LOG.info(f"Wrote signals file: {OUTPUT_FILE}")

    LOG.info("========================")
    LOG.info("Pipeline executed successfully!")
    LOG.info("========================")
    LOG.info("END main()")



# === CONDITIONAL EXECUTION GUARD ===

if __name__ == "__main__":
    main()
