# Odoo

> Category: [resources](../../index.md)

## What it is

Odoo is a suite of business apps (sales, inventory, accounting and more) on one platform, as open-source community and commercial enterprise editions (edition split: Open).

## Notable ideas

- Apps are **modules that build on each other**: one app's data feeds the next (for example sales leading to stock and invoices). Our reading: modules are linked through shared records, not by import. This is one reference for linking resources to other programs through interfaces.
- Documented here because of that module linking (ADR 0013). The linking itself is ⚠️: the documentation index hints at it, a detail page was not read.

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

- ✅ Odoo documentation (master), https://www.odoo.com/documentation/master/applications.html, retrieved 2026-11-10; the version switcher lists versions 14 to 20
- ⚠️ Odoo 20 released September 2026, secondary source https://ecosire.com/blog/latest-odoo-version, retrieved 2026-11-10 (vendor-partner blog, not confirmed on odoo.com)
- ⚠️ GitHub odoo/odoo has no published releases, https://github.com/odoo/odoo/releases, retrieved 2026-11-10

## Documented versions

| Version | Contents |
|---------|----------|
| [latest](latest/description.md) | description, features, layout, menus, shortcuts, api |
