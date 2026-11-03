# QGIS - Funktionen

## Hauptfunktionen

### Daten und Layer
- Formate: GeoPackage, Shapefile, GeoJSON, PostGIS, WMS/WFS/WMTS, COG/GeoTIFF, SpatiaLite
- Koordinatensysteme (CRS-On-the-fly), Tabellen-Joins/Relations, Attribut-Editor mit Field Calculator

### Analyse (Processing)
- Overlays (Buffer, Intersect, Union), Statistik, Raster-Kalküle, Netzwerk-Analysen (QNEAT/ORS-Plugins)
- **Modell-Designer**: Analyseketten als wiederverwendbare Prozesse

### Präsentation
- Druckerstellung (Layouts mit Legende, Nordpfeil, Atlas-Ausgaben je Feature!), SLD/qml-Styling, 3D-Ansichten

### Veröffentlichen
- **QGIS Server** (eingebaut via FCGI): OGC WMS/WFS/WCS aus dem Projekt (.qgs) — FreeSynergy-Karten-Backend!
- Web-Export-Plugins (qgis2web → Leaflet/MapLibre-Code)

## Was QGIS NICHT kann

- **kein Multiplayer-Web-Editor** (Desktop-Werkzeug; Server = Lesen/Dienste)
- **kein Echtzeit-Collaboration-Editing** (Datenbanken können es, QGIS nicht als Team-UI)
- **keine mobile Datenerfassung im Kern** (QField/Mergin als Begleit-Apps — anderes Projekt)
- Batch-Koordinatenkonvertierung nur über Projekt-Workflows

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| Plugin-Katalog (hunderte) | in-App-Installation |
| GRASS/GDAL nativ verschaltet | Processing |
| QField/Mergin/Mobile | Schwesterprojekte |
