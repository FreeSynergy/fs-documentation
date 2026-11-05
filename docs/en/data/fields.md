# Standard fields

Fields are the building blocks of the [models](models.md). Across all programs they are **named the same way**, so that components, frontends and workflows work without a translation layer.

## Standard steward per field group

Per the rule in [conventions.md](conventions.md) every field needs an evidence. The full derivation is in [standards.md](standards.md) and [mappings.md](mappings.md); here is the short version per section. ✅ evidenced, ⚠️ still to evidence.

| Field group | Steward | Evidence |
|-------------|---------|----------|
| ID fields (`id`, `externalId`) | JSContact `uid`, JSCalendar `uid` | ✅ RFC 9553 §2.1.9, RFC 8984 §4.1.2 |
| time fields (`createdAt`, `updatedAt`) | JSContact `created`/`updated` (type `UTCDateTime`), JSCalendar `created`/`updated`/`sequence` | ✅ RFC 9553 §1.4.5 and §2.1, RFC 8984 §4.1 |
| time fields (`start`, `timezone`, `recurrenceRule`) | JSCalendar `start`, `duration`, `timeZone`, `recurrenceRules` | ✅ field names evidenced. **Our format rule "ISO 8601 with offset" is not covered by that yet** ⚠️ |
| name fields (`name`, `firstName`, `lastName`) | JSContact `name.components[]` and `name.full`; schema.org `name`, `headline` | ✅ RFC 9553 §2.2.1; schema.org/Name, schema.org/headline |
| communication fields (`email`, `emails`, `phones`, `handle`) | JSContact `emails`, `phones`, `onlineServices`; vCard `TEL`, `EMAIL`, `IMPP` | ✅ RFC 9553 §2.3; RFC 6350 §6.4 |
| status and priority enums | JSCalendar `priority`, `freeBusyStatus`, `privacy`, `status`, `participationStatus` | ✅ RFC 8984 §4.4 and §5.1.3 |
| permission fields (`visibility`, `roles`, `permissions`, `scopes`) | **no steward found.** Candidate ODRL (reachability checked, content not read) | ⚠️ |
| metadata fields (`tags`, `locale`, `revision`) | JSContact `keywords`, `language`, `localizations`; JSCalendar `categories`, `keywords`, `color` | ✅ RFC 9553 §2.7 and §2.8; RFC 8984 §4.2 |
| content fields (`body`, `bodyFormat`, `blocks`) | RFC 9073 `STYLED-DESCRIPTION` (`FMTTYPE`, `DERIVED`), JSCalendar `descriptionContentType` | ✅ RFC 9073 §6.5; RFC 8984 §4.2.3 |
| UI and interaction fields (`ariaLabel`, `role`, …) | these are **not** database fields — they belong in the component documentation | ⚠️ evidence from HTML/ARIA not looked up |

Consequence: the field names in this file stay our **internal** spelling. What becomes of them on outward export is in [mappings.md](mappings.md).

## ID fields

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `id` | string | ✅ | unique, opaque resource ID | `"doc_01HZXD8R7M"` |
| `externalId` | string | ➖ | ID in the source system when synchronising | `"_mediaWiki:1234"` |
| `slug` | string | ➖ | URL-readable path part, unique within the parent object | `"project-a/overview"` |
| `parentId` | reference | ➖ | parent resource | `"doc_01HZXC"` |

Rules:

- prefix + sortable ID (`<type>_<uuid>` (UUIDv7)), no running numbers outwards
- `slug` only for addressable resources (`Document`, `Space`, `Team`)

## Time fields

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `createdAt` | datetime | ✅ | time of creation (system) | `"2026-10-01T09:00:00+02:00"` |
| `updatedAt` | datetime | ✅ | last change (system) | `"2026-10-30T18:22:10+01:00"` |
| `deletedAt` | datetime \| null | ➖ | time of the soft delete | `null` |
| `start` / `end` | datetime | ✅ (Event) | beginning and end | `"2026-11-05T10:00:00+01:00"` |
| `dueAt` | datetime \| null | ➖ | due date of a task | `"2026-11-01T17:00:00+01:00"` |
| `allDay` | boolean | ➖ | appointment without a time | `true` |
| `timezone` | string | ✅ (Event) | IANA time zone | `"Europe/Berlin"` |
| `recurrenceRule` | string \| null | ➖ | RRULE per RFC 5545 | `"FREQ=WEEKLY;BYDAY=WE"` |
| `duration` | duration | ➖ | ISO 8601 duration | `"PT1H30M"` |

Rules:

- always ISO 8601 with offset, never "bare" local timestamps
- `date` fields (`YYYY-MM-DD`) only for dates without a time (e.g. date of birth)
- durations as ISO 8601 duration (`PT30M`), not as a number of minutes

## Types and representation

