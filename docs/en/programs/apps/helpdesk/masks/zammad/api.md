# Zammad - API documentation

## Overview

Zammad is API-first: every UI action is a REST call under `/api/v1`. On top come webhooks (outbound) and an event/trigger system. Authentication via person access token, OAuth2 or session.

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| REST JSON `/api/v1/...` | Tickets, articles, customers, organisations, tags, knowledge base | official |
| Webhooks | Event → HTTP POST (configurable conditions) | official |
| WebSocket `/ws` | Live UI updates | official-internal |
| GraphQL | — | ❌ |

## Authentication

- **Token**: `Authorization: Token <abc>` (profile → access tokens, scopes such as `ticket.r`)
- **OAuth2/OIDC**: client credentials or authorization code; `Authorization: Bearer <jwt>`
- Session cookie in the browser; Basic only for the LDAP login endpoints

## Core endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/v1/tickets` | Tickets (filter/sort via parameters) |
| `GET` | `/api/v1/tickets/{id}` | Ticket details |
| `POST` | `/api/v1/tickets` | Create a ticket |
| `PUT` | `/api/v1/tickets/{id}` | Change attributes |
| `DELETE` | `/api/v1/tickets/{id}` | Delete |
| `GET` | `/api/v1/tickets/{id}/articles` | Article list |
| `POST` | `/api/v1/tickets/{id}/articles` | Write an article (`body`, `type`, attachments optional) |
| `GET/POST` | `/api/v1/users`, `/api/v1/organisations` | Customer context |
| `GET` | `/api/v1/tags` · `POST /api/v1/tags/add` | Tagging |
| `GET` | `/api/v1/object_manager_attributes` | Read dynamic fields |
| `POST` | `/api/v1/form_to_ticket` (portal endpoint per instance) | Form tickets |

## Example

Request:

```http
POST /api/v1/tickets/42/articles HTTP/1.1
Authorization: Token <token>
Content-Type: application/json

{
  "body": "<p>Hello, the technician is coming on Thursday.</p>",
  "type": "note",
  "form_id": null
}
```

Response: `200 OK` with the article object (`id`, `ticket_id`, `created_by`, `type`).

## Webhooks

Configuration under admin → webhooks. Event patterns: `ticket.create`, `ticket_update`, `ticket.article_created` …

```json
{ "event": "ticket.article_created",
  "object": { "id": 128, "ticket_id": 42, "type": "customer", "from": "b@example.org" },
  "changed_by": 3, "timestamp": 1793421000 }
```

Optional signatures (shared secret + HMAC) and condition filters (field/value).

## Rate limits

No built-in API limits (protection via reverse proxy/recommendation: keep the token scopes minimal).

## SDKs and client libraries

- **official**: Ruby `zammad-sdk`, CLI `zammad-console`
- **community**: Python `pyzammad`, Node `zammad-client`
- **imports**: Zendesk/Freshdesk/RT/OTRS import via UI and CLI (`zammad rake`)

## Skin note

The ticket/article/user fields mirror the standard model ([models.md](../../../../../data/models.md)); dynamic fields correspond to [fields.md](../../../../../data/fields.md) (`object_manager_attributes`).
