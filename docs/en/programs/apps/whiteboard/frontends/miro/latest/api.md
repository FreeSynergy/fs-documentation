# Miro - API documentation

## Overview

The Miro REST API (`https://api.miro.com/v2/…`, JSON) with OAuth2. Boards, items (stickies/shapes/frameworks), frames, cards, members. Webhooks for board/item changes. App Kit for your own Miro apps.

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| REST v2 boards/items | CRUD, search (`/boards/{id}/items`) | official |
| Webhooks | `board.item.created/updated/deleted`, `board.member.*` | official |
| App Kit SDK (JS) | your own apps on the canvas | official |
| GraphQL | betas of individual products | ❌ generally not |

## Authentication

- OAuth2 **authorization code** (user) or **client credentials** (enterprise/M2M)
- Header `Authorization: Bearer <token>`; scope e.g. `boards:read boards:write`

## Core endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/v2/boards` | List boards |
| `POST` | `/v2/boards` | Create a board |
| `GET` | `/v2/boards/{id}/items` | Items (filter `type=sticky_note`) |
| `POST` | `/v2/boards/{id}/stickies` | Create a sticky |
| `POST` | `/v2/boards/{id}/frames` | Create a frame |
| `PATCH` | `/v2/boards/{id}/items/{itemId}` | Change (content, position) |
| `DELETE` | `/v2/boards/{id}/items/{itemId}` | Delete |
| `GET` | `/v2/boards/{id}/members` | Participants |
| `POST` | `/v2/webhooks` | Subscribe a webhook |

## Example

Request:

```http
POST /v2/boards/<board_id>/stickies HTTP/1.1
Authorization: Bearer <token>
Content-Type: application/json

{ "data": { "content": "Idea: launch a skin market", "parent": null },
  "geometry": { "x": 120, "y": 340, "width": 220, "height": 220 },
  "style": { "fillColor": "#FFF2A8" } }
```

Response: `201` with the item (`id`, `type:"sticky_note"`, `data`, `geometry`, `style`).

## Webhooks

`POST /v2/webhooks` with `type:"board.item.updated"`, `board_id`, `callback_url`; signature header for verification; a retry mechanism exists.

## Rate limits

**~50 requests/second per board; 1,000/min per user** (documentation reference values; 429 + Retry-After).

## SDKs and client libraries

- App Kit SDK (JS/TS) is official; REST examples in the documentation
- Zapier/Make connectors are available

## Frontend note

Sticky/frame/connector correspond to the whiteboard building blocks in the component documentation; item JSON → [models.md](../../../../../../data/models.md) (shape records analogous to tldraw).
