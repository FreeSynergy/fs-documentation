# Gallery — Frontends

Frontends of well-known programs in this category, analysed for their **functions** — nothing is copied (ADR 0013). A program is documented here because it is widely learned or because it has a notable idea. Our own program for this category is `FreeSynergy.Gallery` (ADR 0017); its capabilities and status live in [requirements](../requirements.md).

## Programs

| Program | Versions | What it is |
|---------|----------|------------|
| [Coppermine](coppermine/index.md) | [latest](coppermine/latest/description.md) | Coppermine (CPG) is a classic web toolkit for photo galleries with albums, categories, comments, ratings and role permissions. |
| [Damselfly](damselfly/index.md) | [latest](damselfly/latest/description.md) | Damselfly is a lightweight, fast-starting photo gallery with AI recognition (faces, scenes, text/OCR, similarity search) based on PostgreSQL vectors. |
| [Immich](immich/index.md) | [latest](immich/latest/description.md) | Immich is a self-hosted photo and video management solution (server + mobile app): uploads from the phone, face and object recognition, timelines, albums, shared galleries and a complete REST API. |
| [LibrePhotos](librephotos/index.md) | [latest](librephotos/latest/description.md) | LibrePhotos is the open-source alternative to Google Photos: automatic backup via an app, face and object recognition, timeline, albums and shared galleries. |
| [Lychee](lychee/index.md) | [latest](lychee/latest/description.md) | Lychee is a lean, self-hosted photo gallery with albums, sharing via links and a clean REST API. |
| [Nextcloud Photos](nextcloud-photos/index.md) | [latest](nextcloud-photos/latest/description.md) | The Photos app of Nextcloud is the gallery surface on top of the Files app: chronology, albums, Shared view, folder selection and (from NC 25+) Recognizer/facial-recognition integration. |
| [PhotoPrism](photoprism/index.md) | [latest](photoprism/latest/description.md) | PhotoPrism indexes an existing photo collection, recognises content and faces, and presents it as a searchable web gallery with albums and sharing. |
| [Piwigo](piwigo/index.md) | [latest](piwigo/latest/description.md) | Piwigo is a classic web-toolkit photo gallery: category tree, roles and permissions per folder, themes, extensions and a complete webservice API. |
| [Apple Photos](apple-photos/index.md) | [latest](apple-photos/latest/description.md) | Apple Photos is the photo library of Apple platforms; notable for text in images (Live Text) and a merge-able Duplicates album. |

## File set per program (ADR 0012)

```
programs/apps/gallery/frontends/<program>/
├── index.md        what it is, notable ideas, documented versions, sources
├── changelog.md    changes between documented versions (≥ 2 versions)
└── <version>/
    ├── description.md    required · Detailed description, differentiation, who it suits
    ├── features.md       required · What the program can do — and what not
    ├── layout.md         required · Window structure, regions, panels
    ├── menus.md          required · Menu structure, context menus, menus by role
    ├── shortcuts.md      required · Keyboard shortcuts
    ├── api.md            required · APIs and protocols, authentication, rate limits
    ├── themes/index.md   required · Themes: colours, typography, spacing — what can be rebuilt
    ├── interaction.md    if needed · Hover, focus, drag, gestures (finger, mouse, pen)
    ├── states.md         if needed · UI states and transitions
    ├── events.md         if needed · Events to the outside (webhooks, push, streams)
    ├── limits.md         if needed · Known limitations
    ├── i18n.md           if needed · Localisation, writing direction
    └── dependencies.md   if needed · Which of our components a frontend in this style needs
```

Protocols (Matrix, IMAP, CalDAV, …) are not frontends; they are described under [data](../../../../data/standards.md).
