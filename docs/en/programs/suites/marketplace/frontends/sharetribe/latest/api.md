# Sharetribe - API Documentation

## Overview

The **Marketplace API** (`https://api.sharetribe.com/v1/`, JSON) is the core of the Flex/One platform: listings, users, bookings, transactions, reviews, images, webhooks. Custom frontends are built on it.

**API types at a glance**

| Type | Use | Status |
|-----|------------|--------|
| REST v1 (`/listings`, `/people`, `/bookings`, `/transactions`, `/reviews`) | marketplace CRUD | official |
| OAuth2 (client credentials; `Sharetribe-Application-Key`, `Sharetribe-Marketplace-ID` header) | app auth | official |
| Webhooks | transaction/listing events (signed) | official |
| GraphQL | — | ❌ |

## Authentication

```
POST /v1/token  (grant_type=client_credentials)
→ access_token (app identity; for user actions the `On-Behalf-Of: <userId>` header)
```

## Core endpoints

| Method | Endpoint | Description |
|---------|----------|--------------|
| `GET` | `/v1/listings/search?public_search=…&lat=&lng=&bound_n_km=5` | search (geo!) |
| `POST` | `/v1/listings` | create listing (listing_type, price, images) |
| `POST` | `/v1/images` | image upload (Base64) |
| `POST` | `/v1/people/create` | register user |
| `POST` | `/v1/booking` | request booking (listing, start/end) |
| `POST` | `/v1/transactions/initiate` | start transaction (depending on process type) |
| `POST` | `/v1/transactions/{id}/accept|transition` | process steps |
| `GET` | `/v1/reviews?listing=…` | reviews |

## Example

Geo search:

```http
GET /v1/listings/search?public_search=fahrrad%20lenen&
    lat=52.517&lng=13.404&bound_n_km=6 HTTP/1.1
Authorization: Bearer <token>
Sharetribe-Application-Key: <app-key>
Sharetribe-Marketplace-ID: <mp-id>
```

Response: `{ "data": [ { "id": "…", "attributes": { "title": "Lastenrad",
"price": { "amount": 1200, "currency": "EUR" }, "publicData": { "location": … }}}],
"meta": { "totalItems": 14 } }`

## Webhooks

Console → Integrations: events (`transaction transition requested/accepted`, `new listing`) → POST with `X-Sha1-HMAC` signature (secret).

## Rate Limits

Documented dynamically based on marketplace volume (spikes throttled; 429 with backoff).

## Skin note

Listing `publicData.location` = GeoJSON connection to maps skins; transaction/process model → [models.md](../../../../../../data/models.md) (offer/request/commitment/review).
