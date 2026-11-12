# Todoist

> Kategorie: [tasks](../../index.md) · Typ: persönlicher und Team-Aufgabenmanager (Web, Apps) · Anbieter: Doist · Lizenz: proprietär

## Was es ist
Todoist ist ein plattformübergreifender Aufgabenmanager mit Projekten, Abschnitten, Labels, Prioritäten und Datumsangaben in natürlicher Sprache.

## Bemerkenswerte Ideen
Warum dieses Programm hier dokumentiert ist (ADR 0013). Nur Funktionsanalyse, eigene Formulierung.

- Filtersprache: eine kleine Abfragesyntax über Aufgaben mit UND, ODER, NICHT, Gruppierung, Platzhaltern und Ausgabe über mehrere Listen — ein Vorbild für eine Sprache gespeicherter Abfragen in unserem Programm Tasks.
- Filter werden gespeichert und wie Projekte in der Seitenleiste aufgelistet.

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
| https://www.todoist.com/help/articles/introduction-to-filters-V98wIH | offizielle Hilfe, Filter | ✅ 2026-11-10 |
