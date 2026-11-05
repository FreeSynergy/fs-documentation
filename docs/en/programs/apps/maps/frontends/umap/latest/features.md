# uMap - Features

## Main features

### Map chart
- Markers/lines/areas/circles with icon choice, colour, popup (text/HTML/images), attributes as data fields
- **Layers**: grouping + clustering + filtering; a data table per layer

### Exchange
- Import/export: GeoJSON, GPX, KML, CSV/KCSV; "data as link" (remote GeoJSON as a source!)
- Embedding (iframe), links for viewing/co-writing

### Collaboration
- Real-time multiplayer editing (newer versions), edit-token link, configurable anonymous editing
- Version/history function of the maps (instance-dependent)

## What uMap does NOT do

- **no routing/navigation** (pure presentation; for navigation frontends → OsmAnd/Organic)
- **no fine geometry tools** (buffer/intersection → QGIS)
- **no depth of roles** (only owner/token editors/public)
- Attribute data without relations (flat)

## Extensions and integrations

| Integration | Method |
|-------------|--------|
| Remote GeoJSON | Live data sources from your own services |
| iframe embedding | CMS/wiki's own pages |
| Self-hosting (Django) | Full data control |
