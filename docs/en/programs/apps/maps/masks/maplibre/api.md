# MapLibre - API documentation

## Overview

Two API levels: the **JS map API** (`maplibregl`) and the **data/style formats** (style spec, vector tiles/PMTiles) plus **SDKs for Android/iOS**. No server product — the tile stack is your own choice.

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| JS API `Map`, `addSource/addLayer/setPaintProperty` | Map control/layers | official |
| Style spec v8 | Style JSON (portable) | official |
| `queryRenderedFeatures`, `project/unproject` | Hit tests/coordinates | official |
| Tile APIs (self-hosted) | `/tiles/{z}/{x}/{y}.pbf`, `style.json` | Convention |
| Webhooks/GraphQL | — | ❌ |

## Core methods

| Method | Description |
|--------|-------------|
| `map.setStyle(url,{diff:true})` | Change the style (diff update) |
| `map.addSource("punkte",{type:"geojson",data})` + `addSource` update (`setData`) | Live data |
| `map.addLayer({id,type:"circle",source,paint})` | Layer |
| `map.setPaintProperty(l,"circle-color",expr)` | Styling at runtime |
| `map.flyTo({center,zoom,bearing})` | Animated camera |
| `maplibregl.Marker().setLngLat().addTo(map)` | DOM marker |

## Example

```js
const map = new maplibregl.Map({
  container: "map",
  style: "https://tiles.example.org/osm-bright.json"
});
map.addSource("standpunkte", { type: "geojson",
  data: { type: "FeatureCollection", features: [] } });
map.addLayer({ id: "pk", type: "circle", source: "standpunkte",
  paint: { "circle-radius": 7, "circle-color": "#d33" } });
// Polling / own update channel:
source.setData(geojson);
```

## Tile setups (schema)

```
style.json  → sources: { osm: { tiles: ["https://t…/{z}/{x}/{y}.pbf"] } }
Operation: tilemaker/pmtiles + Martin/TileServer GL or Cloudflare (PMTiles)
```

## Rate limits

Not on the library side; tile server limits.

## Skin note

Location points as a GeoJSON source + `setData` channels = live group maps; style control allows the FreeSynergy colour world (keep the Maputnik asset in the repository).
