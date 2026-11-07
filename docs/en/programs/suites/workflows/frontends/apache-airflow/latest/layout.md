# Apache Airflow - Structure and UI/UX

## Architecture view

```
Git-Repo (dags/) ──► dag-file-processors ──► Metadata-DB (Postgres)
                          │                        ▲
                    scheduler (schedule)           │ api-server (REST v2)
                          ▼                        ▼
                workers (Celery/K8s/Local)     Web-UI (FastAPI/React)
```

## UI layout

```
┌──────────────────────────────────────────────────────────────────┐
│ Airflow   DAGs | Browse | Datasets | Triggers | Admin   👤      │
├──────────────────────────────────────────────────────────────────┤
│ DAG list: Name | Last runs ▮▮▮▯▮ | Pause ⏸ | Trigger ▶           │
│  etl_nightly  ▮▮▮▮▮  ✔✔✔✔✔                                     │
│  report_mom   ▮▮▯▮▮  ✔✔✖✔✔                                     │
│ Detail:  Graph view → Task instances → Log/trace tabs           │
└──────────────────────────────────────────────────────────────────┘
```

- 3.x UI: dark theme, grid run view, log viewer with timestamp search

## UI/UX

- functional-technical; states as colored chips (green/yellow/red/grey)
- Shareable filter URLs (e.g. `?state=failed`)

## Interactions

- Trigger dialog (JSON conf, logical dates), task drill-down (try numbers)
- No drag & drop editing — a DAG change = code deployment

## Responsive design

- Desktop-oriented; read-only on mobile

## Accessibility

- Standard tables/dialogs; graph views limited (text alternatives: grid)

## Performance

- Many DAGs: tune `dag_file_processor`, cache parsing; avoid massive XCom use (external XCom backends)
