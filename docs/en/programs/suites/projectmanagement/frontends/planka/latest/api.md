# Planka - API documentation

## Overview

Planka (Node.js + React, Sequelize) has a stable internal **REST API** that the frontend
itself uses — which makes it the documentable interface for frontend integrations.
Real-time changes run over a **Socket.io** channel.

**API kinds at a glance**

| Kind | Use | Status |
|------|-----|--------|
| REST `/api/all`, `/api/...` | full access to projects, boards, lists, cards, users | official-internal, stable |
| Socket.io (`/socket.io`) | live updates (card moved, comment) | official-internal |
| Webhooks | — | ❌ not available |
| GraphQL | — | ❌ not available |

## Authentication

- **Session cookie** (`sess`) after login; HTTP-only
- Alternative: **bearer token** (API token per user under account → API)
- Login: `POST /api/accessTokens` with e-mail/password; 2FA optional (TOTP)

## Main endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/all` | the whole state (projects, boards, lists, cards, users) in one go |
| `POST` | `/api/accessTokens` | login, sets the cookie |
| `POST` | `/api/projects` | create a project |
| `PATCH` | `/api/projects/{id}` | change a project |
| `DELETE` | `/api/projects/{id}` | delete a project |
| `POST` | `/api/boards/{boardId}/lists` | create a list/column |
| `POST` | `/api/lists/{listId}/cards` | create a card |
| `PATCH` | `/api/cards/{id}` | change a card (title, description, due date, listId) |
| `DELETE` | `/api/cards/{id}` | delete a card |
| `POST` | `/api/cards/{id}/comments` | comment |
| `POST` | `/api/cards/{id}/checklistItems` | subtask |
| `POST` | `/api/projects/{projectId}/users` | add a member |

## Example

Request:

```http
POST /api/lists/42/cards HTTP/1.1
Authorization: Bearer <api-token>
Content-Type: application/json

{
  "name": "Map the frontend API",
  "description": "Fields onto data/models.md",
  "dueDate": "2026-11-05T10:00:00.000Z",
  "labelIds": ["640f..."],
  "memberIds": ["641a..."]
}
```

Response: `201 Created` with the card object (`id`, `createdBy`, `listId`, `type: "tasks"`, `position`).

## Socket.io events (excerpt)

| Event | Direction | Description |
|-------|-----------|-------------|
| `card create/update/delete` | server → client | live board changes |
| `card move` | both ways | position/list changed |
| `comment create` | server → client | new comment |

## Rate limits

Built-in limits: ❌ (only Node defaults); proxy limits recommended for production.

## SDKs and client libraries

- Official SDKs: ❌
- Community: REST with any HTTP client; `fetch` examples in the Planka frontend source code (the authoritative reference)

## Frontend note

Map Planka cards onto the task model ([models.md](../../../../../../data/models.md)); the `position` field corresponds to the list sorting logic ([fields.md](../../../../../../data/fields.md)).
