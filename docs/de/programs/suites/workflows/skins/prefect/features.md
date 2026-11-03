# Prefect - Funktionen

## Hauptfunktionen

### Flows als Python
- `@flow`/`@task` mit Retries, Caching (Result-Persistenz), Subflows, Parameters via Pydantic
- `prefect.yaml` + `prefect deploy`: Build/Deploy-Pipeline (Git, Docker-Images, Conda)

### Deployment-Betrieb
- **Deployments**: versionierte Flow-Snapshots mit Schedules (cron/rrule), Parameter, Concurrency-Limits, Tags
- **Work Pools/Workers**: Infra-Auswahl (Process, Docker, Kubernetes, Cloud Run…), Auto-Failover
- Hybrid: Code läuft lokal, Orchestrierung in Cloud/Server

### Observability und Events
- Runs/Timeline/Gantt mit Log-Streams, Artifacts (Tabellen/Plots/Bilder), SLA-Monitore
- **Events + Automations**: ereignisbasierte Reaktionen (rerun, notify, webhook)

## Was Prefect NICHT kann

- **kein No-Code-Editor** (Definition immer Python; UI konfiguriert nur Deployments)
- **kein Streaming** (Batch/Event-Trigger ja, Datenströme nein)
- **Data-Framework wie Dagsters Assets** nur ansatzweise (artifacts statt Datenlineage)
- Self-hosted Server jünger als Airflow-Ökosystem; Provider-Breite ≠ Airflow

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| `prefect-aws/-dbt/-docker…` Collections | offizielle Integrationspakete |
| REST-API (Server/Cloud identisch) | offiziell dokumentiert |
| Terraform-Provider (Cloud) | Infrastruktur-as-Code |