| Type | Notation | Example |
|------|----------|---------|
| `string` | `"..."` | `"Anna Weber"` |
| `number` | number without thousands separator | `19.99` |
| `integer` | integer | `42` |
| `boolean` | `true` / `false` | `false` |
| `datetime` | ISO 8601 with offset | `"2026-10-31T06:00:00+01:00"` |
| `date` | `YYYY-MM-DD` | `"2026-10-31"` |
| `duration` | ISO 8601 Duration | `"PT30M"` |
| `enum` | lowercase, singular | `"active"` |
| `array[]` | list of values or references | `["tag_01", "tag_02"]` |
| `object` | free object, valid against a JSON Schema | `{"layout":"grid"}` |
| `reference` | ID string with the model reference in the docs | `"user_01HZXA"` |
| `markdown` | Markdown text | `"**Important**: …"` |
| `richtext` | block structure (block array) | `[{"type":"heading", …}]` |
| `html` | only when importing from foreign systems | `"<b>…</b>"` |
| `null` | missing value | `null` |

## Name fields

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `firstName` | string | ✅ | first name | `"Anna"` |
| `lastName` | string | ✅ | last name | `"Weber"` |
| `displayName` | string | ✅ | display name (the system can derive it) | `"Anna Weber"` |
| `name` | string | ✅ | single name for organisations/boards | `"Nordwind GmbH"` |
| `pronouns` | string | ➖ | form-of-address pronouns | `"she/her"` |
| `title` | string | ✅ | title of a resource | `"Introduction"` |

## Communication fields

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `email` | string | ➖ | main email (User) | `"anna@example.org"` |
| `emails` | array[] | ➖ | several addresses (Contact) | `[{"type":"work","value":"…"}]` |
| `phones` | array[] | ➖ | numbers in E.164 format | `[{"type":"mobile","value":"+4930123456"}]` |
| `urls` | array[] | ➖ | web addresses | `[{"type":"profile","value":"https://…"}]` |
| `handle` | string | ➖ | account name in a service | `"@anna:matrix.org"` |
| `channelId` | reference | ✅ (Message) | target channel | `"chan_01HZYC"` |

## Status and priority enums

| Field | Values | Meaning |
|-------|--------|---------|
| `status` (resource) | `draft`, `active`, `archived`, `deleted` | lifecycle |
| `status` (task) | `open`, `in_progress`, `done`, `archived` | progress of work |
| `status` (document) | `draft`, `published`, `archived` | publication |
| `status` (event) | `confirmed`, `tentative`, `cancelled` | appointment status |
| `status` (user) | `active`, `invited`, `disabled`, `deleted` | account status |
| `priority` | `low`, `normal`, `high`, `urgent` | urgency |
| `visibility` | `private`, `workspace`, `public` | visibility |
| `role` | `owner`, `admin`, `editor`, `commenter`, `viewer` | permission |
| `lifecycle` (contact) | `lead`, `prospect`, `customer`, `churned` | customer status |
| `response` (attendee) | `accepted`, `declined`, `tentative`, `needsAction` | acceptance or rejection of an appointment |

Rules:

- enums are lowercase, singular, with an underscore instead of a hyphen (`in_progress`)
- new values may be added additively, existing ones are never removed
- the display text comes from `locales/<code>.json`, never from the data value

## Permission fields

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `visibility` | enum | ➖ | visibility of the resource | `"workspace"` |
| `ownerId` | reference (User) | ➖ | owner | `"user_01HZXA"` |
| `roles` | array[] | ✅ (User, Membership) | list of roles | `["editor"]` |
| `permissions` | array[] | ➖ | individual rights | `["document:read", "document:write"]` |
| `scopes` | array[] | ➖ | API scopes of an integration | `["read:documents"]` |

## Metadata fields

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `tags` | array[] (Tag) | ➖ | keywords | `["docs", "wiki"]` |
| `category` | string | ➖ | category directory of the app | `"wiki"` |
| `locale` | string | ➖ | language code of the resource | `"en"` |
| `metadata` | object | ➖ | program-specific extra data | `{"mediawikiNamespace":0}` |
| `revision` | number | ➖ | current version number | `7` |
| `etag` | string | 🔁 | change marker for `If-Match` | `"W/\"7-a1b2\""` |
| `source` | string | ➖ | origin of the record | `"import:csv-2026-10"` |

## Content fields

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `body` | markdown | ➖ | running text (message, comment) | `"Hello everyone"` |
| `bodyFormat` | enum | ➖ | format of `body` | `"markdown"` |
| `blocks` | array[] (Block) | ✅ (Document) | structured content | `[{"type":"heading", …}]` |
| `excerpt` | string | ➖ | short preview, max. 280 characters | `"Introduction to …"` |
| `wordCount` | number | 🔁 | number of words | `512` |

## UI and interaction fields

These fields appear in component attributes ([components](../components/)) and in `layout.md`:

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `ariaLabel` | string | accessible description | `"open search"` |
| `role` | string | ARIA role | `"button"` |
| `animation` | string | animation name | `"fade-in"` |
| `duration` | number | animation duration in ms | `300` |
| `onTap` / `onSwipe` / `onShake` | function | gesture callbacks | — |
| `columns` / `rows` / `span` | number | grid layout of a widget | `4` |
| `order` | number | sort position | `12` |

## Null values and defaults

| Case | Notation | Remark |
|------|----------|--------|
| value deliberately empty | `null` | always this form |
| empty list | `[]` | never `null` for lists |
| empty text in a required field | not allowed | validation error |
| optional without a value | omit the field | in the request; `null` in the response |

## See also

- [data models](models.md)
- [data formats](formats.md)
- [conventions](conventions.md)
- [data API](api.md)
