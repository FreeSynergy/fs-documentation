# Piwigo - Funktionen

## Hauptfunktionen

### Galerie-Struktur
- Beliebig tiefe Kategorien (Alben), ein Bild in mehreren Kategorien
- Status je Bild: veröffentlicht, wartend, privat; Sichtbarkeit je Gruppe
- Tags, benutzerdefinierte Felder, Beschreibung/Untertitel, EXIF-Anzeige

### Präsentation
- Themes und Templates, Startseite konfigurierbar, Slideshow, Direktlink zu voller Größe
- Mehrsprachigkeit, RTL, RSS, Sitemap
- Bestbewertung, Zähler, Kommentare mit Moderation

### Verwaltung
- „AddPictures“: Ordner vom Server in die Galerie übernehmen (Sync)
- Batch-Verwaltung: Rotieren, Metadaten, Kategorien, Tags, Löschen in Serien
- Wasserzeichen-Cron, Größen generieren (TH/CU/…), Import aus Picasa/Piwigo-Export

## Was Piwigo NICHT kann

- **Keine Gesichts-/Objekterkennung und semantische Suche** in der Basis (nur per Plugins, dann begrenzt) (❌)
- **Kein Handy-Auto-Backup** als Kernfunktion (❌)
- **Kein Video-Streaming** mit Adaptiver Bitrate — Video nur per Player-Plugin (❌)
- **Keine moderne Foto-Cloud-Timeline** wie Immich, Oberfläche ist klassisches Webbaukasten-Design
- **Keine echte Bildbearbeitung** (nur Rotieren, Zuschneiden, Wasserzeichen) (❌)

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| Webservice-API `ws.php` | offiziell, von Mobile-Apps genutzt |
| Plugins | >300 Erweiterungen (Comment, Metadata, Video-js, Companion …) |
| Companion (App) | offizielle Mobile-App, Upload aus Rolle |
| OAuth2/Social | Login/Registrierung via Provider (Plugin) |
| Import | Picasa, Piwigo-Export, FTP/Sync-Ordner |
