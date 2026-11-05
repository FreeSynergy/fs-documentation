# Events (Calendar) – Standards Update

Researched: 2026-11-05 · by: Claude subagent

Scope: what changed since the existing evidence (RFC 8984, 5545, 7265, 5546, 6638, 6578, 9073, 9074, 6868).
Legend: ✅ verified on a primary source · ⚠️ inferred, partly verified, or not yet final

---

## 1. JSCalendar 2.0 – `draft-ietf-calext-jscalendarbis`

**Status:** `-22`, dated 2026-10-05 (datatracker "last updated" 2026-10-04). Calext WG state "Submitted to IESG for Publication". IESG state "AD Evaluation::AD Followup" (AD Andy Newton). Intended status Proposed Standard. **Not an RFC yet.** It obsoletes RFC 8984 once approved.
> "This specification defines version "2.0" of JSCalendar … This document obsoletes RFC 8984, also referred to as version "1.0""
https://datatracker.ietf.org/doc/draft-ietf-calext-jscalendarbis/ ✅

**Goal:** better round-tripping with iCalendar, and alignment with JSContact (registry policy, validation, versioning).
> "The newly defined version "2.0" aims to improve interoperability with existing iCalendar-based systems. It also aligns its definitions with JSContact"
https://www.ietf.org/archive/id/draft-ietf-calext-jscalendarbis-22.txt ✅

### Key differences from RFC 8984 (Appendix A of -22) ✅

All items below come from https://www.ietf.org/archive/id/draft-ietf-calext-jscalendarbis-22.txt, Appendix A.

| Area | Change |
|---|---|
| Object types | **`Event`, `Task` and `Group` all remain** (§2.1–2.3). `Group` is **not** removed: "A Group is a collection of Event … and/or Task … objects." |
| `title` | Unchanged; it is **not** renamed to `name` (§3.2.1). |
| `@type` | Now **optional in most cases**: "the "@type" property is optional in the majority of cases" (this follows the JSContact notation). |
| `version` | **New and mandatory**, with the values `"1.0"` and `"2.0"`. The media type gets an optional `version` parameter (§1.9.2, §3.1.2, §7.1). |
| Recurrence | `recurrenceRules` (array) is **obsolete** and replaced by single-valued `recurrenceRule`. `excludedRecurrenceRules` is **obsolete**, because EXRULE is deprecated. |
| Time zones | `timeZones` (custom VTIMEZONE-like objects) and the `TimeZone`/`TimeZoneRule` types are **obsolete**. Only IANA TZDB IDs are allowed. `timeZone` and `recurrenceIdTimeZone` can no longer be `null`. |
| End time zone | `Location.relativeTo` and `Location.timeZone` are **obsolete**. They are replaced by **`Event.endTimeZone`**. |
| Locations | **New `mainLocationId`**, because iCalendar allows only one LOCATION. `Location.description` and `VirtualLocation.description` are **reserved** (removed for now). |
| Links | `Link.cid` is **obsolete**. `Link.display` is now multi-valued. `Link.rel` allows extension relation types (RFC 9253 LINKREL) and defaults to `"enclosure"`. |
| Organizer | `replyTo` is now **reserved** and replaced by **`organizerCalendarAddress`**. `sentBy` requires that property. |
| Participants | `sendTo` is **reserved** and replaced by **`Participant.calendarAddress`** (a single calendar address). Many participant properties now require `calendarAddress`. `delegatedTo`, `delegatedFrom` and `memberOf` now hold calendar addresses instead of participant IDs. **Obsolete:** `Participant.language`, `Participant.locationId`, `progressUpdated`. **New:** `Participant.descriptionContentType`. **Reserved for JMAP or future iTIP work:** `scheduleSequence`, `scheduleUpdated`, `invitedBy`, `participationComment`, `scheduleAgent`, `scheduleForceSend`, `scheduleStatus`, `requestStatus`. |
| Roles | New `required` role. The `attendee` and `contact` roles are removed, and `owner` is redefined. `roles` is no longer mandatory. |
| Task | `progress` loses the value `cancelled`. If `timeZone` is set, at least one of `due` or `start` is required. `start` is required when there is a recurrence. Rich task status is deferred to a future extension (VSTATUS, RFC 10051). |
| Alerts | `relatedTo` uses the new `snooze` relation (RFC 9074). The default `trigger` type is `OffsetTrigger`. |
| Localization | `localizations` is **reserved** (removed until iCalendar can express it). |
| JMAP-only | `useDefaultAlerts` is reserved for JMAP Calendars. |
| Types | `PatchObject` can now patch array members. `UTCDateTime`, `LocalDateTime` and `Duration` **no longer allow fractional seconds**. `color` must be 6-digit hex only. `privacy` must preserve unknown values and treat them as private. |
| New reserved | `extra` (a name that is guaranteed never to be used), `excluded` (internal use only). |

