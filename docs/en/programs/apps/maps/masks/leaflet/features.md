# Leaflet - Features

## Main features

- **Layers**: `L.tileLayer` (raster), `L.imageOverlay`, `L.geoJSON` (vector data directly), marker/popup/tooltip, polyline/polygon/circle
- **Interaction**: panning/zoom (touch), click handlers, the `L.control.*` system, custom controls
- **Rendering**: retina tiles, CSS filter overlays, SVG/canvas renderers (`preferCanvas`)
- **Data handling**: `L.geoJSON` loads GeoJSON directly — the language of all the other map skins

## What Leaflet does NOT do

- **no 3D/terrain** (no tilting/pitch — use MapLibre/Cesium for that)
- **no vector-tile styling engine** (the style comes from the tile server)
- **no built-in clustering/drawing** (plugins: leaflet.markercluster, leaflet-draw/Geoman)
- Large point masses (>100k) are sluggish without WebGL plugins (→ Leaflet + deck.gl)

## Extensions and integrations

| Integration | Method |
|-------------|--------|
| Plugin ecosystem (tiles, heatmaps, measuring tool) | Community, BSD-compatible |
| OSM/WMS/WMTS/TMS | Standard layer adapters |
| React/Vue/Angular | Wrapper libraries available |
