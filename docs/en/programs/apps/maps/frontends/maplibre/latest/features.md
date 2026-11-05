# MapLibre - Features

## Main features

### Vector tiles + style spec
- PBF vector tiles styled at runtime (colours/lines/labels per zoom), sprite/glyph system
- **GL Style JSON**: sources (vector/raster/geojson), layer types (fill/line/circle/symbol/heatmap/3D extrusion)

### Rendering and 3D
- WebGL(-2): pitch/yaw camera, terrain (DEM tiles), building extrusion, filling of big data (heatmap)
- Markers/popups as a DOM overlay above the canvas

### Data paths
- GeoJSON sources live, `setData` updates; tile sources (template/URL)
- Tile stacks: Tilemaker/Planetiler → Martin/TileServer GL (self-hosted)

## What MapLibre does NOT do

- **no editor for map contents** (styling yes, data capture no)
- **no ready-made base map in the package** — tiles must be chosen/hosted
- WebGPU/indoor niches: not yet; the accessibility of the canvas is limited (DOM overlays needed)
- Print/PDF export only via detours (snapshot)

## Extensions and integrations

| Integration | Method |
|-------------|--------|
| MapLibre Android/iOS SDKs (descendants of Mapbox Native) | Apps |
| deck.gl layers (overlay) | Analytical maps |
| PMTiles | Single-file tile archives (serverless!) |
