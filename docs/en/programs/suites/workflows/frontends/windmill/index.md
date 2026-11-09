# Windmill

> Category: [workflows](../../index.md)

## What it is

Windmill is an open-source (AGPLv3 community edition) platform for scripts, flows, apps and AI agents, self-hostable or hosted. Rust backend, Svelte frontend, PostgreSQL as store and job queue.

## Notable ideas

- **Script first**: a script in many languages becomes at once an auto-generated form, an HTTP endpoint and a schedulable job.
- **Flows, apps and scripts from one base**: flows chain scripts (visual editor, YAML or workflows as code); apps put a frontend on scripts and flows.
- **Workers pull by tag** from the queue; sandboxed execution.
- Listed here for the idea that code is the unit and the interface is generated (ADR 0013).

## Sources

- ✅ Windmill introduction: https://www.windmill.dev/docs/intro (fetched 2026-11-10)
- ✅ Windmill repository (README): https://github.com/windmill-labs/windmill (fetched 2026-11-10)
- ⚠️ Latest release: not shown in the fetched page

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
