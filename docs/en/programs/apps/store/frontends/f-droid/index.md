# F-Droid

> Category: [store](../../index.md)

## What it is

F-Droid is a community-run catalogue and installer client for free-software Android apps. The project builds apps from source and publishes them in a repository; the client app browses repositories and installs and updates apps.

## Notable ideas

- **Anti-Features**: an app that is free software but has questionable behaviour carries visible labels (ads, tracking, non-free dependencies, non-free network services, known vulnerability and others), so the user decides with the facts in view.
- **Reproducible builds**: the project aims to rebuild each app from source and check that the result matches the developer's signed release; the app page shows the reproducibility status.
- **Several repositories**: the client can add third-party repositories next to the main one.
- Listed here as a reference for honest, label-based app information (ADR 0013).

## Sources

- ✅ F-Droid, Anti-Features: https://f-droid.org/docs/Anti-Features/ (fetched 2026-11-10)
- ✅ F-Droid, Reproducible Builds: https://f-droid.org/docs/Reproducible_Builds/ (fetched 2026-11-10)
- ⚠️ Repository index specification: page not reachable under the guessed URL; details in api.md are Open

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
