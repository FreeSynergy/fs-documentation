# Linear

> Kategorie: [tasks](../../index.md) · Typ: Issue-Tracker / Produktplanung · Anbieter: Linear Orbit, Inc. · Lizenz: proprietär

## Was es ist
Linear ist ein Issue-Tracker für Teams, auf Tempo gebaut: per Tastatur bedienbar, mit Cycles (zeitlich begrenzten Iterationen), Projekten, Initiativen und einem Triage-Eingang.

## Bemerkenswerte Ideen
Warum dieses Programm hier dokumentiert ist (ADR 0013). Nur Funktionsanalyse, eigene Formulierung.

- Triage: ein eigener Eingang für Issues aus Integrationen oder von Personen außerhalb des Teams; eine Person nimmt an, lehnt ab, markiert als Duplikat oder stellt zurück, bevor die Arbeit in den Fluss kommt.
- Cycles: sich wiederholende, zeitlich begrenzte Iterationen, automatisch angelegt; unerledigte Arbeit wandert weiter, optionale Abkühlphase, gespeicherter Fortschrittsverlauf.
- Tempo: Aktionen mit einer einzigen Taste und ein Befehlsmenü; Änderungen aus der API werden in Echtzeit an alle Clients übertragen.

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
| https://linear.app/docs | offizielle Dokumentation, Übersicht | ✅ 2026-11-10 |
| https://linear.app/docs/triage.md | offizielle Dokumentation, Triage | ✅ 2026-11-10 |
| https://linear.app/docs/use-cycles.md | offizielle Dokumentation, Cycles | ✅ 2026-11-10 |
| https://linear.app/docs/api-and-webhooks.md | offizielle Dokumentation, API und Webhooks | ✅ 2026-11-10 |
