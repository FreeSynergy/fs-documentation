# Felt

> Category: [maps](../../index.md) · Type: browser GIS, shared maps · Vendor: Felt · Licence: proprietary

## What it is
Felt is a browser-based mapping and GIS service where several people edit the same map at once. Layers come from uploaded files or connected data sources; maps are shared by link and can be embedded.

## Notable ideas
- Shared editing with live changes, like a document. Why: maps become a team artefact.
- Comments and viewing without a paid seat, links without login. Why: low barrier for outsiders.
- Layers connected to databases stay current. Why: a map as a live view, not a copy.
- Open REST API, JS SDK and webhooks. Why: a good model for our own map interface.

## Documented versions
| Version | Documented on | Status |
|---------|---------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ✅ |

## Protocols and standards used
GeoJSON, KML, Shapefile, GeoPackage, GeoTIFF as uploads; WFS, WMTS, STAC as sources (all from the vendor page).

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
| https://felt.com ✅ | product page | 2026-11-10 |
| https://help.felt.com ✅ | help centre index | 2026-11-10 |
| https://developers.felt.com ✅ | developer docs overview | 2026-11-10 |
