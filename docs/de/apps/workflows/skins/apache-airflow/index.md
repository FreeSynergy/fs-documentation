# Apache Airflow Dokumentation

## Übersicht

Apache Airflow (Apache-2.0) orchestriert datenintensive Pipelines als **DAGs in Python**: Planner (Scheduler) rechnet Zeitpläne, Executors verteilen Tasks an Worker. Betrieben als Selbstbau-Cluster (Local/Kubernetes/Celery) oder Managed (MWAA, Astronomer). Airflow 3.x mit Task-SDK und neuem UI.

## Dateistruktur

- [menu.md](menu.md) - UI-Navigation (DAGs, Browse, Admin), Cluster-Komponenten
- [features.md](features.md) - DAGs, Scheduling, Datasets/Assets, Was Airflow NICHT kann
- [description.md](description.md) - Abgrenzung zu n8n Make (Events) und Prefect
- [structure.md](structure.md) - Komponenten (Scheduler/Worker/UI) + UI-Layout
- [shortcuts.md](shortcuts.md) - Kurzbefehle (UI minimal, CLI zentral)
- [api.md](api.md) - Stable REST API v2, CLI, importDags
