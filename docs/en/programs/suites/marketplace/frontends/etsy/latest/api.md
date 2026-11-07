# Etsy - API Documentation

## Overview

**Open API v3** (`https://openapi.etsy.com/v3`, JSON). Read access with an API key; extended read/write operations with an OAuth2 access token (scopes such as `listings_r`, `listings_w`, `receipts_r`, `shops_r`, `feedback_r`). App approval required.

**API types at a glance**

| Type | Use | Status |
|-----|------------|--------|
| REST v3 | shops, listings, receipts, reviews, taxonomy | official (app acceptance) |
| OAuth2 Authorization Code + **PKCE** | user access | official |
| Webhooks | — | ❌ (polling) |
| GraphQL | — | ❌ |

## Authentication

```
GET /v3/application/shops/{shopId}?api_key=<key>          (app level)
Authorization: Bearer <oauth-access-token>                (user level)
```

## Core endpoints

| Method | Endpoint | Description |
|---------|----------|--------------|
| `GET` | `/v3/shops/{shop_id}/listings?limit=25&includes=Images` | listings |
| `GET` | `/v3/shops/{shop_id}/receipts` | orders |
| `POST/PATCH` | `/v3/shops/{id}/listings` / `/v3/listings/{id}` | create/change (scopes `listings_*`) |
| `GET` | `/v3/ships-to-regions`, `/v3/taxonomy/…*` | shipping/taxonomy helpers |
| `GET` | `/v3/listings/{id}/reviews` | reviews |

## Example

```http
GET /v3/shops/12345678/receipts?limit=50&sort_field=created&sort_order=desc
x-api-key: <api-key>
Authorization: Bearer <token-mit-receipts_r>
```

Response:

```json
{ "count": 50, "results": [
  { "receipt_id": 998877, "listing_id": 554433, "name": "Keramikset",
    "quantity": 1, "total_price": { "amount": 5240, "scale": 2, "currency_code": "EUR" },
    "shipping_address": { "name": "…", "country": "DE" }, "is_shipped": false } ] }
```

## Rate Limits

**~10,000 requests/day per app** (documented guideline; 429 + backoff, header `X-Edg-Ratelimit-*`).

## SDKs and client libraries

- official: OpenAPI spec + sample scripts; community wrappers (Python/Node)

## Skin note

A `receipts` poll (5–15 min) replaces missing webhooks; normalize field names in [fields.md](../../../../../../data/fields.md) (amounts with `scale`!).
