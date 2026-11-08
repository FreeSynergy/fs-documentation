# Mapping Systems

## In short

FreeSynergy Maps brings map data to your device and keeps the places you care about. It answers the question: can I have my own map, and still use it when the network is gone? It loads a map piece by piece, only what you look at, and you can download a whole region to use offline.

## What is different here

- There is no default map server and nothing is copied. You point it at any map source you choose, in the open PMTiles format.
- It does not hammer public servers: it will not use the OpenStreetMap tile servers, it requires a clear User-Agent, and it asks for few requests.
- The required attribution is written into every downloaded region.
- Places are stored as GeoJSON, an open standard. Maps owns the places interface.
- Tiles are cached on your disk with a size limit you set.

## Where it stands today

Latest tag: `v0.2.0`. Today it is the core, without a window. It can read map tiles from a remote or local PMTiles file and cache them on disk with a hard size limit and a seven-day expiry. It can download a region for offline use, telling you the number of tiles and a size estimate first, with a tile limit, progress and a cancel option. It keeps places as GeoJSON (create, update, delete, find by name, find everything inside an area) and reads and writes `geo:` links.

Not there yet (planned): a window and the drawing of maps (tile decoding, styles, search by address and routes are not started), a server so other programs can reach it, live notification when a place changes. The interface for places is a draft with no consumer yet.

## Overview

This section contains documentation for various mapping and GIS systems.

## Available Systems

- **openstreetmap** - Collaborative map project
- **mapbox** - Customizable maps
- **leaflet** - Interactive maps library
- **cesium** - 3D globe and map engine
- **qgis** - GIS software
- **arcgis** - Geographic information system
- **google-maps** - Google Maps API
- **openlayers** - Maps library
- **carto** - Geospatial platform
- **maplibre** - Open source mapping
- **tangram** - Real-time 3D maps
- **mapnik** - Map rendering engine
- **geoserver** - Geospatial server
- **postgis** - Spatial database
- **mapbox-gl-js** - Interactive maps

## What is a Mapping System?

A mapping system is software for creating, displaying, and analyzing maps and geographic data. Mapping systems include:

- Map display and navigation
- Geospatial data management
- Map layers and styles
- Geocoding and reverse geocoding
- Route planning and navigation
- Geospatial analysis

## Application Areas

- **Navigation**: Route planning and navigation
- **GIS**: Geographic information systems
- **Logistics**: Logistics and transportation
- **Environment**: Environmental monitoring and analysis
- **Urban planning**: Urban planning and development
- **Tourism**: Tourism and travel

## Benefits of Mapping Systems

- **Visualization**: Visualize geographic data
- **Analysis**: Geospatial analysis
- **Integration**: Integration with other data
- **Interactivity**: Interactive maps
- **Mobile**: Mobile map applications

## Selection Criteria

When choosing a mapping system, consider the following criteria:

- **Features**: Which features are required?
- **Scalability**: How many maps and users?
- **Ease of use**: How user-friendly is it?
- **Integration**: Integration with other tools
- **Costs**: Free or paid?
- **Open Source**: Is the system open source?

## Related Categories

- [ERP](../../suites/erp/) - Enterprise resource planning
- [Project Management](../../suites/projectmanagement/) - Project management

## Quick Start

1. **Select system**: Choose a system based on requirements
2. **Installation/Account**: Install system or create account
3. **Configuration**: Customize and configure the system
4. **Import data**: Import geographic data
5. **Create maps**: Create first maps

## More Information

Further information can be found in the documentation of individual mapping systems.

## Frontends

<!-- gen:frontends (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
Analysed programs (7), by function, nothing copied (ADR 0012/0013):

- [Leaflet](frontends/leaflet/index.md) — Leaflet (BSD-2-Clause) is the lightweight JavaScript map library: raster tiles, markers, polygons, layer switching, touch support — the standard on which uMap and thousands of map widgets sit.
- [MapLibre](frontends/maplibre/index.md) — MapLibre (BSD, a fork from Mapbox GL JS after the licence change) is the **vector-map engine**: tiles + style JSON (GL Style Spec), WebGL rendering with 3D tilts, custom styles (Maputnik), self-hos…
- [OpenStreetMap](frontends/openstreetmap/index.md) — OpenStreetMap (OSM) is the worldwide collaborative mapping platform: everyone edits the geodata ("the wiki of maps").
- [Organic Maps](frontends/organic-maps/index.md) — Organic Maps (GPL, subscription-free nonprofit app) is the lean offline map/navigation app (Android/iOS/desktop): fast, sparing with data (no tracking/advertising logic), OSM-based, with own places…
- [OsmAnd](frontends/osmand/index.md) — OsmAnd (Apache-2.0) is the offline navigation app based on OSM (Android/iOS): downloadable map regions, routing (car/bike/foot; public-transport planner available offline), POI search, track record…
- [QGIS](frontends/qgis/index.md) — QGIS (GPL) is the professional desktop GIS: layers (shapefile/GeoPackage/PostGIS/WMS), analysis tools (buffers, overlays, geoprocessing), print layouts, **QGIS Server** (OGC services) and Python (P…
- [uMap](frontends/umap/index.md) — uMap (uMap Project, free software) is **collaborative map diagramming**: own layers with markers/polylines/polygons, popup contents (HTML), sharing via link, multi-user editing.

Overview: [frontends](frontends/index.md)
<!-- /gen:frontends -->
