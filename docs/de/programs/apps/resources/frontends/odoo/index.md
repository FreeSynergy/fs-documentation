# Odoo

> Kategorie: [resources](../../index.md)

## Was es ist

Odoo ist eine Sammlung von Geschäfts-Apps (Verkauf, Lager, Buchhaltung und mehr) auf einer Plattform, als Community-Edition mit offenem Quellcode und als kommerzielle Enterprise-Edition (Aufteilung der Editionen: Open).

## Bemerkenswerte Ideen

- Apps sind **Module, die aufeinander aufbauen**: die Daten einer App speisen die nächste (zum Beispiel führt ein Verkauf zu Lager und Rechnungen). Unsere Lesart: Module sind über gemeinsame Datensätze verknüpft, nicht durch Import. Das ist eine Referenz dafür, Ressourcen über Schnittstellen mit anderen Programmen zu verknüpfen.
- Hier wegen dieser Modulverknüpfung aufgeführt (ADR 0013). Die Verknüpfung selbst ist ⚠️: das Dokumentationsverzeichnis deutet darauf hin, eine Detailseite wurde nicht gelesen.

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

- ✅ Odoo-Dokumentation (master), https://www.odoo.com/documentation/master/applications.html, abgerufen 2026-11-10; der Versionsumschalter listet die Versionen 14 bis 20
- ⚠️ Odoo 20 im September 2026 veröffentlicht, Zweitquelle https://ecosire.com/blog/latest-odoo-version, abgerufen 2026-11-10 (Blog eines Partners des Anbieters, nicht auf odoo.com bestätigt)
- ⚠️ GitHub odoo/odoo hat keine veröffentlichten Releases, https://github.com/odoo/odoo/releases, abgerufen 2026-11-10

## Dokumentierte Versionen

| Version | Inhalt |
|---------|--------|
| [latest](latest/description.md) | Beschreibung, Funktionen, Layout, Menüs, Tastenkürzel, API |
