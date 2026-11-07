# Synology DSM

> Category: [desktop](../../index.md)

## What it is

Synology DiskStation Manager (DSM) is the proprietary operating system of Synology NAS devices, with a complete **desktop portal in the browser**: main menu, window management, app bar, desktop widgets, package centre and control panel. Management API access runs via `GET/POST /webapi/entry.cgi` with `SYNO.*` APIs; default ports are **5000 (HTTP)** and **5001 (HTTPS)**.

## Notable ideas

_To do: what does this program do that others don't? Why is it documented here (ADR 0013)?_

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
