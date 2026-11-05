# uMap - API documentation

## Overview

uMap is open with its data: the map data exists as **GeoJSON** (export link, remote sources). The Django instance has JSON endpoints for maps/datalayers (short-lived across versions — for skin integration primarily use export/import + remote GeoJSON).

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| Export GeoJSON/GPX/KML (`/export/` in the map menu) | Pull the data out | official |
| Remote data (URL layer) | Data in (live GeoJSON) | official |
| Internal REST-like endpoints (`/map/{id}/`, `/datalayer/…`) | UI-internal | instance-dependent (not stable) |
| Webhooks | — | ❌ |
| GraphQL | — | ❌ |

## Authentication

- Public maps: none
- Editing via the **edit-token link** (secret in the link) or instance login (self-hosted)

## Pattern: the data cycle for skins

```
FreeSynergy database → GeoJSON endpoint (your own service)
      → uMap layer "Remote Data" (reloaded automatically)
      → the group's manual additions → export → feed back
```

GeoJSON schema (practical):

```json
{ "type": "FeatureCollection", "features": [
  { "type": "Feature",
    "geometry": { "type": "Point", "coordinates": [9.058, 48.530] },
    "properties": { "_title": "Treffpunkt Hbf",
      "_description": "Brunnenseite", "_iconClass": "tintred" } } ] }
```

(`_title`/`_description`/`_iconClass` = uMap conventions.)

## Embedding

iframe from "share": `https://uMap.example.org/map/{id}#/{zoom}/{lat}/{lng}` — deep links onto markers via a `marker-{id}` hash.

## Rate limits

On the instance operator's side (using OSM tiles via a proxy is recommended).

## Skin note

Location point skins write GeoJSON and use uMap as the **view layer**; the permission logic stays in FreeSynergy ([standpunkte.md](../../../standpunkte.md)).
