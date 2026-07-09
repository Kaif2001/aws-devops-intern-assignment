# Load Testing Report

## Tool Used

Grafana k6

## Test Configuration

- Virtual Users (VUs): 20
- Duration: 30 seconds

## Results

| Metric | Value |
|---------|-------|
| Total Requests | 361 |
| Successful Requests | 360 |
| Failed Requests | 1 |
| Success Rate | 99.72% |
| Average Response Time | 65.74 ms |
| Maximum Response Time | 424.61 ms |

## Observations

- Application remained available during testing.
- Success rate was 99.72%.
- Average response time remained under 100 ms.
- Only one request failed during shutdown.
- Overall application performance is stable.

## Suggested Improvements

- Deploy behind Nginx.
- Use Gunicorn for production.
- Enable Auto Scaling.
- Add CloudWatch alarms.
- Use an Application Load Balancer.