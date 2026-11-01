# Coppermine - Beschreibung

## Was das Programm macht

Coppermine stellt Fotos in einer Webbaukasten-Galerie bereit: Kategorien und Alben strukturieren die Sammlung, Kommentare und Bewertungen aktivieren die Gemeinschaft, Rollen regeln, wer was sehen und hochladen darf.

## Vorteile

- **bewährter Funktionsumfang** einer Community-Galerie (Kommentare, Bewertungen, Alben)
- **einfacher Betrieb** auf jedem PHP/MySQL-System
- **Hooks** erlauben eigene Logik, ohne den Kern zu forken

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **Piwigo** | aktiv entwickelt, größere Plugin-Landschaft, Webservice-API; Coppermine ohne API. |
| **Zenphoto** | ähnlicher Webbaukasten, aber Alben-Vererbung und eigene „zpCore“-API. |
| **Lychee** | moderne Oberfläche mit REST-API, aber ohne Community-Funktionen. |

## Technische Details

- **Backend**: PHP (aktuelle Zweige: PHP 8-kompatibel), MySQL/MariaDB
- **Bilder**: Original + vorher generierte Vorschaugrößen, Wasserzeichen-Cron
- **Frontend**: Theme-System mit Templates, teils feste Layouts
- **Auth**: eigene Benutzertabellen, Bridge-Integrationen
- **Deployment**: Shared-Hosting, Docker, Bare-Metal
- **Lizenz**: GPLv3

## Für wen geeignet

- Bestehende Coppermine-Installationen, die in FreeSynergy abgebildet werden sollen
- Betreiber, die eine Community-Galerie ohne Cloud-Komfort betreiben
- Als Vergleichsfall in Skin-Projekten, weil **keine API** existiert (Migrationsaufwand zeigen)
