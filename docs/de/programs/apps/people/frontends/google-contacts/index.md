# Google Contacts

!!! warning "Maschinell übersetzt, noch nicht geprüft / Machine-translated, not yet reviewed"
    Diese Seite wurde maschinell aus der englischen Fassung übersetzt und noch nicht von einem Menschen geprüft.
    This page was machine-translated from the English version and has not yet been reviewed by a person.

> Kategorie: [people](../../index.md) · Typ: Kontaktverwaltung (Web, Android) · Anbieter: Google · Lizenz: proprietär

## Was es ist

Google Contacts ist das Adressbuch, das an ein Google-Konto gebunden ist. Es wird im Browser genutzt und ist in Android eingebaut; die Kontakte werden auf alle Geräte synchronisiert, die am Konto angemeldet sind. Noch nicht gespeicherte Kontakte werden in einer eigenen Gruppe „Weitere Kontakte“ aufbewahrt.

## Bemerkenswerte Ideen

Warum dieses Programm hier dokumentiert ist (ADR 0013):

- **Vorschläge zum Zusammenführen** („Zusammenführen & korrigieren“): das Programm findet doppelte Einträge einer Person selbst und bietet an, sie einzeln oder alle auf einmal zusammenzuführen; zusammengeführte Kontakte lassen sich wieder trennen. Relevant für uns, weil Duplikate der Hauptverfall jedes Adressbuchs sind, das aus mehreren Quellen importiert.
- **Weitere Kontakte**: Personen, denen man nur geschrieben hat, werden getrennt vom eigentlichen Adressbuch gehalten, bis man sie übernimmt. Das ist ein Modell für „bekannt“ gegenüber „einmal gesehen“.
- **Änderungsverlauf** pro Kontakt, sodass eine Bearbeitung rückgängig gemacht werden kann.

## Dokumentierte Versionen

| Version | Dokumentiert am | Status |
|---------|-----------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ⚠️ nur aus Hilfeseiten; die laufende Oberfläche wurde nicht geprüft |

## Verwendete Protokolle und Standards

Standards für Kontaktdaten sind unter [data/people](../../../../../data/people/index.md) beschrieben. Welche Protokolle Google Contacts Dritten anbietet, steht in [api.md](latest/api.md) (offen).

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
| https://support.google.com/contacts/answer/7078226 ✅ | offizielle Hilfeseite (Duplikate zusammenführen) | 2026-11-10 |
| https://support.google.com/contacts/answer/1069522 ✅ | offizielle Hilfeseite (Kontakte hinzufügen, Synchronisation, Weitere Kontakte, Verlauf) | 2026-11-10 |
