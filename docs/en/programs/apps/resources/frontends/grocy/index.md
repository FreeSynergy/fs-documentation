# Grocy

> Category: [resources](../../index.md)

## What it is

Grocy is a self-hosted web app for household groceries and chores: stock, shopping list, recipes, meal plan, chores, tasks, equipment and batteries.

## Notable ideas

- **Stock of consumables** with due dates, minimum amounts, and barcode entry: the model for material that is used up (see [Resources](../../index.md)).
- Missing items flow automatically to a shopping list; recipes show whether the stock suffices.
- Feature flags hide modules a household does not use; custom fields and user-defined object types exist.
- Documented because it combines stock, tasks and planning for small groups (ADR 0013).

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

- ✅ Grocy home page, https://grocy.info/, retrieved 2026-11-10
- ✅ Grocy releases, https://github.com/grocy/grocy/releases (4.7.1, 04 Sep; year not shown), retrieved 2026-11-10

## Documented versions

| Version | Contents |
|---------|----------|
| [latest](latest/description.md) | description, features, layout, menus, shortcuts, api |
