# Nextcloud Photos - API documentation

## Overview

The gallery uses the platform APIs: **WebDAV** for files, **OCS** for albums and sharing, additional Photos endpoints under `/apps/photos/api`. All access is user-specific and follows the permissions of the Files app.

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| WebDAV `/remote.php/dav/files/<user>/` | Files, metadata, folders | official standard |
| OCS `/ocs/v2.php/...` | Albums, sharing, navigation, preview | official |
| Photos endpoints `/index.php/apps/photos/api/v1/…` | Chronology, folder selection | official (app-internal) |
| GraphQL / webhooks | — (webhooks only as an app) | ❌ |

## Authentication

- **Basic with app password** for WebDAV: `Authorization: Basic …`
- **OCS**: the same principle, header `OCS-APIRequest: true`
- **Session cookie** in the web UI
- SSO (SAML/OIDC) provides Nextcloud sessions; API passwords remain necessary for clients

## Core endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `PROPFIND` | `/remote.php/dav/files/<user>/` | Folder contents incl. `_displayname`, `getlastmodified` |
| `GET` | `/remote.php/dav/files/<user>/Fotos/IMG.jpg` | File content |
| `PUT` | `/remote.php/dav/files/<user>/Fotos/IMG.jpg` | Upload |
| `GET` | `/index.php/core/preview?fileId=<id>&x=512&y=512` | Generated preview |
| `GET` | `/index.php/apps/photos/api/v1/preview/<fileId>` | Preview at gallery resolution |
| `GET` | `/ocs/v2.php/apps/photos/folders` | Folders selected for the gallery |
| `GET/POST` | `/ocs/v2.php/apps/files_sharing/api/v1/shares` | Shares (link/user/group) |
| `GET/POST/DELETE` | `/index.php/apps/files_sharing/publiclink/...` | Public links |
| `GET` | `/ocs/v2.php/privatedata` | Favourites and album metadata (KVI) |

## Example

Request:

```http
PROPFIND /remote.php/dav/files/kal/Fotos/ HTTP/1.1
Authorization: Basic <user:app-password>
Depth: 1
OCS-APIRequest: true
```

Response: `207 Multi-Status` with DAV-XML; per image `getcontenttype`, `creationdate` (EXIF capture), `fileid`.

## Rate limits

No API quotas; throttling comes from PHP worker limits, the `throttling` app (login) and the reverse-proxy configuration.

## SDKs and client libraries

- **official**: WebDAV clients (ncdu, rclone, Cyberduck), client apps iOS/Android
- **community**: Python `nextcloud-api-wrapper`, Node `nextcloud-node-client`
- **export**: WebDAV rsync, Occ commands for metadata scan

## Frontend note

File/share objects correspond to the standard model ([models.md](../../../../../../data/models.md)); preview URLs behave as in [fields.md](../../../../../../data/fields.md) (`fileId` as the reference).
