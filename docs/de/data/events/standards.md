# Termine – Standards

> Belege stehen zentral in [standards.md](../standards.md) — **nichts aus dem Web nachladen.**

## Kernstandard (aktualisiert 2026-11-05, `temp/research/events-standards.md`)

| Standard | Beleg | Rolle |
|----------|-------|-------|
| **JSCalendar 2.0** — `draft-ietf-calext-jscalendarbis-22` (2026-10-05, IESG-Review, macht RFC 8984 obsolet) | ✅ | **Speichermodell** (ADR 0026): `version: "2.0"` pflicht; eingehende RFC-8984-Daten werden beim Import hochgezogen |
| JSCalendar 1.0, RFC 8984 | ✅ | Import/Kompatibilität |

**Was sich in 2.0 ändert (✅):** neu `version` (pflicht), `mainLocationId`, `organizerCalendarAddress`, `Participant.calendarAddress`, `Event.endTimeZone`; `@type` meist optional; `recurrenceRules` → ein einziges `recurrenceRule`. **Obsolet:** `timeZones` (nur noch IANA-IDs), `excludedRecurrenceRules`, `Link.cid`, `Location.timeZone`/`relativeTo`, `Participant.language`/`locationId`, Bruchteile von Sekunden. **Reserviert (zunächst herausgenommen):** `replyTo`, `sendTo`, `localizations`, iTIP-Planungs-Eigenschaften (`scheduleSequence`, `invitedBy`, `requestStatus`, …). `Event`, `Task`, `Group` und `title` bleiben.

Die RFC-8984-Eigenschaftslisten unten bleiben als 1.0-Referenz gültig.

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
| JSCalendar ↔ iCalendar-Mapping-Entwurf (-29) | ✅ AD-Follow-up | Umrechnungsregeln für Export/Import |
| **RFC 10051** Task-Erweiterungen für iCalendar (2026-10) | ✅ | umfangreicherer Task-Status (Projektmanagement) — noch keine JSCalendar-Form → Anbieter-Eigenschaft `freesynergy.net:taskStatus` |
| RFC 9253 (Beziehungen/Links), RFC 7953 (Verfügbarkeit) | ✅ | unverändert |
| **JMAP Calendars** (`draft-ietf-jmap-calendars-33`) | ✅ gebilligt, RFC-Editor-Warteschlange (wartet auf JSCalendar 2.0) | Kalender-Zugriffsprotokoll, baut auf JSCalendar 2.0 |
| JMAP Sharing, RFC 9670 (2024) | ✅ | Kalender teilen |
| JMAP Tasks | ✅ 2023 abgelaufen, WG plant IESG März 2027 | beobachten |
| **AS2 `Event`, `Invite`, `Accept`, `TentativeAccept`, `Reject`** | ✅ | Envelope und Einladungsprotokoll (ADR 0020) |
| FEP-8a8e (Termine im Fediverse) | ✅ Entwurf | Eigenschaft `timezone`, RSVP über `Join`/`Invite` + `Accept` |
| IANA tzdb **2026f** (2026-10-27); RFC 9557 IXDTF (2024) | ✅ | Zeitzonen als IANA-IDs; IXDTF nur für unsere APIs/Protokolle |
| abgelaufen: VPOLL, subscription-upgrade, series, itip-participants | ✅ | — |

## Warum JSCalendar und nicht jCal

jCal ist die JSON-Hülle **über der iCalendar-Grammatik** (Eigenschaftslisten mit Parametern); JSCalendar ist ein echtes Objektmodell — für eine Datenbank ist JSCalendar die Arbeitsrepräsentation, iCalendar/jCal sind Export (Standpunkt aus [standards.md](../standards.md)).

## Offene Standard-Punkte

- Namenskonflikt: JSCalendar `title` (Anzeigename) vs. `name` (JSContact/schema.org/AS2) — Regel ist **offene Entscheidung 1** in [standards.md](../standards.md).
- ~~jscalendarbis lesen~~ → erledigt 2026-11-05: wir speichern 2.0 (Risiko: das IESG-Review kann noch Details ändern).
- **Lücken → Kandidaten für eigene Spec:** Delegation und Gegenvorschläge, Planungsstatus (in 2.0 reserviert), Task-Status, Lokalisierung, Umfragen/Verfügbarkeit (VPOLL abgelaufen), Zeitzonen-Politik.
