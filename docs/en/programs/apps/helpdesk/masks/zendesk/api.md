# Zendesk - API documentation

## Overview

The Zendesk REST **API v2** (`https://<subdomain>.zendesk.com/api/v2/…`, JSON) counts as one of the most complete helpdesk APIs: tickets, users, orgs, help centre, custom objects, business rules. Plus webhooks and trigger-out (via webhook conditions).

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| REST JSON v2 | Full CRUD, cursor pagination | official |
| Webhooks (REST out/in) | Event streams, inbound endpoints | official |
| Sunshine platform (custom objects, actions) | Integrate external data | official (plan-dependent) |
| GraphQL | Only selected areas (Talk/custom object betas) | ❌ not comprehensive |

## Authentication

| Method | Use |
|--------|-----|
| `ZDK-API-TOKEN: <token>` + `login/email/token` basic | Server-to-server |
| OAuth 2.0 (authorization code, PKCE) | Apps/user-delegated |
| JWT (apps/SSO) | App context |
| OAuth app credentials + admin scopes | Admin actions |

## Core endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/v2/tickets.json` | List (filter `?status=open&per_page=100`) |
| `POST` | `/api/v2/tickets.json` | Create a ticket |
| `GET/PATCH/DELETE` | `/api/v2/tickets/{id}.json` | Detail/change/delete |
| `POST` | `/api/v2/tickets/{id}/comments.json` | Comment/reply/note (`public` true/false) |
| `GET` | `/api/v2/users.json`, `/api/v2/organizations.json` | Context |
| `POST` | `/api/v2/macros/{id}/apply.json?sid=…` | Apply a macro |
| `GET/POST` | `/api/v2/help_center/articles.json` | Knowledge base |
| `GET` | `/api/v2/slas.json`, `/api/v2/business_rules_jobs…` | Business rules |
| `POST` | `/api/v2/webhooks` | Manage webhook (with `webhook_endpoint`) |
| `GET` | `/api/v2/webhooks/webhooks_events` | Delivery events |

## Example

Request:

```http
POST /api/v2/tickets.json HTTP/1.1
Authorization: Basic base64(agent@mail.com/token/API_TOKEN)
Content-Type: application/json

{ "ticket": {
    "subject": "Printer offline",
    "comment": { "body": "No printing since 09:00.", "public": true },
    "requester_id": 12345,
    "tags": ["printer", "hw"],
    "priority": "high" } }
```

Response: `201 Created` with the ticket JSON (`id`, `status:"new"`, `via`, `audit_ids`).

## Webhooks

- Outgoing: events `ticket.created`, `comment.created`, `ticket.updated` … (signature: `x-zendesk-webhook-signature` HMAC)
- Inbound: your own endpoint as a trigger source (`/api/v2/webhooks`, "webhooks" in the admin centre)

## Rate limits

- Basic-auth requests: **700 requests/5 min per account**;
- OAuth user tokens: 500/5 min/client;
- on 429: follow the `Retry-After` header.

## SDKs and client libraries

- Official client libs: Ruby `zendesk zendesk_api_client_rb`, Python `zendesk`, Node `node-zendesk`, Java
- The Zendesk app framework for UI extensions (iframe apps, `client.request`)

## Skin note

`ticket.comment`, `audit`, `user` correspond directly to the [comment/user model](../../../../../data/modelle.md) — Zendesk v2 is a good patron for FreeSynergy ticket fields ([felder.md](../../../../../data/felder.md)).
