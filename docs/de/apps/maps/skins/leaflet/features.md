# Leaflet - Funktionen

## Hauptfunktionen

- **Layer**: `L.tileLayer` (Raster), `L.imageOverlay`, `L.geoJSON` (Vektor-Daten direkt), Marker/Popup/Tooltip, Polyline/Polygon/Circle
- **Interaktion**: Panning/Zoom (Touch), Click-Handler, `L.control.*`-System, Custom Controls
- **Darstellung**: Retina-Kacheln, CSS-Filter-Overlays, SVG/Canvas-Renderer (`preferCanvas`)
- **Datenhaltung**: `L.geoJSON` lädt GeoJSON direkt — die Sprache aller anderen Karten-Skins

## Was Leaflet NICHT kann

- **kein 3D/Gelände** (kein Kippen/Pitch — dafür MapLibre/Cesium)
- **keine Vektorkachel-Styling-Engine** (Stil kommt vom Kachel-Server)
- **kein Clustering/Zeichnen eingebaut** (Plug-Ins: leaflet.markercluster, leaflet-draw/Geoman)
- große Punktmassen (>100k) ohne WebGL-Plugins träge (→ Leaflet+deck.gl)

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| Plugin-Ökosystem (Kacheln, Heatmaps, Messer) | Community, BSD-kompatibel |
| OSM/WMS/WMTS/TMS | Standard-Layer-Adapter |
| React/Vue/Angular | Wrapper-Bibliotheken vorhanden |
