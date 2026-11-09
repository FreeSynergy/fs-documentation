# Syncthing

> Category: [files](../../index.md) · [frontends](../index.md)

## What it is

Syncthing is a free program that keeps chosen folders identical between devices directly, with no central server ✅ (concept; the intro page does not state it, see Open). Control is a web GUI on `localhost:8384` ✅. Licence: Open (not read).

## Notable ideas

- **Device to device:** each device has an ID made from its certificate; two devices connect only when each has added the other's ID ✅.
- **Folders are shared per device,** chosen when adding the device ✅.
- **Discovery and relays:** global and local discovery, and public relays when no direct path exists; all on by default and can be switched off ✅. Relayed data stays encrypted end to end ✅.
- **TLS 1.2/1.3** between devices; fingerprint checked against the accepted list ✅.
- **Untrusted (encrypted) devices** exist as a documentation topic ✅; details Open.
- Why here: the reference for sync without a server (ADR 0013, ADR 0019).

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

- https://docs.syncthing.net/intro/getting-started.html ✅ 2026-11-10
- https://docs.syncthing.net/users/security.html ✅ 2026-11-10
- https://docs.syncthing.net/dev/rest.html ✅ 2026-11-10
