# Signal Design for System Monitoring

Continuous Intelligence | Project 03 | Example Report

## Overview

This project explores how raw operational measurements
can be transformed into useful monitoring signals.

Individual measurements provide information,
but derived signals can make system behavior
easier to interpret and compare.

## Data

The example contains 10 observations of system activity.

Each observation includes:

- `requests` - number of requests handled.
- `errors` - number of failed requests.
- `total_latency_ms` - cumulative response time.

[View Example Dataset](https://github.com/denisecase/cintel-03-signal-design/blob/main/data/system_metrics.csv)

## Methods

The pipeline creates three monitoring signals.

### Error Rate

Error rate measures the proportion of failed requests.

    error_rate = errors / requests

### Average Latency

Average latency estimates response time per request.

    avg_latency_ms = total_latency_ms / requests

### Throughput

The example uses the number of requests per observation
as its throughput indicator.

    throughput = requests

The pipeline handles zero-request observations
without dividing by zero.

## Results

The example signals reveal:

| Signal | Observed Range |
|---|---|
| Error rate | 0% to 2.5% |
| Average latency | 25.0 to 33.71 ms |
| Requests per observation | 60 to 200 |

The output contains the original measurements
alongside the derived monitoring signals.

[View Signal Results](https://github.com/denisecase/cintel-03-signal-design/blob/main/artifacts/signals.csv)

## Interpretation

Error rate provides a useful indicator of reliability,
while average latency describes responsiveness.

Request counts provide additional context about activity.

Together, these signals offer a more informative view
of system behavior than the raw measurements alone.

## Limitations

The example does not establish acceptable performance
thresholds or evaluate changes over time.

Request counts are not normalized by elapsed time,
so they represent throughput only when observation
intervals are comparable.

## Conclusion

Effective monitoring begins with thoughtful signal design.

Signals should reflect the operational questions
that the monitoring system is intended to answer.

## Documentation Index

- **Home** - this landing page
- [**Project Instructions**](project-instructions.md)
- [**Glossary**](glossary.md)
- [**API**](api.md)
- [**Reactive App**](./app/index.html)

## Project Links

- [GitHub Repository](https://github.com/denisecase/cintel-03-signal-design)
- [Example Pipeline](https://github.com/denisecase/cintel-03-signal-design/blob/main/src/cintel/signal_design.py)
- [Results and Artifacts](https://github.com/denisecase/cintel-03-signal-design/tree/main/artifacts)
- [Project Instructions](project-instructions.md)

## Project Resources

- [Project Instructions](project-instructions.md)
- [Professional Python Guide](https://denisecase.github.io/pro-analytics-02/)
- [Professional Python Project Explainer](https://pup-pack.github.io/professional-python-project-explainer/).
- [Suggested Datasets](https://denisecase.github.io/pro-analytics-02/reference/datasets/cintel/)
