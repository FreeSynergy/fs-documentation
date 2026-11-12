# Zulip

!!! warning "Maschinell übersetzt, noch nicht geprüft / Machine-translated, not yet reviewed"
    Diese Seite wurde maschinell aus der englischen Fassung übersetzt und noch nicht von einem Menschen geprüft.
    This page was machine-translated from the English version and has not yet been reviewed by a person.

> Kategorie: [messenger](../../index.md) · Typ: Team-Chat · Anbieter: Zulip-Projekt · Lizenz: Open Source (Lizenzname offen)

## Was es ist

Zulip ist ein Team-Chat, der in Kanälen organisiert ist; jede Nachricht gehört zu einem Thema. Man kann ihn auch per E-Mail nutzen: Eine Nachricht kann per E-Mail an einen Kanal gesendet werden.

## Bemerkenswerte Ideen

Warum dieses Programm hier dokumentiert ist (ADR 0013):

- **Ein Thema bei jeder Nachricht**: der Absender benennt einen kurzen, konkreten Betreff; eine Antwort landet automatisch im gerade gelesenen Thema. Unterhaltungen bleiben getrennt, ohne eine zweite Ebene „Strang“. Für uns relevant: Es löst die Flut in belebten Gruppenchats und passt auf einen Gesprächskontext.
- **Ansichten nach Themen**: die Seitenleiste zeigt aktuelle Themen je Kanal; der Posteingang zeigt Themen mit ungelesenen Nachrichten; „Aktuelle Unterhaltungen“ zeigt Aktivität.
- Themen können umbenannt oder verschoben, als erledigt markiert und stummgeschaltet werden (im Hilfe-Index genannt; Details nicht gelesen).
- Tastaturbedienung, zum Beispiel zum nächsten ungelesenen Thema springen.

## Dokumentierte Versionen

| Version | Dokumentiert am | Status |
|---------|-----------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ⚠️ zwei Hilfeseiten |

## Verwendete Protokolle und Standards

Eigene REST-API; Brücken zu Matrix existieren (siehe Matrix-Brückenliste). Siehe [Nachrichtenstandards](../../../../../data/messages/standards.md).

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
| [api.md](latest/api.md) | APIs und Protokolle, Authentifizierung, Rate Limits |

⚠️ Fehlende Pflichtdateien: `themes/index.md`
<!-- /gen:versions -->

## Quellen

| Quelle | Art | Abgerufen |
|--------|-----|-----------|
| https://zulip.com/help/introduction-to-topics ✅ | offizielle Hilfe | 2026-11-10 |
| https://zulip.com/help/ ✅ | offizieller Hilfe-Index | 2026-11-10 |
| https://matrix.org/ecosystem/bridges/ ✅ | Liste der Matrix-Brücken (Zulip erscheint) | 2026-11-10 |
