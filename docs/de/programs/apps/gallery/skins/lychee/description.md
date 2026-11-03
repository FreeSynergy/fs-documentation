# Lychee - Beschreibung

## Was das Programm macht

Lychee stellt Fotos in Alben ins Netz: hochladen, Alben anlegen, Links mit oder ohne Passwort teilen. Der Fokus liegt auf einer schnellen Galerie und einer aufgeräumten API statt auf KI-Funktionen.

## Vorteile

- **leichtgewichtig**: läuft auf kleinem Shared-Hosting/VPS, schnelle Oberfläche
- **saubere REST-API** mit dokumentierten Endpunkten, gut für Skin-Anbindung
- **Freigaben mit Ablauf und Passwort** alltagstauglich implementiert

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **Piwigo** | Themes und Rechte pro Kategorie, riesiges Plugin-Ökosystem; Lychee ist moderner, aber funktional enger. |
| **PhotoPrism** | Index und KI-Suche über bestehende Ordner; Lychee hat keine Index-Pipeline. |
| **Immich** | Foto-Cloud mit Apps und KI; Lychee ist bewusst einfache Galerie. |

## Technische Details

- **Backend**: PHP 8 / Laravel, MySQL, MariaDB oder PostgreSQL
- **Frontend**: React (Lychee-front), separat deployed in v5
- **Bilder**: generierte Größen (Thumb, Small, Medium, High), Original bleibt
- **Auth**: lokal, OAuth2/OIDC-Provider, API-Token pro Benutzer
- **Deployment**: Docker Compose, Bare-Metal mit Composer
- **Lizenz**: MIT (v4/v5)

## Für wen geeignet

- Kleine bis mittlere Galerien mit Fokus auf Teilen und Geschwindigkeit
- FreeSynergy-Gallery-Skins mit Modell Album / Photo / Share
- Betreiber ohne Bedarf an KI-Erkennung
