# Helodesk - API documentation

## Overview

Helodesk provides a **REST API** (JSON) for contacts, cases and messages, plus **webhooks** for call/case events. The API is functional but smaller than those of Zendesk/Freshdesk; telephony configuration (IVR) is only partly automatable. For skin work: read/write contact + case, receive events.

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| REST JSON (`api.helodesk.com`) | Contacts, cases, notes, call logs (read) | official |
| Webhooks | Call/case events as POST | official |
| Embed widgets | Chat/callback/form via script | official |
| GraphQL | — | ❌ |

## Authentication

- API token (administration → API/developers) as `Authorization: Bearer <token>` (details per account version in the Helodesk developer docs)
- HTTPS-only; IP allow-lists possible per contract

## Endpoints (concept, check the current state)

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET/POST` | `/contacts` | Search/create contacts (phone, mail) |
| `GET/PATCH` | `/contacts/{id}` | Detail/change |
| `GET/POST` | `/cases` | Cases (filter status/queue) |
| `GET/PATCH` | `/cases/{id}` | Status, owner, custom fields |
| `POST` | `/cases/{id}/notes` | Append a note |
| `GET` | `/calls` | Call logs (duration, queue, recording link if active) |
| `POST` | `/webhooks` | Manage webhook endpoints |

> Note: Helodesk maintains the detailed reference behind the developer interface; check field names before integration against the documented schema reference — nothing is invented here deliberately.

## Example (concept)

```http
GET /cases?status=open&queue=support HTTP/1.1
Host: api.helodesk.com
Authorization: Bearer <token>
```

```json
{ "cases": [ { "id": "4821", "subject": "Reklamation", "channel": "call",
               "status": "open", "queue": "support", "contact_id": "9734" } ] }
```

## Webhooks

Events include: incoming call, case created/updated, message received. Payload formats in the developer docs; endpoint with retry.

## Rate limits

Not publicly standardised; design integrations to be friendly (backoff on 429).

## SDKs and client libraries

- Official SDKs: ❌; connectors for HubSpot/Salesforce/Pipedrive + Zapier/Make cover the standard cases
- REST is sufficient for your own integration

## Skin note

The contact-case-channel triad matches the model approach ([models.md](../../../../../data/models.md): Contact ↔ Event/Comment ↔ Task); recording links as file references.
