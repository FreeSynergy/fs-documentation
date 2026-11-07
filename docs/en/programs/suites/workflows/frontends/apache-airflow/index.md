# Apache Airflow Documentation

## Overview

Apache Airflow (Apache-2.0) orchestrates data-intensive pipelines as **DAGs in Python**: the planner (scheduler) calculates schedules, executors distribute tasks to workers. Operated as a self-built cluster (Local/Kubernetes/Celery) or as a managed service (MWAA, Astronomer). Airflow 3.x with Task SDK and new UI.

## File structure

- [menu.md](latest/menus.md) - UI navigation (DAGs, Browse, Admin), cluster components
- [features.md](latest/features.md) - DAGs, scheduling, datasets/assets, what Airflow CANNOT do
- [description.md](latest/description.md) - Differentiation from n8n, Make (events) and Prefect
- [structure.md](latest/layout.md) - Components (scheduler/worker/UI) + UI layout
- [shortcuts.md](latest/shortcuts.md) - Keyboard shortcuts (UI minimal, CLI central)
- [api.md](latest/api.md) - Stable REST API v2, CLI, importDags
