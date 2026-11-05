# Monica - API Documentation

## Overview

Monica has a stable **REST API** (`/api/`) with a personal token — it covers contacts, activities, tasks, notes, gifts and relationships. Webhooks push changes out.

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| REST JSON `/api/...` | Full CRUD | official |
| Webhooks | Push on events | official (configurable per user) |
| GraphQL | — | ❌ |
| CalDAV/CardDAV | — | ❌ (export only as a file) |

## Authentication

- Token (Settings → API) as `Authorization: Bearer <token>`
- All endpoints are user-scoped (circle isolation)

## Endpoints (core)

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/contacts` | Contacts (paginated, `query` filter) |
| `POST` | `/api/contacts` | Create contact |
| `GET` | `/api/contacts/{id}` | Detail |
| `PUT` | `/api/contacts/{id}` | Change |
| `DELETE` | `/api/contacts/{id}` | Delete |
| `GET/POST` | `/api/contacts/{id}/activities` | Read/create activities |
| `GET/POST` | `/api/tasks` | Tasks |
| `GET/POST` | `/api/notes` | Notes |
| `GET/POST` | `/api/gifts` | Gifts |
| `GET` | `/api/activity-types`, `/api/relationship-types` | Type catalogues |

## Example

Request:

```http
POST /api/contacts HTTP/1.1
Authorization: Bearer <token>
Content-Type: application/json

{
  "first_name": "Andrea",
  "last_name": "Berg",
  "gender_id": 1,
  "description": "Wandergruppe"
}
```

Response:

```json
{
  "data": {
    "id": 341,
    "first_name": "Andrea",
    "last_name": "Berg",
    "complete_name": "Andrea Berg",
    "description": "Wandergruppe",
    "url": "https://monica.example.org/contact/341"
  }
}
```

## Webhooks

Configuration under Settings → Webhooks (URL + secret). Events include: `contact.created`, `activity.added`, `task.completed` — JSON body with the object and an `event` field, signature via `X-Monica-Signature` (HMAC-SHA256).

## Rate limits

Default: **no** hard API rate limiting; set it instance-side via the web server.

## SDKs and client libraries

- Official SDKs: ❌
- Community: PHP/JS examples in the Monica wiki; REST + `curl` suffices

## Frontend note

The Monica structure is the reference for the contact-with-event model ([models.md](../../../../../../data/models.md)); the webhooks correspond to the standard event fields ([fields.md](../../../../../../data/fields.md)).
