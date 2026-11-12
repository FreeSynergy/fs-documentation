# Obsidian

> Kategorie: [wiki](../../index.md) · Typ: lokal gespeicherte Markdown-Notizen (Local-first) · Anbieter: Dynalist Inc. (Obsidian) · Lizenz: proprietäre App; kostenlos für die private Nutzung, kommerzielle Lizenz verfügbar (laut Hilfe-Startseite)

## Was es ist
Obsidian bearbeitet einen Ordner mit einfachen Markdown-Dateien (einen Tresor), mit Verlinkungen zwischen Notizen, Erweiterungen und optionalen kostenpflichtigen Diensten Sync und Publish.

## Bemerkenswerte Ideen
Warum dieses Programm hier dokumentiert ist (ADR 0013). Nur Funktionsanalyse, in eigenen Worten.

- Rückverweise: für jede Notiz eine Liste der Notizen, die auf sie verlinken, und der unverlinkten Erwähnungen ihres Namens — ein automatischer Rückverweis-Index ohne Datenbank.
- Canvas: eine unendliche zweidimensionale Fläche mit Notizen, Medien und Webseiten und beschrifteten Verbindungen, gespeichert im offenen Format JSON Canvas.
- Einfache Dateien plus ein Erweiterungssystem; Befehlspalette.

## Dokumentierte Versionen
| Version | Dokumentiert am | Status |
|---------|-----------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ⚠️ teilweise verifiziert, Lücken als „Offen“ markiert |

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
| https://obsidian.md/help/Plugins/Backlinks | offizielle Hilfe, Rückverweise | ✅ 2026-11-10 |
| https://obsidian.md/help/Plugins/Canvas | offizielle Hilfe, Canvas | ✅ 2026-11-10 |
| https://obsidian.md/help/Home | offizielle Hilfe-Startseite | ✅ 2026-11-10 |
| https://obsidian.md/help/Plugins/Command+palette | offizielle Hilfe, Befehlspalette | ⚠️ nur ein Tastenkürzel 2026-11-10 |
