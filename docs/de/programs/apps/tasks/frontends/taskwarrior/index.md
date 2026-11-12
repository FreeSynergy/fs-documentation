# Taskwarrior

!!! warning "Maschinell übersetzt, noch nicht geprüft / Machine-translated, not yet reviewed"
    Diese Seite wurde maschinell aus der englischen Fassung übersetzt und noch nicht von einem Menschen geprüft.
    This page was machine-translated from the English version and has not yet been reviewed by a person.

> Kategorie: [tasks](../../index.md) · Typ: To-do-Manager für die Kommandozeile · Anbieter: GothenburgBitFactory-Community · Lizenz: frei und Open Source (Lizenzversion: Open)

## Was es ist
Taskwarrior ist ein To-do-Manager für die Kommandozeile. Aktuelle stabile Version auf der Projektseite: 3.5.0.

## Bemerkenswerte Ideen
Warum dieses Programm hier dokumentiert ist (ADR 0013). Nur Funktionsanalyse, eigene Formulierung.

- Berechnete Dringlichkeit: Jede Aufgabe bekommt einen Wert aus gewichteten Faktoren, so sortiert sich die Liste selbst; alle Gewichte sind vom Nutzer einstellbar — eine nachvollziehbare Alternative zur manuellen Priorität.
- Berichtsansichten und Filter auf der Kommandozeile.

## Dokumentierte Versionen
| Version | Dokumentiert am | Stand |
|---------|-----------------|-------|
| [latest](latest/description.md) | 2026-11-10 | ⚠️ teilweise geprüft, Lücken als "Open" markiert |

## Dokumentierte Versionen

<!-- gen:versions (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
| Version | Required files present |
|---------|------------------------|
| [latest](latest/description.md) | 6/7 |

### latest

| File | Contents |
|------|----------|
| [description.md](latest/description.md) | Detailed description, differentiation, who it suits |
| [features.md](latest/features.md) | What the program can do — and what not |
| [layout.md](latest/layout.md) | Window structure, regions, panels |
| [menus.md](latest/menus.md) | Menu structure, context menus, menus by role |
| [shortcuts.md](latest/shortcuts.md) | Keyboard shortcuts |
| [api.md](latest/api.md) | APIs and protocols, authentication, rate limits |

⚠️ Missing required files: `themes/index.md`
<!-- /gen:versions -->

## Quellen
| Quelle | Art | Abgerufen |
|--------|-----|-----------|
| https://taskwarrior.org/ | offizielle Website | ✅ 2026-11-10 |
| https://taskwarrior.org/docs/urgency/ | offizielle Dokumentation, Dringlichkeit | ✅ 2026-11-10 |
