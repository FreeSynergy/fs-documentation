# MapLibre - Funktionen

## Hauptfunktionen

### Vektorkacheln + Stil-Spec
- PBF-Vektorkacheln zur Laufzeit gestylt (Farben/Linien/Labels per Zoom), Sprite/Glyph-System
- **GL Style JSON**: Quellen (vector/raster/geojson), Layertypen (fill/line/circle/symbol/heatmap/3D-extrusion)

### Rendering und 3D
- WebGL(-2): Pitch/Yaw-Kamera, Geländeterrain (DEM-Fliesen), Gebäude-Extrusion, Filling von Big Data (heatmap)
- Marker/Popup als DOM-Overlay über Canvas

### Datenwege
- GeoJSON-Quellen live, `setData`-Updates; Kachelquellen (Template/URL)
- Kachel-Stacks: Tilemaker/Planetiler → Martin/TileServer GL (self-hosted)

## Was MapLibre NICHT kann

- **kein Editor für Karteninhalte** (Styling ja, Datenerfassung nein)
- **keine fertige Basiskarte im Paket** — Tiles müssen gewählt/gehostet werden
- WebGPU/Indoor-Nischen: noch nicht; Accessibility des Canvas eingeschränkt (DOM-Overlays nötig)
- Print-/PDF-Export nur über Umwege (Snapshot)

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| MapLibre Android/iOS-SDKs (Nachfahren von Mapbox Native) | Apps |
| deck.gl-Layer (Overlay) | analytische Karten |
| PMTiles | einzelne Datei-Kachelarchive (Serverless!) |
