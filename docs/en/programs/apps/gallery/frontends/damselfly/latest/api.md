# Damselfly - API Documentation

## Overview

Damselfly offers a JSON API for upload, search, folders and administration. It is used by the web frontend and is the only route for automation (import scripts, bulk upload).

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| REST JSON `/api/...` | Upload, search, albums, people, administration | official |
| Upload endpoints (multipart) | Single and bulk | official |
| GraphQL / webhooks | — | ❌ |

## Authentication

- **Session cookie** after login
- **API token** for scripts (can be generated in the admin area), header `Authorization: Bearer <token>`
- Reverse-proxy auth (e.g. authelia) is frequently placed in front

## Core endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/Upload` | File upload (multipart, target folder) |
| `POST` | `/api/Upload/Chunked` | Large files in chunks |
| `GET` | `/api/Search` | Search (`searchTerm`, `folderId`, `labels`, `dateFrom/To`) |
| `POST` | `/api/Search/Similar` | Similarity search (`imageId`) |
| `GET` | `/api/Images/{id}` | Metadata, labels, people |
| `PATCH` | `/api/Images/{id}` | Title, favourite, label, folder |
| `DELETE` | `/api/Images/{id}` | Delete image |
| `GET/POST` | `/api/Albums` | Read/create albums |
| `GET` | `/api/People` | Face clusters, naming via `PATCH` |
| `POST` | `/api/Sync/Push` · `/api/Sync/Pull` | Folder reconciliation |
| `GET` | `/api/Index/Status` | Pending index tasks |

## Example

Request:

```http
POST /api/Search/Similar HTTP/1.1
Authorization: Bearer <token>
Content-Type: application/json

{ "imageId": 4711, "limit": 20 }
```

Response: `200 OK` with `{ "results": [ { "id": 4802, "distance": 0.12 } ] }`.

## Rate limits

No hard limits; upload sizes and the number of workers configure the throughput (`MAX_UPLOAD_SIZE`, queue size).

## SDKs and client libraries

- **official**: no SDKs; import examples in the release notes
- **Community**: Bash/PowerShell scripts for bulk upload
- **Export**: folder export via the filesystem, metadata as an XMP sidecar

## Skin note

Image/album/person/label correspond to the standard model ([models.md](../../../../../../data/models.md)); the ID type is an integer.
