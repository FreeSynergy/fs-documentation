# Prefect - Beschreibung

## Was das Programm macht

Prefect nimmt Airflow die Betriebslast ab: Flows bleiben einfacher Python-Code, Deployments übernehmen Zeitplan + Infrastruktur, die UI zeigt Runs live. „Deploy first“: Der Weg von Skript → produktivem Zeitplan ist das Kernprodukt.

## Vorteile

- **Developer-Experience** hervorragend (Tests lokal, Deploy per CLI)
- **hybrides Modell**: Rechenlast bleibt im eigenen Cluster, Orchestrierung optional Cloud
- **Automations/Events** ohne Sensor-Bastelei

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **Airflow** | Referenz-Architektur, Provider-Breite; Prefect jünger/agiler |
| **Dagster** | Asset-/Lineage-Zentrierung; Prefect Flow-zentriert |
| **n8n** | App-Integrationen visuell; Prefect Python-Code |

## Technische Details

- **Stack**: Python (FastAPI-Server, Postgres), Event-Clients, Workers als Prozesse/Container
- **Modelle**: Flow, TaskRun, Deployment, Work Pool, Block, Event
- **Auth**: API-Keys (Cloud/Self-hosted), `PREFECT_API_KEY`/`PREFECT_API_URL`
- **Lizenz**: Apache-2.0 (Core), Cloud kommerziell

## Für wen geeignet

- Python-Teams, die Orchestrierung ohne Scheduler-Ops wollen
- FreeSynergy-Szenarien: Deployments für nächtliche Hautp-Skins (CRM↔ERP-Sync)
