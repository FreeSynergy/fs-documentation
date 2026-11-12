# Felt

> Kategorie: [maps](../../index.md) · Typ: GIS im Browser, geteilte Karten · Anbieter: Felt · Lizenz: proprietär

## Was es ist
Felt ist ein browserbasierter Dienst für Karten und GIS, in dem mehrere Personen gleichzeitig dieselbe Karte bearbeiten. Ebenen stammen aus hochgeladenen Dateien oder verbundenen Datenquellen; Karten werden per Link geteilt und können eingebettet werden.

## Bemerkenswerte Ideen
- Gemeinsame Bearbeitung mit Live-Änderungen, wie bei einem Dokument. Warum: Karten werden zu einem Teamartefakt.
- Kommentieren und Ansehen ohne bezahlten Platz, Links ohne Anmeldung. Warum: niedrige Hürde für Außenstehende.
- Mit Datenbanken verbundene Ebenen bleiben aktuell. Warum: eine Karte als Live-Ansicht, nicht als Kopie.
- Offene REST-API, JS-SDK und Webhooks. Warum: ein gutes Modell für unsere eigene Kartenoberfläche.

## Dokumentierte Versionen
| Version | Dokumentiert am | Status |
|---------|-----------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ✅ |

## Verwendete Protokolle und Standards
GeoJSON, KML, Shapefile, GeoPackage, GeoTIFF als Uploads; WFS, WMTS, STAC als Quellen (alle von der Anbieterseite).

## Dokumentierte Versionen

<!-- gen:versions (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
| Version | Pflichtdateien vorhanden |
|---------|------------------------|
| [latest](latest/description.md) | 6/7 |

### latest

| Datei | Inhalt |
|------|----------|
| [description.md](latest/description.md) | Ausführliche Beschreibung, Abgrenzung, für wen geeignet |
| [features.md](latest/features.md) | Was das Programm kann — und was nicht |
| [layout.md](latest/layout.md) | Fensterstruktur, Bereiche, Panels |
| [menus.md](latest/menus.md) | Menüstruktur, Kontextmenüs, Menüs nach Rolle |
| [shortcuts.md](latest/shortcuts.md) | Tastaturkürzel |
| [api.md](latest/api.md) | APIs und Protokolle, Authentifizierung, Ratenlimits |

⚠️ Fehlende Pflichtdateien: `themes/index.md`
<!-- /gen:versions -->

## Quellen
| Quelle | Art | Abgerufen |
|--------|-----|-----------|
| https://felt.com ✅ | Produktseite | 2026-11-10 |
| https://help.felt.com ✅ | Index des Hilfecenters | 2026-11-10 |
| https://developers.felt.com ✅ | Überblick Entwicklerdokumentation | 2026-11-10 |
