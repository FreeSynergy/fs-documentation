# QGIS - Beschreibung

## Was das Programm macht

QGIS ist die Werkstatt für Geodaten: Daten vorbereiten, analysieren, kartografisch erzählen, als OGC-Dienst veröffentlichen. Überall dort, wo Standpunkte **geprüft, gepuffert, aggregiert** werden müssen, führt der Weg über QGIS.

## Vorteile

- **vollständiges GIS** unter GPL, Plattform übergreifend
- Processing = Automatisierbarkeit (Modelle, PyQGIS, Batch)
- Server im Projekt: aus dem Desktop direkt WMS veröffentlichen

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **ArcGIS Pro** | kommerziell, enterprise-verzahnt; QGIS offen/Community |
| **uMap/Leaflet** | Endanwender-Karten; QGIS Analyse-Werkstatt |
| **GRASS GIS** | Analyse-Maschine; QGIS = GUI + GRASS-Anbindung |

## Technische Details

- **Stack**: C++/Qt, Python (PyQGIS), GDAL/GEOS/PROJ-Bibliotheken
- **Formate**: GeoPackage (Standard!), PostGIS als Server-Basis
- **Deploy**: Desktop-Installer, Docker für QGIS Server, OGC via FCGI/MapServer-Konkurrenz
- **Lizenz**: GPL

## Für wen geeignet

- Kartengruppen mit Analyseanspruch + Betrieb eigener Kartendienste ([standpunkte.md](../../standpunkte.md))
