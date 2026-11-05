# Standardised data

Standardised data describe in which **formats**, **models** and **fields** FreeSynergy programs, components and masks exchange information.

## Why standardisation?

- **Interoperability**: messenger, wiki, calendar and desktop dashboards use the same field names
- **Reusability**: components (`table`, `list-view`, `calendar-view`) work with any model
- **Migration capability**: data can be moved between programs (export/import)
- **Predictability**: masks (`apps/<category>/masks/<program>/api.md`) describe the same API style
- **Automation**: workflows and webhooks access stable paths

## Data domains (decided 2026-11-01)

Every domain has a directory with its own `index.md`; every standard inside it a subdirectory with `description.md` + `storage.md`.

| Domain | Directory | Canonical standard | Further standards |
|--------|-----------|--------------------|-------------------|
| Contacts | [contacts/](contacts/index.md) | JSContact (RFC 9553/9554) ✅ | vCard, jCard, CardDAV |
| Messages | [messages/](messages/index.md) | AS2 `Note`/`Article` ✅ | JMAP, RFC 5322, MLS (⚠️) |
| Appointments | [events/](events/index.md) | JSCalendar (RFC 8984) ✅ | iCalendar, CalDAV, iTIP |
| Geodata | [geodata/](geodata/index.md) | GeoJSON (RFC 7946) ✅ | geo: URI, ISO 19160 |
| Login / accounts | [login/](login/index.md) | OIDC ✅ (2026-11-02), OAuth 6749 ✅, WebAuthn ✅ | SCIM (⚠️), WebFinger, kanidm |
| Identity / Web of Trust | [identity/](identity/index.md) | WoT Spec v0.1.0-draft (VC, DIDComm, did:key) ✅ reviewed | Docking points: AS2 `Relationship`, `publicKey` |
| Profile | [profile/](profile/index.md) | AS2 `Actor` projection onto JSContact ✅ | schema.org `Person` (⚠️) |
| Projects | [projects/](projects/index.md) | ❌ no open data spec – our own work | ISO 21502 (process) ✅, MSPDI (de facto) ✅, JSCalendar `Task` |

**Proposed but not yet decided**: `aufgaben/` (JSCalendar already covers `Task`), `dokumente/` (block structure = the biggest gap), `dateien/`, `verschlagwortung/` (Web Annotation ✅), `kommentare/`, `benachrichtigungen/`, `organisationen/`.

The **envelope** (AS2 + ActivityPub, decisions in [standards.md](standards.md)) is cross-cutting and not a domain of its own.

## Data areas (cross-section)

| File | Content |
|------|---------|
| [standards.md](standards.md) | Which existing standards cover which data area (with evidence and unverified points) |
| [mappings.md](mappings.md) | Our fields ↔ standard fields (initially Contact, Name, headline) |
| [formats.md](formats.md) | Exchange formats (JSON, YAML, TOML, CSV, NDJSON, ICS, VCF, GeoJSON, …) |
| [models.md](models.md) | Standard models (User, Message, Document, Event, Task, Contact, …) |
| [fields.md](fields.md) | Standard fields, types, enums, required fields |
| [conventions.md](conventions.md) | Naming, file structures, versioning, validation, i18n |
| [api.md](api.md) | Unified CRUD pattern, pagination, filters, error format, webhooks |

## Standard models (overview)

| Model | Short description | Category reference |
|-------|-------------------|--------------------|
| **User** | Account with profile, roles, status | all |
| **Team** | Organisation, group, workspace | all |
| **Message** | Chat, comment or mail message | messenger |
| **Document** | Page, post, article with blocks | wiki |
| **Block** | Content element in a Document | components |
| **Event** | Appointment with start, end, participants | calendar |
| **Task** | Task with due date and status | project management |
| **Contact** | Person with contact data and organisation | contact, crm |
| **Location** | Place with address and GeoJSON coordinate | maps |
| **File** | File with storage location, type, size | all |
| **Tag** | Keyword for categorisation | all |
| **Comment** | Comment attached to a resource | all |
| **Notification** | Notification to a user | all |
| **Revision** | Version of a resource | wiki, components |
| **Integration** | Webhook, API key, connector | workflows |

## Data types

| Type | Notation | Example |
|------|----------|---------|
| `string` | Text in `"..."` | `"Anna Weber"` |
| `number` | Integer or decimal number | `42`, `19.99` |
| `boolean` | `true` / `false` | `true` |
| `datetime` | ISO 8601 | `"2026-10-31T06:00:00+01:00"` |
| `date` | `YYYY-MM-DD` | `"2026-10-31"` |
| `duration` | ISO 8601 Duration | `"PT30M"` |
| `enum` | fixed value list | `"active"` |
| `array[]` | list | `["tag-a", "tag-b"]` |
| `object` | nested object | `{ "city": "Berlin" }` |
| `reference` | ID of another model | `"user_01H…" \| User` |
| `markdown` | Markdown text | `"**Important**"` |
| `null` | explicitly empty | `null` |

## Basic rules

1. **IDs are opaque strings** — never interpret them as numbers; internally a ULID, externally the absolute IRI `https://<instance>/<domain>/<ulid>` (decision 3)
2. **Times always with time zone offset** or explicitly `allDay: true`
3. **Empty values are `null`**, not `""` (exception: required text fields)
4. **Enums are lowercase and singular** (`active`, not `Active`)
5. **New fields are additive** — existing fields are never renamed
6. **Every resource carries `id`, `createdAt`, `updatedAt`**
7. **Audience rule:** `to`/`cc`/`bto`/`bcc` control where copies land — they do not replace authorisation of the resource (decision 2)

## Directory structure

```
docs/en/data/
├── index.md            (this file)
├── standards.md        standards register + decisions of 2026-11-01
├── mappings.md         our fields ↔ standard fields
├── formats.md          exchange formats
├── models.md          standard models
├── fields.md           standard fields and types
├── conventions.md     naming and versioning rules
├── api.md              unified API pattern
├── contacts/           ├── index.md └── jscontact/{description,storage}.md
├── messages/           ┐
├── events/             │ every domain:
├── geodata/            │ index.md + description.md
├── login/              │ + technical.md + standards.md
├── identity/           │ + examples.md
├── profile/            │
└── projects/           ┘
```

## See also

- [Components](../components/) — attributes and data types of the UI elements
- [Gestures](../interactions/gestures/) — interaction data (thresholds, callbacks)
- [Animations](../interactions/animations/) — animation attributes and durations
- [Programs](../programs/) — programs with their own `api.md` per mask
- [Desktop masks](../programs/platform/desktop/masks/) — example of API documentation following the pattern
