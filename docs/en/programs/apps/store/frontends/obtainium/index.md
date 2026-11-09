# Obtainium

> Category: [store](../../index.md)

## What it is

Obtainium is an Android app that installs and updates other apps directly from their release pages (for example Git hosting releases) and notifies the user about new versions. It is open source (GPL-3.0).

## Notable ideas

- **Direct from the source**: no intermediate store; the user adds the address of an app's release page and the app follows it.
- **Many source types**: GitHub, GitLab, Forgejo and Codeberg, F-Droid and third-party F-Droid repositories, IzzyOnDroid, SourceHut, direct APK links, an HTML fallback for pages that link APKs, and several other stores.
- **Shared app configurations** collected by the community.
- Listed here for the idea of a client that tracks releases of the publisher itself (ADR 0013).

## Sources

- ✅ Obtainium repository (README): https://github.com/ImranR98/Obtainium (fetched 2026-11-10)
- ✅ Obtainium releases: https://github.com/ImranR98/Obtainium/releases (fetched 2026-11-10; v1.7.4 shown, 01 Nov)
- ✅ Wiki start page: https://wiki.obtainium.imranr.dev/ (fetched 2026-11-10)
- ⚠️ Wiki subpages (UI overview, tracking, deep links): not reachable under the guessed URLs

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
