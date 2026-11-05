# Lychee - Funktionen

## Hauptfunktionen

- **Alben und Unteralben** mit Sortierung nach Datum/Titel, Cover-Auswahl
- **Freigaben** pro Album: Link, Passwort, Gültigkeit, Rechte (Ansehen/Herunterladen)
- **Upload** per Drag & Drop, URL-Import, Ordner-Upload; Stapelverarbeitung der Größen
- **Lightbox** mit Vollbild, Slideshow, EXIF-Overlay, Drehen und Zuschneiden
- **Smart Albums**: gespeicherte Suche, die automatisch befüllt wird
- **Mehrere Nutzer** mit Quotas und eigenen Alben

## Was Lychee NICHT kann

- **Keine Gesichts-/Objekterkennung**, keine semantische Suche (❌)
- **Kein Handy-Auto-Backup** (Upload nur manuell/Web, App von Drittanbietern) (❌)
- **Keine Kategorien-Rechtematrix wie Piwigo** (Freigaben nur pro Album) (❌)
- **Kein Video-Streaming** (Videos werden nur heruntergeladen) (❌)
- **Keine Themes/Galerievorlagen** — einheitliche React-Oberfläche (❌)

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| REST-API `/api` | offiziell, vollständig |
| OAuth2/SSO | Anbieter konfigurierbar (Apple, GitHub, Google …) |
| Webhooks | — (❌) |
| Storage | lokaler Ordner, external disk-Adapter begrenzt unterstützt |
| Import | aus Lightroom-Exporten, URL-Import |
