# Listmonk

!!! warning "Maschinell übersetzt, noch nicht geprüft / Machine-translated, not yet reviewed"
    Diese Seite wurde maschinell aus der englischen Fassung übersetzt und noch nicht von einem Menschen geprüft.
    This page was machine-translated from the English version and has not yet been reviewed by a person.

> Kategorie: [marketing](../../index.md) · Typ: Verwaltung für Newsletter und Verteilerlisten · Anbieter: Listmonk-Projekt · Lizenz: AGPL-3.0

## Was es ist
Listmonk ist eine selbst gehostete Verwaltung für einseitige Verteilerlisten und Newsletter. Es wird als eigenständige Binärdatei ausgeliefert, mit PostgreSQL als einziger Abhängigkeit. Backend in Go, Frontend in Vue.

## Bemerkenswerte Ideen
- **Segmentierung per Abfrage auf Abonnenten** — Listen werden über eine Abfrage zugeschnitten statt über feste Gruppen (ADR 0013).
- **Eine Binärdatei, eine Datenbank** — klein im Betrieb.
- **Messenger** — Versandkanäle jenseits von E-Mail sind austauschbar.
- **Transaktionale E-Mail** über dieselbe API.

## Dokumentierte Versionen
| Version | Dokumentiert am | Status |
|---------|-----------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ⚠️ |

## Verwendete Protokolle und Standards
SMTP (angenommen ⚠️, nicht gelesen); OIDC für die Anmeldung. Siehe [Datenstandards](../../../../../data/standards.md).

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
| https://listmonk.app/docs/ | offizielle Dokumentation ✅ (nur Navigation und Überblick) | 2026-11-10 |
