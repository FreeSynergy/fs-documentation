# Apache Airflow - Funktionen

## Hauptfunktionen

### DAGs in Python
- `@dag`/`@task`-Dekoratoren (Task-SDK), `PythonOperator`, Sensoren (`Sensor`), Retries/Timeouts, SLA-Meldungen
- **Datasets/Assets**: DAG B startet, wenn DAG A ein Dataset aktualisiert (Event-Kopplung)
- **deferrable Operator/Sensoren** (Async-Warteschlange statt Worker-Blockade)

### Zeit und Betrieb
- Cron-/Zeitintervall-Scheduling, Catchup/Backfill, manuelles Triggern mit `logical_date`
- Pools (Parallelität), Prioritäten, XComs (Daten zwischen Tasks), Logs pro Task-Instance
- Alert-/Notifier-Framework (neu in 3.x) für Benachrichtigungsregeln

### Operate
- RBAC (Users/Roles/Teams), Connections-Vault (Secret-Backends), CLI + Stable REST API, Prometheus-Metriken, Tests (`dag.test()`)

## Was Airflow NICHT kann

- **kein Echtzeit/Streaming**: Minuten-Takt und Batch-Denken
- **kein Fachbereich-Selbstbedienungs-Editor** (DAGs = Code + Deployment)
- **keine eingebauten Transformations-Bibliotheken** (dbt/Spark external)
- Self-Setup erfordert DevOps-Reife (Postgres, Redis/Executor, Zeitzonen-Sorgen)

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| Provider-Pakete | 300+ Operatoren (AWS, Snowflake, dbt, Kubernetes…) |
| REST v2 + CLI | offiziell stable |
| Terraform/K8s-Provider | Cluster-Verwaltung |
