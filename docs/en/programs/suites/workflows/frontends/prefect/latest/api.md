# Prefect - API Documentation

## Overview

The Prefect server (self-hosted as well as Cloud) speaks a **REST API under `/api` (JSON)** — the UI itself is a client of it. Objects: flows, deployments, flow_runs, task_runs, work_pools, blocks, events. Authentication with an API key.

**API types at a glance**

| Type | Use | Status |
|-----|------------|--------|
| REST `/api/…` | CRUD + filters (filter syntax like UI queries) | documented (internally stable, but labeled "internal API" with version notes) |
| Events API (`POST /api/event/resource`) | Submit your own events → automations | official |
| Outgoing webhooks | As an action in automations | official |
| GraphQL | — | ❌ |

## Authentication

- `Authorization: Bearer <api-key>` (Cloud: UI → API keys; server: configurable SimpleAuth token)
- Python client: `prefect.client.get_client()` encapsulates everything

## Core endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| `POST` | `/api/deployments/filter` | Search deployments (filter/sort) |
| `POST` | `/api/deployments/{id}/create_flow_run` | Start run (`parameters`, `tags`) |
| `POST` | `/api/flow_runs/filter` | Filter runs by states |
| `GET` | `/api/flow_runs/{id}` | Run details |
| `POST` | `/api/events/events/instrument` | Report external event |
| `GET` | `/api/work_pools` | Pools |
| `POST` | `/api/block_documents/query` | Read blocks |

## Example

Start a deployment:

```http
POST /api/deployments/6f1a…/create_flow_run HTTP/1.1
Authorization: Bearer <key>
Content-Type: application/json

{ "parameters": { "kunde": 4711 }, "tags": ["skin"] }
```

Response: `201` → `{ "id": "…", "state": {"type":"SCHEDULED"}, "parameters": {…} }`

External event (e.g. S3 upload):

```json
{ "event": "s3.object.created", "resource": {"prefect.resource.id": "s3.bucket.reports"},
  "event occurred": "…ISO…" }
```

## Rate limits

Cloud: documented quotas for events/API (by plan tier); self-hosted: server capacity.

## SDKs and client libraries

- **Official**: Python SDK `prefect` (`get_client`, `run_deployment`), `prefect-client` (lightweight, without server imports)
- Terraform provider for Cloud management

## Skin note

Deployment/run objects = planning model in [models.md](../../../../../../data/models.md); automation events match the event channels of the app skins.
