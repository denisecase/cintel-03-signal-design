# Project Instructions

## WEDNESDAY: Complete Workflow Phase 1-3

Follow the instructions in
[⭐ **Workflow: Apply Example**](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/).

Complete:

1. Phase 1. **Start & Run** – copy the project and confirm it runs
2. Phase 2. **Change Authorship** – update the project to your name and GitHub account
3. Phase 3. **Read & Understand** – review the project structure and code

## FRIDAY/SUNDAY: Complete Workflow Phases 4-5

Complete:

1. Phase 4. **Make a Technical Modification**
2. Phase 5. **Apply the Skills to a New Problem**

# Topic

Signal design for monitoring system behavior.

In this project, you will transform **raw system metrics** into **derived signals** that are easier to interpret and monitor.

Signals help analysts detect problems, understand performance, and monitor how systems behave over time.

# Learning Objectives

After completing this project, you should be able to:

- Explain why analysts design signals from raw data
- Create derived metrics using simple calculations
- Add new signal columns to a DataFrame
- Run and validate a professional Python project
- Interpret signals that describe system behavior

# Example Code

The example file is located in:

```
src/cintel/signal_design_case.py
```

It demonstrates:

- reading system metrics from a CSV file
- creating derived signals from raw measurements
- protecting calculations from division-by-zero
- writing signal outputs to an artifacts file
- logging the pipeline process

Run the example and review the code before creating your own version.

# Dataset

The example dataset is located in the `data/` folder.

Example fields include:

- `requests`
- `errors`
- `total_latency_ms`

Each row represents a **system observation**.

Signals are created from these measurements to help monitor system behavior.

# Your Phase 4: Technical Modification Task

Using the example as a guide:

1. Copy `src/cintel/signal_design_case.py`.
2. Rename the copy to `src/cintel/signal_design_yourname.py`.
3. Run your copied file to confirm it executes correctly.
4. Modify the file by adding **at least one additional signal**.

Possible signals include:

- error rate per request
- average latency per request
- requests per time unit
- ratio-based metrics

Your new signal should be added as a new column in the DataFrame.

Then:

- run the project
- confirm the new signal appears in the output artifact
- confirm the program logs useful messages

The goal of this phase is to verify that you can **modify a working project and observe the result**.

# Phase 5: Apply the Skills

In Phase 5 you will apply signal design to a new situation.

Possible approaches include:

- modifying the dataset
- introducing additional system signals
- applying the method to a different monitoring scenario

Examples might include:

- website traffic monitoring
- application performance monitoring
- service request analysis
- sensor or environmental measurements

Document your changes in the project documentation (`docs/`):

- describe the signals you added
- explain why they are useful
- describe what they reveal about the system

Signal design is a key step in **continuous intelligence**, because monitoring systems depend on signals that clearly describe system behavior.

If you would like to apply these skills to a real dataset instead of the provided example data, see suggested datasets:

https://denisecase.github.io/pro-analytics-02/reference/datasets/cintel/
