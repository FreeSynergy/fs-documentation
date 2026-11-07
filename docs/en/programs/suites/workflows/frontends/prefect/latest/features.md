# Prefect - Features

## Main features

### Flows as Python
- `@flow`/`@task` with retries, caching (result persistence), subflows, parameters via Pydantic
- `prefect.yaml` + `prefect deploy`: build/deploy pipeline (Git, Docker images, Conda)

### Deployment operations
- **Deployments**: versioned flow snapshots with schedules (cron/rrule), parameters, concurrency limits, tags
- **Work pools/workers**: infrastructure choice (process, Docker, Kubernetes, Cloud Run…), automatic failover
- Hybrid: code runs locally, orchestration in Cloud/server

### Observability and events
- Runs/timeline/Gantt with log streams, artifacts (tables/plots/images), SLA monitors
- **Events + automations**: event-based reactions (rerun, notify, webhook)

## What Prefect CANNOT do

- **No no-code editor** (definitions are always Python; the UI only configures deployments)
- **No streaming** (batch and event triggers yes, data streams no)
- **Data framework like Dagster's assets** only partially (artifacts instead of data lineage)
- Self-hosted server is younger than the Airflow ecosystem; provider breadth ≠ Airflow

## Extensions and integrations

| Integration | Route |
|-------------|-----|
| `prefect-aws/-dbt/-docker…` collections | official integration packages |
| REST API (server/Cloud identical) | officially documented |
| Terraform provider (Cloud) | Infrastructure as code |
