# Coppermine - Funktionen

## Hauptfunktionen

- **Kategorien und Alben** mit Rechten je Album, private Alben pro Benutzer
- **Upload** über Web-Formular (mehrstufig), FTP-Import („Add files“-Modus)
- **Kommentare, Bewertungen, Favoriten**, Besuchs- und Bildzähler
- **Vorschaugrößen und Wasserzeichen**, Neuberechnung per Wartungsfunktion
- **Themes** (Layouts) und Sprachdateien, Blöcke für Seitenränder
- **Plugin-Schnittstelle** (`plugin_api`) für eigene Erweiterungen und Eingriffe in Abläufe

## Was Coppermine NICHT kann

- **Keine dokumentierte REST-API** für externe Clients (❌)
- **Keine Gesichts-/Objekterkennung**, keine semantische Suche (❌)
- **Kein Video-Streaming** (nur Einbettung per Player-Plugin) (❌)
- **Kein Auto-Backup von Handys** (❌)
- **Keine moderne Bildbearbeitung** (nur Rotieren, Zuschneiden, Wasserzeichen) (❌)
- **Kein responsives Standardlayout** ohne Theme-Anpassung (ältere Themen sind fest) (⚠)

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| `plugin_api` | PHP-Filter/Hooks in Upload-, Anzeige- und Admin-Abläufen |
| Themes | eigene Layouts mit Templates und CSS |
| Bridge | Anbindung an CMS (Joomla, WordPress, bbPress) |
| Import | FTP-Ordner, CSV/Batch-Werkzeuge von Drittanbietern |
| Authentifizierung | eigene Benutzer, Bridge-Login über CMS |
