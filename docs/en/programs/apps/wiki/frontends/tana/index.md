# Tana

> Category: [wiki](../../index.md) · Type: outliner / knowledge graph · Vendor: Tana Inc. · Licence: proprietary

## What it is
Tana is an outliner where every line is a node and nodes can be turned into typed objects with fields.

## Notable ideas
Why this program is documented here (ADR 0013). Function analysis only, own wording.

- Supertags: tagging a node makes the whole node a typed object with a template of fields; all nodes with a supertag form a collection shown as a table. Matches our type-description idea (ADR 0066).
- Supertag inheritance: one tag extends another and adds fields or defaults.
- Search nodes: live queries embedded anywhere.

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
| https://outliner.tana.inc/learn/features/supertags | official docs, supertags | ✅ 2026-11-10 |
