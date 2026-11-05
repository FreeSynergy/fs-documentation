# Piwigo - Beschreibung

## Was das Programm macht

Piwigo verwaltet Fotos als Webbaukasten-Galerie: Kategorien bilden die Struktur, Rollen entscheiden über Sichtbarkeit, Themes bestimmen das Aussehen. Bilder liegen auf dem Server und werden per Sync oder Upload übernommen.

## Vorteile

- **Sehr reif und stabil**, seit über 15 Jahren in Betrieb, großer Plugin-Fundus
- **Feingranulare Rechte** (Gruppen × Kategorien) — gut für Vereine und Behörden
- **Günstig zu betreiben**: einfacher LAMP-Stack, Shared-Hosting-tauglich
- **Design frei anpassbar** über Themes und Templates

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **Immich / LibrePhotos** | Foto-Cloud mit Apps und KI, aber ohne Themes und Rechtebaum. |
| **PhotoPrism** | Index über Ordner mit KI-Suche, aber keine Galerie-Rechte pro Ordner. |
| **Coppermine** | ähnlicher Webbaukasten, aber ältere Codebasis und kleiner werdende Community. |

## Technische Details

- **Backend**: PHP 8, MySQL/MariaDB, keine Framework-Pflicht (eigener Kern)
- **Bilder**: Original + generierte Größen (TH, CU, LI), Wasserzeichen per Cron
- **Frontend**: Smarty-artige Templates, Themes mit CSS-Overrides
- **Auth**: lokal, Plugins für LDAP/OAuth2/Social Login
- **Deployment**: Shared-Hosting, Docker, Bare-Metal; Upgrade über das Admin-Interface
- **Lizenz**: GPLv2+

## Für wen geeignet

- Vereine, Schulen, Kommunen, die eine kuratierte öffentliche Galerie brauchen
- FreeSynergy-Gallery-Skins mit Modell Category / Image / Tag / Group
- Betreiber, die Design und Rechte stärker steuern wollen als die KI
