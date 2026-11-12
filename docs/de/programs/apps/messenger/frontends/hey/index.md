# HEY

!!! warning "Maschinell übersetzt, noch nicht geprüft / Machine-translated, not yet reviewed"
    Diese Seite wurde maschinell aus der englischen Fassung übersetzt und noch nicht von einem Menschen geprüft.
    This page was machine-translated from the English version and has not yet been reviewed by a person.

> Kategorie: [messenger](../../index.md) · Typ: E-Mail · Anbieter: Basecamp (auf den gelesenen Seiten nicht geprüft) · Lizenz: proprietär ⚠️

## Was es ist

HEY ist ein gehosteter E-Mail-Dienst mit eigenen Apps und einer Weboberfläche. Der Adressraum ist @hey.com; eigene Domains und das Senden von externen Adressen sind möglich. Es verändert den Posteingang selbst, statt das übliche Ordnermodell zu kopieren.

## Bemerkenswerte Ideen

Warum dieses Programm hier dokumentiert ist (ADR 0013):

- **Der Screener**: Ein Absender, der zum ersten Mal schreibt, wird zurückgehalten, bis die Person entschieden hat, ob er wieder schreiben darf. Für uns relevant: Zustimmung, bevor eine fremde Person den Posteingang erreicht, passend zu People-first.
- **Imbox, The Feed, Paper Trail**: drei Orte nach Art der Post: Menschen und Dienste, die einem wichtig sind; Newsletter (bereits geöffnet, neueste zuerst); Belege und transaktionale Post.
- **Set Aside, Reply Later, Bubble Up**: Stapel für später und ein Weg, eine Mail wegzuschicken, damit sie oben wieder erscheint.
- **Clips** (gespeicherte Textausschnitte aus Mails) und **Collections** (mehrere Verläufe auf einer benannten, teilbaren Seite).

## Dokumentierte Versionen

| Version | Dokumentiert am | Status |
|---------|-----------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ⚠️ eine Funktionsseite; Tastenkürzel, API und Layout nicht gelesen |

## Verwendete Protokolle und Standards

HEY ist dafür bekannt, Drittanbieter-Clients keine offenen Mail-Protokolle anzubieten; das wurde hier nicht geprüft (offen). Siehe [Nachrichtenstandards](../../../../../data/messages/standards.md).

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
| https://www.hey.com/features/ ✅ | Funktionsseite des Anbieters | 2026-11-10 |
