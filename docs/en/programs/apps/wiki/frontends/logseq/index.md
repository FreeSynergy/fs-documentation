# Logseq

> Category: [wiki](../../index.md) · Type: outliner / knowledge graph, privacy-first · Vendor: Logseq (open-source project) · Licence: AGPL-3.0

## What it is
Logseq is an open-source outliner where every bullet is a block that can be referenced from elsewhere; a database version is replacing the Markdown-file version.

## Notable ideas
Why this program is documented here (ADR 0013). Function analysis only, own wording.

- Block references and embeds: refer to or live-embed a single block in other places; referenced blocks show where they are used (linked and unlinked references).
- DB version: pages and blocks unified as nodes with tags and typed properties; tags extend other tags and inherit properties — close to Tana's idea.
- Queries (simple and advanced) shown as table, list or gallery.

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
| https://github.com/logseq/logseq | project repository | ✅ 2026-11-10 |
| https://raw.githubusercontent.com/logseq/docs/master/db-version.md | official docs, DB version | ✅ 2026-11-10 |
| https://discuss.logseq.com/t/the-difference-between-logseqs-block-embeds-and-block-references/8459 | community forum post, references vs embeds | ⚠️ not vendor docs 2026-11-10 |
