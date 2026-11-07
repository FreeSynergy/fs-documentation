# HubSpot - API Documentation

## Overview

**CRM REST v3** (`https://api.hubapi.com/…`, JSON) with private app token; webhooks for object and email events; plus hub-specific APIs (marketing, forms, conversations).

**API types at a glance**

| Type | Usage | Status |
|-----|------------|--------|
| REST CRM v3 (`/crm/v3/...`) | Contacts, Companies, Deals, Tickets, Objects | official |
| Search API (`/crm/v3/objects/{type}/search`) | filter by properties | official |
| Associations (`/crm/v3/associations/...`) | object relations | official |
| Webhooks | crm.contact.created/updated/deleted, contactPropertiesChanged… | official (signed) |
| GraphQL | — | ❌ |

## Authentication

- **Private app token** (`Authorization: Bearer pat-…`) with fine-grained scopes (`crm.objects.contacts.read/write` …)
- OAuth2 (public apps); legacy API keys discontinued

## Core endpoints

| Method | Endpoint | Description |
|---------|----------|--------------|
| `GET` | `/crm/v3/objects/contacts?properties=email,firstname&after=…` | list (cursor) |
| `POST` | `/crm/v3/objects/contacts` | create |
| `GET/PATCH/DELETE` | `/crm/v3/objects/contacts/{id}` | detail |
| `POST` | `/crm/v3/objects/contacts/search` | search by properties |
| `POST` | `/crm/v3/associations/Contact/Company/default` | associate |
| `GET` | `/crm/v3/properties/contacts` | field properties (metadata) |
| `POST` | `/webhooks/v3/{appId}/subscriptions` | webhook subscription |

## Example

Request:

```http
POST /crm/v3/objects/contacts HTTP/1.1
Authorization: Bearer pat-abc
Content-Type: application/json

{ "properties": { "email": "a@example.org", "firstname": "Andrea",
                  "lastname": "Berg", "lifecyclestage": "lead" } }
```

Response: `201`

```json
{ "id": "1234567890", "properties": { "email": "a@example.org", "lifecyclestage": "lead",
  "createdate": "2026-10-31T16:55:02.123Z" }, "createdAt": "2026-10-31T16:55:02.123Z" }
```

## Webhooks

`POST /webhooks/v3/{appId}/settings` + subscriptions; payload signed (HMAC `x-hubspot-signature`), retry logic included.

## Rate limits

**~100 requests/10 s per portal/token** (higher on some plans, burst headers `x-rate-limit-*`); 429 with reset time.

## SDKs and client libraries

- Official client SDKs: Node (`@hubspot/api-client`), Python (`hubspot-api-client`), PHP, Java
- HubL/client JS for website context

## Skin note

Property API = field catalog for automatic mapping ([fields.md](../../../../../../data/fields.md)); lifecycle stages → standard pipeline field.
