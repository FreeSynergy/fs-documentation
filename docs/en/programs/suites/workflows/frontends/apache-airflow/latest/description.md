# Apache Airflow - Description

## What the program does

Airflow is the scheduling service for data pipelines: you describe dependencies (DAG) and schedules in Python, and the scheduler keeps them reliably — including catching up on historical runs. It orchestrates; it does not transform by itself.

## Advantages

- **Standard for batch orchestration**, huge provider ecosystem
- **Versionable pipelines** (code, Git, tests)
- **Predictable**: time-driven and data-driven triggering both possible

## Differentiation

| System | Difference |
|--------|-------------|
| **n8n/Make/Zapier** | Event/app automation, UI-first; Airflow = code-based batch |
| **Prefect** | More modern hybrid execution, less ops overhead; Airflow = reference architecture |
| **Dagster** | Asset-centric; Airflow task/schedule-centric |

## Technical details

- **Architecture**: metadata DB (Postgres), scheduler, DAG file processors, API server (FastAPI), workers (Local/Celery/K8s)
- **Authentication**: session login, RBAC; API: Basic/Session/JWT, `simple` auth configurable
- **Deployment**: Helm/Astronomer, MWAA (AWS), Composer (GCP)
- **License**: Apache-2.0

## Who it is for

- Data engineering teams with plannable pipelines
- FreeSynergy scenarios: Airflow as the backbone for nightly sync/report skins across all modules
