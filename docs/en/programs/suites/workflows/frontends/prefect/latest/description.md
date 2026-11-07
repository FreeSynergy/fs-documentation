# Prefect - Description

## What the program does

Prefect takes the operational burden off Airflow: flows remain simple Python code, deployments handle scheduling and infrastructure, and the UI shows runs live. "Deploy first": the path from script to production schedule is the core product.

## Advantages

- **Outstanding developer experience** (local tests, deploy via CLI)
- **Hybrid model**: compute stays in your own cluster, orchestration optionally in the cloud
- **Automations/events** without sensor tinkering

## Differentiation

| System | Difference |
|--------|-------------|
| **Airflow** | Reference architecture, provider breadth; Prefect is younger/more agile |
| **Dagster** | Asset/lineage-centric; Prefect is flow-centric |
| **n8n** | App integrations visually; Prefect uses Python code |

## Technical details

- **Stack**: Python (FastAPI server, Postgres), event clients, workers as processes/containers
- **Models**: flow, task run, deployment, work pool, block, event
- **Auth**: API keys (Cloud/self-hosted), `PREFECT_API_KEY`/`PREFECT_API_URL`
- **License**: Apache-2.0 (core), Cloud commercial

## Who it is for

- Python teams that want orchestration without scheduler operations
- FreeSynergy scenarios: deployments for nightly main-skin syncs (CRM↔ERP)
