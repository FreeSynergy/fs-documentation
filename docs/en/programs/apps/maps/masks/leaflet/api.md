# Leaflet - API documentation

## Overview

Leaflet is the API: a JS library, no server interface. The integration points are the **layer URLs** (tiles/WMS/GeoJSON) that Leaflet loads, and the event API of the app.

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| JS API `L.map/L.tileLayer/L.geoJSON` | Map set-up/events | official |
| Data adapters | WMS/WMTS/TMS/`L.geoJSON(url)` (fetch wrapper) | official |
| REST/webhooks of your own data | The backend app's concern (e.g. FreeSynergy GeoJSON) | — |
| GraphQL | — | ❌ |

## Core objects

| Object | Description |
|--------|-------------|
| `L.map(id, {center,zoom})` | Map instance |
| `L.tileLayer(urlTemplate,{attribution,maxZoom})` | Raster layer |
| `L.geoJSON(data,{pointToLayer,onEachFeature})` | GeoJSON layer |
| `L.marker(latlng,{draggable})` | Draggable point (location point editor!) |
| `L.featureGroup`, `L.layerGroup` | Collections (show/hide) |
| `map.on("click"|"moveend")` | Events |

## Example

```js
const map = L.map("karte").setView([48.53, 9.058], 14);
L.tileLayer("https://tile.osm.example/{z}/{x}/{y}.png",
  { attribution: "© OpenStreetMap contributors" }).addTo(map);

fetch("/api/standpunkte.geojson")
  .then(r => r.json())
  .then(d => L.geoJSON(d, {
    onEachFeature: (f, l) => l.bindPopup(f.properties.beschreibung)
  }).addTo(map));
```

Drag a marker → send it back:

```js
m.on("dragend", () =>
  fetch("/api/standpunkte/" + m.id, { method: "PUT",
    body: JSON.stringify({ lat: m.getLatLng().lat, lon: m.getLatLng().lng }) }));
```

## Rate limits

Nonexistent — the tile/data servers decide (observe the OSM usage policies!).

## Skin note

A complete location point (Standpunkte) skin in ~50 lines: FreeSynergy provides the GeoJSON + PUT endpoints; Leaflet = the view layer ([standpunkte.md](../../standpunkte.md)).
