# Prefect - Menu items

## UI navigation

| Menu | Content |
|------|--------|
| Flows | Flow run lists, timeline, Gantt (run details, subflows) |
| Deployments | Create (from CLI `prefect deploy`), schedules, concurrency, parameter schemas |
| Work Pools | Infrastructure assignment (process/Docker/Kubernetes/…, concurrency limits) |
| Blocks | Configuration building blocks (credentials, S3 paths, SSH…) with UI editor |
| Automations | Event rules ("flow-run.failed → Slack / rerun") |
| Events | Event stream of all runs/infrastructure |
| Notifications/SLAs | Notification channels, fault tolerances |
| Admin (self-hosted) | Accounts/API keys, accounts (Cloud), service accounts |

## CLI hub (`prefect …`)

`deployment run`, `worker start`, `block register/build`, `cloud login`, `deployment schedule toggle` — the UI mirrors the CLI objects.

## Menus by role

Cloud/server: roles (admin/member/reader) per account; API keys for automations.
