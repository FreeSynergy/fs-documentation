# LibrePhotos - Menu items

## Main navigation (left bar)

| Menu | Description |
|------|-------------|
| Search | Full-text and semantic search (CLIP), filter bar |
| Places | Map, place list, "Places" groups |
| Albums | Own albums, auto albums (date, event) |
| People | Recognised faces, names, merging |
| Photos / videos | Filter by type and capture date |
| Favourites | Marked captures |
| Shared | Albums shared by other users |
| Deleted | Trash with restoration |

## Settings (gear)

| Area | Content |
|------|---------|
| Account | Password, language, theme, two-factor |
| Gallery | Timeline grouping, thumbnail size, NSFW filter |
| ML | Face/object recognition on/off, model selection, execution |
| Upload | Import folder, duplicate behaviour |

## Administration (admin only)

| Menu | Content |
|------|---------|
| Users | Accounts, groups, quota, invitations |
| Scan jobs | "Full scan", "Face scan", "CLIP index", status/abort |
| Tasks | View running background jobs (Celery) |
| Storage | Path layout (`MEDIA_ROOT`), cleanup |

## Context menus

| Object | Actions |
|--------|---------|
| Capture | Favourite, download, delete, search similar, assign person, album |
| Multi-selection | Add to album, share, tag, delete |
| Album | Edit, cover, share (user/link), download (ZIP) |
| Person | Name, face crop, merge, exclude |

## Menus by role

| Role | Visible |
|------|---------|
| User | Search, own albums, shared content |
| Admin | Additionally administration and scan control |
| Guest | Only shared albums (read, download depending on the share) |
