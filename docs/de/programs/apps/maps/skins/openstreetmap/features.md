# OpenStreetMap - Funktionen

## Hauptfunktionen

### Datenmodell und Editieren
- Knoten/Ways/Relations + **Tagging** (`highway=residential`, `amenity=cafe`) — Presets in iD, JOSM-Presets mit Validierung
- Changesets mit Kommentar, Diskussions-Threads, Undo-Rollen der Community
- GPS-Traces, Bild-Geotags als Rohmaterial

### Abfrage und Dienste
- **Overpass API**: SQL-artige QL-Abfragen auf OSM-Objekte („alle Mülleimer in Stadt X“)
- **Nominatim**: Suchen/Rückwärts-Geocoding (Usage-Policy!)
- Kacheln (Raster) und Vektorkacheln kommerzieller + öffentlicher Anbieter (OSM-Basiskarten unendlich viele)

### Community-Werkzeuge
- OSM Chalets/Tasking-Manager (Humanitarian), MapRoulette-Mikroaufgaben, HOT-Projekte
- QA-Tools: KeepRight, OSM Hydrant

## Was OSM NICHT kann

- **keine garantierte Kartenqualität** — Datenqualität je Region unterschiedlich
- **kein „Amt“**: Adress-/Gebäudedefinitionen teils unvollständig
- Nominatim-Standardinstanz: **keine Massen-SLAs** (eigene Instanz für Last)
- **3D/Indoor**: Nischen (Indoor-Tagging experimentell)
- Kachel-Rendering betreibt OSM selbst nur für Standardkarte (Batch-Updates)

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| OSM-API/Overpass/Nominatim | offene HTTP-APIs |
| Overlays: Mapillary, Kartographer (Wikipedia) | Community-Dienste |
| Lizenz-Hinweis „© OpenStreetMap contributors“ | Pflicht bei Nutzung |
