# PhotoPrism - API documentation

## Overview

PhotoPrism provides a JSON REST API under `/api/v1` (documentation at `/api` or Swagger). The web UI and the CLI (`photoprism command`) use the same endpoints.

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| REST JSON `/api/v1/...` | Photos, albums, folders, labels, people, search | official |
| CLI commands | Index, backup, admin tasks | official |
| Webhooks | Index/media events | optional |
| GraphQL | — | ❌ |

## Authentication

- **Basic**: `Authorization: Basic base64(user:pass)` for account access
- **Bearer/client**: `Authorization: Bearer <client-secret>` with scopes (`read`, `write`)
- **Session**: Cookie after login for the web UI

## Core endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/v1/photos?q=<suche>&count=60` | Search (label, person, place, period) |
| `GET` | `/api/v1/photos/{uid}` | Detail with EXIF and labels |
| `POST` | `/api/v1/photos` | Create photo/upload (`data`, `upload[]`) |
| `PUT` | `/api/v1/photos/{uid}` | Change (title, label, favourite, public) |
| `DELETE` | `/api/v1/photos/{uid}` | Remove from the index |
| `GET` | `/api/v1/albums` · `POST /api/v1/albums` | Read/create albums |
| `GET` | `/api/v1/folders/{uid}` | Folder tree |
| `GET/POST` | `/api/v1/batch` | Batch actions (label, album, public) |
| `GET` | `/api/v1/labels` · `POST /api/v1/labels` | Labels, confirm AI suggestions |
| `GET` | `/api/v1/people` · `PUT /api/v1/people/{uid}` | Name people, crop face |
| `POST` | `/api/v1/index` | Trigger an index recalculation |
| `GET` | `/api/v1/file/{hash}` | File/preview stream at the desired size |
| `POST` | `/api/v1/share` | Share link with expiry and password |

## Example

Request:

```http
GET /api/v1/photos?q=label:beach+person:anna&count=10 HTTP/1.1
Authorization: Bearer <client-secret>
Accept: application/json
```

Response: `200 OK` with `{ "data": [ { "id": "abc123", "title": "…", "labels": ["beach"] } ], "count": 10 }`.

## Rate limits

No fixed API quotas; configurable limits via reverse proxy and `PHOTOPRISM_ADMIN_API_*`. Prefer the batch endpoints to avoid request storms.

## SDKs and client libraries

- **official**: `photoprism-client` (Go), the CLI as reference client
- **community**: Python and Node clients, examples in the API docs
- **import/export**: folder import, `photoprism export`, ExifTool sidecars

## Skin note

Photo/album/label/person correspond to the standard model ([models.md](../../../../../data/models.md)); EXIF fields follow [fields.md](../../../../../data/fields.md).
