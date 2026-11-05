# GLPI - API documentation

## Overview

GLPI offers an official **REST API** (`/apirest.php`) with session-based authentication: init → session token → CRUD calls. It covers practically all object types generically (`Ticket`, `Computer`, `User`, …).

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| REST `/apirest.php` | CRUD + search for all core objects | official |
| XML-RPC (old) | Legacy integration | deprecated |
| Plugin APIs | e.g. webhooks, inventory | plugin-dependent |
| GraphQL | — | ❌ |

## Authentication

1. `POST /apirest.php/initSession` with header `Session-Token: empty` and credentials
   - `Authorization: Basic …` or `Login+Password`
   - or an API token (`App-Token`) + user/key for service accounts
2. The response provides `session_token`; all subsequent requests with header `Session-Token: <t>`
3. `killSession` to terminate

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/salut.php` | Health check |
| `POST` | `/apirest.php/initSession` | Start a session |
| `POST` | `/apirest.php/{Objekt}` | Create (`input={…}`) |
| `GET` | `/apirest.php/{Objekt}/{id}` | Read |
| `GET` | `/apirest.php/{Objekt}` (with `range`, `order`) | List |
| `POST` | `/apirest.php/{Objekt}/{id}` | Change (`input={…}`) |
| `DELETE` | `/apirest.php/{Objekt}/{id}` | Delete |
| `GET` | `/apirest.php/{Objekt}/search?criteria=[…]` | Search with filter criteria |
| `GET` | `/apirest.php/Ticket/{id}/getFollowups` | Subobjects (followups, tasks, documents) |
| `POST` | `/apirest.php/Entity/{id}/changeActiveEntity` | Switch entity/entity |

## Example

Request:

```http
POST /apirest.php/HTTP/1.1
Host: glpi.example.org
Session-Token: abc123
Content-Type: application/json

{ "input": {
    "name": "VPN bricht ab",
    "content": "seit 08:40 mehrfach",
    "categories_id": 12,
    "entities_id": 0,
    "users_id_recipient": 5 } }
```

Response:

```json
{ "id": 9982 }
```

## Rate limits

None built in; session timeout (default 30 min) and `App-Token` rotation are admin-side.

## SDKs and client libraries

- **official**: PHP libraries (glpi-project); REST with any HTTP client
- **community**: Python wrappers (`pyglpi`), Node examples
- **CLI**: `glpi:crm:*` console commands for maintenance

## Skin note

The ticket↔asset link is what is distinctive about GLPI — FreeSynergy skins map it onto relations in the [model set](../../../../../../data/models.md) (`ticket.related = [file, device]`).
