# Location points (Standpunkte) for groups

A cross-page function of the maps category: **location points (Standpunkte)** are places managed jointly by several people — meeting points, storage sites, demonstration-route checkpoints, offer locations (marketplace reference) — with notes, responsibilities and visibility rules.

## Requirements (brief)

1. **Capture**: every member creates/changes points (name, coordinates, note, category)
2. **See**: live map in browser + **offline on mobile**
3. **Share**: links/embeds for third parties, exportable data
4. **Navigation**: points reach the mobile navi (GPX/KML/OVF)
5. **Permissions**: who may change what, visibility per group

## Building blocks from this category

| Building block | Contribution |
|----------------|--------------|
| **uMap** | Collaborative map editor (group layers, popup notes, edit-token links) — capture + see |
| **OpenStreetMap/Overpass** | Public location points (POIs) as starting data; reporting your own places |
| **Leaflet/MapLibre** | Skin view: FreeSynergy GeoJSON as a live layer (web) |
| **QGIS** | Analysis: buffers ("who lives <500 m?"), clustering, quality checks; QGIS Server → WMS/WFS |
| **OsmAnd / Organic Maps** | Mobile navigation to location points via GPX/OVF/KML import |

## Reference chain (FreeSynergy skin)

```
FreeSynergy DB (table: standpunkte)
   ├─ GET /geojson  →  uMap "remote data" + Leaflet/MapLibre dashboard
   ├─ Export GPX/KML/OVF  →  OsmAnd/Organic Maps (offline)
   └─ GeoPackage → QGIS (checking/buffering) → QGIS Server WMS (organisation maps)
```

Permissions stay in FreeSynergy (DB roles); the map tools are views with read/write links.

## Scenarios

- **Club**: maintain hut/hiking destinations, send the tour by GPX to the phone
- **Initiatives**: assembly locations + route waypoints (uMap public, editable only via token)
- **Marketplace**: provider locations on a map (skins: small ads/area search)
- **Disaster response**: reporting points compared via Overpass with OSM infrastructure

## Open points

- Collision/duplicate checking on point import (QGIS "near" or PostGIS)
- Timezone/timestamp conventions as in [data/](../../../data/models.md)
