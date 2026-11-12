# Superhuman Mail

!!! warning "Maschinell übersetzt, noch nicht geprüft / Machine-translated, not yet reviewed"
    Diese Seite wurde maschinell aus der englischen Fassung übersetzt und noch nicht von einem Menschen geprüft.
    This page was machine-translated from the English version and has not yet been reviewed by a person.

> Kategorie: [messenger](../../index.md) · Typ: E-Mail-Client (für bestehende Konten) · Anbieter: Superhuman (vormals Grammarly) · Lizenz: proprietär

## Was es ist

Superhuman Mail ist ein kostenpflichtiger E-Mail-Client, der auf bestehenden Postfächern aufsetzt und auf Geschwindigkeit ausgelegt ist: eine Befehlspalette, ein tastaturorientierter Ablauf und ein geteilter Posteingang. Eigentümerschaft: Das Unternehmen Grammarly hat Superhuman Mail 2025 übernommen und sich im Oktober 2025 in Superhuman umbenannt; die Mail-App heißt nun Superhuman Mail. Die Anbieterseite listet weitere Produkte (Go, Docs, Calendar).

## Bemerkenswerte Ideen

Warum dieses Programm hier dokumentiert ist (ADR 0013):

- **Geteilter Posteingang (Split Inbox)**: der Posteingang wird nach Regeln in mehrere Listen geteilt (Absender, Domain, Empfänger, Betreff, Label). Er teilt den Posteingang einer Person; es ist kein gemeinsamer Posteingang mehrerer Personen.
- **Befehlspalette (Cmd/Strg+K)** als einziger Einstieg für Aktionen, einschließlich des Anlegens von Splits. Auf dem Mobilgerät öffnet ein Zwei-Finger-Tippen sie.
- **Tastatur zuerst**: ein Kürzel für fast jede Aktion.
- Die Anbieterseite nennt außerdem automatische Entwürfe, automatische Labels, automatisches Archivieren und die Freigabe der Verfügbarkeit (KI-gestützt; für uns wäre eine rein lokale Verarbeitung nötig, ADR 0029).

## Dokumentierte Versionen

| Version | Dokumentiert am | Status |
|---------|-----------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ⚠️ Anbieterseite und Suchergebnisse des Hilfecenters; Hilfeseiten lieferten 403 |

## Verwendete Protokolle und Standards

Arbeitet auf bestehenden Konten; welche Protokolle, ist offen. Siehe [Nachrichtenstandards](../../../../../data/messages/standards.md).

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
| https://superhuman.com/ ✅ | Startseite des Anbieters | 2026-11-10 |
| https://www.engadget.com/ai/grammarly-has-rebranded-to-superhuman-151001417.html ⚠️ | Presse (Umbenennung; nur im Suchergebnis gesehen) | 2026-11-10 |
| https://help.superhuman.com/article/586-split-inboxes-2-0 ⚠️ | Hilfecenter (nur im Suchergebnis gesehen) | 2026-11-10 |
| https://help.superhuman.com/hc/en-us/articles/46005619081101 ⚠️ | Hilfecenter (nur im Suchergebnis gesehen) | 2026-11-10 |
