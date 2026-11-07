# OPNsense

> Category: [desktop](../../index.md)

## What it is

OPNsense is a firewall and router distribution (FreeBSD-based, Deciso) with a complete web UI: interfaces, firewall rules (pf), NAT, VPN, services and plugins are configured via menus, with changes activated by "Apply". Every UI function follows an MVC pattern and can be addressed via the REST API under `/api/<module>/<controller>/<method>` with API key (Basic Auth).

## Notable ideas

_To do: what does this program do that others don't? Why is it documented here (ADR 0013)?_

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
