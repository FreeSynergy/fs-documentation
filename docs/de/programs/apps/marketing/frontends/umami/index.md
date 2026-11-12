# Umami

!!! warning "Maschinell übersetzt, noch nicht geprüft / Machine-translated, not yet reviewed"
    Diese Seite wurde maschinell aus der englischen Fassung übersetzt und noch nicht von einem Menschen geprüft.
    This page was machine-translated from the English version and has not yet been reviewed by a person.

> Kategorie: [marketing](../../index.md) · Typ: Web- und Produktanalyse · Anbieter: Umami Software · Lizenz: MIT

## Was es ist
Umami ist ein auf Datenschutz ausgerichtetes Werkzeug für Webanalyse. Ein Tracking-Skript sendet Seitenaufrufe und eigene Ereignisse an Umami, das Besucherzahlen, Kampagnen, Verhalten und Conversions zeigt. Es läuft selbst gehostet (Next.js, PostgreSQL) oder als Cloud-Dienst.

## Bemerkenswerte Ideen
- **Produktanalyse-Ansichten auf einem schlanken Werkzeug** — Ereignisse, Trichter, Bindung, Nutzerpfade, Ziele und UTM-Verfolgung, ohne Cookies und ohne seitenübergreifendes Tracking (ADR 0013).
- **Teams** — Gruppen teilen Websites und Berichte.
- **MCP-Endpunkt (optional, standardmäßig aus)** — programmatischer Zugriff für Werkzeuge mit API-Schlüsseln.

## Dokumentierte Versionen
| Version | Dokumentiert am | Status |
|---------|-----------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ✅ |

## Verwendete Protokolle und Standards
HTTP/JSON-API; kein Datenstandard für Ereignisse gefunden. Siehe [Datenstandards](../../../../../data/standards.md).

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
| [api.md](latest/api.md) | APIs und Protokolle, Authentifizierung, Rate Limits |

⚠️ Fehlende Pflichtdateien: `themes/index.md`
<!-- /gen:versions -->

## Quellen
| Quelle | Art | Abgerufen |
|--------|-----|-----------|
| https://docs.umami.is/docs/ | offizielle Dokumentation ✅ | 2026-11-10 |
| https://github.com/umami-software/umami | Quell-README ✅ | 2026-11-10 |
