# ERPNext

> Category: [resources](../../index.md)

## What it is

ERPNext is an open-source business management suite built on the Frappe framework. It covers accounting, stock, sales, purchasing, manufacturing and assets.

## Notable ideas

- Every record type is a **DocType**: one definition describes the fields, how records are named, and the database table. The list view and the form view then exist without further code. This is the model for generating our own forms from a data type description (see the Admin view in the [map](../../../map.md)).
- Documented here because of that generation principle (ADR 0013); nothing else is taken.

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

- ✅ ERPNext releases, https://github.com/frappe/erpnext/releases (v16.54.0, 06 Nov; year not shown on the page), retrieved 2026-11-10
- ✅ Frappe DocType basics, https://docs.frappe.io/framework/user/en/basics/doctypes, retrieved 2026-11-10
- ✅ Frappe REST API, https://docs.frappe.io/framework/user/en/api/rest, retrieved 2026-11-10

## Documented versions

| Version | Contents |
|---------|----------|
| [latest](latest/description.md) | description, features, layout, menus, shortcuts, api |
