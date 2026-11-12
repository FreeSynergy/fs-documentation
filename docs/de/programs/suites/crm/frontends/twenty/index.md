# Twenty

!!! warning "Maschinell übersetzt, noch nicht geprüft / Machine-translated, not yet reviewed"
    Diese Seite wurde maschinell aus der englischen Fassung übersetzt und noch nicht von einem Menschen geprüft.
    This page was machine-translated from the English version and has not yet been reviewed by a person.

> Kategorie: [crm](../../index.md) · Typ: Open-Source-CRM · Anbieter: Twenty (twentyhq) · Lizenz: Open Core, AGPL-3.0 für den größten Teil des Codes ⚠️ (eine gesonderte kommerzielle Lizenz für mit Enterprise gekennzeichnete Dateien, laut einer Angabe eines Dritten)

## Was es ist
Twenty ist ein Open-Source-CRM, als Alternative zu den großen kommerziellen gebaut. Es hat Personen, Unternehmen und Verkaufschancen, anpassbare Ansichten und Workflows und ist als Code erweiterbar. Es läuft als Cloud-Dienst oder selbst gehostet mit Docker Compose.

## Bemerkenswerte Ideen
- **Eigene Objekte als vollwertige Objekte** — eigene Objekte und Felder werden im Code mit einem SDK deklariert, versionierbar und prüfbar; eigene Objekte erhalten dieselben Tabellen und Berechtigungen wie eingebaute (ADR 0013). Relevant für unser CRM als Suite über Personen (siehe [Anforderungen](../../requirements.md)).
- **Ansichten als Arbeitsfläche** — Tabellen-, Kanban- und Kalenderansichten, jeweils mit Filtern, Sortierung und Gruppierung.
- **Webhooks sowie REST und GraphQL** für dieselben Datensätze.

## Dokumentierte Versionen
| Version | Dokumentiert am | Status |
|---------|-----------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ✅ |

## Verwendete Protokolle und Standards
REST, GraphQL, Webhooks. Siehe [Datenstandards](../../../../../data/standards.md).

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
| https://github.com/twentyhq/twenty | Quell-README ✅ | 2026-11-10 |
| https://docs.twenty.com/developers/introduction | offizielle Dokumentation ✅ | 2026-11-10 |
| https://docs.twenty.com/getting-started/key-features | offizielle Dokumentation ⚠️ (nur über Suche) | 2026-11-10 |
