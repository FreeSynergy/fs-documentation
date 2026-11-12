# OmniFocus

> Kategorie: [tasks](../../index.md) · Typ: persönlicher Aufgabenmanager / GTD (Apple-Plattformen) · Anbieter: The Omni Group · Lizenz: proprietär

## Was es ist
OmniFocus ist ein Aufgabenmanager für Mac, iPhone, iPad, Apple Watch und Vision Pro, dazu OmniFocus im Web, ausgelegt auf langfristige Projekte und die wöchentliche Überprüfung.

## Bemerkenswerte Ideen
Warum dieses Programm hier dokumentiert ist (ADR 0013). Nur Funktionsanalyse, eigene Formulierung.

- Perspektiven: gespeicherte Ansichten über alle Aufgaben (Standard-Perspektiven und in Pro eigene), definiert durch Filter, Gruppierung und Sortierung; das entspricht unserer Idee gespeicherter Abfragen über die Daten des Aufgabeninhabers.
- Überprüfung: Projekte erhalten ein Überprüfungsintervall und werden als überprüft markiert; eine eigene Perspektive listet, was zur Überprüfung ansteht.
- Verfügbarkeitsmodell: sequenzielle, parallele und Einzelaktions-Projekte entscheiden, welche Aktionen verfügbar sind; die Zustände "On Hold" und "Dropped" blenden Einträge aus.

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
| https://www.omnigroup.com/omnifocus/ | offizielle Produktseite | ✅ 2026-11-10 |
| https://support.omnigroup.com/documentation/omnifocus/universal/4.7.1/en/welcome/ | offizielles Referenzhandbuch | ✅ 2026-11-10 |
| https://support.omnigroup.com/documentation/omnifocus/mac/4.0.3/en/perspectives | offizielles Handbuch, Perspektiven (teilweise gelesen, 100000 von 137815 Zeichen) | ⚠️ 2026-11-10 |
