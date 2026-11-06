# Consul - API Documentation

## Overview

Consul publishes **REST JSON endpoints** for participation data (proposals, debates, polls, budget items) plus OAuth2 for app access. The API is primarily read-only; write endpoints depend on the version and installation — check.

**Overview of API types**

| Type | Use | Status |
|-----|------------|--------|
| REST `/api/v1/…` (e.g. proposals, polls, budgets) | Public content | official |
| OAuth2 authentication for private content and apps | Access | official |
| Webhooks | Depends on version/installation (older versions without) | limited |
| GraphQL | — | ❌ |

## Authentication

- Public endpoints: none
- Apps: OAuth2 (client credentials/authorisation code); the administrator grants access

## Core endpoints

| Method | Endpoint | Description |
|---------|----------|--------------|
| `GET` | `/api/v1/proposals.json` | Proposals (pagination, `sort`) |
| `GET` | `/api/v1/proposals/{id}.json` | Detail |
| `GET` | `/api/v1/polls.json` | Votes |
| `GET` | `/api/v1/budgets.json` + `/budgets/{id}/investments` | Citizen budget |
| `GET` | `/api/v1/debates.json` | Debates |

## Example

Request:

```http
GET /api/v1/proposals.json?limit=20&sort=supports_count HTTP/1.1
Accept: application/json
```

Response:

```json
{ "data": [
  { "id": 903, "title": "Bike street north", "supports": 812,
    "theme": "Movilidad", "url": "https://consul.example/proposals/903" } ] }
```

## Rate limits

Set per instance (city server); usual practice is generous limits for read access.

## Skin note

JSON field names (supports_count, investments) can be adopted directly as a reference in [models.md](../../../../../../data/models.md); for live sync, plan export jobs instead of webhooks.
