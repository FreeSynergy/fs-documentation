# Immich - API Documentation

## Overview

Immich is REST-based under `/api` (OpenAPI/Swagger under `/api/docs`). All clients (web, mobile, CLI) use the same endpoints. On top of that there are internal job queues (BullMQ) and webhooks.

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| REST JSON `/api/...` | Assets, albums, people, search, sharing, administration | official |
| Swagger-UI `/api/docs` | Interactive reference | official |
| Webhooks | Events (asset.create …) → HTTP POST | official |
| GraphQL | — | ❌ |
| WebSocket | Upload/job progress (internal) | unofficial |

## Authentication

- **API key**: header `x-api-key: <key>` (per user, scopes read/admin)
- **JWT session**: `Authorization: Bearer <jwt>` after login, refresh via cookie
- **OAuth2/OIDC**: an external provider can be configured (Authentik, Keycloak, Google …)

## Core endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/albums` | Albums of the account |
| `POST` | `/api/albums` | Create album (`albumName`, `assetIds`) |
| `POST` | `/api/albums/{id}/assets` | Add captures |
| `POST` | `/api/albums/{id}/sharing` | Share with a user |
| `GET` | `/api/assets` | Assets with filters (`userId`, `isFavorite`, `takenAfter`) |
| `GET` | `/api/assets/{id}` | Detail incl. EXIF |
| `GET` | `/api/assets/{id}/original` | Download the original |
| `POST` | `/api/assets` | Metadata entry before upload (`deviceAssetId`, `checksum`) |
| `PUT` | `/api/asset-status` | Batch: favourite, archive, trash, duplicate marking |
| `POST` | `/api/search/metadata` | Search by EXIF/place/person/date |
| `POST` | `/api/search/smart` | Semantic CLIP search (`{ "q": "dog at the lake" }`) |
| `GET` | `/api/people` | Recognised people, `updatePerson` for naming |
| `POST` | `/api/share` | Public link (`expiresAt`, `password`, `allowDownload`) |
| `POST` | `/api/jobs/{name}` | Re-trigger a job type (`THUMBNAIL`, `FACIAL_RECOGNITION`) |
| `GET/POST` | `/api/admin/users` | User management (admin only) |

## Example

Request:

```http
POST /api/search/smart HTTP/1.1
x-api-key: <key>
Content-Type: application/json

{ "q": "bicycle in the city", "size": 20 }
```

Response: `200 OK` with `{ "assets": { "items": [ { "id": "…", "originalFileName": "IMG_1.jpg" } ], "count": 20 } }`.

## Rate limits

No hard API limit is built in; limits in the reverse proxy plus job throttling (`IMMICH_MACHINE_LEARNING_QUEUE_CONCURRENCY`) are recommended.

## SDKs and client libraries

- **official**: `@immich/sdk` (TypeScript, generated from OpenAPI), an official CLI for upload/import
- **Community**: Python `immich-api-client`, Go and Rust clients
- **Imports**: Google Photos import, ExifTool-based metadata takeover

## Skin note

Asset/album/share correspond to the standard model ([models.md](../../../../../data/models.md)); the EXIF fields follow [fields.md](../../../../../data/fields.md).
