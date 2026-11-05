# osTicket - API documentation

## Overview

osTicket v1 has a lean **REST API** (JSON, also XML) with an API key. It covers tickets and user profiles; deeper customizing runs directly through the database (not supported).

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| REST `/api/v1/tickets.json` … | Create/read tickets, append, assign | official |
| Email ingest (subject header) | Ticket/thread control via mail | official |
| XML variant `.xml` | Alternative | official |
| Webhooks | — | ❌ |

## Authentication

- **API key** from admin → API settings, header `X-API-Key: <key>` or query `api=`
- Alternatively a ticket "user key" (link token) for read-only ticket access

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/v1/tickets.json` | Create a ticket |
| `GET` | `/api/v1/tickets.json?ticket=#4711&key=…` | Read a ticket (with user-key or key+Q) |
| `POST` | `/api/v1/tickets/answer.json` | Append an answer |
| `POST` | `/api/v1/tickets/note.json` | Internal note |
| `POST` | `/api/v1/tickets/claim.json` | Assign |
| `POST` | `/api/v1/tickets/close.json` | Close |
| `POST` | `/api/v1/users.json` | Create/update a customer profile |
| `GET` | `/api/v1/users.json?q=b@example.org` | Search for a profile |

## Example

Request:

```http
POST /api/v1/tickets.json HTTP/1.1
X-API-Key: <api-key>
Content-Type: multipart/form-data; charset=utf-8

name=Ben Klein&email=b@example.org&subject=Drucker offline&topic=hardware&message=Seit 9 Uhr...
```

Response:

```json
{ "data": { "number": "XRT-4712", "status": "open", "url": "https://help.example.org/?a=tickets&t=XRT-4712&key=..." } }
```

## Email control

In the subject: replying to a ticket reference `Re: [#XRT-4712 …]` preserves the thread; `#topic-slug`, `#status-open`, `#pri-high` set fields on ingest.

## Rate limits

None built in; limit via the web server/anti-spam (flood thresholds in the ticket settings).

## SDKs and client libraries

- Official SDKs: ❌ (curl/`requests` recipes in the API docs)
- CLI: your own scripts against the API; import wizard for legacy tickets (CSV)

## Skin note

The status model new/open/pending/closed → the standard ticket status list ([models.md](../../../../../../data/models.md)); the API field names correspond to [fields.md](../../../../../../data/fields.md).
