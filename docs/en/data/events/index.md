# Appointments

Calendar entries, series, participants — and **tasks**: JSCalendar (RFC 8984) defines the object types `Event` **and** `Task` (both ✅ evidenced, property lists in [standards.md](../standards.md)).

## Standards in this domain

| Standard | Evidence | Role in FreeSynergy |
|----------|----------|---------------------|
| **JSCalendar, RFC 8984** | ✅ | **canonical model** (working representation in the database) |
| **iCalendar, RFC 5545** | ✅ | file export/import, `RRULE` series |
| **jCal, RFC 7265** | ✅ | JSON wrapper over the iCalendar grammar |
| **iTIP, RFC 5546** | ✅ | invitation protocol |
| **CalDAV Scheduling, RFC 6638** / **SYNC, RFC 6578** | ✅ | server integration, sync (`syncToken`) |
| **RFC 9073 / RFC 9074** | ✅ | rich-text descriptions, alarm extensions |
| Revision `draft-ietf-calext-jscalendarbis` | ✅ found, content unread | will obsolete RFC 8984 — watch it |

## Open points

- Naming conflict `title` (JSCalendar) vs. `name` (JSContact/schema.org/AS2): the rule is still pending (open decision 1 in [standards.md](../standards.md))

## See also

- [standards.md → Calendar](../standards.md)
- [mappings.md](../mappings.md)
- The separate `tasks/` domain is unnecessary as long as JSCalendar `Task` suffices
