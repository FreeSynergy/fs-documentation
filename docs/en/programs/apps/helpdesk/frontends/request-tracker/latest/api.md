# Request Tracker - API documentation

## Overview

RT has two official APIs: the classic **REST 1.0** (show/create/edit/correspond, text/plain + XML/JSON) and the more modern **JSON-RPC 2.0** (`/REST/2.0`). In addition there is the all-powerful CLI `rt`.

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| REST 1.0 (`/REST/1.0/...`) | show/create/edit/correspond/comment | official |
| REST 2.0 JSON-RPC (`/REST/2.0`) | Structured objects, bulk | official (since RT 4.4) |
| CLI `rt` | Everything, also cron automation | official |
| Webhooks | — | ❌ (extensions/triggers instead of webhooks) |

## Authentication

- **Basic auth** or `user=…&pass=…` (REST 1.0)
- **REST 2.0**: HTTP header `X-Rest-Protocol: JSON`, Basic or session cookie
- Create an API user with a reduced rights set (best practice)

## REST 1.0

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/REST/1.0/show/ticket/4711` | Ticket as a text object |
| `GET` | `/REST/1.0/search/tickets?query=…` | Query result |
| `POST` | `/REST/1.0/new/ticket` | Create (form: `Queue`, `Requestor`, `Subject`, `Text`) |
| `POST` | `/REST/1.0/edit/ticket/4711` | Change fields |
| `POST` | `/REST/1.0/comment/ticket/4711` | Internal note |
| `POST` | `/REST/1.0/correspond/ticket/4711` | Reply to the customer |

`?format=xml`/`out=json` optional.

## REST 2.0 (JSON-RPC)

```json
{
  "jsonrpc": "2.0",
  "method": "edit",
  "params": {
    "type": "ticket",
    "objects": ["4711"],
    "data": { "Status": "resolved" }
  },
  "id": 3
}
```

Response:

```json
{
  "jsonrpc": "2.0",
  "result": { "action": "set", "tickets": [{ "id": "4711", "Status": "resolved", "LastUpdated": "2026-10-31T14:00:00Z" }] },
  "id": 3
}
```

Important methods: `create`, `edit`, `show`, `lookup`, `search`, `correspond`, `comment`, `user_tickets`, `tickets_who_have_queue`.

## Example (curl, REST 2.0)

```bash
curl -u svc-bot:secret -H 'X-Rest-Protocol: JSON' -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","method":"search","params":{"type":"ticket","queue":"hw","query":"Status = new"},"id":1}' \
  https://rt.example.org/REST/2.0
```

## Rate limits

None built in; best practices: your own API user, proxy limits, avoid transaction floods via scrips.

## SDKs and client libraries

- The Perl API (`RT->API`) as the reference in the core
- Community: Python `rtrest`, Node `rt-client`; REST 2.0 is trivial in any language

## Skin note

The transaction model (ticket = header, transactions = events) is the model for the [comment/event model](../../../../../../data/models.md).
