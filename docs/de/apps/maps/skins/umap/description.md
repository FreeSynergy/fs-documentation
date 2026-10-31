# uMap - Beschreibung

## Was das Programm macht

uMap macht aus OSM-Karten gemeinsam gepflegte Themencards: Wanderung mit Hütten, Mitglieder-Standorte, Demo-Treffpunkte — Ebenen, Marker mit Popup-Text, Teil-Link geradewegs ins Wiki.

## Vorteile

- **null GIS-Wissen nötig**, sofort kollaborativ
- **Daten bleiben als GeoJSON greifbar** (Import/Export/Remote-Quellen)
- self-hostbar, in FreeSynergy-Umgebung gut integrierbar

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **Google My Maps** | proprietär, kein Export-Kreislauf; uMap offen |
| **QGIS-Web-Publizieren** | Profi-Workflows; uMap Endanwender-Editor |
| **OSM direkt** | globale Daten; uMap private/Gruppen-Karten auf OSM-Basis |

## Technische Details

- **Stack**: Django (Python), PostgreSQL/PostGIS, Leaflet-Frontend
- **Modelle**: Map (JSON-Datenblob oder datamode remote), Datalayer, Pict
- **Auth**: Instanz-Login optional; Kartenzugriff per Link/Token
- **Lizenz**: MPL-2.0 (uMap), OSM-Daten ODbL

## Für wen geeignet

- Gruppen, die Orte gemeinsam sammeln/kommentieren → Kern des [Standpunkte-Modells](../../standpunkte.md)
