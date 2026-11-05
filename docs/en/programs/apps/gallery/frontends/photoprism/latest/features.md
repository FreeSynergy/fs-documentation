# PhotoPrism - Features

## Main features

### Indexing
- The collection folder is scanned once and then updated incrementally (also via the CLI `photoprism index`)
- EXIF/XMP, video metadata, sidecar files; duplicates via checksum
- Thumbnails and suitable sizes are generated, the originals remain untouched

### Search and detection
- Full-text, label (AI suggestions + manual), colour, place, camera, date, media type
- Face clustering with naming and birthday; face "search like this"
- Similarity search via image vectors (Plus/CE), OCR on text in images

### Presentation
- Albums (physical folders or virtual selections), stories, slideshow, public share links
- Watermark and download rights per share (Plus), password protection for links

### Organisation
- Renaming/moving in the folder tree, tagging, favourites, archive, hiding
- Import from the import folder, cleanup (duplicates, missing previews)

## What PhotoPrism does NOT do

- **No auto-backup from the phone** like Immich — upload only via web/CLI/sync (❌)
- **No end-to-end video streaming player** with multi-track selection (❌)
- **Image editing only elementary**: crop, rotation, timestamp — no layers/RAW development (❌)
- **No freely designable gallery pages/themes** like Piwigo (❌)
- **Face and semantic AI partly only in the Plus/CE variant** (the Community Edition is reduced)

## Extensions and integrations

| Integration | Method |
|-------------|--------|
| REST API `/api/v1` | official, complete |
| Webhooks | `PHOTOPRISM_WEBHOOK_*` optional |
| Authentication | OIDC/SSO, LDAP (Plus), API key, Basic |
| Storage | own folder, S3 import/export (Plus) |
| Sharing | share links, public gallery folders |
