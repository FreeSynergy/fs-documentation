# Immich - Description

## What the program does

Immich replaces a provider's photo-cloud service with your own instance: phones upload everything, the server generates thumbnails, videos in streaming resolution, face and object recognition, and the browser shows timelines, maps and albums. Sharing happens via albums, users or public links.

## Advantages

- **Google-Photos-like UX** with modern search and a people view
- **Self-hosted and data sovereignty**: the originals stay in your own storage (S3 as well)
- **Mobile first**: genuine auto-backup, also in the background
- **API-first**: every UI step is a documented REST call, ideal for frontend integration

## Differentiation

| System | Difference |
|--------|------------|
| **PhotoPrism** | Stronger on indexing/search, a more conservative web UI, ML optional; Immich has the better app and timeline. |
| **LibrePhotos** | A similar idea, but a leaner base and older frontends. |
| **Piwigo** | A classic web-toolkit gallery design, roles per folder, themes; but no face/semantic AI. |
| **Nextcloud Photos** | Good integration into an existing Nextcloud, but a weaker timeline/AI than Immich. |

## Technical details

- **Server**: NestJS (Node.js), PostgreSQL, Redis/BullMQ jobs, the Immich machine-learning service
- **Storage**: filesystem or S3-compatible, originals unchanged, derivatives in `library/`
- **Frontends**: web app (Svelte/React), iOS/Android (Flutter), CLI
- **Auth**: e-mail/password, OAuth2/OIDC, API keys per user
- **Deployment**: Docker Compose (recommended), Helm, bare metal possible
- **Licence**: AGPLv3 (mobile apps GPLv3)

## Who it suits

- A private and team-oriented photo/video archive with auto-backup
- FreeSynergy gallery frontends with the standard model album / asset / person / share
- Migrations from Google Photos (an import tool is available)
