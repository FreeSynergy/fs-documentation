# Windmill

> Kategorie: [workflows](../../index.md)

## Was es ist

Windmill ist eine quelloffene Plattform (Community-Edition unter AGPLv3) für Skripte, Flows, Apps und KI-Agenten, selbst hostbar oder gehostet. Backend in Rust, Frontend in Svelte, PostgreSQL als Speicher und Auftragswarteschlange.

## Bemerkenswerte Ideen

- **Skript zuerst**: ein Skript in vielen Sprachen wird zugleich zu einem automatisch erzeugten Formular, einem HTTP-Endpunkt und einem planbaren Auftrag.
- **Flows, Apps und Skripte aus einer Basis**: Flows verketten Skripte (visueller Editor, YAML oder Workflows als Code); Apps legen eine Oberfläche auf Skripte und Flows.
- **Worker holen Aufträge per Schlagwort** aus der Warteschlange; Ausführung in einer Sandbox.
- Hier aufgeführt wegen der Idee, dass der Code die Einheit ist und die Oberfläche erzeugt wird (ADR 0013).

## Quellen

- ✅ Einführung in Windmill: https://www.windmill.dev/docs/intro (abgerufen 2026-11-10)
- ✅ Windmill-Repository (README): https://github.com/windmill-labs/windmill (abgerufen 2026-11-10)
- ⚠️ Neueste Version: auf der abgerufenen Seite nicht angezeigt

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
