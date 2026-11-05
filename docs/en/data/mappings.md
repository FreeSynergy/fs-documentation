# Field mappings

This file maps **our existing fields** onto evidenced standards. It is the
place where conflicts become visible before any code exists.

Rule: an entry counts only if it has a source. As in
[standards.md](standards.md): ✅ evidenced (retrieved 2026-10-31 at RFC Editor
/ w3.org / schema.org), ⚠️ unchecked, ❌ evidenced as absent.

Every example here is **taken verbatim from the specifications or assembled
from their field names** — no invented fields.

## Contact

Our definition is in [models.md](models.md#contact). This is the comparison:

| Our field | Evidenced counterpart | Source | Note |
|-----------|-----------------------|--------|------|
| `id` | `uid` (mandatory in JSContact), vCard `UID` | ✅ RFC 9553 §2.1.9, RFC 6350 | Our ID is an internal ULID. That is not enough for AS2 (see below) |
| `firstName` + `lastName` | `name.components[]` with `kind`: `given`, `given2`, `surname`, `surname2`, `title`, `credential`, `generation`, `separator` | ✅ RFC 9553 §2.2.1.2 | **The two-field model is too poor.** JSContact covers middle name, second family name (Spanish), honorific titles and generational suffix this way |
| — (missing) | `name.full` | ✅ RFC 9553 §2.2.1.1 | this is exactly the single `name` you want |
| `displayName` | `name.full` or `name` | ✅ RFC 9553, schema.org `name` | in ours it is only 🔁 derived — that fits, derive instead of store |
| `emails[] {type, value}` | `emails` → `Resource` with `uri`, `contexts`, `pref`, `label`, `mediaType`, `kind` | ✅ RFC 9553 §1.4.4, §2.3.1 | `type` is called `contexts` there; the COMMON values are `private` and `work` |
| `phones[] {type, value}` | `phones` → `Resource` | ✅ RFC 9553 §2.3.3 | vCard side: `TEL` with `TYPE` parameters |
| — (missing) | `onlineServices` | ✅ RFC 9553 §2.3.2 | the right place for `handle` (`@anna:matrix.org`); vCard calls it `IMPP` |
| `organization` | `organizations{}` with `name`, `units[]` (`OrgUnit.name`), `sortAs`, `contexts` | ✅ RFC 9553 §2.2.3 | multi-valued and with organisational units — better than one string |
| `jobTitle` | `titles` | ✅ RFC 9553 §2.2.5 | vCard side: `TITLE` (position) and `ROLE` (function) are **two different** properties |
| `addresses[]` | `addresses{}` → `Address` with `components[]` (`kind`: `number`, `name`, `block`, `locality`, `region`, `postcode`, `country`, `district`, `subdistrict`, `room`, `apartment`, `floor`, `building`, `direction`, `landmark`, `postOfficeBox`, `separator`), `countryCode`, `coordinates`, `timeZone`, `full`, `isOrdered`, `defaultSeparator`, `pref`, `contexts` (incl. `billing`, `delivery`) | ✅ RFC 9553 §2.5.1 | our `street`/`houseNumber`/`postalCode`/`city` are a **Western-Europeanisation**; the component types are the standard |
| `lat`/`lng` (in Location) | `Address.coordinates` as a `geo:` URI | ✅ RFC 9553 §2.5.1.1, RFC 5870 | |
| `ownerId` | `relatedTo` with `Relation.relation` | ✅ RFC 9553 §2.1.8 | roles are relations between cards there, not a foreign-key field |
| — (missing) | `keywords`, `notes`, `anniversaries`, `preferredLanguages`, `languages`, `media`, `links`, `cryptoKeys`, `calendars`, `schedulingAddresses`, `nicknames`, `speakToAs` (pronouns, grammatical gender), `localizations`, `members` | ✅ RFC 9553 §2.1–2.8 | free gain if we adopt the model instead of rebuilding it |
| `lifecycle` | **no counterpart** | ❌ vCard 4.0 contains no such concept | a real gap, see below |

### What an evidenced JSContact document looks like

Structure from RFC 9553 (§2.2.1, figure 20) — field names taken over unchanged:

```json
{
  "@type": "Card",
  "uid": "con_01HZXH7Q3T8V2B4C6D9E0F1A2K",
  "name": {
    "components": [
      { "kind": "surname", "value": "Weber" },
      { "kind": "separator", "value": " " },
      { "kind": "given", "value": "Anna" }
    ],
    "isOrdered": true
  },
  "emails": {
    "e1": { "uri": "mailto:anna@example.org", "contexts": { "work": true } }
  },
  "addresses": {
    "k23": {
      "contexts": { "work": true },
      "components": [
        { "kind": "number", "value": "12" },
        { "kind": "separator", "value": " " },
        { "kind": "name", "value": "Invalid Street" },
        { "kind": "locality", "value": "Berlin" },
        { "kind": "postcode", "value": "10557" },
        { "kind": "country", "value": "Germany" }
      ],
      "countryCode": "DE",
      "defaultSeparator": ", ",
      "isOrdered": true
    }
  }
}
```

The difference to our current model is not cosmetic: **`name` is an object with
parts and a `full` view**, which is why CRM, messenger, calendar and ERP can
read the same field and still render it differently.

## Name: the conflict the standards themselves have

Evidenced:

| System | Field for "display name" | Evidence |
|--------|--------------------------|----------|
| JSContact | `name` (object with `full`) | ✅ RFC 9553 §2.2.1 |
| JSCalendar | `title` (string) | ✅ RFC 8984 §4.2.1 |
| AS2 | `name`, multilingual `nameMap` | ✅ W3C AS2 Core §4.1 |
| schema.org | `name` on `Thing`, subproperty of `rdfs:label`; plus `headline` on `CreativeWork` | ✅ schema.org/Name, schema.org/headline |
| iCalendar | `SUMMARY` | ✅ RFC 5545 (event header) |

That means: **there is no single standard name.** "Always `name`" is therefore
not a statement about a standard but **our own rule** — and precisely why we
have to fix it in advance.

Proposal (not decided yet):

1. Internally the display field is called **`name`** everywhere (string,
   mandatory, one value per language via `nameMap` where needed).
2. Structured name **parts** only for people and organisations
   (`nameComponents[]` following JSContact).
3. `title` in JSCalendar/ICS is an **export alias**, not its own data field. In
   the database there is no `title` and no `displayName` next to `name`.
4. For documents: `name` = display name of the resource, `headline` only if we
   want schema.org compatibility for texts.

## Heading in the text → `name` of the resource

This is your example (a Notion heading that should become the name in the
database). Evidenced state: **no standard says the first heading is the name of
an object.** What exists and is usable as a building block for this:

| Building block | What it provides | Evidence |
|----------------|------------------|----------|
| W3C Web Annotation Model | a statement **about** a part of a text without changing the text: `body` (the tag/value), `target` (the place), selectors `RangeSelector`, `TextQuoteSelector`, `TextPositionSelector`; motif `classifying` = "classify the target as something" | ✅ |
| AS2 | `name` / `nameMap` as display name, `id` as an **absolute IRI** (mandatory per Core §4.1), `Link` with `href`/`mediaType` | ✅ |
| schema.org | `name` (general), `headline` (headline of a `CreativeWork`) | ✅ |
| RFC 9073 | `STYLED-DESCRIPTION` (rich-text description, `VALUE=TEXT`/`URI`, `FMTTYPE`, `DERIVED`) and `STRUCTURED-DATA` (structured data on an event, e.g. `application/ld+json`) | ✅ |
| RFC 8984 | `descriptionContentType`, `localizations` | ✅ |

### Finding from the existing material (checkable, already contradictory today)

Two places in this documentation already describe content **differently** — and
the heading question sits exactly between them:

| Place | What it says there |
|-------|--------------------|
| `components/workbenches/fields/rich-text-editor/attributes.md` | attribute `value`, type `string`, description "value (HTML)" |
| `data/models.md`, model `Block` | `type` with values `text`, `heading`, `image`, `table`, `code`, `callout`; type-dependent attributes in `props`; `content` as `array[] \| markdown`; further `order`, `align` |

Three consequences we must clean up before "heading → `name`" can work:

1. There are **two content representations** (HTML in the editor, block array
   in the model) and **no** documented mapping between them. A heading is
   `<h1>` in one case and a block in the other — which of the two ends up in
   the database is open.
2. The block has **no field for the heading level**. `level` (or `depth`) does
   not exist in `models.md`. Without that level we cannot say which heading is
   the "main heading".
3. For structured block content I found **no** standard. Common forms such as
   ProseMirror/TipTap JSON or Markdown AST are de-facto formats of foreign
   implementations, **not checked** by me here ⚠️. Markdown plus front matter in
   `formats.md` is our own convention, not a standard.

What we would have to decide ourselves is **a single rule** — for example:
*"A block with `type: heading` and `level: 1` standing as the first block of a
document writes its text into the document's `name`; the assignment is stored
as an annotation with motif `classifying`."* That would be a candidate for our
own specification, because exactly this rule does not exist anywhere.

Open points before we decide this:

1. What happens when someone edits the heading — is `name` pulled along, or is
   `name` decoupled afterwards?
2. What happens with two H1 blocks?
3. Does the same rule apply to `Task` (title from the first block?) and
   `Event` (`SUMMARY`)?
4. Should tags/mentions in the text land as annotations in the same way (motif
   `tagging`), so they can be queried across modules?

## Event and Task

The basis is **JSCalendar, RFC 8984** (see [standards.md](standards.md)). Our
definitions are in [models.md](models.md#event) and
[models.md](models.md#task).

| Our field | JSCalendar counterpart | Evidence | Note |
|-----------|------------------------|----------|------|
| `title` | `title` | ✅ §4.2.1 | here our models and the standard happen to agree — for people the same concept is called `name` |
| `start` | `start` | ✅ §5.1.1 | |
| `end` (mandatory in ours) | **does not exist** — JSCalendar works with `duration` | ✅ §5.1.2 | **real conflict.** Example from RFC 8984 §6.1: `"start": "2020-01-15T13:00:00"`, `"timeZone": "America/New_York"`, `"duration": "PT1H"` |
| `allDay` | `showWithoutTime` | ✅ §4.2.4 | |
| `timezone` | `timeZone`, `timeZones` | ✅ §4.7.1, §4.7.2 | the capitalisation differs |
| `locationId` | `locations` (sub-objects), `virtualLocations`, `Participant.locationId` | ✅ §4.2.5, §4.2.6, §4.4.6 | JSCalendar knows several places per event, we only one |
| `attendees[]` | `participants` (map of participant IDs) | ✅ §4.4.6 | |
| `attendees[].response` | `participationStatus` | ✅ §4.4.6 | values: `needs-action`, `accepted`, `declined`, `tentative`, `delegated`. **Our `needsAction` violates our own enum rule** (fields.md: lowercase, `_`) → internally `needs_action` |
| — (missing in ours) | `roles` — **mandatory**, at least one: `owner`, `attendee`, `optional`, `informational`, `chair`, `contact` | ✅ §4.4.6 | our participant model cannot tell apart: invited, merely informed, responsible, room |
| — (missing in ours) | `kind` of the participant: `individual`, `group`, `location`, `resource` | ✅ §4.4.6 | rooms and officials are participants — important for room booking |
| — (missing in ours) | `sendTo` (`imip`, `other`), `expectReply`, `scheduleAgent` (`server`, `client`, `none`), `participationComment` | ✅ §4.4.6 | capable of invitations without an extra table |
| `recurrenceRule` (RRULE string) | `recurrenceRules` — **objects**, not strings | ✅ §4.3.3 | RecurrenceRule: `@type`, `frequency` (`yearly`, `monthly`, `weekly`, `daily`, `hourly`, …), `interval`, `rscale`, `skip`, `firstDayOfWeek`, `byDay`, `byMonthDay`, `byMonth`, `byYearDay`, `byWeekNo`, `byHour`, `byMinute`, `bySecond`, `bySetPosition`, `count`, `until` |
| — (missing in ours) | `excludedRecurrenceRules` §4.3.4, `recurrenceOverrides` §4.3.5, `excluded` §4.3.6, `recurrenceId` §4.3.1, `recurrenceIdTimeZone` §4.3.2 | ✅ | **exceptions to series** our model cannot represent today — the most common calendar bug |
| `status` | `status` (event) | ⚠️ §5.1.3 | property evidenced, **value list not read** — do not present our values as a standard |
| `reminders` | `alerts`, `useDefaultAlerts` | ✅ §4.5.2, §4.5.1 | background: RFC 9074 extends VALARM |
| `calendarId` (mandatory in ours) | **no counterpart** in RFC 8984 | ❌ evidenced | `calendarIds` does **not** occur in RFC 8984. Calendar membership lives one level up — which spec governs that, I have **not checked** ⚠️ |
| `priority` (`low`/`normal`/`high`/`urgent`) | `priority` | ⚠️ §4.4.1 | the property exists, **value range not read** |
| Task `dueAt` | `due` | ✅ §5.2.1 | |
| Task `estimate` | `estimatedDuration` | ✅ §5.2.3 | |
| Task `progress` (0–100) | `percentComplete` §5.2.4 **and** `progress` §5.2.5 | ⚠️ | JSCalendar has both. The value range of `progress` is not evidenced for me — **0–100 is our decision, not a standard** |
| Task `assigneeIds`, `boardId`, `order` | **no counterpart** | ❌ | this is the "project structure" gap from [standards.md](standards.md) |

### Evidenced JSCalendar document (participants and series)

Field names and enum values are taken from RFC 8984 §4.2–4.5:

```json
{
  "@type": "Event",
  "uid": "evt_01HZXF2M3N4P5Q6R7S8T9U0V1W",
  "updated": "2026-10-30T18:22:10Z",
  "title": "Team sync",
  "start": "2026-11-05T10:00:00",
  "timeZone": "Europe/Berlin",
  "duration": "PT1H",
  "recurrenceRules": [
    { "@type": "RecurrenceRule", "frequency": "weekly", "byDay": ["WE"] }
  ],
  "participants": {
    "p1": {
      "@type": "Participant",
      "name": "Anna Weber",
      "email": "anna@example.org",
      "kind": "individual",
      "roles": { "attendee": true },
      "participationStatus": "accepted"
    },
    "p2": {
      "@type": "Participant",
      "name": "Room 3.12",
      "kind": "location",
      "roles": { "attendee": true },
      "participationStatus": "accepted"
    }
  }
}
```

Side finding: for the recurrence pattern JSCalendar refers to the RECUR value
type from RFC 5545 **and RFC 7529** ("Non-Gregorian Recurrence Rules …", in the
JSCalendar field `rscale`). If we store RRULE only as a string, we lose that
connection.

## Foreign systems not checked yet

I have **not** evidenced these, so I claim nothing about their field names:

| System | State |
|--------|-------|
| Mastodon (REST API, account fields) | ⚠️ not checked. Evidenced only: Mastodon introduces `Hashtag` as a subtype of AS2 `Link` and refers to `activitystreams#Hashtag` |
| Kanidm (attribute names) | ⚠️ not checked |
| MS Project, W6C, MSPDI | ⚠️ not checked |
| EN 16931, CII, XRechnung, Peppol, GS1, ISO 4217 | ⚠️ not checked |
| LDAP/`inetOrgPerson` | ⚠️ not checked |

These rows must be evidenced one by one **before** we map field names onto
them. Otherwise we build on rumours.

## See also

- [Data standards](standards.md)
- [Data models](models.md)
- [Standard fields](fields.md)
- [Data formats](formats.md)
- [Conventions](conventions.md)
