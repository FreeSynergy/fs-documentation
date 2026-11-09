# Huginn

> Category: [workflows](../../index.md)

## What it is

Huginn is an open-source (MIT) system, self-hosted, in which agents watch the web and other sources and act on what they find. It is a Ruby on Rails app with a web interface; the README calls it a hackable alternative to IFTTT or Zapier.

## Notable ideas

- **Agents and events**: each agent creates events and can consume the events of others; the whole is a directed graph, shown as an event-flow diagram in the UI.
- **Watching, not only reacting**: agents scrape sites and watch feeds, mailboxes, webhooks and MQTT topics.
- **Small transformation languages**: JavaScript, Liquid templates and jq.
- Listed here for the idea of agents that watch and pass on events (ADR 0013).

## Sources

- ✅ Huginn repository (README): https://github.com/huginn/huginn (fetched 2026-11-10)
- ⚠️ Maintenance: maintained by one person in spare time (README); releases section empty in the fetched page

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
