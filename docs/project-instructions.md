# Project Instructions

## Goal

Apply **signal design** to transform raw system measurements
into useful indicators of operational behavior.

## A. Set Up Machine

Complete [Workflow A: Set Up Machine](https://denisecase.github.io/pro-analytics-02/workflow-a-set-up-machine/)
if your machine is not ready.

## B. Explore Example Project

Follow [Workflow B: Explore Example Project](https://denisecase.github.io/pro-analytics-02/workflow-b-explore-example-project/).

Explore how the example:

- Reads system metrics using Polars.
- Calculates error rate from requests and errors.
- Calculates average latency per request.
- Handles division by zero.
- Creates new signal columns.
- Saves the resulting signals as a CSV artifact.

Consider why the derived signals may be more informative
than the original measurements.

## C. Start New Project

Follow [Workflow C: Start New Project](https://denisecase.github.io/pro-analytics-02/workflow-c-start-new-project/).

IMPORTANT: New repository name:
**cintel-03-signal-design**.

VERIFY: You have completed git add-commit-push to GitHub at least twice.

## D. Apply Skills

Follow [Workflow D: Apply Skills](https://denisecase.github.io/pro-analytics-02/workflow-d-apply-skills/).

**Your problem:** Investigate how service reliability
relates to request volume.

You may use the example dataset with a new analytical
question or choose another appropriate dataset.

### Progression 1. Your Project Works Like the Example

Ensure your new custom project runs like the example.

Verify that key files have been updated to use **your GitHub account** and
the **new custom repository name**.

### Progression 2. Make a Technical Modification

Add at least one new signal.

For example, calculate the proportion
of successful requests:

    success_rate = (requests - errors) / requests

Handle observations with zero requests appropriately.

Verify the new signal and explain what it measures.

### Progression 3. Apply to a New Problem

Investigate whether service reliability differs
between observations with higher and lower request volumes.

- Define how request volumes will be grouped.
- Calculate useful reliability signals.
- Compare the observations.
- Save the resulting signals and comparisons.
- Interpret what the signals reveal.

You may apply the same techniques to a different
monitoring scenario if preferred.

## E. Finalize Project

Follow [Workflow E: Finalize Project](https://denisecase.github.io/pro-analytics-02/workflow-e-finalize/).

Use `docs/index.md` to report:

- Data and operational question.
- Signals designed and their calculations.
- Technical modifications.
- Results and a relevant visual.
- Interpretation and limitations.

Include a clickable link to your repository and artifacts.

## Success

- [ ] README.md project-specific links use **your GitHub account**
- [ ] README.md project-specific links use **your custom repository name**.
- [ ] docs/index.md project-specific links use **your GitHub account**
- [ ] docs/index.md project-specific links use **your custom repository name**.
- [ ] pyproject.toml `name` has been changed to use **your custom repository name**.
- [ ] The `src/cintel` folder reflects your authorship and custom work.
- [ ] All necessary commands are provided and work successfully.
- [ ] Links to the Professional Python Guide (pro-analytics-02) remain unchanged.
- [ ] Commit history shows **at least** the git add-commit-push history required in the instructions.

---

[◄ Back to Home](index.md)
