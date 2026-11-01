# Termine

Kalendereinträge, Serien, Teilnehmer — und **Aufgaben**: JSCalendar (RFC 8984) definiert die Objekttypen `Event` **und** `Task` (beides ✅ belegt, Eigenschaftslisten in [standards.md](../standards.md)).

## Standards in dieser Domäne

| Standard | Beleg | Rolle bei FreeSynergy |
|----------|-------|-----------------------|
| **JSCalendar, RFC 8984** | ✅ | **kanonisches Modell** (Arbeitsrepräsentation in der Datenbank) |
| **iCalendar, RFC 5545** | ✅ | Datei-Export/Import, `RRULE`-Serien |
| **jCal, RFC 7265** | ✅ | JSON-Hülle über iCalendar-Grammatik |
| **iTIP, RFC 5546** | ✅ | Einladungsprotokoll |
| **CalDAV Scheduling, RFC 6638** / **SYNC, RFC 6578** | ✅ | Server-Integration, Sync (`syncToken`) |
| **RFC 9073 / RFC 9074** | ✅ | Rich-Text-Beschreibungen, Alarmerweiterungen |
| Revision `draft-ietf-calext-jscalendarbis` | ✅ gefunden, Inhalt ungelesen | wird RFC 8984 obsolet machen — beobachten |

## Offene Punkte

- Namenskonflikt `title` (JSCalendar) vs. `name` (JSContact/schema.org/AS2): Regel steht noch aus (offene Entscheidung 1 in [standards.md](../standards.md))

## Siehe auch

- [standards.md → Kalender](../standards.md)
- [mappings.md](../mappings.md)
- Die separate Domäne `aufgaben/` erübrigt sich, solange JSCalendar-`Task` ausreicht
