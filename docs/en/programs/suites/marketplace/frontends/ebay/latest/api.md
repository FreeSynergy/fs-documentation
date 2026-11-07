# eBay - API Documentation

## Overview

Modern **Sell/Browse family** (JSON, REST): `Inventory API` (items), `Listing API` (offers), `Sell Feed API` (bulk), `Fulfillment API` (orders), `Browse API` (catalog/search). Plus the classic Trading API (XML). Everything uses OAuth2.

**API types at a glance**

| Type | Use | Status |
|-----|------------|--------|
| REST `https://api.ebay.com/sell/inventory/v1/…` | inventory items | official |
| REST `/sell/listing/v1/inventory_listing/` | create/change listings | official |
| REST `/sell/fulfillment/v1/order/…` | orders, shipping status | official |
| REST `/buy/browse/v1/item/search` | search (market research) | official |
| Trading XML (`verifyAddItem` etc.) | legacy | official |
| Push events | not freely available; polling/feed status | limited |

## Authentication

1. App in the Developer Portal (request auth scopes)
2. Application token: `POST /identity/v1/oauth2/client_token` (client_credentials)
3. User token: authorization code flow → access + refresh; `Authorization: Bearer`

## Core endpoints

| Method | Endpoint | Description |
|---------|----------|--------------|
| `PUT` | `/sell/inventory/v1/inventory_item/{sku}` | create/update item |
| `POST` | `/sell/inventory/v1/inventory_item/{sku}/offer` | marketplace offer (price, marketplace_id EBAY_DE) |
| `POST` | `/sell/listing/v1/inventory_listing/` | publish listing (auction/FixedPrice) |
| `GET` | `/sell/fulfillment/v1/order?orderStatus=INTEGRATION_PENDING` | orders |
| `POST` | `/sell/fulfillment/v1/order/{id}/shipping_fulfillment` | report shipment (tracking) |
| `GET` | `/buy/browse/v1/item/search?q=…&fieldgroups=…` | market search |

## Example

```http
POST /sell/listing/v1/inventory_listing/ HTTP/1.1
Authorization: Bearer <user-access-token>
Content-Type: application/json

{ "sku": "KER-004", "marketplaceId": "EBAY_DE", "format": "FIXED_PRICE",
  "availableForCheckout": true,
  "listingPolicyId": "5000123", "fulfillmentPolicyId": "5000234" }
```

Response: `{ "listingId": "…", "sku": "KER-004", "status": "PUBLISHED" }`

## Rate Limits

Documented per API/operation (e.g. several hundred requests/min plus daily quotas per seller level); errors `429` + `X-ebay-*` headers.

## SDKs and client libraries

- official SDKs (Node/Java), Postman collections; Trading SDK historical

## Skin note

Order/listing readers for dashboard skins; normalize fee/field names in [fields.md](../../../../../../data/fields.md); observe API usage policies (compliance skin!).
