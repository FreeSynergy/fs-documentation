# Termine – Standards

> Belege stehen zentral in [standards.md](../standards.md) — **nichts aus dem Web nachladen.**

## Kernstandard

| Standard | Beleg | Rolle |
|----------|-------|-------|
| **JSCalendar, RFC 8984** | ✅ | kanonisches Modell (Beschluss 1): Objekttypen `Event`, `Task`, `Group` |

**Geprüfte Eigenschaften (RFC 8984, ✅):** `@type`, `uid`, `relatedTo`, `prodId`, `created`, `updated`, `sequence`, `method`, `title`, `description`, `descriptionContentType`, `showWithoutTime`, `locations`, `virtualLocations`, `links`, `locale`, `keywords`, `categories`, `color`, `recurrenceId`, `recurrenceRules`, `excludedRecurrenceRules`, `recurrenceOverrides`, `excluded`, `priority`, `freeBusyStatus`, `privacy`, `replyTo`, `sentBy`, `participants`, `requestStatus`, `useDefaultAlerts`, `alerts`, `localizations`, `timeZone`, `timeZones` — Event: `start`, `duration`, `status`; Task: `due`, `start`, `estimatedDuration`, `percentComplete`, `progress`, `progressUpdated`.

**Participant-Modell (RFC 8984, ✅):** `name`, `email`, `description`, `sendTo` (`imip`, `other`), `kind` (`individual`, `group`, `location`, `resource`), `roles` (Pflicht, mindestens eine: `owner`, `attendee`, `optional`, `informational`, `chair`, `contact`), `locationId`, `language`, `participationStatus` (`needs-action`, `accepted`, `declined`, `tentative`, `delegated`), `participationComment`, `expectReply`, `scheduleAgent`, `scheduleForceSend`.

## Umgebende Standards (alle ✅)

| Standard | Beleg | Rolle |
|----------|-------|-------|
| iCalendar, RFC 5545 | ✅ | Datei-Export/Import; `RRULE`-Regelwerk |
| jCal, RFC 7265 | ✅ | JSON-Hülle über iCalendar-Grammatik (Exportvariante) |
| iTIP, RFC 5546 | ✅ | Einladungsprotokoll |
| CalDAV Scheduling, RFC 6638 | ✅ | Server-Integration |
| CalDAV SYNC, RFC 6578 | ✅ | Sync-Mechanismus (`sync_token`) |
| RFC 9073 | ✅ | `STYLED-DESCRIPTION` (Rich-Text), `STRUCTURED-DATA` |
| RFC 9074 | ✅ | VALARM-Erweiterungen (`alerts`/Reminders) |
| RFC 6868 | ✅ | gemeinsame Escape-Regeln iCal/vCard |
| RFC 5322 §3.4.1 | ✅ | Format von `Participant.email` |
| `draft-ietf-calext-jscalendarbis` | ✅ gefunden, Inhalt ungelesen ⚠️ | wird RFC 8984 obsolet machen — beobachten |

## Warum JSCalendar und nicht jCal

jCal ist die JSON-Hülle **über der iCalendar-Grammatik** (Eigenschaftslisten mit Parametern); JSCalendar ist ein echtes Objektmodell — für eine Datenbank ist JSCalendar die Arbeitsrepräsentation, iCalendar/jCal sind Export (Standpunkt aus [standards.md](../standards.md)).

## Offene Standard-Punkte

- Namenskonflikt: JSCalendar `title` (Anzeigename) vs. `name` (JSContact/schema.org/AS2) — Regel ist **offene Entscheidung 1** in [standards.md](../standards.md).
- jscalendarbis lesen, sobald beschlossen wird, RFC 8984 abzulösen.
