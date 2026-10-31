# Apache Airflow - Menüpunkte

## UI-Navigation (Kopf)

| Menü | Inhalt |
|------|--------|
| DAGs | Liste (Filter Runs/State), Trigger, Pause, Detail-Graph (Ablauf, Task-Instances, Logs) |
| Browse | DAG-Runs, Tasks (über alle DAGs), Imports (Parsing-Fehler) |
| Datasets/Assets | Daten-Abhängigkeiten zwischen DAGs |
| Triggers | Trigger-Jobs (eventbasierte DAG-Starts) |
| Admin | Connections (Zugänge), Variables, Pools, Pools/Prioritäten, Users/Roles/Teams (RBAC), Alerts/Notifiers (neu) |

## Cluster-Ebene (Administration)

| Ebene | Werkzeuge |
|-------|-----------|
| `airflow` CLI | dags list/test, tasks run, users create, connections add, db migrate |
| `dag-processor` | Parsen der DAG-Dateien |
| `scheduler` | Zeitplan + SLA, Backfill |
| `workers` (Celery/K8s/Local) | Task-Ausführung |
| `api-server`/UI | REST `/api/v2` + Web |

## Menüs nach Rolle

Admin: Users/Connections; User: Trigger/Pause; Viewer: lesen; Task-Level-Rechte über Rollen-Mapping (RBAC ab 2.4/3.x Standard).
