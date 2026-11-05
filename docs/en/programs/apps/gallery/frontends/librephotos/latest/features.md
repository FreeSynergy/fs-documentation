# LibrePhotos - Features

## Main features

### Capture
- Mobile apps (iOS/Android) with auto-backup, web upload, import from folders
- Duplicate detection via hash, incremental scan on file changes

### Detection and search
- CLIP-based semantic search ("red glasses at the beach")
- Face clustering with naming and merging, object recognition, location recognition
- Timeline, event detection (event-based auto albums)

### Presentation
- Albums, auto albums, slideshow, shared albums with permissions
- Map view with cluster markers, location groups

## What LibrePhotos does NOT do

- **No web-toolkit design** (no themes/gallery templates) — the interface is a fixed app (❌)
- **No real image editing** beyond cropping (❌)
- **No video transcoding for adaptive streaming** (files are served directly) (❌)
- **No mature API documentation** — the endpoints are functional but less stable than Immich/PhotoPrism (⚠)
- **No multi-tenant multi-instance capability** (❌)

## Extensions and integrations

| Integration | Method |
|-------------|--------|
| REST API (Django REST) | official, used end-to-end by the web UI |
| Background jobs | Celery + Redis, scan pipelines |
| Authentication | Token, OAuth2 providers (optional), TwoFactor |
| Search | PostgreSQL, embedding vectors |
| Maps | Leaflet/MapLibre tiles (self-hosted) |
