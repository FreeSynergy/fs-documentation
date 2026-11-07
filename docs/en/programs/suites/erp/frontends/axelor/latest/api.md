# Axelor - API Documentation

## Overview

Every exposed model gets **REST endpoints under `/ws/rest/<model>`** (JSON): `fetch`, `search`, `create`, `update`, `delete`, plus custom actions. Batch calls are collected; authentication is via Basic (user/pass or API user), or JWT for token flows.

**Overview of API types**

| Type | Use | Status |
|-----|------------|--------|
| REST `/ws/rest/partner|saleOrder|invoice…` | CRUD + `search` query (JSON rules) | official (activatable per model) |
| `/ws/rest/batch` | multiple operations per request | official |
| Action endpoints (`/ws/rest/saleOrder/confirm` or similar) | workflow actions | official (custom actions) |
| Inbound webhooks | not built in (use batch/REST reactively) | ❌ |
| GraphQL | — | ❌ |

## Authentication

- `Authorization: Basic base64(user:pass)` (simple client standard)
- JWT after the login endpoint for session clients

## Core endpoints

| Method | Endpoint | Description |
|---------|----------|--------------|
| `GET` | `/ws/rest/partner/{id}` | Record |
| `POST` | `/ws/rest/partner` | create |
| `PUT` | `/ws/rest/partner/{id}` | update |
| `POST` | `/ws/rest/saleOrder/search` | search (`{"domain":[["state","=","confirmed"]],"fields":[…]}`) |
| `POST` | `/ws/rest/saleOrder/confirm` | model action (example) |
| `DELETE` | `/ws/rest/invoice/{id}` | delete |

## Example

Request:

```http
POST /ws/rest/partner/search HTTP/1.1
Authorization: Basic <bot:pass>
Content-Type: application/json

{ "domain": [["isCustomer","=",true]], "fields": ["fullName","email"], "limit": 50 }
```

Response: `200`

```json
{ "data": [ { "id": 41, "fullName": "Muster AG", "email": "vertrieb@muster.de" } ],
  "_searchCount": true }
```

## Batch

```http
POST /ws/rest/batch
{ "data": [ { "action": "create", "model": "partner", "data": {…} } ] }
```

## Rate limits

Not built in; gateway limits recommended.

## SDKs and client libraries

- No official SDKs; REST clients + Swagger export (make OpenAPI available per version)

## Skin note

Model name = endpoint: the skin mapping can read the model catalogue from builder metadata (analogous to [fields.md](../../../../../../data/fields.md)).
