# Apache Airflow - Struktur und UI/UX

## Architektur-Sicht

```
Git-Repo (dags/) ──► dag-file-processors ──► Metadata-DB (Postgres)
                          │                        ▲
                    scheduler (Zeitplan)           │ api-server (REST v2)
                          ▼                        ▼
                workers (Celery/K8s/Local)     Web-UI (FastAPI/React)
```

## UI-Layout

```
┌──────────────────────────────────────────────────────────────────┐
│ Airflow   DAGs | Browse | Datasets | Triggers | Admin   👤      │
├──────────────────────────────────────────────────────────────────┤
│ DAG-Liste: Name | Letzte Runs ▮▮▮▯▮ | Pause ⏸ | Trigger ▶       │
│  etl_nightly  ▮▮▮▮▮  ✔✔✔✔✔                                     │
│  report_mom   ▮▮▯▮▮  ✔✔✖✔✔                                     │
│ Detail:  Graph-Ansicht → Task-Instances → Log-/Trace-Tabs       │
└──────────────────────────────────────────────────────────────────┘
```

- 3.x-UI: dunkles Theme, Grid-Run-Ansicht, Log-Viewer mit Zeitstempel-Suche

## UI/UX

- funktional-technisch; Zustände als Farbchips (grün/gelb/rot/grau)
- Filter-URLs teilbar (z.B. `?state=failed`)

## Interaktionen

- Trigger-Dialog (JSON-Conf, logische Daten), Task-Drilldown (Try-Nummern)
- Kein Drag&Editing — DAG-Änderung = Code-Deployment

## Responsive Design

- Desktop-orientiert; Mobil lesend

## Accessibility

- Standard-Tabellen/Dialoge; Graph-Ansichten eingeschränkt (Textalternativen: Grid)

## Performance

- viele DAGs: `dag_file_processor`-Tuning, Parsen cachen; XCom-Massen vermeiden (External XCom Backends)
