# Snipe-IT

> Kategorie: [resources](../../index.md)

## Was es ist

Snipe-IT ist eine Open-Source-Web-App für die Verwaltung von IT-Anlagen. Sie erfasst Anlagen, Zubehör, Komponenten, Verbrauchsgüter und Lizenzen sowie, wer sie besitzt.

## Bemerkenswerte Ideen

- **Ausgabe und Rücknahme**: Ein Artikel wird an eine Person, einen Ort oder eine andere Anlage übergeben; solange er draußen ist, kann er nicht erneut zugewiesen werden. Die Rücknahme bringt ihn zurück in den Bestand oder markiert ihn zur Reparatur.
- Vier Artikelklassen mit unterschiedlichen Regeln: Anlagen (gekennzeichnet, einzeln), Zubehör (austauschbar), Komponenten (Teile, die an Anlagen ausgegeben werden), Verbrauchsgüter (werden aufgebraucht, nie zurückgegeben).
- Statusbezeichnungen (nicht einsetzbar, einsetzbar, archiviert, ausstehend) zeigen, ob ein Artikel zugewiesen werden kann.
- Hier aufgeführt, weil es das klarste Vorbild für das Verleihen von Dingen mit Rückgabe ist (ADR 0013).

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

- ✅ Snipe-IT-Überblick, https://snipe-it.readme.io/docs/overview, abgerufen 2026-11-10
- ✅ Snipe-IT-Releases, https://github.com/grokability/snipe-it/releases (v8.8.3, 22. Okt; Jahr nicht angezeigt; benötigt PHP 8.2), abgerufen 2026-11-10

## Dokumentierte Versionen

| Version | Inhalt |
|---------|--------|
| [latest](latest/description.md) | Beschreibung, Funktionen, Layout, Menüs, Tastenkürzel, API |
