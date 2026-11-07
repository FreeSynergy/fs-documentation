# Odoo - API Documentation

## Overview

By default, Odoo instances speak **XML-RPC/JSON-RPC** against the ORM (`/XML-RPC/common`, `/jsonrpc`) — every model and every field is reachable this way. Newer versions add **REST modules** (standardised REST endpoints, available per version/plan — check current state) and webhooks (Enterprise).

**Overview of API types**

| Type | Use | Status |
|-----|------------|--------|
| XML-RPC/JSON-RPC (`execute_kw`) | model CRUD, search/read/create/write/unlink | official (standard) |
| REST (`/api/…` via REST module) | JSON endpoints per model/endpoint | officially new (check case by case) |
| Webhooks (ir.ql/Enterprise) | record changes → POST | official (Enterprise features) |
| OAuth2/OIDC | API access, portal login | official (newer versions) |
| GraphQL | — | ❌ |

## Authentication

- Session-based: `uid` + `password`/API key per RPC call (`database, uid, password, model, method, args`)
- API keys for users (Settings → Account), OAuth2 for new REST APIs

## Core operations (RPC)

| Method | Description |
|---------|--------------|
| `execute_kw(db, uid, pw, model, "search", [[domain]])` | IDs after filter |
| `…, "read", [[ids], [fields]]` | read records |
| `…, "create", [{fields}]` | create |
| `…, "write", [[ids], {fields}]` | change |
| `…, "name_create" / "web_search_read"` | convenience methods |
| Workflow methods (`action_confirm`, `action_invoice_create`) | state transitions |

## Example

Request (JSON-RPC envelope shortened):

```json
{ "jsonrpc":"2.0", "method":"call", "params": {
  "service":"common","method":"authenticate","params":["demo","api_user","key"] }, "id":1 }
```

Record:

```json
{ "service":"object","method":"execute_kw",
  "params":["demo", 2, "key", "res.partner", "create",
     [{"name":"Muster AG","email":"vertrieb@muster.de","phone":"+49 30 1234"}]] }
```

Response: `1234` (record ID).

## Webhooks (Enterprise)

Settings → Webhooks: event (create/update) + secret; HMAC-signed JSON payloads to the callback URL.

## Rate limits

No built-in limits (instance/worker limits); throttle JSON-RPC at the reverse proxy.

## SDKs and client libraries

- `xmlrpc.client` (stdlib), **`odoo` Python library** / `odoorpc`, JS RPC in the web framework
- `odoo-bin shell` for ORM interaction from the console

## Skin note

Model/field catalogue via RPC (`ir.model.fields`) = ideal source for automatic mapping ([fields.md](../../../../../../data/fields.md)).
