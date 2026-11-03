# uMap - Funktionen

## Hauptfunktionen

### Karten-Diagramm
- Marker/Linien/Flächen/Kreise mit Icon-Auswahl, Farbe, Popup (Text/HTML/Bilder), Attribute als Datenfelder
- **Ebenen**: Gruppierung + Clustering + Filter; Datentabelle pro Ebene

### Austausch
- Import/Export: GeoJSON, GPX, KML, CSV/KCSV; „Daten als Link“ (Remote-GeoJSON als Quelle!)
- Einbetten (iframe), Links zum Anschauen/Mitschreiben

### Kollaboration
- Echtzeit-Multiplayer-Edit (neuere Versionen), Edit-Token-Link, anonyme Bearbeitung konfigurierbar
- Versions-/Historienfunktion der Karten (Instanzabhängigkeit)

## Was uMap NICHT kann

- **kein Routing/Navigation** (reine Darstellung; für Navigations-Skins → OsmAnd/Organic)
- **keine Feingeometrie-Werkzeuge** (Buffer/Schnitt → QGIS)
- **keine Rollentiefen** (nur Eigentümer/Token-Redakteure/Öffentlich)
- Attributdaten ohne Beziehungen (flach)

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| Remote-GeoJSON | Live-Datenquellen aus eigenen Diensten |
| iframe-Einbettung | CMS-Wiki-eigene Seiten |
| Self-hosting (Django) | volle Datenkontrolle |
