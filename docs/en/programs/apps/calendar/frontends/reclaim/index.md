# Reclaim

> Category: [calendar](../../index.md) · [frontends](../index.md)

## What it is

Reclaim (Reclaim.ai) is a web service that works on top of a Google or Outlook calendar and places tasks, habits and meetings into free time. ✅ (help centre; which calendars: Open.) It has a current version 2.0 and a legacy 1.0 ✅.

## Notable ideas

- **Tasks and habits placed automatically:** a task has a due date and an estimate; Reclaim blocks time for it before the deadline and moves it when the calendar changes ✅.
- **Priorities P1 to P4** decide what wins when time is short; due dates can outweigh priority ✅ (search snippet of the help centre).
- **Focus time** defends open blocks for deep work ✅.
- Why here: our tasks and calendar meet at this point (ADR 0013).

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

- https://help.reclaim.ai/en/ ✅ 2026-11-10 (index)
- https://help.reclaim.ai/en/articles/11325700-habits-vs-tasks-vs-focus-time-when-to-use-each-in-reclaim ✅ 2026-11-10 (describes legacy 1.0)
- Priority text from a search snippet of help.reclaim.ai ⚠️ 2026-11-10
