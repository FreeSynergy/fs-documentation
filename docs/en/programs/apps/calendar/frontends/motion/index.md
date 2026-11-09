# Motion

> Category: [calendar](../../index.md) · [frontends](../index.md)

## What it is

Motion (usemotion.com) is a commercial planner with calendar, tasks and projects. Its auto-scheduler arranges tasks on the calendar. Used through desktop and mobile apps ✅. It has a public API ✅.

## Notable ideas

- **Auto-scheduling:** the task list becomes calendar blocks, using priority, deadline, duration, dependencies and calendar availability; it recomputes when something changes ✅. Tasks can be paused or taken off auto-scheduling ✅.
- **Several work schedules** (for example work and personal) decide where tasks may land ✅.
- Why here: dependencies between tasks are a point Reclaim's sources do not show (ADR 0013).

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

- https://docs.usemotion.com/ ✅ 2026-11-10 (API)
- https://www.usemotion.com/help/time-management/auto-scheduling/concept-auto-scheduling ✅ 2026-11-10
- https://www.usemotion.com/help/time-management/auto-scheduling ⚠️ 2026-11-10 (search snippet)
