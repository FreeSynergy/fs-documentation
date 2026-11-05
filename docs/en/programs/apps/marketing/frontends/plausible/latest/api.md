# Plausible - API documentation

## Overview

Two lean interfaces: the **events API** (tracking without/in addition to the script) and the **stats API** (read access to the dashboard metrics). Plus a CSV/JSON export of the raw data (self-hosted: ClickHouse directly).

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| Events API (`POST /api/event`) | Custom events/goals from apps | official |
| Stats API (`GET /api/v1/stats/*`) | Timeseries, top values, aggregation | official (API key) |
| Export (self-hosted) | JSON raw data export endpoint | official |
| GA import | Import assistant | official |
| Webhooks/GraphQL | — | ❌ |

## Authentication

- Events API: none (the domain reference works via `url`/referrer checks; `X-API-Key` optional)
- Stats API: `Authorization: Bearer <api-key>`

## Core endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/event` | Event (`name`, `url`, `props`) |
| `GET` | `/api/v1/stats/realtime/visitors` | Live visitors |
| `GET` | `/api/v1/stats/timeseries` | Daily series (filters `period`, `date`, `filters`) |
| `GET` | `/api/v1/stats/aggregate` | Metrics aggregated |
| `GET` | `/api/v1/stats/top-pages` | Top pages |

## Example

Report a goal:

```http
POST /api/event HTTP/1.1
Content-Type: application/json

{ "name": "Donation", "url": "https://org/donate",
  "domain": "org.example", "props": { "amount": 25 } }
```

Response: `202`.

Metrics:

```http
GET /api/v1/stats/aggregate?site_id=org.example&period=30d
    &metrics=visits,conversion_rate&filters=event:is:Donation
Authorization: Bearer <api-key>
```

## Rate limits

Cloud: generous limits (events throttled roughly per domain); self-hosted: the server.

## SDKs and client libraries

- Official JS/HTTP documentation, community wrappers (Python), plug-ins for CMSs
- Events signature header (observe the self-hosted `reverse_proxy` notes)

## Skin note

The goal name = the standard event word in [fields.md](../../../../../../data/fields.md); the stats API is ideal for wiki KPI tiles (caching! 5–10 min).
