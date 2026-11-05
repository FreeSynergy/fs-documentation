# MapLibre - API Dokumentation

## Übersicht

Zwei API-Ebenen: **JS-Karten-API** (`maplibregl`) und **Daten-/Stilformate** (Style Spec, Vektorkacheln/PMTiles) plus **SDKs für Android/iOS**. Kein Server-Produkt — der Kachelstack ist selbst gewählt.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| JS-API `Map`, `addSource/addLayer/setPaintProperty` | Kartensteuerung/Layer | offiziell |
| Style Spec v8 | Stil-JSON (portabel) | offiziell |
| `queryRenderedFeatures`, `project/unproject` | Hit-Teste/Koordinaten | offiziell |
| Kachel-APIs (selbst gehostet) | `/tiles/{z}/{x}/{y}.pbf`, `style.json` | Konvention |
| Webhooks/GraphQL | — | ❌ |

## Kernmethoden

| Methode | Beschreibung |
|---------|--------------|
| `map.setStyle(url,{diff:true})` | Stil wechseln (Diff-Update) |
| `map.addSource("punkte",{type:"geojson",data})` + `addSource`-Update (`setData`) | Live-Daten |
| `map.addLayer({id,type:"circle",source,paint})` | Ebene |
| `map.setPaintProperty(l,"circle-color",expr)` | Styling zur Laufzeit |
| `map.flyTo({center,zoom,bearing})` | animierte Kamera |
| `maplibregl.Marker().setLngLat().addTo(map)` | DOM-Marker |

## Beispiel

```js
const map = new maplibregl.Map({
  container: "karte",
  style: "https://tiles.example.org/osm-bright.json"
});
map.addSource("standpunkte", { type: "geojson",
  data: { type: "FeatureCollection", features: [] } });
map.addLayer({ id: "pk", type: "circle", source: "standpunkte",
  paint: { "circle-radius": 7, "circle-color": "#d33" } });
// Polling/eigener Update-Kanal:
quelle.setData(geojson);
```

## Kachel-Setups (Schema)

```
style.json  → sources: { osm: { tiles: ["https://t…/{z}/{x}/{y}.pbf"] } }
Betrieb: tilemaker/pmtiles + Martin/TileServer GL oder Cloudflare (PMTiles)
```

## Rate Limits

nicht bibliotheksseitig; Kachelserver-Limits.

## Skin-Hinweis

Standpunkte als GeoJSON-Quelle + `setData`-Kanäle = Live-Gruppenkarten; Stil-Hoheit erlaubt FreeSynergy-Farbwelt (Maputnik-Asset im Repository ablegen).
