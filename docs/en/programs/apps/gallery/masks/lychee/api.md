# Lychee - API documentation

## Overview

Lychee v5 speaks a JSON REST API under `/api`. The frontend and mobile clients use these endpoints exclusively; the reference lives in the repository (`openapi` branches) and in the controller sources.

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| REST JSON `/api/...` | Albums, photos, shares, users, settings | official |
| Share links `/public/…` | public access to albums | official |
| Webhooks / GraphQL | — | ❌ |

## Authentication

- **Session**: login `/api/Login` with user/password, cookie session
- **API token**: `Authorization: Bearer <token>` (can be created in the user settings)
- **OAuth2/OIDC**: provider login, then a regular session

## Core endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/Albums` · `GET /api/Root` | Root trees: albums, photos, tags |
| `GET` | `/api/Album?id=<id>` | Album with photos and preview levels |
| `POST` | `/api/Album` | Create album (`title`, `parent_id`) |
| `POST` | `/api/Album/{id}` | Change album |
| `DELETE` | `/api/Album/{id}` | Delete album |
| `POST` | `/api/Photo` | Upload photo (multipart, `album_id`) |
| `GET` | `/api/Photo?id=<id>` | Photo details |
| `POST` | `/api/Photo/{id}` | Change (title, description, favourite, rotation) |
| `DELETE` | `/api/Photo/{id}` | Delete photo |
| `POST` | `/api/Share/Album` | Share (`can_download`, `password`, `expires_at`) |
| `GET` | `/api/Share` | List own shares |
| `POST` | `/api/Search` | Search by title/description/album |
| `GET` | `/api/Instances` | Version, settings (diagnostics) |

## Example

Request:

```http
POST /api/Album HTTP/1.1
Authorization: Bearer <token>
Content-Type: application/json

{ "title": "Sommer 2026", "parent_id": null, "sort": "date_desc" }
```

Response: `200 OK` with `{ "data": { "id": "Abc123", "title": "Sommer 2026" } }`.

## Rate limits

No API quotas are built in; limits in the web server and upload sizes via `post_max_size`/`upload_max_filesize` are recommended.

## SDKs and client libraries

- **official**: no SDKs, but complete API usage in the React frontend as the reference
- **community**: Python/Node clients for bulk upload
- **import**: URL import, Lightroom export folders

## Skin note

Album/photo/share correspond to the standard model ([modelle.md](../../../../../data/modelle.md)); IDs are strings and must be treated as such.
