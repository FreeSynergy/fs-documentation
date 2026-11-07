# Apache Airflow - Features

## Main features

### DAGs in Python
- `@dag`/`@task` decorators (Task SDK), `PythonOperator`, sensors (`Sensor`), retries/timeouts, SLA notifications
- **Datasets/Assets**: DAG B starts when DAG A updates a dataset (event coupling)
- **Deferrable operators/sensors** (async queue instead of blocking workers)

### Time and operations
- Cron/time-interval scheduling, catchup/backfill, manual triggering with `logical_date`
- Pools (parallelism), priorities, XComs (data between tasks), logs per task instance
- Alert/notifier framework (new in 3.x) for notification rules

### Operate
- RBAC (users/roles/teams), connections vault (secret backends), CLI + Stable REST API, Prometheus metrics, tests (`dag.test()`)

## What Airflow CANNOT do

- **No real-time/streaming**: minute-level cadence and batch thinking
- **No self-service editor for business departments** (DAGs = code + deployment)
- **No built-in transformation libraries** (dbt/Spark external)
- Self-setup requires DevOps maturity (Postgres, Redis/executor, time zone issues)

## Extensions and integrations

| Integration | Route |
|-------------|-----|
| Provider packages | 300+ operators (AWS, Snowflake, dbt, Kubernetes…) |
| REST v2 + CLI | officially stable |
| Terraform/K8s providers | Cluster management |
