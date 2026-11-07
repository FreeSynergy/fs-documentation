# n8n - API Documentation

## Overview

Two API layers: the **workflow execution API** (`/rest/v1`, instance management/triggers) and **webhooks** as entry points for workflows. Identical for self-hosted and cloud.

**API types at a glance**

| Type | Use | Status |
|-----|------------|--------|
| REST `/rest/v1/workflows|executions|credentials` | Management, triggers (`/workflows/{id}/activate`) | official |
| Workflow webhooks | `POST /webhook/<path>`, test `/webhook-test/<path>` | official |
| Webhook responses | Workflow → HTTP response (sync/async) | official |
| GraphQL | — | ❌ |

## Authentication

- **API key** (instance → Settings → API): header `X-N8N-API-KEY: <key>`
- Webhooks: own auth (header token, Basic) or query secret
- Cloud and self-hosted are the same

## Core endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| `GET/POST` | `/rest/v1/workflows` | List/create workflows (JSON definition) |
| `PATCH/DELETE` | `/rest/v1/workflows/{id}` | Modify/delete |
| `POST` | `/rest/v1/workflows/{id}/activate` | Activate |
| `POST` | `/rest/v1/workflows/{id}/run` | Start manually (with `data`) |
| `GET` | `/rest/v1/executions` | History (filter by status/workflow) |
| `GET` | `/rest/v1/executions/{id}` | Single log incl. node data |
| `POST` | `/webhook/<name>` | Workflow trigger |
| `POST` | `/webhook/<name>`, `respond: "allNodesFinished"` | Async response later via `/webhook-response/<id>` |

## Example

Start a workflow via API:

```http
POST /rest/v1/workflows/42/run HTTP/1.1
X-N8N-API-KEY: <key>
Content-Type: application/json
{ "data": { "ticket": 9982 } }
```

Webhook trigger:

```bash
curl -X POST https://n8n.example.org/webhook/ticket-in \
  -H 'Content-Type: application/json' -d '{"ticket":{"id":9982}}'
```

## Rate limits

No general API limit by default; webhook/queue capacity depends on the instance (workers, Redis). Cloud plans: execution/concurrency quotas.

## SDKs and client libraries

- CLI `n8n` (administration), **n8n-mcp**/community SDKs (Python `n8n-client`)
- Workflow JSON as exchange format (import/export/source control)

## Skin note

n8n workflow JSON = reference for integration skins: triggers + steps + error paths as standardized flows ([models.md](../../../../../../data/models.md) → workflow/event).
