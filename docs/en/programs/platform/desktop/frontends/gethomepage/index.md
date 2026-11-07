# gethomepage (Library)

> Category: [desktop](../../index.md)

## What it is

`gethomepage` refers to the **API library layer** of the project `gethomepage/homepage`: the service clients, proxy handlers, configuration readers and helper functions that turn the YAML entries in `services.yaml` into actual HTTP calls to Sonarr, Pi-hole, Proxmox, Docker or Kubernetes. The library has **no user interface of its own** – operation and configuration take place via the dashboard.

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
