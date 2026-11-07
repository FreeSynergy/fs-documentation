# ERPNext - API Documentation

## Overview

Frappe provides a **generic JSON REST API for all doctypes**: `/api/resource/<DocType>`. The schema (field types, links, mandatory fields) can be read via the API itself — ideal for skin mapping. Webhooks for changes.

**Overview of API types**

| Type | Use | Status |
|-----|------------|--------|
| REST `/api/resource/<DocType>` | CRUD + lists (filter/sort/pagination) | official |
| `/api/method/<path>` | whitelisted Python functions (workflow actions, reports) | official |
| Doctype metadata (`/api/v2/doctype/<name>`) | field catalogue | official |
| Webhooks | doctype event → POST (secret signature) | official |
| GraphQL | — | ❌ |

## Authentication

- User API key/secret: `Authorization: token <api_key>:<api_secret>`
- OAuth2/OIDC (providers such as Server), cookie session for UI clients

## Core endpoints

| Method | Endpoint | Description |
|---------|----------|--------------|
| `GET` | `/api/resource/Customer?filters=[["mobile_no","like","%1234"]]` | list |
| `POST` | `/api/resource/Customer` | create |
| `GET/PUT/DELETE` | `/api/resource/Customer/CUST-00042` | detail (named IDs!) |
| `POST` | `/api/method/frappe.client.insert` | generic insert |
| `GET` | `/api/v2/doctype/Sales Invoice/` | metadata field list |
| `POST` | `/api/method/erpnext.controllers.website_list_for_contact…` | module methods |

## Example

Request:

```http
POST /api/resource/Sales Invoice HTTP/1.1
Authorization: token abc123:def456
Content-Type: application/json

{ "customer": "Kunde X", "due_date": "2026-11-15",
  "items": [{ "item_code": "BERATUNG-TAG", "qty": 3, "rate": 850 }] }
```

Response: `200` → document JSON (`name`: `ACC-SINV-2026-00117`, `rounded_total`: 2550, links, `doctype`).

## Webhooks

Doctype + event (after_insert/on_submit…), callback + signing secret; payload contains document JSON + `request_id`.

## Rate limits

No built-in default limits; Frappe Cloud/proxy set quotas.

## SDKs and client libraries

- `frappe` Python library (official, server-side + client use), community SDKs (Node/PHP)
- Postman collection in the Frappe documentation

## Skin note

Doctype metadata → automatic [mapping](../../../../../../data/fields.md); watch named document IDs (`CUST-…`) in composite models.
