# Wekan - API documentation

## Overview

REST API with a **personal token** (profile → application programming interface). Endpoints
for boards, lists, cards, comments; additionally **invoke webhooks** (incoming hooks as a
card intake) and **outgoing webhooks**.

**API kinds at a glance**

| Kind | Use | Status |
|------|-----|--------|
| REST `/api/…` (JSON) | boards/lists/cards CRUD | official (thinly documented) |
| Invoke webhooks | POST from outside → card/comment/status | official |
| Outgoing webhooks | board activity → HTTP POST | official |
| GraphQL | — | ❌ |

## Authentication

- Personal token: `Authorization: Bearer <token>` or `?token=<token>`
- The token can be created in the user profile (scope: the creator's account)

## Core endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/boards.json` | the boards of the token |
| `POST` | `/api/createBoard` | create a board (`{"board":{title},"orgId":…}`) |
| `GET` | `/api/boards/{boardId}/lists` | lists incl. the swimlane reference |
| `POST` | `/api/boards/{boardId}/lists/new` | create a list |
| `POST` | `/api/boards/{boardId}/lists/{listId}/cards/new` | create a card |
| `POST` | `/api/cards/{cardId}/comments/new` | comment |
| `POST` | `/api/boards/{boardId}/lists/{listId}/cards/{cardId}/move` | move a card |
| `POST` | `/api/boards/{boardId}/archive` | archive a board |

## Example

Request:

```http
POST /api/boards/abcd1234/lists/ef5678/cards/new HTTP/1.1
Authorization: Bearer <token>
Content-Type: application/json

{ "title": "Alert: disk 91%", "description": "node-3 /var",
  "labelIds": ["red"], "customFields": { "host": "node-3" } }
```

Response: `200` → `{ "_id": "…", "title": "Alert: disk 91%", "listId": "ef5678" }`

## Invoke webhooks (incoming)

Board → integrations → create "invoke webhook"; call the URL:

```bash
curl -X POST "https://wekan.example.org/invite/hooks/<hook-id>?token=<token>" \
  -d "title=New order&comment=from the shop system"
```

## Webhooks (outgoing)

JSON per event (`activityType`: movedCard, addedCard, commented …) with board/list/card
IDs; a secret header is configurable.

## Rate limits

None built in; instance limits via the proxy.

## SDKs and client libraries

- no official SDKs; curl/requests recipes in the documentation/community
- import scripts (Trello) in the source code serve as an API reference

## Frontend note

The swimlane level extends the [board model](../../../../../../data/models.md)
(board → swimlane → list → card).
