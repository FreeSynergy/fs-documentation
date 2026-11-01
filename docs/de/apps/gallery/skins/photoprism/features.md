# PhotoPrism - Funktionen

## Hauptfunktionen

### Indexierung
- Sammelordner wird einmalig gescannt und danach inkrementell aktualisiert (auch per CLI `photoprism index`)
- EXIF/XMP, Video-Metadaten, Sidecar-Dateien; Duplikate über Prüfsumme
- Vorschaubilder und passende Größen werden erzeugt, Originale bleiben unangetastet

### Suche und Erkennung
- Volltext, Label (KI-Vorschläge + manuell), Farbe, Ort, Kamera, Datum, Medien­typ
- Gesichts-Clustering mit Benennen und Geburtstag; Gesichts-„Suche wie dieses“
- Ähnlichkeitssuche über Bildvektoren (Plus/CE), OCR auf Text in Bildern

### Präsentation
- Alben (physische Ordner oder virtuelle Selektion), Stories, Diashow, public Share-Links
- Wasserzeichen und Download-Rechte pro Freigabe (Plus), Passwortschutz für Links

### Organisation
- Umbenennen/Verschieben im Ordnerbaum, Tagging, Favoriten, Archiv, Verstecken
- Import aus Import-Ordner, Aufräumen (Duplikate, fehlende Vorschauen)

## Was PhotoPrism NICHT kann

- **Kein Auto-Backup vom Handy** wie Immich — Upload nur über Web/CLI/Sync (❌)
- **Kein durchgängiger Video-Streaming-Player** mit Mehrspur-Auswahl (❌)
- **Bildbearbeitung nur elementar**: Crop, Rotation, Zeitstempel — keine Ebenen/RAW-Entwicklung (❌)
- **Keine frei gestaltbaren Galerie-Seiten/Themes** wie Piwigo (❌)
- **Gesichts- und Semantik-KI teils nur in der Plus/CE-Variante** (Community-Edition ist reduziert)

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| REST-API `/api/v1` | offiziell, vollständig |
| Webhooks | `PHOTOPRISM_WEBHOOK_*` optional |
| Authentifizierung | OIDC/SSO, LDAP (Plus), API-Key, Basic |
| Storage | eigener Ordner, S3-Import/Export (Plus) |
| Sharing | Freigabe-Links, öffentliche Galerie-Ordner |
