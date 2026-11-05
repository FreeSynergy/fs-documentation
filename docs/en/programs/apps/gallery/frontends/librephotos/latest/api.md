# LibrePhotos - API documentation

## Overview

Django-REST endpoints under `/api/`, used by the web UI and the apps. The API is functionally complete, but not versioned and without an official OpenAPI reference.

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| REST JSON `/api/...` | Photos, albums, people, search, upload | official (stably undocumented) |
| Django admin | Administration | web only |
| Celery jobs | Scan, ML | internal |
| GraphQL / webhooks | — | ❌ |

## Authentication

- **Token**: `Authorization: Token <token>` (the login endpoint provides the token)
- **Session cookie** in the browser
- Two-factor optional for accounts

## Core endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/auth/token/` | Login, provides token |
| `GET` | `/api/photos` | Listing with filters (`user`, `album`, `date`) |
| `GET` | `/api/photos/{id}` | Detail incl. EXIF and faces |
| `POST` | `/api/photos/upload/` | Upload (multipart) |
| `GET` | `/api/search` | Full-text and semantic (`search_text`, `time`) |
| `GET/POST` | `/api/albums` | Read/create albums |
| `POST` | `/api/albums/{id}/photos` | Add captures |
| `GET` | `/api/people` | People and faces |
| `POST` | `/api/people/{id}/merge` | Merge people |
| `POST` | `/api/share` | Album sharing (link/user) |
| `POST` | `/api/tasks/scan` | Trigger a scan task |

## Example

Request:

```http
POST /api/search HTTP/1.1
Authorization: Token <token>
Content-Type: application/json

{ "search_text": "dog in the garden", "user": 3, "time": "all" }
```

Response: `200 OK` with `{ "results": [ { "id": 812, "image": "/media/samples/…jpg" } ] }`.

## Rate limits

No API limits are preconfigured; Django caching and reverse-proxy limits are recommended.

## SDKs and client libraries

- **official**: no SDKs; the reference is the API calls of the React client
- **community**: Python scripts for import/export in repository dependencies
- **export**: folder export via the admin command `manage.py export`

## Frontend note

The photo/album/person model corresponds to [models.md](../../../../../../data/models.md); because versioning is missing, field changes should be checked on upgrades.
