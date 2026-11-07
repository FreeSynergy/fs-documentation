# Zapier - API Documentation

## Overview

Zapier offers APIs for two directions: (1) **Zapier platform APIs** (building your own apps, prefill webhooks, REST hooks as triggers), (2) **organization/zap management APIs** (list/run zaps via REST; credentials via API secret).

**API types at a glance**

| Type | Use | Status |
|-----|------------|--------|
| REST `/api/v1/zaps` (organization) | Manage/trigger zaps | official (Team/Enterprise) |
| REST hooks (objects) | Push triggers: a zap listens on your own REST endpoints | official |
| Prefill webhooks | Fill fields for zap forms | official |
| OAuth2 (platform) | Own connectors | official |
| GraphQL | — | ❌ |

## Authentication

- Platform: OAuth2 (client credentials/authorization code)
- Organization API: API secret (`Authorization: Bearer <jwt>` after login via `identities/jwt`)

## Core endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| `GET` | `/api/v1/zaps` | Zaps of the account |
| `POST` | `/api/v1/zaps/{zapId}/run` | Run zap (input fields) |
| `POST` | `/resthooks/v2/subscriptions` | Subscribe REST hook (your own API as trigger) |
| `POST` | `/prefill/webhook/…` | Answer prefill |
| `POST` | `/platform/v1/deployments` | Deploy your own apps (the `zapier` CLI uses this) |

## Example

Run a zap:

```http
POST /api/v1/zaps/1234567/run HTTP/1.1
Authorization: Bearer <jwt>
Content-Type: application/json

{ "fields": { "Name": "Ada", "E-Mail": "ada@example.org" } }
```

Response: `200` → `{ "zapRun": { "status": "in_progress", "id": "run_…" } }`

## Prefill (push trigger support)

```json
{ "bundle": { "trigger_data": {…} }, "authentication": {…} }
→ Response: { "fields": { "ticket_id": 9982 } }
```

## Rate limits

Documented per API (moderate, 429 with backoff); platform calls subject to per-app limits.

## SDKs and client libraries

- **`zapier` CLI** (official, platform development: `zapier build/validate/push`)
- REST hooks with their own HMAC signature scheme (`x-zapier-hook` schema)

## Skin note

Zap structure (trigger + steps + paths) = simplified flow model for beginner templates ([models.md](../../../../../../data/models.md)).
