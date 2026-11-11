# Taskwarrior

> Category: [tasks](../../index.md) · Type: command-line task manager · Vendor: GothenburgBitFactory community · Licence: free and open source (licence version Open)

## What it is
Taskwarrior is a command-line to-do manager. Current stable release on the project site: 3.5.0.

## Notable ideas
Why this program is documented here (ADR 0013). Function analysis only, own wording.

- Computed urgency: every task gets a score from weighted terms, so the list sorts itself; all weights are user-configurable — a transparent alternative to manual priority.
- Report-based views and filters on the command line.

## Documented versions
| Version | Documented on | Status |
|---------|---------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ⚠️ partly verified, gaps marked "Open" |

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
| Source | Kind | Retrieved |
|--------|------|-----------|
| https://taskwarrior.org/ | official site | ✅ 2026-11-10 |
| https://taskwarrior.org/docs/urgency/ | official docs, urgency | ✅ 2026-11-10 |
