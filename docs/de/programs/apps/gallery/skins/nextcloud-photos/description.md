# Nextcloud Photos - Beschreibung

## Was das Programm macht

Nextcloud Photos zeigt die Fotos, die in der Nextcloud liegen: Chronologie über gewählte Ordner, Alben als virtuelle Sammlungen, Teilen über die üblichen Nextcloud-Mechanismen. Es ist keine eigene Medienverwaltung, sondern eine Ansicht auf der Dateien-Plattform.

## Vorteile

- **ein System für Dateien und Fotos**: Sync, Rechte, Versionierung inklusive
- **Reife Sharing-Funktionen** (Links mit Passwort/Ablauf, Upload-Links)
- **Mobile Auto-Uploads** seit Jahren stabil

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **Immich** | dedizierte Foto-Cloud mit KI-Suche und Timeline; Nextcloud Photos bleibt Dateiansicht. |
| **Memories** (Nextcloud-App) | Galerie-Ersatz mit Timeline und recognition, näher an Immich als die Core-Photos-App. |
| **PhotoPrism** | indexiert Ordner und liefert starke Suche; Nextcloud bringt die Ordner mit. |
| **Piwigo** | kuratierte Webbaukasten-Galerie mit Themes und Rechtebaum. |

## Technische Details

- **Backend**: PHP auf Nextcloud-Plattform, Dateien-Tabelle als Grundlage
- **Frontend**: Vue 2/3 (Photos-App), Viewer der Files-App
- **Speicher**: Primary Storage, externe Storage-Backends möglich
- **Auth**: Nextcloud-Nutzer, App-Passwörter, SSO (SAML/OIDC), WebDAV
- **Deployment**: Snap/Docker/ bare metal, PHP-FPM + MariaDB/PostgreSQL, Redis empfohlen
- **Lizenz**: AGPLv3

## Für wen geeignet

- Organisationen mit bestehender Nextcloud, die Fotos ohne Zweitsystem zeigen wollen
- FreeSynergy-Gallery-Skins, die WebDAV und Sharing-Objekte mitnutzen
- Private Nutzer mit Auto-Upload-Bedarf und Dateizugriff
