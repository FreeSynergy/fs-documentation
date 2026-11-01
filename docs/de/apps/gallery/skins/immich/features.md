# Immich - Funktionen

## Hauptfunktionen

### Erfassung und Upload
- Auto-Backup der Handy-Fotos (iOS/Android), Duplikaterkennung, Fortschritts-Wiederaufnahme
- Web-Upload ganzer Ordner, import aus anderen Systemen (CLI `immich-cli`, Google-Photos-Import)
- EXIF/XMP-Auswertung: Kameradaten, GPS, Aufnahmedatum; Umkehrgeocoding für Orte

### Organisation
- Zeitleiste (Tag/Monat/Jahr), Kalenderansicht, Maps-Ansicht (Kacheln auf eigenen Karten)
- Alben, Geteilte Alben, Geteilte Links (Passwort, Ablauf, Download-Recht)
- Stapel (Stacks) für Bracketing/Panorama, Favoriten, Archiv, Mülleimer mit Frist
- Schlagwörter und eigene Suchbegriffe; Smart Search (CLIP) für „strand“, „cat“ …

### Erkennung
- Gesicht clustering mit benannten Personen, Gesichts-Biometrie
- Objekterkennung, Szenenerkennung, semantische Suche
- Duplikaterkennung (pHash), Ähnlichkeitssuche pro Aufnahme

### Bearbeitung
- Crop/Drehen, Zeitstempel korrigieren, xmp-Seiteneffekte; Videos: Transcoding (H.264/HEVC, Thumbnails/GIF)
- Stapelverarbeitung von Miniaturbildern und Vorschaumaßstäben (Original bleibt unverändert)

## Was Immich NICHT kann

- **Kein vollständiger Bildeditor** (keine Ebenen, keine RAW-Entwicklung in der App) — RAW wird nur als Original gespeichert (❌)
- **Kein Digital-Rights-Management / Watermarking** (❌)
- **Kein klassisches Webbaukasten-Galeriedesign** (keine frei positionierbaren Galerien à la Piwigo-Erweiterungen)
- **Keine mehrsprachige Öffentliche-Website-Galerie** im Stil einer CMS-Galerie; Share-Seiten sind schlicht
- **Kein Offline-Zugriff auf die volle Bibliothek** auf dem Desktop-Client

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| REST-API + API-Keys | offiziell, vollständig |
| Webhooks | Server-Ereignisse → HTTP |
| Externe Bibliotheken | Ordner-Mount, read-only SCAN |
| ML-Modelle | herunterladbare Modelle, GPU via CUDA/OpenVINO |
| Objekt-/Cloud-Speicher | S3-kompatibler Storage-Bucket konfigurierbar |
| Authentifizierung | OAuth2/OIDC, LDAP nicht integriert (❌) |
