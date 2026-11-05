# Mautic - API documentation

## Overview

The **REST API under `/api/…` (JSON)** covers almost all objects: contacts (+custom fields), segments, campaigns, emails, forms, reports. Plus webhooks (events → your own backend) and form/tracking endpoints for embedding.

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| REST `/api/contacts|segments|campaigns|emails|forms|reports` | CRUD + actions | official |
| OAuth2 (authorization code/client credentials) + Basic | Access | official |
| Webhooks | `mautic.contact_created/updated`, email sent… | official |
| Form POST (`{MauticUrl}/form/submit` or `/c/{id}`) | External forms | official |
| GraphQL | — | ❌ |

## Authentication

1. Configuration → API access: create an OAuth2 client (redirect `urn:ietf:wg:oauth:2.0:oob` for scripts)
2. `POST /oauth/v2/token` → `access_token` → `Authorization: Bearer …`
   (Basic with an API user is possible for quick setups, OAuth2 is recommended.)

## Core endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET/POST` | `/api/contacts` | Contacts (filter via `search=`, `start/limit`) |
| `GET/PATCH/DELETE` | `/api/contacts/{id}` | Detail/change/delete |
| `POST` | `/api/contacts/{id}/edit` | Replacement PUT |
| `POST` | `/api/segments/{id}/contacts/add` | Segment membership |
| `GET/POST` | `/api/campaigns`, `/api/campaigns/{id}/contacts/{cid}/add` | Campaign control |
| `GET` | `/api/reports/{id}/data` | Report data (CSV/JSON) |
| `POST` | `/api/forms/{id}/submit` | Submit a form |

## Example

Request:

```http
POST /api/contacts HTTP/1.1
Authorization: Bearer <token>
Content-Type: application/json

{ "email": "ada@example.org", "firstname": "Ada",
  "tags": [12], "custom_fields": { "verein_rolle": "Foerderer" } }
```

Response: `201` → `{ "contact": { "id": 4711, "points": 0, "datesegmente": … } }`

## Webhooks

Configuration → webhooks: event (contact.updated) + URL + secret (payload signed via the `X-Mautic-Signature` HMAC); asynchronous, retries present.

## Rate limits

Not hard-coded; instance limits/recommendation: batch imports via the API + cron.

## SDKs and client libraries

- The official PHP SDK (`mautic/api-library`), community (Python/Node)
- Import/export recipes in the documentation

## Frontend note

The custom field catalog (`/api/customfields`) feeds directly into [fields.md](../../../../../../data/fields.md); webhooks as the event source in the event model.
