# Sage - API Documentation

## Overview

**There is no single "Sage API".** Access per product:

| Product | API access | Status |
|---------|-----------|--------|
| Sage Business Cloud (accounting/CRM) | REST (developer.sage.global), OAuth2, webhooks | official |
| Sage 100 | "Sage 100 Connector/SDK", partly DB read access (licence required) | commercial |
| Sage 50 | import/export interfaces (file formats), no open REST | limited |
| Sage X3 | REST/middleware layer (version-specific), batch processes | official (project business) |

## Sage Business Cloud (representative)

**Auth**: OAuth2 (app registration in the Developer Portal), `Authorization: Bearer`.

**Core endpoints** (product variants differ — endpoint lists in the portal):

| Method | Endpoint (example) | Description |
|---------|---------------------|--------------|
| `GET` | `/contacts` | customers/suppliers |
| `GET/POST` | `/sales-invoices` | outgoing documents |
| `GET` | `/accounts` | chart of accounts |
| `POST` | `/webhooks` | event subscriptions |

**Example:**

```http
GET /sales-invoices?where=total_gt(1000)&pageSize=50 HTTP/1.1
Authorization: Bearer <token>
```

Response (JSON): document list with `id`, `contact`, `total`, `status` — field catalogue per endpoint documented in the portal.

## Sage 100/X3 (practice)

- Integration via official **connector licences** or export routines (CSV/ASCII, GoBD/DATEV formats)
- X3: REST function calls + "flows" (batches) via the middle layer of the project partner — detailed contracts are project-specific

## Rate limits

The Cloud portal documents limits per app/tenant (moderate; 429 backoff).

## Skin note

Sage skin = **adapter pattern**: a thin converter per Sage line onto FreeSynergy standard models; never model "Sage in general" ([models.md](../../../../../../data/models.md) + product switch).
