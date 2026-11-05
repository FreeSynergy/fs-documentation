# Request Tracker (RT) Dokumentation

> Kategorie: [helpdesk](../../index.md)

## Übersicht

Request Tracker von Best Practical ist der Veteran der Ticketsysteme: Perl-basiert, extrem regexp-/skriptgetrieben, mit REST 1.0 und JSON-RPC 2.0 API. Skaliert in großen Organisationen (Universitäten, ISPs) und gilt als Referenz für Ticket-Workflows.

## Bemerkenswerte Ideen

_Zu tun: Was kann dieses Programm, das andere nicht können? Warum ist es hier dokumentiert (ADR 0013)?_

## Dokumentierte Versionen

<!-- gen:versions (Spiegel von docs/en; ADR 0011) — edits inside are overwritten -->
| Version | Pflichtdateien vorhanden |
|---------|------------------------|
| [latest](latest/description.md) | 6/7 |

### latest

| Datei | Inhalt |
|------|----------|
| [description.md](latest/description.md) | Abgrenzung zu Zammad, GLPI, osTicket |
| [features.md](latest/features.md) | Queues, Scrips, Saved Searches, Was RT NICHT kann |
| [layout.md](latest/layout.md) | Query-basierte Listen, Create-Page, Update-Page |
| [menus.md](latest/menus.md) | Menüstruktur Create/Browse/Query/Logs/Admin |
| [shortcuts.md](latest/shortcuts.md) | keine UI-Shortcuts, dafür Strong-Aliase |
| [api.md](latest/api.md) | REST 1.0 (`/REST/1.0`), JSON-RPC 2.0, CLI `rt` |

⚠️ Fehlende Pflichtdateien: `themes/index.md`
<!-- /gen:versions -->
