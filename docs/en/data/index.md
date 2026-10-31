# Standardized Data

Standardized data describe in which **formats**, **models**, and **fields** FreeSynergy programs, components, and skins exchange information.

## Why Standardization?

- **Interoperability**: Messenger, wiki, calendar, and desktop dashboards use the same field names
- **Reusability**: Components (`table`, `list-view`, `calendar-view`) work with any model
- **Migration capability**: Data can be moved between programs (export/import)
- **Predictability**: Skins (`apps/<category>/skins/<program>/api.md`) describe the same API style
- **Automation**: Workflows and webhooks access stable paths

## Data Areas

| File | Content |
|------|---------|
| `formate.md` | Exchange formats (JSON, YAML, TOML, CSV, NDJSON, ICS, VCF, GeoJSON, …) |
| `modelle.md` | Standard models (User, Message, Document, Event, Task, Contact, …) |
| `felder.md` | Standard fields, types, enums, required fields |
| `konventionen.md` | Naming, file structures, versioning, validation, i18n |
| `api.md` | Unified CRUD pattern, pagination, filters, error format, webhooks |

## Standard Models (overview)

| Model | Short description | Category reference |
|-------|-------------------|--------------------|
| **User** | Account with profile, roles, status | all |
| **Team** | Organization, group, workspace | all |
| **Message** | Chat, comment, or mail message | messenger |
| **Document** | Page, post, article with blocks | wiki |
| **Block** | Content element in a Document | components |
| **Event** | Appointment with start, end, participants | kalender |
| **Task** | Task with due date and status | projektmanagement |
| **Contact** | Person with contact data and organization | kontakt, crm |
| **Location** | Place with address and GeoJSON coordinate | maps |
| **File** | File with storage location, type, size | all |
| **Tag** | Keyword for categorization | all |
| **Comment** | Comment attached to a resource | all |
| **Notification** | Notification to a user | all |
| **Revision** | Version of a resource | wiki, components |
| **Integration** | Webhook, API key, connector | workflows |

## Data Types

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

## Basic Rules

1. **IDs are opaque strings** — never interpret them as numbers
2. **Times always with time zone offset** or explicitly `allDay: true`
3. **Empty values are `null`**, not `""` (exception: required text fields)
4. **Enums are lowercase and singular** (`active`, not `Active`)
5. **New fields are additive** — existing fields are never renamed
6. **Every resource carries `id`, `createdAt`, `updatedAt`**

## Directory Structure

```
docs/en/data/
├── index.md            (this file)
├── formate.md          Exchange formats
├── modelle.md          Standard models
├── felder.md           Standard fields and types
├── konventionen.md     Naming and versioning rules
└── api.md              unified API pattern
```

## See also

- [Gestures](../gestures/index.md) — interaction data (thresholds, callbacks)
- [Animations](../animations/index.md) — animation attributes and durations
- [Wiki](../apps/wiki/index.md) — program with its own skins
- [Messenger](../apps/messenger/index.md) — program with its own skins
