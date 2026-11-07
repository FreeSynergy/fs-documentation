# CS-Cart Multi-Vendor - API Documentation

## Overview

CS-Cart exposes a **REST API (`/api`)** for core objects: products, orders, categories, customers, shipments. Multivendor fields (vendor_id, fees) are integrated. Authentication via API key (scope admin/seller/customer).

**API types at a glance**

| Type | Use | Status |
|-----|------------|--------|
| REST `/api/products|orders|…` | CRUD with JSON | official |
| API keys (per role) | authentication | official |
| Webhooks (add-on/core depending on version) | order/product events | check (version) |
| GraphQL | — | ❌ |

## Authentication

- Create the API key in the backend; request header `Authorization: <key>` (scheme per version in the knowledge base)

## Core endpoints

| Method | Endpoint | Description |
|---------|----------|--------------|
| `GET/POST` | `/api/products` | Products (filterable by `vendor_id`) |
| `GET/PUT` | `/api/products/{id}` | Detail/change |
| `GET` | `/api/orders?status=open` | Orders |
| `PUT` | `/api/orders/{id}` | Status updates (vendor view) |
| `GET/POST` | `/api/categories`, `/api/products/{id}/images` | Catalog parts |

## Example

Request:

```http
GET /api/products?fields=product_id,product,vendors,price&limit=50 HTTP/1.1
Authorization: <api-key>
```

Response (excerpt):

```json
{ "products": [ { "product_id": 1042, "product": "Keramikset",
  "price": "48.00", "vendors": [{ "vendor_id": 3, "company": "Töpferei Nord" } ] } ] }
```

## Rate Limits

Not hard-coded; hosting limits and throttling recommended.

## Skin note

The `vendor_id` relation is the marketplace feature in the data model → [models.md](../../../../../../data/models.md) (listing ↔ provider); normalize sync fields in [fields.md](../../../../../../data/fields.md).
