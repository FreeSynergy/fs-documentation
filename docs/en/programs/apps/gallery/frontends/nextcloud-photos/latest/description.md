# Nextcloud Photos - Description

## What the program does

Nextcloud Photos shows the photos that are stored in the Nextcloud: a chronology over the selected folders, albums as virtual collections, sharing via the usual Nextcloud mechanisms. It is not its own media management, but a view on top of the files platform.

## Advantages

- **one system for files and photos**: sync, permissions, versioning included
- **mature sharing features** (links with password/expiry, upload links)
- **mobile auto-uploads** stable for years

## Differentiation

| System | Difference |
|--------|------------|
| **Immich** | A dedicated photo cloud with AI search and timeline; Nextcloud Photos remains a file view. |
| **Memories** (Nextcloud app) | A gallery replacement with timeline and recognition, closer to Immich than the core Photos app. |
| **PhotoPrism** | Indexes folders and provides strong search; Nextcloud brings the folders along. |
| **Piwigo** | A curated web-toolkit gallery with themes and a permission tree. |

## Technical details

- **Backend**: PHP on the Nextcloud platform, the files table as the foundation
- **Frontend**: Vue 2/3 (Photos app), the viewer of the Files app
- **Storage**: primary storage, external storage backends possible
- **Auth**: Nextcloud users, app passwords, SSO (SAML/OIDC), WebDAV
- **Deployment**: Snap/Docker/bare metal, PHP-FPM + MariaDB/PostgreSQL, Redis recommended
- **Licence**: AGPLv3

## Who it suits

- Organisations with an existing Nextcloud that want to show photos without a second system
- FreeSynergy gallery frontends that also use WebDAV and sharing objects
- Private users with an auto-upload need and file access
