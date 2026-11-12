# Reclaim

!!! warning "Maschinell übersetzt, noch nicht geprüft / Machine-translated, not yet reviewed"
    Diese Seite wurde maschinell aus der englischen Fassung übersetzt und noch nicht von einem Menschen geprüft.
    This page was machine-translated from the English version and has not yet been reviewed by a person.

> Kategorie: [calendar](../../index.md) · [frontends](../index.md)

## Was es ist

Reclaim (Reclaim.ai) ist ein Webdienst, der auf einem Google- oder Outlook-Kalender aufsetzt und Aufgaben, Gewohnheiten und Besprechungen in freie Zeit legt. ✅ (Hilfecenter; welche Kalender: offen.) Es gibt eine aktuelle Version 2.0 und eine alte Version 1.0 ✅.

## Bemerkenswerte Ideen

- **Aufgaben und Gewohnheiten werden automatisch platziert:** eine Aufgabe hat ein Fälligkeitsdatum und eine Schätzung; Reclaim blockiert dafür Zeit vor der Frist und verschiebt sie, wenn sich der Kalender ändert ✅.
- **Prioritäten P1 bis P4** entscheiden, was gewinnt, wenn die Zeit knapp ist; Fälligkeitsdaten können die Priorität überwiegen ✅ (Suchausschnitt des Hilfecenters).
- **Fokuszeit** hält offene Blöcke für konzentriertes Arbeiten frei ✅.
- Warum hier: Unsere Aufgaben und unser Kalender treffen an dieser Stelle zusammen (ADR 0013).

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

- https://help.reclaim.ai/en/ ✅ 2026-11-10 (Index)
- https://help.reclaim.ai/en/articles/11325700-habits-vs-tasks-vs-focus-time-when-to-use-each-in-reclaim ✅ 2026-11-10 (beschreibt Version 1.0)
- Prioritätstext aus einem Suchausschnitt von help.reclaim.ai ⚠️ 2026-11-10
