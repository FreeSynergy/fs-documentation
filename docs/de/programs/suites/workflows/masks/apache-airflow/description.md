# Apache Airflow - Beschreibung

## Was das Programm macht

Airflow ist der Zeitplan-Dienst für Datenpipelines: Man beschreibt Abhängigkeiten (DAG) und Zeitpläne in Python, der Scheduler hält sie zuverlässig ein — inkl. Nachholen historischer Läufe. Es orchestriert, es transformiert nicht selbst.

## Vorteile

- **Standard für Batch-Orchestrierung**, riesiges Provider-Ökosystem
- **Versionierbare Pipelines** (Code, Git, Tests)
- **Vorhersagbar**: Zeit- und datengetriebene Auslösung beides möglich

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **n8n/Make/Zapier** | Event-/App-Automation, UI-first; Airflow = Code-Batch |
| **Prefect** | modernere Hybrid-Execution, weniger Ops-Ballast; Airflow = Referenz-Architektur |
| **Dagster** | asset-zentriert; Airflow task-/zeitplan-zentriert |

## Technische Details

- **Architektur**: metadata DB (Postgres), scheduler, dag-file processors, api-server (FastAPI), workers (Local/Celery/K8s)
- **Authentifizierung**: Session-Login, RBAC; API: Basic/Session/JWT, `simple`-Auth konfigurierbar
- **Deploy**: Helm/Astronomer, MWAA (AWS), Composer (GCP)
- **Lizenz**: Apache-2.0

## Für wen geeignet

- Data-Engineering-Teams mit planbaren Pipelines
- FreeSynergy-Szenarien: Airflow als Rückgrat für nächtliche Sync-/Report-Skins über alle Module
