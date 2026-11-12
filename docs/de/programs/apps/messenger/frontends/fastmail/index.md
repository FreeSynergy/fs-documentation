# Fastmail

!!! warning "Maschinell übersetzt, noch nicht geprüft / Machine-translated, not yet reviewed"
    Diese Seite wurde maschinell aus der englischen Fassung übersetzt und noch nicht von einem Menschen geprüft.
    This page was machine-translated from the English version and has not yet been reviewed by a person.

> Kategorie: [messenger](../../index.md) · Typ: gehostete E-Mail mit Web- und mobilen Apps · Anbieter: Fastmail · Lizenz: proprietär ⚠️

## Was es ist

Fastmail ist ein kostenpflichtiger, gehosteter E-Mail-Dienst mit Web- und mobilen Apps; Kalender und Kontakte gehören zum Angebot. Eigene Domains können genutzt werden.

## Bemerkenswerte Ideen

Warum dieses Programm hier dokumentiert ist (ADR 0013):

- **Masked Email**: pro Anmeldung oder Registrierung wird eine zufällige Adresse erzeugt. Unternehmen können zwei solche Adressen nicht miteinander verknüpfen; eine beschriftete Adresse zeigt bei eingehender Post ein Masken-Symbol; eine Adresse, die Spam erhält, lässt sich abschalten, wobei auch sichtbar wird, wer sie weitergegeben hat. Die Passwortmanager 1Password und Bitwarden lassen sich für die Erstellung bei der Registrierung anbinden. Eigene Domains sind möglich (weniger anonym, aber übertragbar).
- **Aliasse** sind davon getrennt: gewählte Adressen für langlebige Identitäten, mit eigenem Absendernamen oder eigener Signatur.

Relevant für uns: eine Adresse pro Beziehung, widerrufbar, ohne die echte Identität zu ändern.

## Dokumentierte Versionen

| Version | Dokumentiert am | Status |
|---------|-----------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ⚠️ eine Anbieterseite |

## Verwendete Protokolle und Standards

JMAP wird auf der gelesenen Seite nicht genannt; die API-Dokumentation des Anbieters prüfen (offen). Siehe [Nachrichtenstandards](../../../../../data/messages/standards.md).

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
| https://www.fastmail.com/features/masked-email/ ✅ | Funktionsseite des Anbieters | 2026-11-10 |
