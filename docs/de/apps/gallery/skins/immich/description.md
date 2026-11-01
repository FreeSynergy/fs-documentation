# Immich - Beschreibung

## Was das Programm macht

Immich ersetzt den Foto-Cloud-Dienst eines Anbieters durch eine eigene Instanz: Handys laden alles hoch, der Server erzeugt Vorschaubilder, Videos in Streaming-Auflösung, Gesichts- und Objekterkennung, und der Browser zeigt Zeitleisten, Karten und Alben. Freigaben erfolgen über Alben, Benutzer oder public Links.

## Vorteile

- **Google-Photos-artige UX** mit moderner Suche und Personenansicht
- **Self-Hosted und Datenhoheit**: Originale bleiben im eigenen Speicher (auch S3)
- **Mobile First**: echtes Auto-Backup, auch im Hintergrund
- **API-first**: jeder UI-Schritt ist ein dokumentierter REST-Call, ideal für Skin-Anbindung

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **PhotoPrism** | stärker Indexierung/Suche, Web-UI konservativer, ML optional; Immich hat die bessere App und Zeitleiste. |
| **LibrePhotos** | ähnliche Idee, aber schlankere Basis und ältere Frontends. |
| **Piwigo** | klassisches Webbaukasten-Galeriedesign, Rollen pro Ordner, Themes; dafür keine Gesichts-/Semantik-KI. |
| **Nextcloud Photos** | gute Integration in eine bestehende Nextcloud, aber schwächere Timeline/KI als Immich. |

## Technische Details

- **Server**: NestJS (Node.js), PostgreSQL, Redis/BullMQ-Jobs, Immich-Machine-Learning-Service
- **Speicher**: Dateisystem oder S3-kompatibel, Originale unverändert, Derivate in `library/`
- **Frontends**: Web-App (Svelte/React), iOS/Android (Flutter), CLI
- **Auth**: E-Mail/Passwort, OAuth2/OIDC, API-Keys pro Benutzer
- **Deployment**: Docker Compose (empfohlen), Helm, Bare-Metal möglich
- **Lizenz**: AGPLv3 (Mobil-Apps GPLv3)

## Für wen geeignet

- Privates und teamorientiertes Foto-/Video-Archiv mit Auto-Backup
- FreeSynergy-Gallery-Skins mit Standardmodell Album / Asset / Person / Share
- Migrationen aus Google Photos (Importwerkzeug vorhanden)
