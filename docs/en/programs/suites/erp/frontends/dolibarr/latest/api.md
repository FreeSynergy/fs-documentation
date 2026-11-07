# Dolibarr - API Documentation

## Overview

**REST API v3** under `/api/index.php` (JSON), enabled under Home → Modules → "API REST". Objects as endpoints (thirdparties, invoices, orders, products, projects, users, members…), CRUD + filters. API keys per user. Webhooks via the add-on module "API REST hooks"; internally there are additionally trigger/hook classes for PHP extensions.

**Overview of API types**

| Type | Use | Status |
|-----|------------|--------|
| REST v3 (`/api/index.php/<object>`) | CRUD, lists (limit/sortfield/`sqlfilters`) | official |
| API key (`Authorization: Bearer` / `?apikey=`) | authentication | official |
| Webhooks (module) | object events → POST | official (module) |
| PHP triggers (`modXxx::…`) | server-side hooks for modules | official |
| GraphQL | — | ❌ |

## Authentication

1. Admin → Users → generate API keys
2. `Authorization: Bearer <key>` (recommended) or session token after login

## Core endpoints

| Method | Endpoint | Description |
|---------|----------|--------------|
| `GET` | `/api/index.php/thirdparties?limit=10&sortfield=t.rowid&sortorder=DESC&sqlfilters=(t.nom:LK:%25GmbH%25)` | filter third parties |
| `GET/POST/PUT/DELETE` | `/api/index.php/thirdparties/{id}` | detail/CRUD |
| `GET/POST` | `/api/index.php/invoices` | customer invoices (POST with `lines` array) |
| `GET` | `/api/index.php/invoices/{id}` | incl. lines/payments |
| `POST` | `/api/index.php/orders` | orders |
| `GET/POST` | `/api/index.php/products` | products |
| `GET/POST` | `/api/index.php/projects` | projects |

## Example

Request:

```http
GET /api/index.php/thirdparties?sqlfilters=(t.client:=:2)&limit=50 HTTP/1.1
Authorization: Bearer <api-key>
Accept: application/json
```

Response: `200`

```json
{ "count": 2, "thirdparties": [
  { "id": 12, "nom": "Muster AG", "client": 1, "email": "vertrieb@muster.de",
    "code_client": "CLI-0012" } ] }
```

Create an invoice: `POST /api/index.php/invoices` with `{ "socid": 12, "type": 0, "lines": [{"product_id": 3, "qty": 2, "price": 120}] }`.

## Webhooks (module)

Activate the module → define hooks (object + event such as `createInvoice`), payload as JSON to the target URL; signature optionally configurable.

## Rate limits

No internal limits; hosting/proxy level.

## SDKs and client libraries

- No official SDKs; `curl` recipes in the online documentation (dolibarr.org/wiki)
- Community libraries (PHP/Node) for API v3

## Skin note

Encapsulate the `sqlfilters` syntax (t.field:op:value) cleanly in sync skins; document the numeric prefix `CLI-…` as in [fields.md](../../../../../../data/fields.md).
