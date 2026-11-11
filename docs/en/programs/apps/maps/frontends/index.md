# Maps — Frontends

Frontends of well-known programs in this category, analysed for their **functions** — nothing is copied (ADR 0013). A program is documented here because it is widely learned or because it has a notable idea. Our own program for this category is `FreeSynergy.Maps` (ADR 0017); its capabilities and status live in [requirements](../requirements.md).

## Programs

| Program | Versions | What it is |
|---------|----------|------------|
| [Felt](felt/index.md) | [latest](felt/latest/description.md) | Felt is a browser-based mapping and GIS service where several people edit the same map at once. |
| [Google Earth](google-earth/index.md) | [latest](google-earth/latest/description.md) | Google Earth shows the planet as a 3D globe in the browser and in mobile apps. |
| [Leaflet](leaflet/index.md) | [latest](leaflet/latest/description.md) | Leaflet (BSD-2-Clause) is the lightweight JavaScript map library: raster tiles, markers, polygons, layer switching, touch support — the standard on which uMap and thousands of map widgets sit. |
| [MapLibre](maplibre/index.md) | [latest](maplibre/latest/description.md) | MapLibre (BSD, a fork from Mapbox GL JS after the licence change) is the **vector-map engine**: tiles + style JSON (GL Style Spec), WebGL rendering with 3D tilts, custom styles (Maputnik), self-hos… |
| [OpenStreetMap](openstreetmap/index.md) | [latest](openstreetmap/latest/description.md) | OpenStreetMap (OSM) is the worldwide collaborative mapping platform: everyone edits the geodata ("the wiki of maps"). |
| [Organic Maps](organic-maps/index.md) | [latest](organic-maps/latest/description.md) | Organic Maps (GPL, subscription-free nonprofit app) is the lean offline map/navigation app (Android/iOS/desktop): fast, sparing with data (no tracking/advertising logic), OSM-based, with own places… |
| [OsmAnd](osmand/index.md) | [latest](osmand/latest/description.md) | OsmAnd (Apache-2.0) is the offline navigation app based on OSM (Android/iOS): downloadable map regions, routing (car/bike/foot; public-transport planner available offline), POI search, track record… |
| [QGIS](qgis/index.md) | [latest](qgis/latest/description.md) | QGIS (GPL) is the professional desktop GIS: layers (shapefile/GeoPackage/PostGIS/WMS), analysis tools (buffers, overlays, geoprocessing), print layouts, **QGIS Server** (OGC services) and Python (P… |
| [uMap](umap/index.md) | [latest](umap/latest/description.md) | uMap (uMap Project, free software) is **collaborative map diagramming**: own layers with markers/polylines/polygons, popup contents (HTML), sharing via link, multi-user editing. |

## File set per program (ADR 0012)

```
programs/apps/maps/frontends/<program>/
├── index.md        what it is, notable ideas, documented versions, sources
├── changelog.md    changes between documented versions (≥ 2 versions)
└── <version>/
    ├── description.md    required · Detailed description, differentiation, who it suits
    ├── features.md       required · What the program can do — and what not
    ├── layout.md         required · Window structure, regions, panels
    ├── menus.md          required · Menu structure, context menus, menus by role
    ├── shortcuts.md      required · Keyboard shortcuts
    ├── api.md            required · APIs and protocols, authentication, rate limits
    ├── themes/index.md   required · Themes: colours, typography, spacing — what can be rebuilt
    ├── interaction.md    if needed · Hover, focus, drag, gestures (finger, mouse, pen)
    ├── states.md         if needed · UI states and transitions
    ├── events.md         if needed · Events to the outside (webhooks, push, streams)
    ├── limits.md         if needed · Known limitations
    ├── i18n.md           if needed · Localisation, writing direction
    └── dependencies.md   if needed · Which of our components a frontend in this style needs
```

Protocols (Matrix, IMAP, CalDAV, …) are not frontends; they are described under [data](../../../../data/standards.md).
