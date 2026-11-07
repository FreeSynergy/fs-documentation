# Tryton - API Documentation

## Overview

Tryton servers speak **XML-RPC or JSON-RPC** under `/rpc` (also `/jsonrpc`). Pattern: `common.login` → session ID; afterwards model methods as RPC function names `Model.<name>.execute_kw`. Field/model metadata are themselves RPC objects — schema readable.

**Overview of API types**

| Type | Use | Status |
|-----|------------|--------|
| RPC `Model.x.read/create/write/unlink` | CRUD (execute/execute_kw) | official (core) |
| `common.login`/`common.session_login` | authentication | official |
| `ir.model*` models | field catalogue/metadata | official |
| Webhooks | not built in | ❌ |
| GraphQL | — | ❌ |

## Authentication

```
common.login(database="firma", user="sync", password="…", context={})
→ { "session": "2c7d…", "user_id": 3 }
```

Every model call carries `session` + `context` (language, company IDs).

## Core methods

| Method (RPC name) | Description |
|--------------------|--------------|
| `Model.account.move.execute` | `read`/`create`/`write` wrapper via execute_kw |
| `Model.party.find_and_count(domain)` | search |
| `Model.sale.sale.action_confirm([ids])` | workflow actions |
| `Model.ir.model_fields.read(...)` | field catalogue for mapping |
| `common.set_metadata` / `common.message` | client handling |

## Example (JSON-RPC)

Request:

```json
{ "method": "call", "params": {
  "id": 1, "method": "Model.party.execute_kw",
  "args": ["2c7d…", {"language":"de_DE","tz":"Europe/Berlin"},
           [], "search_read", [[["name","like","%Muster%"]],
           ["name","email"]], {"limit": 20}] } }
```

Response: `result: [{ "id": 41, "name": "Muster AG", "email": "vertrieb@muster.de" }]`

## Workflow actions

`Model.sale.sale.action_confirm` / `action_process` — state transitions explicit (state fields), exactly as in the client.

## Rate limits

None built in; server/proxy limits.

## SDKs and client libraries

- **Official**: `trytond` library (client code uses the same classes), `proteus` (ORM-like Python client)
- JSON-RPC recipes in the Tryton wiki

## Skin note

Always set `context` (language/company/TZ) explicitly in sync skins — the most frequent source of errors; metadata via `ir.model.fields` → [fields.md](../../../../../../data/fields.md).
