# Freshdesk - API documentation

## Overview

REST API v2 under `https://<firma>.freshdesk.com/api/v2/` (JSON). Ticket/conversation CRUD, contacts, products, CBDs (custom fields), automations only in part. Webhooks deliver events.

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| REST v2 | Tickets, conversations, contacts, solutions, CCIs | official |
| Webhooks (`/api/v2/webhooks`) | Event → POST (ticket created/updated/reply…) | official |
| Developer platform | Serverless functions, custom actions | official |
| GraphQL | — | ❌ |

## Authentication

- **API key**: basic auth `curl -u agent@mail.com:APIKEY` (key under admin → mobile & API)
- **OAuth2**: for marketplace apps/developer platform
- Rate limit per account/minute; `Retry-After` on 429

## Core endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/v2/tickets?filter=open&product_id=…` | Tickets (filter parameters) |
| `POST` | `/api/v2/tickets` | Create |
| `GET/PATCH/DELETE` | `/api/v2/tickets/{id}` | Detail / change / delete |
| `POST` | `/api/v2/tickets/{id}/reply` | Public reply |
| `POST` | `/api/v2/tickets/{id}/private_note` | Internal note |
| `POST` | `/api/v2/tickets/{id}/notes` | Note (legacy) |
| `GET` | `/api/v2/tickets/{id}/conversations` | History |
| `GET/POST` | `/api/v2/contacts` | Customers |
| `GET/POST` | `/api/v2/solutions/articles` | KB |
| `GET/POST` | `/api/v2/webhooks` | Manage webhooks |

## Example

Request:

```http
POST /api/v2/tickets/1024/reply HTTP/1.1
Authorization: Basic base64(agent@mail.com:APIKEY)
Content-Type: application/json

{ "body": "We have corrected the invoice.", "files": [] }
```

Response: `200 OK` with a conversation object (`id`, `incoming:false`, `source:2`).

## Webhooks

Events include: `ticket.create`, `ticket.update`, `reply.created`, `note.created`, `contact.create`. Payload = ticket/conversation JSON; retry with backoff; secret header configurable.

## Rate limits

The documentation states **100 requests/minute per API key** (a guideline; on exceeding it HTTP 429 + `Retry-After`).

## SDKs and client libraries

- official: Python `freshdesk` (Freshworks), Node `freshdesk-sdk` (old, note this), PHP
- developer platform: `fd` CLI for custom functions

## Skin note

Conversations/ticket fields run parallel to Zendesk — a shared mapping in [models.md](../../../../../../data/models.md) (`Comment.public`, `Ticket.status`).
