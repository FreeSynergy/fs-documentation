# Attio

> Category: [crm](../../index.md) · Type: CRM (SaaS) · Vendor: Attio · Licence: proprietary

## What it is
Attio is a commercial CRM with a flexible data model. Records of people and companies are filled in automatically (enrichment), and e-mail and calendar can be synced. Objects, attributes, lists and views are configurable.

## Notable ideas
- **Enrichment** — records are filled automatically with data from outside; this is bound to the standard objects, which carry the built-in enrichment attributes (ADR 0013).
- **Standard and custom objects** — People and Companies exist from the start; Deals, Users and Workspaces can be switched on; admins add custom objects (paid plans).

## Documented versions
| Version | Documented on | Status |
|---------|---------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ⚠️ |

## Protocols and standards used
REST API, SDK and MCP are named (developer docs not read). See [data standards](../../../../../data/standards.md).

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
| https://attio.com/help | official help ✅ | 2026-11-10 |
| https://attio.com/help/reference/attio-101/attios-data-model/understanding-objects | official help ⚠️ (via search summary) | 2026-11-10 |
| https://attio.com/help/reference/managing-your-data/objects/create-and-manage-custom-objects | official help ⚠️ (via search summary) | 2026-11-10 |
