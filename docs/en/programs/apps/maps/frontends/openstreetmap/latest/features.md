# OpenStreetMap - Features

## Main features

### Data model and editing
- Nodes/ways/relations + **tagging** (`highway=residential`, `amenity=cafe`) — presets in iD, JOSM presets with validation
- Changesets with a comment, discussion threads, the community's undo roles
- GPS traces, image geotags as raw material

### Querying and services
- **Overpass API**: SQL-like QL queries on OSM objects ("all waste bins in city X")
- **Nominatim**: search/reverse geocoding (usage policy!)
- Tiles (raster) and vector tiles from commercial + public providers (endless OSM base maps)

### Community tools
- OSM Chalets/tasking manager (humanitarian), MapRoulette micro-tasks, HOT projects
- QA tools: KeepRight, OSM Hydrant

## What OSM does NOT do

- **no guaranteed map quality** — data quality differs by region
- **no "official office"**: address/building definitions partly incomplete
- The Nominatim standard instance: **no mass SLAs** (your own instance for load)
- **3D/indoor**: niches (indoor tagging experimental)
- OSM itself only runs tile rendering for the standard map (batch updates)

## Extensions and integrations

| Integration | Method |
|-------------|--------|
| OSM API/Overpass/Nominatim | Open HTTP APIs |
| Overlays: Mapillary, Kartographer (Wikipedia) | Community services |
| Licence notice "© OpenStreetMap contributors" | Mandatory when using |
