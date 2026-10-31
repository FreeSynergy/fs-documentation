# MapLibre - Beschreibung

## Was das Programm macht

MapLibre rendert Karten als Vektor-Stapel: Der Browser zeichnet Straßen/Gebäude/Labels aus Kacheln im eigenen Stil — skalierbar, animierbar, 3D-fähig. Aus der Mapbox-GL-Gemeinschaft entstanden, als freier Zweig (Fork) nach deren Lizenzwechsel.

## Vorteile

- **freier Stil-Freiraum** (Maputnik, eigene Kacheln, PMTiles-Dateien)
- **Performance** bei großen Datenmengen (WebGL)
- API kompatibel genug zu Mapbox GL, Migration einfach

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **Leaflet** | Raster+DOM, simpel; MapLibre = WebGL/Stil-Engine |
| **Mapbox GL** | Dienst+Token-Pflicht; MapLibre neutral/self-hosted |
| **Cesium** | Globe/Zeitalter-3D; MapLibre bleibt bei Web-Mercator-Karten |

## Technische Details

- **API**: `maplibregl.Map({style: url|json})`, Layer-/Source-API, `queryRenderedFeatures`
- **Kacheln**: pbf + style.json; Alternativen PMTiles (Single-File)
- **Lizenz**: BSD-3

## Für wen geeignet

- Karten-Apps mit Eigenstil/Performance; FreeSynergy-Skins für interaktive Standpunkt-Karten mit 3D/Cluster
