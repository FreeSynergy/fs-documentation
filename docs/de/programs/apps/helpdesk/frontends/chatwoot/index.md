# Chatwoot

!!! warning "Maschinell übersetzt, noch nicht geprüft / Machine-translated, not yet reviewed"
    Diese Seite wurde maschinell aus der englischen Fassung übersetzt und noch nicht von einem Menschen geprüft.
    This page was machine-translated from the English version and has not yet been reviewed by a person.

> Kategorie: [helpdesk](../../index.md) · Typ: Omnichannel-Posteingang für Kundensupport · Anbieter: Chatwoot Inc. · Lizenz: MIT (Enterprise-Edition und kostenpflichtige Lizenzen für Self-Hosting existieren)

## Was es ist
Chatwoot ist eine Plattform für Kundensupport, in der Gespräche aus vielen Kanälen in einem gemeinsamen Posteingang landen. Sie bietet ein Live-Chat-Widget für Websites, E-Mail, Messenger, SMS, soziale Kanäle und Sprache sowie ein Hilfecenter. Betrieben wird sie als Cloud-Dienst oder selbst gehostet.

## Bemerkenswerte Ideen
- **Alle Kanäle in einem Posteingang** — jeder Kanal ist ein Posteingang; Agenten, Teams und Zuweisungsregeln funktionieren für alle gleich (ADR 0013). Passt zu unserem Modell „jeder Kanal ist ein Messenger-Anbieter“ in den [Anforderungen](../../requirements.md).
- **Website-Widget** — ein Snippet, das in eine Seite eingebettet wird; mit Vorab-Chat-Formular und Kontaktdaten.
- **Sprache und Video im Gespräch** — Anrufe werden in der Zeitleiste protokolliert.

## Dokumentierte Versionen
| Version | Dokumentiert am | Status |
|---------|-----------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ✅ |

## Verwendete Protokolle und Standards
Webhooks, WebSocket, REST; Kanalprotokolle sind APIs Dritter (WhatsApp, Twilio und andere). Siehe [Datenstandards](../../../../../data/standards.md).

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
| https://www.chatwoot.com/docs/product | offizielle Dokumentation ✅ | 2026-11-10 |
| https://github.com/chatwoot/chatwoot | Quell-README ✅ | 2026-11-10 |
