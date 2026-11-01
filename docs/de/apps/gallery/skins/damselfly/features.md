# Damselfly - Funktionen

## Hauptfunktionen

- **Inkrementelle Indexierung** über Dateisystem-Watcher; neue Dateien erscheinen automatisch
- **KI-Pipeline**: Gesichts-Clustering, Szenen-/Objektlabels, OCR (Text im Bild), Ähnlichkeitssuche (Vektoren in pgvector)
- **Suche** über Text, Datumsbereich, Ordner, Labels, Personen, Farbe
- **Alben und Freigaben** mit Links und Einbettung (iframe)
- **Duplikaterkennung** und Bulk-Werkzeuge (Umbenennen, Verschieben, Labeln)

## Was Damselfly NICHT kann

- **Kein Handy-Auto-Backup** (Upload nur Web/Sync) (❌)
- **Keine Themes/Galerievorlagen** — einheitliche React-Oberfläche (❌)
- **Keine Rechte pro Ordner** (Freigaben nur pro Album/Link) (❌)
- **Kein Video-Transcoding** (Videos werden nur vorgemerkt/ausgeliefert) (❌)
- **Keine RAW-Entwicklung**, nur Vorschaubereitstellung (❌)

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| REST-API | offiziell, auch für Bulk-Upload |
| Storage | lokaler Ordner, S3-kompatibel in neueren Versionen |
| Authentifizierung | lokale Konten, Reverse-Proxy-Auth |
| Webhooks | — (❌) |
| Backups | Datenbank-Dump plus Ordner-Sync |
