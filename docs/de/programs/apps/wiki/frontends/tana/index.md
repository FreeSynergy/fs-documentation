# Tana

!!! warning "Maschinell übersetzt, noch nicht geprüft / Machine-translated, not yet reviewed"
    Diese Seite wurde maschinell aus der englischen Fassung übersetzt und noch nicht von einem Menschen geprüft.
    This page was machine-translated from the English version and has not yet been reviewed by a person.

> Kategorie: [wiki](../../index.md) · Typ: Gliederungswerkzeug / Wissensgraph · Anbieter: Tana Inc. · Lizenz: proprietär

## Was es ist
Tana ist ein Gliederungswerkzeug, in dem jede Zeile ein Knoten ist und Knoten in typisierte Objekte mit Feldern verwandelt werden können.

## Bemerkenswerte Ideen
Warum dieses Programm hier dokumentiert ist (ADR 0013). Nur Funktionsanalyse, in eigenen Worten.

- Supertags: Ein Knoten mit einem Supertag wird als Ganzes zu einem typisierten Objekt mit einer Vorlage aus Feldern; alle Knoten mit einem Supertag bilden eine Sammlung, die als Tabelle angezeigt wird. Passt zu unserer Idee der Typbeschreibung (ADR 0066).
- Vererbung von Supertags: ein Schlagwort erweitert ein anderes und ergänzt Felder oder Vorgaben.
- Suchknoten: Live-Abfragen, die an beliebiger Stelle eingebettet werden können.

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
| https://outliner.tana.inc/learn/features/supertags | offizielle Dokumentation, Supertags | ✅ 2026-11-10 |
