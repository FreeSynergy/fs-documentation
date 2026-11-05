# Nextcloud Photos - Funktionen

## Hauptfunktionen

- **Chronologie** über alle freigegebenen Ordner, gruppiert nach Tag/Monat/Jahr
- **Alben** (virtuell) und **Ordner-Alben**, Teilen mit Benutzer/Gruppen/Links
- **Mobile Apps** mit Auto-Upload (Fotos und Videos, Ordner wählbar)
- **Preview-Pipeline** mit generierten Vorschaugrößen und optionalem MIME-Handling
- **Ordner-Auswahl**: Steuerung, was in der Galerie erscheint
- **Recognition** (optionale Apps) für Gesichter und Bilderkennung, Suche nach Ordnerinhalten
- **Videos** direkt im Viewer mit Vorherspulen und Streaming-Auslieferung

## Was Photos NICHT kann

- **Keine eigene Bilddatenbank** — Metadaten bleiben in den Dateien/Ordner-Tabellen (❌)
- **Keine semantische Volltext-/CLIP-Suche** in der Basis (nur Ordner/Name, recognition eingeschränkt) (❌)
- **Keine Galerie-Themes/Designvorlagen** (einheitliches Nextcloud-Layout) (❌)
- **Keine Bildbearbeitung** (nur Drehen/Crop in der Files-App-Vorschau) (❌)
- **Keine Webbaukasten-Rechte pro Galerie** (Rechte kommen aus Files-Sharing) (❌)

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| WebDAV (`/remote.php/dav`) | Dateien und Metadaten, Standard-Client-Protokoll |
| OCS/REST | Alben, Photos-Endpunkte, Sharing, Preview |
| Apps | Maps (Orte), Recognizer/Face Recognition, Memories (Alternative) |
| Client-Apps | iOS/Android mit Auto-Upload, Desktop-Sync |
| Authentifizierung | Nextcloud-Nutzer, SAML/OIDC (App), App-Passwörter, WebDAV-Token |
