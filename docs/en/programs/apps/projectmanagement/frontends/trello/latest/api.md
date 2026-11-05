# Trello - API documentation

## Overview

REST API under `https://api.trello.com/1/…` (JSON). Classic authentication via `key` + `token` query parameters; modern OAuth2 for Power-Ups. Webhooks attach to objects (board/list/card).

**API types at a glance**

| Type | Use | Status |
|-----|------------|--------|
| REST v1 | Boards, lists, cards, actions, members | official |
| Webhooks (`/1/webhooks`) | Object changes as POST | official |
| REST 2 API (`api.trello.com/2`) | New endpoints (teams/board fields) | official (growing) |
| GraphQL | — | ❌ |

## Authentication

- `?key=<app-key>&token=<member-token>` (personal token in the account settings)
- OAuth2 (Power-Ups): `Authorization: OAuth oauth_token=…`
- Scoped tokens for Power-Ups (own rights only)

## Core endpoints

| Method | Endpoint | Description |
|---------|----------|--------------|
| `GET` | `/1/boards/{id}/lists` | Lists of a board |
| `POST` | `/1/boards/{id}/lists` | Create a list |
| `GET` | `/1/lists/{id}/cards` | Cards of a list |
| `POST` | `/1/cards` | Create a card (`idList`, `name`, `due`, `desc`, `idMembers`, `labels`) |
| `PUT` | `/1/cards/{id}` | Change it (position, list…) |
| `POST` | `/1/cards/{id}/actions/comments` | Comment |
| `GET` | `/1/boards/{id}/actions` | Activity feed |
| `POST` | `/1/webhooks` | Register a webhook on a board/card |

## Example

Request:

```http
POST /1/cards?idList=62f…&key=KEY&token=TOKEN HTTP/1.1
Content-Type: application/json

{ "name": "Draft the article", "desc": "Outline it in the wiki",
  "due": "2026-11-04T17:00:00.000Z", "idMembers": ["5f…"] }
```

Response: `200` with the card object (`id`, `pos`, `due`, `dateLastEdit`).

## Webhooks

```json
{ "action": { "type": "createCard", "date": "…",
    "data": { "list": {"id": "62f…"}, "card": {"id": "…", "name": "…"} },
    "memberCreator": { "id": "…" } } }
```

Callback with retry; the model is "action events" (also `commentCard`, `updateCard`).

## Rate limits

**~100 requests/10 s per key and member; 100/s per token**, plus board-action limits — 429 with `Retry-After`.

## SDKs and client libraries

- Community SDKs: Python (`py-trello`), Node (`node-trello`), PHP; the official reference is the API docs + Postman
- Power-Up framework: its own JS SDK for in-Trello apps

## Frontend note

board/list/card/pos/labels are the reference vocabulary for kanban masks ([models.md](../../../../../../data/models.md)); the `pos` float matches the sorting logic in [fields.md](../../../../../../data/fields.md).