**Should we store it?** Yes, store 2.0 (see the Recommendation section). It is the newest version, JMAP Calendars already references it (§3), and it is IESG-stage stable. The remaining risk is small changes during AD/IESG review. ⚠️

---

## 2. Other calext RFCs and drafts since 2021

Source for all statuses below: https://datatracker.ietf.org/wg/calext/documents/ (fetched 2026-11-05).

| Document | Status | ✅/⚠️ |
|---|---|---|
| **draft-ietf-calext-jscalendar-icalendar-29**, "JSCalendar: Converting from and to iCalendar" (2026-11-02) | Submitted to IESG, "AD Evaluation::AD Followup" | ✅ |
| **draft-ietf-calext-icalendar-jscalendar-extensions-09**, "iCalendar Format Extensions for JSCalendar" (2026-10-29) | IESG "Waiting for AD Go-Ahead" (IETF Last Call done) | ✅ |
| **RFC 10051**, "Task Extensions to iCalendar" (2026-10). Adds VSTATUS and more to VTODO; updates RFC 5545 | **Published, Proposed Standard** | ✅ |
| **RFC 9253**, "Support for iCalendar Relationships" (2022-08). Adds LINK, RELATED-TO extensions, CONCEPT, REFID | Published, Proposed Standard | ✅ |
| RFC 9073 / 9074 (2021-08) | Published (already evidenced) | ✅ |
| RFC 7953, "Calendar Availability" (VAVAILABILITY, 2016-08) | Published, Proposed Standard. No bis draft. | ✅ |
| RFC 7986, "New Properties for iCalendar" (2016) | Published | ✅ |
| draft-ietf-calext-vpoll-07, "VPOLL: Consensus Scheduling" | **Expired** (2024-10-14). No RFC exists. | ✅ |
| draft-ietf-calext-subscription-upgrade-13 | **Expired** (2025-03-17) after IETF Last Call. No RFC exists. | ✅ |
| draft-ietf-calext-icalendar-series-03 | **Expired** (2021-04) | ✅ |
| draft-ietf-calext-itip-participants-00, "iTip using PARTICIPANT only" | **Expired** (2024-12) | ✅ |
| RFC 9555 | **Not calendar-related**: it is "JSContact: Converting from and to vCard" (now in rfc9555bis). The JSCalendar counterpart is the jscalendar-icalendar draft above. | ✅ |

Quote for RFC 10051:
> "defines extensions to "VTODO" to provide improved status tracking, scheduling, and specification of tasks to allow its use in other contexts, such as process control and project management."
https://www.rfc-editor.org/info/rfc10051 ✅

**There is no iTIP (RFC 5546) successor.** JSCalendar 2.0 explicitly defers iTIP-related participant properties: "This requires further work by IETF to update iTIP [RFC5546]" (jscalendarbis-22, App. A.2.2) ✅

---

## 3. JMAP

| Document | Status | ✅/⚠️ |
|---|---|---|
| **draft-ietf-jmap-calendars-33** (2026-10-14) | IESG approved; **"RFC Ed Queue"**. RFC Editor status "blocked: Reference Not Received", which most likely means it waits for jscalendarbis. It references `[I-D.ietf-calext-jscalendarbis]` throughout, so it is built on **JSCalendar 2.0**. **No RFC number yet.** | ✅ (the cause of the block is ⚠️ inference) |
| draft-ietf-jmap-tasks-06 | **Expired** (last revision 2023-03). WG milestone "Mar 2027 Submit JMAP Tasks document to IESG". | ✅ |
| **RFC 9670**, "JMAP Sharing" (2024) | Published, Proposed Standard | ✅ |

> "This document specifies a data model for synchronizing calendar data with a server using JMAP."
https://datatracker.ietf.org/doc/draft-ietf-jmap-calendars/ ✅

> "This document specifies a data model for sharing data between users using the JSON Meta Application Protocol (JMAP)."
https://www.rfc-editor.org/info/rfc9670 ✅

---

## 4. ActivityStreams 2.0 (W3C Rec) and FEP-8a8e

