# LibrePhotos - Funktionen

## Hauptfunktionen

### Erfassung
- Mobile Apps (iOS/Android) mit Auto-Backup, Web-Upload, Import aus Ordner
- Duplikaterkennung über Hash, Inkrementeller Scan bei Dateiänderungen

### Erkennung und Suche
- CLIP-basierte semantische Suche („rote Brille am Strand“)
- Gesichts-Clustering mit Benennen und Zusammenführen, Objekterkennung, Ortserkennung
- Zeitleiste, Ereigniserkennung (ereignisbasierte Auto-Alben)

### Präsentation
- Alben, Auto-Alben, Diashow, geteilte Alben mit Rechten
- Kartenansicht mit Cluster-Marker, Ortsgruppen

## Was LibrePhotos NICHT kann

- **Kein Webbaukasten-Design** (keine Themes/Galerievorlagen) — Oberfläche ist eine feste App (❌)
- **Keine echte Bildbearbeitung** über Crop hinaus (❌)
- **Kein Video-Transcoding für Adaptives Streaming** (Dateien werden direkt ausgeliefert) (❌)
- **Keine ausgereifte API-Dokumentation** — Endpunkte sind funktional, aber weniger stabil als Immich/PhotoPrism (⚠)
- **Keine mandantenfähige Mehrinstanzfähigkeit** (❌)

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| REST-API (Django REST) | offiziell, Ende-zu-Ende von der Web-UI genutzt |
| Hintergrund-Jobs | Celery + Redis, Scan-Pipelines |
| Authentifizierung | Token, OAuth2-Provider (optional), TwoFactor |
| Suche | PostgreSQL, Embedding-Vektoren |
| Karten | Leaflet/MapLibre-Kacheln (selbst gehostet) |
