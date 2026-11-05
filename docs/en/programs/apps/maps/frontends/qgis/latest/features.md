# QGIS - Features

## Main features

### Data and layers
- Formats: GeoPackage, shapefile, GeoJSON, PostGIS, WMS/WFS/WMTS, COG/GeoTIFF, SpatiaLite
- Coordinate systems (CRS on the fly), table joins/relations, attribute editor with field calculator

### Analysis (processing)
- Overlays (buffer, intersect, union), statistics, raster calculations, network analyses (QNEAT/ORS plugins)
- **Model designer**: analysis chains as reusable processes

### Presentation
- Print creation (layouts with legend, north arrow, atlas outputs per feature!), SLD/qml styling, 3D views

### Publishing
- **QGIS Server** (built in via FCGI): OGC WMS/WFS/WCS from the project (.qgs) — the FreeSynergy map backend!
- Web export plugins (qgis2web → Leaflet/MapLibre code)

## What QGIS does NOT do

- **no multiplayer web editor** (a desktop tool; the server = reading/services)
- **no real-time collaborative editing** (databases can do it, QGIS not as a team UI)
- **no mobile data capture in the core** (QField/Mergin as companion apps — a different project)
- Batch coordinate conversion only via project workflows

## Extensions and integrations

| Integration | Method |
|-------------|--------|
| Plugin catalogue (hundreds) | In-app installation |
| GRASS/GDAL natively wired up | Processing |
| QField/Mergin/Mobile | Sister projects |
