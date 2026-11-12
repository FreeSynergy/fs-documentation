# Huginn

!!! warning "Maschinell übersetzt, noch nicht geprüft / Machine-translated, not yet reviewed"
    Diese Seite wurde maschinell aus der englischen Fassung übersetzt und noch nicht von einem Menschen geprüft.
    This page was machine-translated from the English version and has not yet been reviewed by a person.

> Kategorie: [workflows](../../index.md)

## Was es ist

Huginn ist ein quelloffenes (MIT) System zum Selbsthosting, in dem Agenten das Web und andere Quellen beobachten und auf das reagieren, was sie finden. Es ist eine Ruby-on-Rails-Anwendung mit Weboberfläche; das README nennt es eine anpassbare Alternative zu IFTTT oder Zapier.

## Bemerkenswerte Ideen

- **Agenten und Ereignisse**: jeder Agent erzeugt Ereignisse und kann die Ereignisse anderer verarbeiten; das Ganze ist ein gerichteter Graph, in der Oberfläche als Ereignisfluss-Diagramm dargestellt.
- **Beobachten, nicht nur reagieren**: Agenten lesen Websites aus und beobachten Feeds, Postfächer, Webhooks und MQTT-Themen.
- **Kleine Transformationssprachen**: JavaScript, Liquid-Vorlagen und jq.
- Hier aufgeführt wegen der Idee von Agenten, die Ereignisse beobachten und weitergeben (ADR 0013).

## Quellen

- ✅ Huginn-Repository (README): https://github.com/huginn/huginn (abgerufen 2026-11-10)
- ⚠️ Pflege: wird von einer Person in ihrer Freizeit betreut (README); der Abschnitt Releases war auf der abgerufenen Seite leer

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
