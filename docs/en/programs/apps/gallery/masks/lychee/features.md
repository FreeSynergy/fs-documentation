# Lychee - Features

## Main features

- **Albums and sub-albums** with sorting by date/title, cover selection
- **Shares** per album: link, password, validity, permissions (view/download)
- **Upload** via drag & drop, URL import, folder upload; batch processing of the sizes
- **Lightbox** with fullscreen, slideshow, EXIF overlay, rotate and crop
- **Smart albums**: saved search that is populated automatically
- **Multiple users** with quotas and their own albums

## What Lychee does NOT do

- **No face/object recognition**, no semantic search (❌)
- **No phone auto-backup** (upload only manually/web, third-party app) (❌)
- **No category permission matrix like Piwigo** (shares only per album) (❌)
- **No video streaming** (videos are only downloaded) (❌)
- **No themes/gallery templates** — a uniform React interface (❌)

## Extensions and integrations

| Integration | Method |
|-------------|--------|
| REST API `/api` | official, complete |
| OAuth2/SSO | configurable providers (Apple, GitHub, Google …) |
| Webhooks | — (❌) |
| Storage | local folder, external disk adapters limitedly supported |
| Import | from Lightroom exports, URL import |
