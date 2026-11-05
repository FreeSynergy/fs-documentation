# Help Scout - API documentation

## Overview

REST **v2** under `https://api.helpscout.net/v2/` (JSON, OAuth2 client credentials). Objects: mailboxes, conversations, threads, customers, tags, docs. Webhooks for events.

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| REST v2 | Conversations/threads/customers/tags/docs CRUD | official |
| Webhooks | `conversation.created`, `thread.created`, … | official |
| GraphQL | — | ❌ |

## Authentication

- OAuth2 **client credentials**: `POST /v2/auth/access_token` with `grant_type=client_credentials` (+ client id/secret or JWT signing for partners)
- Subsequent requests: `Authorization: Bearer <token>`

## Core endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/v2/mailboxes` | Mailboxes |
| `GET` | `/v2/conversations?mailbox=…&status=active` | Conversations |
| `GET` | `/v2/conversations/{id}` | Detail incl. threads |
| `POST` | `/v2/conversations/{id}/reply` | Public reply (form/JSON) |
| `POST` | `/v2/conversations/{id}/note` | Internal note |
| `PATCH` | `/v2/conversations/{id}` | Status/assignee/tags |
| `GET/POST` | `/v2/customers`, `/v2/tags` | People, tags |
| `GET/POST` | `/v2/docs/articles` | Knowledge base |
| `POST` | `/v2/users/…` (admin) | Team |

## Example

Request:

```http
POST /v2/conversations/123/reply HTTP/1.1
Authorization: Bearer <token>
Content-Type: application/json

{ "type": "reply", "body": "<p>Hello, the correction is attached.</p>", "assignTo": 456 }
```

Response: `201 Created` with a thread object.

## Webhooks

Subscription per event; delivery with retry; signature check via a shared secret.

## Rate limits

No officially published hard figure; throttling above ~20 req/s is typically answered with 429 — backoff recommended.

## SDKs and client libraries

- Official JS library (`@helpscout/api` wrapper), Python community (`helpscout` packages)
- Zapier/Make connectors for no-code

## Skin note

Conversation = thread tree instead of ticket + comment; the mapping variant in [modelle.md](../../../../../data/modelle.md) under "conversation model".
