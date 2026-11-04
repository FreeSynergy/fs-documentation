# Nextcloud Contacts - API Documentation

## Overview

Contact access runs over **CardDAV (RFC 6352)** at `remote.php/dav/`; sharing/circle metadata over **OCS**. A separate REST "Contacts" API does not exist.

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| CardDAV | Address books, contacts (CRUD) | official |
| OCS Share / Circles | Shares, circles, yellow pages | official |
| Status API | User status shown on the contact card | official-internal |
| REST "/api/contacts" | — | ❌ Not present |

## Authentication

- **Basic auth** over HTTPS (user + app password recommended)
- Session cookies in the browser; Bearer for OCS from an app password is possible
- Two-factor: app passwords are required

## CardDAV endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/.well-known/carddav` | Discovery → `/remote.php/dav/` |
| `PROPFIND` | `/remote.php/dav/addressbooks/users/<user>/` | Address books incl. `addressbook-color`, `sync-token` |
| `REPORT` | `<addressbook-url>` | `addressbook-multiget` / `sync-collection` |
| `GET` | `<addressbook-url>/<uid>.vcf` | A single vCard |
| `PUT` | `<addressbook-url>/<uid>.vcf` | Create/change contact |
| `DELETE` | `<addressbook-url>/<uid>.vcf` | Delete contact (trash-bin logic server-side) |
| `MKCOL` | `/remote.php/dav/addressbooks/users/<user>/<name>/` | New address book |

## Example: create a vCard

```http
PUT /remote.php/dav/addressbooks/users/anna/contacts/andrea.vcf HTTP/1.1
Content-Type: text/vcard; charset=utf-8

BEGIN:VCARD
VERSION:3.0
UID:andrea
N:Berg;Andrea;;;
FN:Andrea Berg
TEL;TYPE=CELL:+49 170 000000
EMAIL;TYPE=WORK:andrea@example.org
END:VCARD
```

Response: `201 Created`, `ETag`.

## OCS (shares/circles)

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/ocs/v2.php/apps/circles/circles` | List circles |
| `POST` | `/ocs/v2.php/apps/files_sharing/api/v1/shares` | Share (also address-book shares, variant types) |
| `GET` | `/cloud/user-status` | Status of the Nextcloud users |

OCS requires the header `OCS-APIRequest: true`.

## Rate limits

Nextcloud throttling on the login endpoints; DAV itself has no fixed limits (brute-force protection is active).

## SDKs and clients

- **JS**: `nextcloudContacts` community clients; the `js-calendav` family; official client examples in the contacts repo (fetch + PROPFIND)
- **CLI**: `curl` with DAV methods; `vdirsyncer`
- **PHP**: `sabre/dav` (server-side reference)

## Skin note

Skin mapping onto the contact model ([modelle.md](../../../../../data/modelle.md)), field names according to vCard 3.0 ([felder.md](../../../../../data/felder.md)).
