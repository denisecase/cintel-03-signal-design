# Apply Ideas

Technique: Create derived metrics (signals) that reveal system behavior more clearly than raw measurements.

Signals help transform raw observations into interpretable indicators.

A good dataset for this module:

- contains multiple related measurements
- allows ratios, averages, or rates to be calculated

## Example Systems

### Website Traffic

Possible fields:

- requests
- errors
- total_latency_ms

Possible signals:

- error_rate = errors / requests
- avg_latency = total_latency_ms / requests

Questions to explore:

- Which signals best indicate system health?
- Are raw counts or derived signals easier to interpret?



### Retail Sales

Possible fields:

- units_sold
- revenue
- customers

Possible signals:

- revenue_per_customer
- units_per_customer

Questions to explore:

- What signals indicate strong or weak performance?
- Which signals help compare days with different traffic levels?



### Fitness Tracker Data

Possible fields:

- steps
- active_minutes
- calories

Possible signals:

- calories_per_minute
- steps_per_minute

Questions to explore:

- Which signals reveal intensity of activity?
- Do derived metrics change how behavior appears?



### Environmental Monitoring

Possible fields:

- temperature
- humidity
- wind_speed

Possible signals:

- temperature_change_rate
- comfort_index

Questions to explore:

- What signals help interpret environmental conditions?
- Are some signals easier to interpret than raw values?
