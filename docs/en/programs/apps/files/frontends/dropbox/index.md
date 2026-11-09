# Dropbox

> Category: [files](../../index.md) · [frontends](../index.md)

## What it is

Dropbox is a commercial cloud storage service with web, desktop and mobile clients and a developer API. ✅ (help centre; client list: Open.)

## Notable ideas

- **File requests:** the owner asks others to send files. The sender needs no account; files land in a chosen folder, private by default ✅. Options: title, description, naming convention, password, deadline with or without late uploads (paid plans) ✅. Per-file limit 2 GB on basic plans, 250 GB on paid ones ✅. Uploads count against the owner's space ✅.
- Why here: a drop-only way to receive files is the case behind "drop-only folder" in our share roles (ADR 0013).

## Documented versions

<!-- gen:versions (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
| Version | Required files present |
|---------|------------------------|
| [latest](latest/description.md) | 6/7 |

### latest

| File | Contents |
|------|----------|
| [description.md](latest/description.md) | Detailed description, differentiation, who it suits |
| [features.md](latest/features.md) | What the program can do — and what not |
| [layout.md](latest/layout.md) | Window structure, regions, panels |
| [menus.md](latest/menus.md) | Menu structure, context menus, menus by role |
| [shortcuts.md](latest/shortcuts.md) | Keyboard shortcuts |
| [api.md](latest/api.md) | APIs and protocols, authentication, rate limits |

⚠️ Missing required files: `themes/index.md`
<!-- /gen:versions -->

## Sources

- https://help.dropbox.com/share/create-file-request ✅ 2026-11-10
- https://help.dropbox.com/share/received-file-request ⚠️ 2026-11-10 (search result only)
- https://dropbox.tech/developers/streamline-file-collection-with-the-file-request-api ⚠️ 2026-11-10 (search result only; a file request API exists)
