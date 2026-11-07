# Make - API Documentation

## Overview

REST API under `https://api.eu1.make.com/api/v2` (EU instances; `api.make.com` global), JSON, token-based. It manages scenarios (start/pause/scheduling), users/organizations, connections; data stores via the "Make table tools" app.

**API types at a glance**

| Type | Use | Status |
|-----|------------|--------|
| REST v2 | users, scenarios (CRUD + scheduling), logs, webhooks | official (API plan required) |
| Custom webhooks (scenario triggers) | `hooks.make.com/<id>` | official |
| "Make table tools" app API | Records in Make tables | official (app) |
| GraphQL | — | ❌ |

## Authentication

- API token (org or user scope): header `Authorization: Token <key>`
- OAuth2 for your own apps/integrations (developer account)

## Core endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| `GET` | `/users/{userId}/scenarios` | List scenarios |
| `POST` | `/users/{userId}/scenarios` | Create scenario (scenario JSON/code) |
| `POST` | `/users/{userId}/scenarios/{id}/schedule` | Scheduling (Minutes/Every/Never) |
| `POST` | `/users/{userId}/scenarios/{id}/start` / `stop` | On/off |
| `GET` | `/users/{userId}/scenarios/{id}/executions` | Executions |
| `GET/POST` | `/users/{userId}/connections` | Connections (app access) |
| `POST` | `/users/{userId}/webhooks` | Create webhook endpoints |

## Example

```http
POST /api/v2/users/123456/scenarios/7890/schedule HTTP/1.1
Authorization: Token <api-token>
Content-Type: application/json

{ "schedule": { "type": "Every", "every": 15 } }
```

Response: `201` / updated scenario record (`id`, `isPaused:false`, `scheduling`).

## Rate limits

Documented quotas per plan (requests per minute moderate, 429 + retry); exact figures in the API documentation.

## SDKs and client libraries

- Official Postman collection; community wrappers (Python/Node)
- Scenario import/export: scenario code (share link/JSON) + API `POST scenarios`

## Skin note

Scenario object (trigger, modules, routes, scheduling) as a template for the flow model ([models.md](../../../../../../data/models.md)).
