# Prefect - API Dokumentation

## Übersicht

Der Prefect-Server (self-hosted wie Cloud) spricht eine **REST-API unter `/api` (JSON)** — die UI selbst ist ein Client davon. Objekte: flows, deployments, flow_runs, task_runs, work_pools, blocks, events. Authentifizierung mit API-Key.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST `/api/…` | CRUD + Filter (Filter-Syntax wie UI-Queries) | dokumentiert (intern stabil, aber „internal API“ mit Versionshinweisen) |
| Events-API (`POST /api/event/resource`) | eigene Ereignisse einliefern → Automations | offiziell |
| Webhooks outgoing | in Automations als Aktion | offiziell |
| GraphQL | — | ❌ |

## Authentifizierung

- `Authorization: Bearer <api-key>` (Cloud: UI → API-Keys; Server: SimpleAuth-Token konfigurierbar)
- Python-Client: `prefect.client.get_client()` kapselt alles

## Kernendpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `POST` | `/api/deployments/filter` | Deployments suchen (Filter/Sort) |
| `POST` | `/api/deployments/{id}/create_flow_run` | Run starten (`parameters`, `tags`) |
| `POST` | `/api/flow_runs/filter` | Runs mit Staaten filtern |
| `GET` | `/api/flow_runs/{id}` | Run-Details |
| `POST` | `/api/events/events/instrument` | externes Event melden |
| `GET` | `/api/work_pools` | Pools |
| `POST` | `/api/block_documents/query` | Blocks lesen |

## Beispiel

Deployment starten:

```http
POST /api/deployments/6f1a…/create_flow_run HTTP/1.1
Authorization: Bearer <key>
Content-Type: application/json

{ "parameters": { "kunde": 4711 }, "tags": ["skin"] }
```

Response: `201` → `{ "id": "…", "state": {"type":"SCHEDULED"}, "parameters": {…} }`

Externes Event (z.B. S3-Upload):

```json
{ "event": "s3.object.created", "resource": {"prefect.resource.id": "s3.bucket.reports"},
  "event occurred": "…ISO…" }
```

## Rate Limits

Cloud: dokumentierte Kontingente für Events/API (Plankaskalen); Self-hosted: Server-Kapazität.

## SDKs und Client-Bibliotheken

- **offiziell**: Python SDK `prefect` (`get_client`, `run_deployment`), `prefect-client` (schlank, ohne Server-Import)
- Terraform-Provider für Cloud-Verwaltung

## Skin-Hinweis

Deployment-/Run-Objekte = Planungsmodell in [modelle.md](../../../../data/modelle.md); Automations-Events passen zu Event-Kanälen der App-Skins.
