# Photo galleries

**The gallery is planned as a view and frontend of [`fs-files`](../files/design.md), no code yet.** See the [earlier design](design.md), the [requirements](requirements.md) and the [overall plan](../roadmap.md).

## Overview

Photo galleries manage image and video collections: they index holdings, generate previews, make content searchable (albums, labels, faces, places) and share results via web galleries or apps. The category includes self-hosted servers (Immich, PhotoPrism, Piwigo …) just as much as photo solutions embedded in groupware (Nextcloud Photos).

## Available systems

- **immich** - Self-hosted photo management with mobile upload, face and place recognition
- **photoprism** - Indexing with labels and faces, Vue web gallery
- **librephotos** - Photo management with ML tagging and timeline view
- **lychee** - Lean, secure self-hosted gallery
- **piwigo** - Web gallery with a large plugin and community base
- **coppermine** - Classic PHP photo gallery (Coppermine Photo Gallery)
- **damselfly** - Lightweight image management directly on Lightroom catalogs
- **nextcloud-photos** - Photo view and sharing within Nextcloud

## Frontends

<!-- gen:frontends (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
Analysed programs (9), by function, nothing copied (ADR 0012/0013):

- [Apple Photos](frontends/apple-photos/index.md) — Photos is the photo and video library app of macOS, iOS and iPadOS, synchronised through iCloud Photos.
- [Coppermine](frontends/coppermine/index.md) — Coppermine (CPG) is a classic web toolkit for photo galleries with albums, categories, comments, ratings and role permissions.
- [Damselfly](frontends/damselfly/index.md) — Damselfly is a lightweight, fast-starting photo gallery with AI recognition (faces, scenes, text/OCR, similarity search) based on PostgreSQL vectors.
- [Immich](frontends/immich/index.md) — Immich is a self-hosted photo and video management solution (server + mobile app): uploads from the phone, face and object recognition, timelines, albums, shared galleries and a complete REST API.
- [LibrePhotos](frontends/librephotos/index.md) — LibrePhotos is the open-source alternative to Google Photos: automatic backup via an app, face and object recognition, timeline, albums and shared galleries.
- [Lychee](frontends/lychee/index.md) — Lychee is a lean, self-hosted photo gallery with albums, sharing via links and a clean REST API.
- [Nextcloud Photos](frontends/nextcloud-photos/index.md) — The Photos app of Nextcloud is the gallery surface on top of the Files app: chronology, albums, Shared view, folder selection and (from NC 25+) Recognizer/facial-recognition integration.
- [PhotoPrism](frontends/photoprism/index.md) — PhotoPrism indexes an existing photo collection, recognises content and faces, and presents it as a searchable web gallery with albums and sharing.
- [Piwigo](frontends/piwigo/index.md) — Piwigo is a classic web-toolkit photo gallery: category tree, roles and permissions per folder, themes, extensions and a complete webservice API.

Overview: [frontends](frontends/index.md)
<!-- /gen:frontends -->

## Frontend documentation

The programs in this category are documented following the wiki schema (seven files per program: `index`, `menu`, `features`, `description`, `structure`, `shortcuts`, `api`) under `programs/apps/gallery/frontends/<program>/`.

**documented (8 programs):**

- [Coppermine](frontends/coppermine/index.md) - Coppermine
- [Damselfly](frontends/damselfly/index.md) - Damselfly
- [Immich](frontends/immich/index.md) - Immich
- [LibrePhotos](frontends/librephotos/index.md) - LibrePhotos
- [Lychee](frontends/lychee/index.md) - Lychee
- [Nextcloud Photos](frontends/nextcloud-photos/index.md) - Nextcloud Photos
- [PhotoPrism](frontends/photoprism/index.md) - PhotoPrism
- [Piwigo](frontends/piwigo/index.md) - Piwigo

Overview: [Frontend directory](frontends/index.md)

Reference schema: [Wiki frontends](../wiki/frontends/index.md) · [Desktop frontends](../../platform/desktop/frontends/index.md) · [Standardised data](../../../data/api.md)
