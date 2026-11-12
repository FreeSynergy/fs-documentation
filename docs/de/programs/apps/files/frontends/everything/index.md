# Everything

!!! warning "Maschinell übersetzt, noch nicht geprüft / Machine-translated, not yet reviewed"
    Diese Seite wurde maschinell aus der englischen Fassung übersetzt und noch nicht von einem Menschen geprüft.
    This page was machine-translated from the English version and has not yet been reviewed by a person.

> Kategorie: [files](../../index.md) · [frontends](../index.md)

## Was es ist

Everything (voidtools) ist ein kostenloses Suchprogramm für Windows, das Dateien und Ordner nach Namen findet, während man tippt ✅. Freeware, nicht Open Source ✅ (als Freeware angegeben).

## Bemerkenswerte Ideen

- **Sofortige Suche nach Namen:** ein Namensindex entsteht in Sekunden bis etwa einer Minute; die Ergebnisse ändern sich mit jedem Tastendruck ✅. Auf NTFS-Datenträgern folgt es dem Änderungsjournal, sodass Änderungen, die bei geschlossenem Programm erfolgten, beim Start nachgeholt werden ✅.
- **Inhalte werden nicht indexiert;** eine Inhaltssuche gibt es, sie ist aber langsam ✅.
- **Kleine Abfragesprache:** Leerzeichen ist UND, `|` ODER, `!` NICHT, Platzhalter, Anführungszeichen, Eingrenzung auf Pfade ✅.
- **Server und Kommandozeile:** HTTP- und ETP/FTP-Server sowie das Kommandozeilenwerkzeug `ES` in der Vollversion, nicht in Lite ✅.
- Warum hier: Es ist die Referenz für `file.search`, die sofort antwortet (ADR 0013).

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

- https://www.voidtools.com/faq/ ✅ 2026-11-10
