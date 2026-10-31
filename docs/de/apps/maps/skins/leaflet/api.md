# Leaflet - API Dokumentation

## Übersicht

Leaflet ist die API: eine JS-Bibliothek, keine Server-Schnittstelle. Integrationspunkte sind **Layer-URLs** (Kacheln/WMS/GeoJSON), die Leaflet lädt, und die Ereignis-API der App.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| JS-API `L.map/L.tileLayer/L.geoJSON` | Kartenaufbau/Events | offiziell |
| Datenadapter | WMS/WMTS/TMS/`L.geoJSON(url)` (fetch-wrapper) | offiziell |
| REST/Webhooks eigener Daten | Sache der Backend-App (z.B. FreeSynergy-GeoJSON) | — |
| GraphQL | — | ❌ |

## Kernobjekte

| Objekt | Beschreibung |
|--------|--------------|
| `L.map(id, {center,zoom})` | Karteninstanz |
| `L.tileLayer(urlTemplate,{attribution,maxZoom})` | Raster-Ebene |
| `L.geoJSON(data,{pointToLayer,onEachFeature})` | GeoJSON-Ebene |
| `L.marker(latlng,{draggable})` | verschiebbarer Punkt (Standpunkt-Editor!) |
| `L.featureGroup`, `L.layerGroup` | Sammlungen (Ein-/Ausblenden) |
| `map.on("click"|"moveend")` | Events |

## Beispiel

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

Marker ziehen → zurücksenden:

```js
m.on("dragend", () =>
  fetch("/api/standpunkte/" + m.id, { method: "PUT",
    body: JSON.stringify({ lat: m.getLatLng().lat, lon: m.getLatLng().lng }) }));
```

## Rate Limits

nicht existent — entscheiden Kachel-/Datenserver (OSM-Nutzungsrichtlinien beachten!).

## Skin-Hinweis

Kompletter Standpunkte-Skin in ~50 Zeilen: FreeSynergy liefert GeoJSON + PUT-Endpunkte; Leaflet = View-Layer ([standpunkte.md](../../standpunkte.md)).
