# Apache Airflow - Menu items

## UI navigation (header)

| Menu | Content |
|------|--------|
| DAGs | List (filter by runs/state), trigger, pause, detail graph (flow, task instances, logs) |
| Browse | DAG runs, tasks (across all DAGs), imports (parsing errors) |
| Datasets/Assets | Data dependencies between DAGs |
| Triggers | Trigger jobs (event-based DAG starts) |
| Admin | Connections (access), variables, pools, priorities, users/roles/teams (RBAC), alerts/notifiers (new) |

## Cluster level (administration)

| Level | Tools |
|-------|-----------|
| `airflow` CLI | dags list/test, tasks run, users create, connections add, db migrate |
| `dag-processor` | Parsing the DAG files |
| `scheduler` | Schedule + SLA, backfill |
| `workers` (Celery/K8s/Local) | Task execution |
| `api-server`/UI | REST `/api/v2` + web |

## Menus by role

Admin: users/connections; user: trigger/pause; viewer: read-only; task-level rights via role mapping (RBAC is the default since 2.4/3.x).
