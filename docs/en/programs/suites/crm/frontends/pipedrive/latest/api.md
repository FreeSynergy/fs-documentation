# Pipedrive - API Documentation

## Overview

Pipedrive offers a **REST API v1** with JSON as the exchange format. It is the official interface for integrations and is well documented at `developers.pipedrive.com`. Authentication uses a personal API token or OAuth2. Events can be reported to external endpoints via **webhooks**.

**API types at a glance**

| Type | Usage | Status |
|-----|------------|--------|
| REST v1 (`https://api.pipedrive.com/v1/`) | Leads, persons, organizations, deals, activities, products, fields, report helper data | Officially documented |
| OAuth2 (`https://oauth.pipedrive.com/`) | app access on behalf of a user | Officially documented |
| Webhooks (`/v1/webhooks`) | send events to own endpoints | Officially documented |
| GraphQL | ❌ Not available | — |
| CalDAV / CardDAV | ❌ Not available | — |
| XML-RPC | ❌ Not available | — |

## Authentication

- **Personal API token**: create it in the avatar menu → Personal settings → "Personal access tokens". Pass it either as query parameter `api_token=...` or as `Authorization: Bearer <token>` (header variant depends on the version; check the API docs).
- **OAuth2**: register an app in the Pipedrive Marketplace or as an internal app.
  - Authorization: `https://oauth.pipedrive.com/oauth/authorize`
  - Code exchange: `POST https://oauth.pipedrive.com/oauth/token`
  - Refresh: call the token endpoint again with `refresh_token`
  - Scopes limit access (e.g. `api:currentuser:read`, `files`, `activityTypes`; full list in the API docs)

## Endpoints

### Base

```
https://api.pipedrive.com/v1/<resource>
```

Read calls use `GET` with parameters (`start`, `limit`), write calls use `POST`/`PUT` with a JSON body, deletion uses `DELETE`.

### Leads and contacts

| Method | Endpoint | Description |
|---------|----------|--------------|
| `GET` | `/v1/leads` | List leads (filter, pagination) |
| `POST` | `/v1/leads` | Create lead |
| `PUT` | `/v1/leads/{id}` | Update lead |
| `DELETE` | `/v1/leads/{id}` | Delete lead |
| `GET` | `/v1/persons` | List contacts |
| `POST` | `/v1/persons` | Create contact |
| `PUT` | `/v1/persons/{id}` | Update contact |
| `DELETE` | `/v1/persons/{id}` | Delete contact |

### Organizations and deals

| Method | Endpoint | Description |
|---------|----------|--------------|
| `GET` | `/v1/organizations` | List organizations |
| `POST` | `/v1/organizations` | Create organization |
| `GET` | `/v1/deals` | List deals (filterable by pipeline and stage) |
| `POST` | `/v1/deals` | Create deal |
| `PUT` | `/v1/deals/{id}` | Update deal (stage, amount, close date) |
| `DELETE` | `/v1/deals/{id}` | Delete deal |
| `GET` | `/v1/deals/{id}/products` | Product lines of a deal |
| `POST` | `/v1/deals/{id}/products` | Add product line to deal |
| `GET` | `/v1/dealFields` | Field definitions for deals |
| `GET` | `/v1/pipelines` | List pipelines |
| `GET` | `/v1/pipelines/{id}/stages` | Stages of a pipeline |

### Activities and communication

| Method | Endpoint | Description |
|---------|----------|--------------|
| `GET` | `/v1/activities` | List activities (type, period, assignee) |
| `POST` | `/v1/activities` | Create activity (task, call, meeting) |
| `PUT` | `/v1/activities/{id}` | Update activity, e.g. mark as done |
| `GET` | `/v1/activities/{id}/participants` | Participating contacts of an activity |
| `POST` | `/v1/files` | Upload file (multipart) and attach it to an object |

### Search, bulk processing, webhooks

| Method | Endpoint | Description |
|---------|----------|--------------|
| `GET` | `/v1/searchResults` | Search objects across types (search term, object type) |
| `POST` | `/v1/deals/bulk` | Create several deals in one call |
| `PUT` | `/v1/{objekt}/bulk` | Update several records at once |
| `DELETE` | `/v1/{objekt}/bulk?ids=...` | Delete several records |
| `GET` | `/v1/webhooks` | List configured webhooks |
| `POST` | `/v1/webhooks` | Create webhook (`subscriber_url`, `model`, `subscription`) |
| `DELETE` | `/v1/webhooks/{id}` | Delete webhook |


## Examples

### Create deal (curl with personal token)

```bash
curl -s -X POST "https://api.pipedrive.com/v1/deals?api_token=PERSONAL_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Website-Relaunch Meyer AG",
    "value": "24000",
    "currency": "EUR",
    "pipeline": 1,
    "stage": 3,
    "expected_close": "2026-12-15"
  }'
```

Response (abridged):

```json
{
  "success": true,
  "data": {
    "id": 148,
    "title": "Website-Relaunch Meyer AG",
    "value": "24000",
    "stage_id": 3,
    "status": "open",
    "add_time": "2026-10-31 12:00:00"
  }
}
```

### Load filtered deals (curl)

```bash
curl -s "https://api.pipedrive.com/v1/deals?api_token=PERSONAL_TOKEN&limit=50&status=open"
```

### Fetch activities (Python)

```python
import requests

BASE = "https://api.pipedrive.com/v1"
TOKEN = "PERSONAL_TOKEN"

r = requests.get(f"{BASE}/activities", params={
    "api_token": TOKEN, "type": "task", "done": "0", "limit": 50,
})
for a in r.json()["data"]:
    print(a["id"], a["subject"], a["due_date"], a["person_name"])
```

### Set up webhook (curl)

```bash
curl -s -X POST "https://api.pipedrive.com/v1/webhooks?api_token=PERSONAL_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "subscriber_url": "https://example.com/pipedrive/webhook",
    "model": "deal",
    "subscription": {
      "deal.add": true,
      "deal.update": true,
      "deal.delete": true
    }
  }'
```

## Rate limits

- According to the API docs, the limit is **100 API requests per minute per company** (rolling window).
- If exceeded, the API responds with **HTTP 429**; retry the request afterwards with a delay (backoff).
- **Batch limit**: bulk calls process at most 50 resources per request; split larger volumes into batches.
- Rates may change per plan and release — check the official API docs before production use.

## Webhooks

- **Models**: `deal`, `person`, `organization`, `activity`, `note`, `product` (availability depends on the version).
- **Events** per model: `add`, `update`, `delete`; additionally `deleted_permanently` and `duplicate_restore` for deals.
- **Payload**: JSON with model, object (`subject`), subscribed event, `company_id` and `user_id`.
- **Delivery**: once per event; your own endpoints should ensure idempotency via the object ID.

## SDKs and client libraries

- **Official**: `pipedrive-api` for Node.js/JavaScript (covers the REST endpoints with types).
- **Unofficial**: community clients for Python, PHP and other languages; check coverage and maintenance before use.

## Operational notes

- Bind personal tokens to a service account with minimal rights and rotate them regularly.
- HTTPS only; do not store tokens in logs or client-side code.
- Custom fields have internal names (often with a prefix); look them up via `dealFields`, `personFields` and `orgFields`, do not guess.

## See also

- [menu.md](menus.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](layout.md)
- [shortcuts.md](shortcuts.md)
