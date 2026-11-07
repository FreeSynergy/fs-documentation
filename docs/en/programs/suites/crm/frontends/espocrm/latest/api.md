# EspoCRM - API Documentation

## Overview

EspoCRM is API-first: the SPA itself talks to **REST /api/v1**. Metadata (fields, entities) can be read via the API — ideal for skin mapping. Webhooks deliver changes.

**API types at a glance**

| Type | Usage | Status |
|-----|------------|--------|
| REST `/api/v1/{entity}` | CRUD, find, mass actions, custom actions | official |
| Webhooks (from workflows/admin) | event → POST | official |
| Hooks (server-side) | events in the core | official (extensions) |
| GraphQL | — | ❌ |

## Authentication

- **API token** (`Authorization: <token>` — generated in the field "API Access Tokens") or **HMAC** (key/secret, signature over path+body), or basic auth (test only)
- Roles control API rights just like UI rights

## Endpoints (generic per entity)

| Method | Endpoint | Description |
|---------|----------|--------------|
| `GET` | `/api/v1/Contact?max=50&offset=0&orderBy=createdAt&where=[{"type":"EQUALS","field":"…"}]` | List/filter (where as JSON) |
| `POST` | `/api/v1/Contact` | create |
| `GET/PATCH/DELETE` | `/api/v1/Contact/{id}` | read / update / delete |
| `POST` | `/api/v1/Contact/{id}/rel/Accounts` | add relation |
| `GET` | `/api/v1/Metadata` | complete data model (fields/layouts) |
| `GET` | `/api/v1/Collection/GlobalSearch?whereStr=…` | global search |
| `POST` | `/api/v1/Contact/{id}/action/{customAction}` | custom actions (extensions) |

## Example

Request:

```http
POST /api/v1/Lead HTTP/1.1
Authorization: <api-token>
Content-Type: application/json

{ "name": "Messekontakt", "accountName": "Beta GmbH",
  "emailAddress": ["kontakt@beta.example"], "status": "New" }
```

Response: `201 Created`

```json
{ "id": "634f…", "name": "Messekontakt", "status": "New", "createdAt": "2026-10-31 16:20:11" }
```

## Webhooks

Admin → Webhooks: event (`Entity:Create/Update/Delete`) + URL + secret; the body contains the entity payload + `action`. Retry with backoff.

## Rate limits

None built in; web server limits recommended.

## SDKs and client libraries

- **Official**: JS client of the SPA (reference), PHP client library, Postman collection
- Community: Python/Node wrappers for REST; Make/Zapier via REST

## Skin note

`GET /api/v1/Metadata` returns the field taxonomy — perfect for automatic mapping to [fields.md](../../../../../../data/fields.md).
