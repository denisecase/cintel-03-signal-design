# Glossary

## Quick Lookup

Common terms used in this module:

- **Signal** - a raw or derived metric used to understand system behavior
- **Raw Metric** - a directly recorded measurement from a system
- **Derived Metric** - a value calculated from one or more raw metrics
- **Error Rate** - proportion of errors relative to total requests
- **Latency** - the time required for a system to respond to a request
- **Throughput** - the amount of work processed by a system per unit of time

## Raw Metric

A measurement recorded directly from a system. Examples:

- number of requests
- number of errors
- total latency

Raw metrics describe what happened but may not be the easiest values to interpret.

## Signal

A **signal** is a raw or derived metric used to understand system behavior.

Signals may be direct measurements or values calculated from other metrics.

Well-designed signals help analysts monitor system health,
recognize patterns, and detect unusual behavior.

Examples include:

- request volume
- error rate
- average latency per request
- throughput

### Error Rate

The proportion of failed requests relative to total requests.
This signal helps identify **reliability problems** in a system.

```text
error_rate = errors / requests
```

### Latency

The **time required** for a system to respond to a request.
In this module, we often compute **average latency per request**:

```text
avg_latency = total_latency_ms / requests
```

### Throughput

The **amount of work processed per unit of time**.

Throughput can be calculated as:

```text
throughput = completed_work / elapsed_time
```

When observation intervals have equal durations,
request counts can serve as a simple indicator of throughput.

When intervals differ, counts should be normalized
by elapsed time to support meaningful comparisons.

Examples include:

- requests per second
- transactions per minute
- messages delivered per hour

## Feature Engineering

The process of creating new variables (features or signals) from existing data.
**Signal design is a form of feature engineering** for monitoring systems.
Feature engineering often includes:

- ratios (errors / requests)
- averages (latency per request)
- aggregations (rolling means)
- transformations (log, scaling, normalization)

## Signal Design

The process of creating useful signals from raw system metrics.
Well-designed signals make system behavior easier to monitor and interpret, which is essential for **continuous intelligence systems**.

---

[◄ Back to 🏠 Home](index.md)
