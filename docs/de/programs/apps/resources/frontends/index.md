# Resources — Frontend-Dokumentation

!!! warning "Maschinell übersetzt, noch nicht geprüft / Machine-translated, not yet reviewed"
    Diese Seite wurde maschinell aus der englischen Fassung übersetzt und noch nicht von einem Menschen geprüft.
    This page was machine-translated from the English version and has not yet been reviewed by a person.

Frontends bekannter Programme dieser Kategorie, analysiert nach ihren **Funktionen** — nichts wird kopiert (ADR 0013). Ein Programm ist hier dokumentiert, weil es weit verbreitet ist oder eine bemerkenswerte Idee hat. Unser eigenes Programm dieser Kategorie ist `FreeSynergy.Resources` (ADR 0017); seine Fähigkeiten und sein Stand stehen in [requirements](../requirements.md).

## Programme

| Programm | Versionen | Was es ist |
|----------|-----------|------------|
| [ERPNext](erpnext/index.md) | [latest](erpnext/latest/description.md) | ERPNext ist eine Open-Source-Suite für die Unternehmensverwaltung auf Basis des Frappe-Frameworks. |
| [Grocy](grocy/index.md) | [latest](grocy/latest/description.md) | Grocy ist eine selbst gehostete Web-App für Haushaltsvorräte und Haushaltsaufgaben: Bestand, Einkaufsliste, Rezepte, Speiseplan, Aufgaben, Geräte und Batterien. |
| [Odoo](odoo/index.md) | [latest](odoo/latest/description.md) | Odoo ist eine Sammlung von Geschäfts-Apps (Verkauf, Lager, Buchhaltung und mehr) auf einer Plattform, als Community-Edition mit offenem Quellcode und als kommerzielle Enterprise-Edition (Aufteilung der Editionen: Open). |
| [Snipe-IT](snipe-it/index.md) | [latest](snipe-it/latest/description.md) | Snipe-IT ist eine Open-Source-Web-App für die Verwaltung von IT-Anlagen. |

## Dateisatz pro Programm (ADR 0012)

```
programs/apps/resources/frontends/<program>/
├── index.md        was es ist, bemerkenswerte Ideen, dokumentierte Versionen, Quellen
├── changelog.md    Änderungen zwischen dokumentierten Versionen (≥ 2 Versionen)
└── <version>/
    ├── description.md    Pflicht · Ausführliche Beschreibung, Abgrenzung, für wen es passt
    ├── features.md       Pflicht · Was das Programm kann — und was nicht
    ├── layout.md         Pflicht · Fensterstruktur, Bereiche, Panels
    ├── menus.md          Pflicht · Menüstruktur, Kontextmenüs, Menüs nach Rolle
    ├── shortcuts.md      Pflicht · Tastatur-Shortcuts
    ├── api.md            Pflicht · APIs und Protokolle, Authentifizierung, Rate Limits
    ├── themes/index.md   Pflicht · Themes: Farben, Typografie, Abstände — was sich nachbauen lässt
    ├── interaction.md    bei Bedarf · Hover, Fokus, Ziehen, Gesten (Finger, Maus, Stift)
    ├── states.md         bei Bedarf · UI-Zustände und Übergänge
    ├── events.md         bei Bedarf · Ereignisse nach außen (Webhooks, Push, Streams)
    ├── limits.md         bei Bedarf · Bekannte Grenzen
    ├── i18n.md           bei Bedarf · Lokalisierung, Schreibrichtung
    └── dependencies.md   bei Bedarf · Welche unserer Bausteine ein Frontend dieser Art braucht
```

Protokolle (Matrix, IMAP, CalDAV, …) sind keine Frontends; sie stehen unter [data](../../../../data/standards.md).