Source for all AS2 definitions: https://www.w3.org/TR/activitystreams-vocabulary/ ✅

| Term | Definition (quote) |
|---|---|
| `Event` | "Represents any kind of event. Extends: Object" |
| `startTime` | "The date and time describing the actual or expected starting time of the object." Range `xsd:dateTime`, functional |
| `endTime` | "The date and time describing the actual or expected ending time of the object." Range `xsd:dateTime`, functional |
| `duration` | "…indicates the object's approximate duration. The value MUST be expressed as an xsd:duration" |
| `location` | "Indicates one or more physical or logical locations associated with the object." Range `Object \| Link` |
| `Invite` | "A specialization of Offer in which the actor is extending an invitation for the object to the target." |
| `Accept` | "Indicates that the actor accepts the object." (The spec's example is accepting an `Invite` of an `Event`.) |
| `TentativeAccept` | "A specialization of Accept indicating that the acceptance is tentative." |
| `Reject` | "Indicates that the actor is rejecting the object." (`TentativeReject` also exists.) |

**Usable as an envelope or log for invitations?** Yes, and the spec's own examples are event invitations (Invite→Event, Accept/TentativeAccept/Reject→Invite). ✅

The limits are as follows (⚠️ my analysis):
- AS2 has no recurrence, no time zone ID, no participant roles, and no delegation.
- `startTime`/`endTime` are offset-based `xsd:dateTime` values, so floating or local times are lost.
- There is no equivalent of iTIP `COUNTER`, `DECLINECOUNTER`, `REFRESH` or `ADD`.
- AS2 therefore works as an envelope and log, but not as the content model.

**FEP-8a8e "A common approach to using the Event object type":** `status: DRAFT`, dateReceived 2025-04-23 (front matter, codeberg main branch). The tracking issue says it may be WITHDRAWN after 2026-04-23 if no further action is taken. It was still DRAFT when fetched on 2026-11-05.
https://codeberg.org/fediverse/fep/src/branch/main/fep/8a8e/fep-8a8e.md ✅ (status) ⚠️ (not final)

What the FEP contains:
- Required properties: `name`, `startTime` and `endTime` (with a `displayEndTime` flag).
- An optional IANA `timezone` property.
- `location` as a `Place` (schema.org `address`) or a `VirtualLocation`, as an array for hybrid events.
- RSVP via `Join`→`Accept`, or `Invite`→`Accept`.
- An `attendees` collection, `joinMode` (`free`/`restricted`/`external`/`none`/`invite`), and `requiredJoinVisibility`.
- Recurrence is **explicitly out of scope**.

**What the platforms use**, according to the FEP history section:
> "Friendica and Hubzilla … using `Invite` for events … applications like Mobilizon or Gancio … chose to make use of the `Create` activity."
https://fep.swf.pub/fep/8a8e/fep-8a8e.html ✅

The FEP says its `joinMode` and `externalParticipationUrl` are "compatible with … the extensions defined by Mobilizon". From that I infer that Mobilizon uses `Join`/`Accept`/`Reject` for participation. ⚠️ I did not verify this against Mobilizon's own documentation, which is not a primary standards source.

---

## 5. Time zones

- **IANA tzdb, current release: 2026f (2026-10-27).** Cuba will not fall back on 2026-11-01. The release also says "No more leap seconds, and leap second tables no longer expire."
  https://data.iana.org/time-zones/tzdb/NEWS ✅
- **RFC 9557**, "Date and Time on the Internet: Timestamps with Additional Information" (IXDTF), Proposed Standard, 2024 (April). It extends RFC 3339 with suffixes such as `[Europe/Berlin]`, and redefines `Z`.
  > "defines an extension to the timestamp format defined in RFC 3339 for representing additional information, including a time zone."
  https://www.rfc-editor.org/info/rfc9557 ✅

**Relevance to JSCalendar** (⚠️ analysis): JSCalendar 2.0 keeps `LocalDateTime` plus a separate `timeZone`/`endTimeZone` (IANA ID). It does **not** use IXDTF, and it drops embedded custom zones and fractional seconds. IXDTF is useful in our AS2 envelope, logs and APIs, to carry the zone alongside `startTime` (for example `2026-12-31T23:00:00+01:00[Europe/Berlin]`). Two points must be checked first:
- AS2 declares `xsd:dateTime` as the range, so strict parsers may reject the suffix. Keep plain RFC 3339 in `startTime` and put the zone in FEP-8a8e `timezone`.
- Re-validate stored events whenever we update tzdb (pin the version, for example `tzdb=2026f`).

---

## Recommendation (OPINION)

> ⚠️ Opinion, not a standards finding.

1. **Content standard: JSCalendar 2.0** (`draft-ietf-calext-jscalendarbis-22`). Store `"version": "2.0"` and the media type `application/jscalendar+json;type=event|task|group`.
   - Reasons: it is the newest version, JMAP Calendars depends on it, and it maps losslessly to iCalendar via the jscalendar-icalendar draft (-29).
   - Track the drafts until they become RFCs, and add a migration hook in case IESG review changes something. Do **not** write 1.0-only properties such as `recurrenceRules`, `timeZones`, `replyTo`, `sendTo` or `localizations`.
   - When importing RFC 8984 data, upgrade it to 2.0. For example, `recurrenceRules[0]` becomes `recurrenceRule`, `replyTo.imip` becomes `organizerCalendarAddress`, and `sendTo` becomes `calendarAddress`.
2. **Tasks: JSCalendar 2.0 `Task`**, shared with project management. For project-management status (VSTATUS, RFC 10051) no JSCalendar extension exists yet.
   - Map it via the iCalendar original, or with a vendor-prefixed property such as `freesynergy.org:status` (§1.8 vendor extensions) until an IETF JSCalendar tasks extension appears.
   - Use `relatedTo` (parent/child/snooze; RFC 9253 semantics) for subtasks and dependencies.
3. **Original:** keep the received bytes unchanged, for example:
   - an iTIP message (`text/calendar; method=REQUEST|REPLY|CANCEL|COUNTER…`) together with its iMIP MIME wrapper if it arrived by mail;
   - an ICS file or feed snapshot;
   - a jCal object;
   - an AP JSON-LD activity.

   Store a hash, the source, `received_at` and the tzdb version used for parsing.
4. **AS2 envelope and activity log** (one log entry per iTIP/AP action):

   | Action | AS2 activity | iTIP equivalent | JSCalendar effect |
   |---|---|---|---|
   | publish event | `Create{Event}` (public, as Mobilizon/Gancio do) | PUBLISH | new Event |
   | invite | `Invite{object: Event, target: [attendees]}` | REQUEST | `participants[*].calendarAddress` |
   | accept / tentative / decline | `Accept` / `TentativeAccept` / `Reject` `{object: Invite}` | REPLY PARTSTAT=ACCEPTED/TENTATIVE/DECLINED | `participationStatus` |
   | self-RSVP to public event | `Join{object: Event}` then `Accept`/`Reject` (FEP-8a8e) | (none) | add participant |
   | change | `Update{Event}` | REQUEST (higher SEQUENCE) | `sequence`++ |
   | cancel | `Delete` (or `Update` + `status: cancelled`) | CANCEL | `status: "cancelled"` |
   | delegate / counter | **no AS2 type**, so use an extension activity | DELEGATE / COUNTER | gap |

   - For federation, put an AS2 `Event` projection inside the envelope that follows FEP-8a8e: `name` taken from `title`, `startTime`/`endTime` computed from `start`+`duration`+`timeZone`, plus `timezone` and `location`.
   - Link that projection to the stored JSCalendar `uid` (for example via `url` or an `attachment` with media type `application/jscalendar+json`).
5. **Gaps our own spec must close:**
   - AS2 lacks recurrence, roles, delegation and counter-proposals. Define `fs:` extension activities or always attach the JSCalendar or iTIP payload.
   - The iTIP scheduling properties are only reserved in JSCalendar 2.0 (`scheduleSequence`, `scheduleStatus`, `invitedBy`, `requestStatus`), so we need an internal schema for scheduling state, or we adopt the JMAP Calendars definitions.
   - VPOLL, availability and series: VPOLL and series are expired drafts, and RFC 7953 has no JSCalendar mapping. Treat them as out of scope or as vendor extensions.
   - Task status (RFC 10051 VSTATUS) has no JSCalendar form yet.
   - Localization: `localizations` is reserved in 2.0, and AS2 `nameMap`/`contentMap` could carry this for public events.
   - Time zone policy: allow IANA IDs only, record the tzdb version, and decide whether to emit IXDTF (RFC 9557) in APIs.
   - Sync: CalDAV (RFC 4791/6638/6578) is the iCalendar surface. JMAP Calendars (RFC pending) is the natural JSON sync API, and its sharing model is RFC 9670.
