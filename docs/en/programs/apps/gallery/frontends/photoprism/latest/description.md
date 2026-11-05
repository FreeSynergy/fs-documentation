# PhotoPrism - Description

## What the program does

PhotoPrism places a database over an existing photo folder: everything is indexed, made preview-ready, tagged and searchable. The interface is a gallery with strong search, albums and shares; the files remain in their folder structure.

## Advantages

- **Keeps your own folder structure** — no proprietary catalogue as the single source of truth
- **Fast, faceted search** (label, colour, place, person, period)
- **Resource-friendly**: Go backend, runs on small servers/NAS
- **Clear roles** (viewer/contributor/admin) for shared installations

## Differentiation

| System | Difference |
|--------|------------|
| **Immich** | App-centred with auto-backup and its own storage; PhotoPrism indexes existing folders. |
| **LibrePhotos** | Closer to Immich (apps, face AI), smaller community. |
| **Piwigo** | A web-toolkit gallery with themes and roles per folder, but without AI detection. |

## Technical details

- **Backend**: Go, SQLite or MariaDB/MySQL, image processing via Imaginary/ImageMagick
- **AI**: TensorFlow models for labels/faces (CE with reduced scope, Plus/CE editions)
- **Frontend**: Vue 2/3 SPA, delivered server-side, responsive
- **Deployment**: Docker Compose (standard), binaries, ARM64/AMD64
- **Licence**: Community Edition AGPLv3, Plus/CE extensions commercial

## Who it suits

- Collections that already exist as a folder tree and only need to be made "gallery-capable"
- FreeSynergy gallery skins with an album / photo / label / person model
- Households and teams with no expectation of phone auto-backup
