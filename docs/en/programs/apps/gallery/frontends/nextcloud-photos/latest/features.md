# Nextcloud Photos - Features

## Main features

- **Chronology** over all shared folders, grouped by day/month/year
- **Albums** (virtual) and **folder albums**, sharing with users/groups/links
- **Mobile apps** with auto-upload (photos and videos, folders selectable)
- **Preview pipeline** with generated preview sizes and optional MIME handling
- **Folder selection**: control over what appears in the gallery
- **Recognition** (optional apps) for faces and image recognition, search by folder contents
- **Videos** directly in the viewer with seeking and streaming delivery

## What Photos does NOT do

- **No own image database** — the metadata stays in the files/folder tables (❌)
- **No semantic full-text/CLIP search** in the base (only folder/name, recognition limited) (❌)
- **No gallery themes/design templates** (a uniform Nextcloud layout) (❌)
- **No image editing** (only rotate/crop in the Files app preview) (❌)
- **No web-toolkit permissions per gallery** (the permissions come from Files sharing) (❌)

## Extensions and integrations

| Integration | Method |
|-------------|--------|
| WebDAV (`/remote.php/dav`) | Files and metadata, standard client protocol |
| OCS/REST | Albums, Photos endpoints, sharing, preview |
| Apps | Maps (locations), Recognizer/Face Recognition, Memories (alternative) |
| Client apps | iOS/Android with auto-upload, desktop sync |
| Authentication | Nextcloud users, SAML/OIDC (app), app passwords, WebDAV tokens |
