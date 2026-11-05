# JMAP crates — research by the user (2026-11-05)

Source: user's own research, pasted into the conversation 2026-11-05. **Not re-checked by Opus** (⚠️),
except the notes at the end.

## MarkAtwood/crate-jmap family (one workspace: JMAP Core, Mail, Calendars, FileNode, Blob, JSCalendar, JSContact, Chat, VTC)

| Area | Crates | Spec |
|------|--------|------|
| JMAP Calendars | `jmap-calendars-types` 0.1.2, `jmap-calendars-server` (19 methods + `CalendarsBackend` trait), `jmap-calendars-client`, `jmap-jscalendar-types` | draft-26 |
| JMAP File Storage | `jmap-filenode-types`, `jmap-filenode-server` (cycle detection, collision policy, cascade destroy, `FileNodeBackend`), `jmap-filenode-client` | draft-13/14 |
| JMAP Blob | `jmap-blob` 0.0.x (RFC 9404, early) | RFC 9404 |
| JSCalendar types | `jmap-jscalendar-types` | RFC 8984 (no 2.0 yet) |

## Other

| Crate | Notes |
|-------|-------|
| `calcard` (Stalwart) | supports **JSCalendar 2.0** (`jscalendarbis-22`, `jscalendar-icalendar-28`, updated 2026-10-27) |
| `jscalendar` (eikopf) | RFC 8984 only |
| `io-jmap` (pimalaya) | client, Calendars draft-27, read-only methods |
| `bifrost-jmap` (Soflutionltd) | client: RFC 8620/8621/8887/9404/9425/9610/9670 + Calendars draft-26 + Sieve draft-14 |
| JMAP Conditional Set (draft-00) | no crate; Mustang (mustang-im) implementing (PR #1634, Oct 2026) |

## Notes by Opus (cross-check with temp/research/messaging-crates.md)

- ⚠️ **calcard licence:** `messaging-crates.md` found that Stalwart moved `calcard` into its main repo
  under `AGPL-3.0-only OR LicenseRef-SEL` (Oct 2026); the last MIT/Apache version on crates.io is
  frozen at **0.3.14**. The JSCalendar 2.0 support of 2026-10-27 is therefore very likely **only in
  the AGPL version** → not usable for us (ADR 0015/0016). To verify before use.
- crate-jmap family: earlier finding "very young (created 2026-05, few stars)" — promising breadth,
  maturity to watch. Calendars implement draft-26 while the current draft is -33.
