# Termine

Kalendereinträge, Serien, Teilnehmende — und **Aufgaben**: JSCalendar (RFC 8984) definiert die Objekttypen `Event` **und** `Task` (beide ✅ belegt, Eigenschaftslisten in [standards.md](../standards.md)).

## Standards in dieser Domäne

| Standard | Beleg | Rolle in FreeSynergy |
|----------|----------|---------------------|
| **JSCalendar, RFC 8984** | ✅ | **kanonisches Modell** (Arbeitsdarstellung in der Datenbank) |
| **iCalendar, RFC 5545** | ✅ | Dateiexport/-import, `RRULE`-Serien |
| **jCal, RFC 7265** | ✅ | JSON-Hülle über der iCalendar-Grammatik |
| **iTIP, RFC 5546** | ✅ | Einladungsprotokoll |
| **CalDAV Scheduling, RFC 6638** / **SYNC, RFC 6578** | ✅ | Serverintegration, Synchronisation (`syncToken`) |
| **RFC 9073 / RFC 9074** | ✅ | Rich-Text-Beschreibungen, Erweiterungen für Erinnerungen (Alarme) |
| Überarbeitung `draft-ietf-calext-jscalendarbis` | ✅ gefunden, Inhalt nicht gelesen | wird RFC 8984 ablösen — beobachten |

## Offene Punkte

- Gespeichertes Modell **JSCalendar 2.0** (Entwurf -22, ADR 0026); Original + AS2-`Event`-Umschlag + `Invite`/`Accept`-Protokoll (ADR 0020/0030)
- `title` vs. `name`: vorgeschlagene Regel — der Inhalt behält `title`, der `name` im Umschlag wird daraus abgeleitet (siehe [standards.md](../standards.md), offene Entscheidung 1)

## Siehe auch

- [standards.md → Kalender](../standards.md)
- [mappings.md](../mappings.md)
- Die eigene Domäne `tasks/` ist unnötig, solange JSCalendar `Task` genügt
