# Prefect - Menüpunkte

## UI-Navigation

| Menü | Inhalt |
|------|--------|
| Flows | Flow-Runs-Listen, Timeline, Gantt (Run-Details, Subflows) |
| Deployments | anlegen (aus CLI `prefect deploy`), Schedules, Concurrency, Parameter-Schemas |
| Work Pools | Infrastruktur-Zuordnung (Process/Docker/Kubernetes/…, Concurrency-Limits) |
| Blocks | Konfigurations-Bausteine (Credentials, S3-Pfade, SSH…) mit UI-Editor |
| Automations | Event-Regeln („flow-run.failed → Slack / Rerun“) |
| Events | Ereignisstrom aller Runs/Infra |
| Notifications/SLAs | Benachrichtigungs-Kanäle, Fehlertoleranzen |
| Admin (Self-hosted) | Accounts/API-Keys, Accounts (Cloud), Service-Accounts |

## CLI-Zentrale (`prefect …`)

`deployment run`, `worker start`, `block register/build`, `cloud login`, `deployment schedule toggle` — UI spiegelt die CLI-Objekte.

## Menüs nach Rolle

Cloud/Server: Rollen (Admin/Member/Reader) je Account; API-Keys für Automatisierungen.
