# Immich - Features

## Main features

### Capture and upload
- Auto-backup of phone photos (iOS/Android), duplicate detection, resume of progress
- Web upload of whole folders, import from other systems (CLI `immich-cli`, Google Photos import)
- EXIF/XMP evaluation: camera data, GPS, capture date; reverse geocoding for places

### Organisation
- Timeline (day/month/year), calendar view, maps view (tiles on your own maps)
- Albums, shared albums, shared links (password, expiry, download permission)
- Stacks for bracketing/panorama, favourites, archive, trash bin with a deadline
- Tags and own search terms; smart search (CLIP) for "beach", "cat" …

### Recognition
- Face clustering with named people, face biometrics
- Object recognition, scene recognition, semantic search
- Duplicate detection (pHash), similarity search per capture

### Editing
- Crop/rotate, correct timestamps, XMP side effects; videos: transcoding (H.264/HEVC, thumbnails/GIF)
- Batch processing of thumbnails and preview sizes (the original stays unchanged)

## What Immich does NOT do

- **No full image editor** (no layers, no RAW development in the app) — RAW is only stored as the original (❌)
- **No digital rights management / watermarking** (❌)
- **No classic web-toolkit gallery design** (no freely positionable galleries in the style of Piwigo extensions)
- **No multilingual public-website gallery** in the style of a CMS gallery; the share pages are plain
- **No offline access to the full library** on the desktop client

## Extensions and integrations

| Integration | Route |
|-------------|-------|
| REST API + API keys | Official, complete |
| Webhooks | Server events → HTTP |
| External libraries | Mount a folder, read-only SCAN |
| ML models | Downloadable models, GPU via CUDA/OpenVINO |
| Object/cloud storage | An S3-compatible storage bucket can be configured |
| Authentication | OAuth2/OIDC, LDAP not integrated (❌) |
