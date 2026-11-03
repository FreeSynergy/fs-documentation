# Leaflet - Beschreibung

## Was das Programm macht

Leaflet stellt „eine Karte ins Div“: Kacheln, Marker, GeoJSON — in ~40 KB JS, überall lauffähig (älteste Smartphones inklusive). Es ist Bibliothek, kein Dienst: Kartenhosting und Daten kommen von woanders (OSM-Kacheln sind der Klassiker).

## Vorteile

- **minimal, stabil, BSD** — API hält seit Jahren
- **GeoJSON-first** = perfekter Partner für uMap/QGIS-Datenkreisläufe
- riesige Plugin-/Tutorial-Landschaft

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **MapLibre GL** | Vektorkacheln, 3D/Pitch, Styling; Leaflet = Raster+SVG-Pragmatismus |
| **OpenLayers** | GIS-Vollausbau (Projektionen, WebGIS-Standards); Leaflet bewusst schmal |
| **Google Maps JS** | proprietär + Kosten; Leaflet frei |

## Technische Details

- **API**: `L.map('id')`, `L.tileLayer(url,{attribution})`, `L.geoJSON(data)`
- **Lizenz**: BSD-2-Clause
- **Alter**: seit 2011 (CloudMade→Community), 1.x stabil gepflegt

## Für wen geeignet

- Wiki-/CMS-Einbettungen, Standpunkt-Dashboards, Prototypen ([standpunkte.md](../../standpunkte.md))
