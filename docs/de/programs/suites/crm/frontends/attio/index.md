# Attio

!!! warning "Maschinell übersetzt, noch nicht geprüft / Machine-translated, not yet reviewed"
    Diese Seite wurde maschinell aus der englischen Fassung übersetzt und noch nicht von einem Menschen geprüft.
    This page was machine-translated from the English version and has not yet been reviewed by a person.

> Kategorie: [crm](../../index.md) · Typ: CRM (SaaS) · Anbieter: Attio · Lizenz: proprietär

## Was es ist
Attio ist ein kommerzielles CRM mit einem flexiblen Datenmodell. Datensätze zu Personen und Unternehmen werden automatisch ergänzt (Anreicherung), und E-Mail sowie Kalender lassen sich synchronisieren. Objekte, Attribute, Listen und Ansichten sind konfigurierbar.

## Bemerkenswerte Ideen
- **Anreicherung** — Datensätze werden automatisch mit Daten von außen gefüllt; das ist an die Standardobjekte gebunden, die die eingebauten Anreicherungsattribute tragen (ADR 0013).
- **Standard- und eigene Objekte** — Personen und Unternehmen sind von Anfang an vorhanden; Geschäfte, Nutzende und Arbeitsbereiche lassen sich einschalten; Administrierende fügen eigene Objekte hinzu (kostenpflichtige Tarife).

## Dokumentierte Versionen
| Version | Dokumentiert am | Status |
|---------|-----------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ⚠️ |

## Verwendete Protokolle und Standards
REST-API, SDK und MCP werden genannt (Entwicklerdokumentation nicht gelesen). Siehe [Datenstandards](../../../../../data/standards.md).

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
| https://attio.com/help | offizielle Hilfe ✅ | 2026-11-10 |
| https://attio.com/help/reference/attio-101/attios-data-model/understanding-objects | offizielle Hilfe ⚠️ (über Suchzusammenfassung) | 2026-11-10 |
| https://attio.com/help/reference/managing-your-data/objects/create-and-manage-custom-objects | offizielle Hilfe ⚠️ (über Suchzusammenfassung) | 2026-11-10 |
