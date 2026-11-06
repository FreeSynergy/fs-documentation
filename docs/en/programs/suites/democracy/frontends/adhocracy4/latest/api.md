# Adhocracy4 - API Documentation

## Overview

Adhocracy4 exposes **REST endpoints per module** (ideas, comments, ratings, projects, map points; JSON, token authentication for write access). Evaluation dashboards read directly via the API.

**Overview of API types**

| Type | Use | Status |
|-----|------------|--------|
| REST `…/ideas/`, `…/comments/`, `…/ratings/`, `/api/projects/` | Module CRUD (read open, write requires authentication) | official |
| Token authentication (user token in header) | Write access | official |
| Export (CSV, administration) | Backing up project data | official |
| Webhooks/GraphQL | — | ❌ |

## Authentication

- Read: public (visible projects)
- Write: `Authorization: Token <user-token>` (session token of the platform)

## Core endpoints

| Method | Endpoint | Description |
|---------|----------|--------------|
| `GET` | `/api/projects/{id}/` | Project metadata (phases, modules) |
| `GET` | `/ideas/?project={id}` | Idea list (module path depends on deployment) |
| `GET/POST` | `…/ideas/{id}/comments/` | Comments |
| `GET/POST` | `…/ideas/{id}/ratings/` | Ratings (point +1/-1/0) |
| `POST` | `/ideas/` | Create idea (API clients = moderation) |

## Example

Request:

```http
GET /api/modules/87/ideas/?ordering=-positive_rating_count HTTP/1.1
Accept: application/json
```

Response:

```json
{ "count": 142, "results": [
  { "id": 903, "name": "Fountain instead of parking strip",
    "positive_rating_count": 31, "comment_count": 7,
    "point": { "type": "Point", "coordinates": [13.404, 52.517] } } ] }
```

## Rate limits

Set per deployment (default: no documented hard limits).

## Skin note

The `point` GeoJSON is the connection point to map skins ([positions](../../../../../apps/maps/standpunkte.md)); map the rating counter in [models.md](../../../../../../data/models.md) as "Support".
