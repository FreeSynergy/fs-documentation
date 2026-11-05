# Data models

Models describe **which** data a program manages. Every model has a standard form; programs may add fields but may not remove or rename standard fields.

Legend: ✅ = required field, ➖ = optional, 🔁 = set by the system.

## User

| Field | Type | Required | Description |
|-------|------|---|-------------|
| `id` | string | ✅ 🔁 | opaque ID, e.g. `user_01HZXA` |
| `username` | string | ✅ | unique login name |
| `displayName` | string | ✅ | display name |
| `email` | string | ✅ | main email address |
| `emailVerified` | boolean | ➖ | address confirmed? |
| `avatarUrl` | string \| null | ➖ | image URL |
| `roles` | array[] | ✅ | `["admin", "editor"]` |
| `status` | enum | ✅ | `active`, `invited`, `disabled`, `deleted` |
| `locale` | string | ➖ | `de`, `en`, `fr` |
| `timezone` | string | ➖ | IANA, e.g. `Europe/Berlin` |
| `metadata` | object | ➖ | program-specific fields |
| `createdAt` | datetime | ✅ 🔁 | time of creation |
| `updatedAt` | datetime | ✅ 🔁 | last change |
| `deletedAt` | datetime \| null | ➖ | soft delete |

## Team

| Field | Type | Required | Description |
|-------|------|---|-------------|
| `id` | string | ✅ 🔁 | `team_01HZXB` |
| `name` | string | ✅ | team/organisation name |
| `slug` | string | ✅ | URL path |
| `kind` | enum | ➖ | `workspace`, `org`, `department` |
| `parentId` | reference \| null | ➖ | parent team |
| `memberCount` | number | 🔁 | number of members |
| `visibility` | enum | ➖ | `private`, `workspace`, `public` |

## Message

| Field | Type | Required | Description |
|-------|------|---|-------------|
| `id` | string | ✅ 🔁 | `msg_01HZXC` |
| `channelId` | reference | ✅ | channel, thread or mail folder |
| `authorId` | reference (User) | ✅ | author |
| `body` | markdown | ✅ | content |
| `bodyFormat` | enum | ➖ | `markdown`, `html`, `plain` |
| `type` | enum | ➖ | `text`, `system`, `file`, `reaction` |
| `replyToId` | reference \| null | ➖ | referenced message |
| `threadId` | reference \| null | ➖ | thread root |
| `attachments` | array[] (File) | ➖ | attachments |
| `reactions` | array[] | ➖ | `{ emoji, userIds }` |
| `mentions` | array[] | ➖ | mentioned user IDs |
| `editedAt` | datetime \| null | ➖ | time of editing |
| `createdAt` | datetime | ✅ 🔁 | time of sending |

## Document / page

| Field | Type | Required | Description |
|-------|------|---|-------------|
| `id` | string | ✅ 🔁 | `doc_01HZXD` |
| `title` | string | ✅ | title |
| `slug` | string | ✅ | URL path, unique within the space |
| `spaceId` | reference | ✅ | wiki area / book |
| `blocks` | array[] (Block) | ✅ | content as blocks |
| `status` | enum | ✅ | `draft`, `published`, `archived` |
| `currentRevision` | number | 🔁 | current version |
| `authorId` | reference (User) | ✅ 🔁 | creator |
| `lastEditorId` | reference (User) | 🔁 | last edit |
| `tags` | array[] (Tag) | ➖ | keywords |
| `parentDocId` | reference \| null | ➖ | parent page |
| `visibility` | enum | ➖ | `public`, `workspace`, `private` |
| `publishedAt` | datetime \| null | ➖ | publication |

## Block

Content building block of a document. `type` corresponds to the [components](../components/).

| Field | Type | Required | Description |
|-------|------|---|-------------|
| `id` | string | ✅ 🔁 | `blk_01HZXE` |
| `type` | string | ✅ | `text`, `heading`, `image`, `table`, `code`, `callout` |
| `props` | object | ✅ | type-dependent attributes (see the component's `attributes.md`) |
| `content` | array[] \| markdown | ➖ | child blocks or text |
| `order` | number | ✅ 🔁 | sorting |
| `align` | enum | ➖ | `left`, `center`, `right` |

## Event

| Field | Type | Required | Description |
|-------|------|---|-------------|
| `id` | string | ✅ 🔁 | `evt_01HZXF` |
| `title` | string | ✅ | appointment title |
| `start` | datetime | ✅ | beginning |
| `end` | datetime | ✅ | end |
| `allDay` | boolean | ➖ | all-day? |
| `timezone` | string | ✅ | IANA time zone |
| `locationId` | reference \| null | ➖ | place |
| `attendees` | array[] (User) | ➖ | participants with `response` |
| `recurrenceRule` | string \| null | ➖ | RRULE per RFC 5545 |
| `calendarId` | reference | ✅ | calendar |
| `status` | enum | ➖ | `confirmed`, `tentative`, `cancelled` |
| `reminders` | array[] | ➖ | `{ offset: "-PT15M" }` |

## Task

| Field | Type | Required | Description |
|-------|------|---|-------------|
| `id` | string | ✅ 🔁 | `task_01HZXG` |
| `title` | string | ✅ | title |
| `description` | markdown | ➖ | description |
| `status` | enum | ✅ | `open`, `in_progress`, `done`, `archived` |
| `priority` | enum | ➖ | `low`, `normal`, `high`, `urgent` |
| `assigneeIds` | array[] (User) | ➖ | assignees |
| `dueAt` | datetime \| null | ➖ | due date |
| `startAt` | datetime \| null | ➖ | start |
| `progress` | number | ➖ | 0–100 |
| `boardId` | reference | ✅ | project, board, list |
| `order` | number | 🔁 | position on the board |
| `estimate` | duration \| null | ➖ | effort estimate |

## Contact

| Field | Type | Required | Description |
|-------|------|---|-------------|
| `id` | string | ✅ 🔁 | `con_01HZXH` |
| `firstName` | string | ✅ | first name |
| `lastName` | string | ✅ | last name |
| `displayName` | string | 🔁 | composed |
| `emails` | array[] | ➖ | `{ type, value }` |
| `phones` | array[] | ➖ | `{ type, value }` (E.164) |
| `organization` | string \| null | ➖ | company |
| `jobTitle` | string \| null | ➖ | role in the company |
| `addresses` | array[] (Location) | ➖ | addresses |
| `ownerId` | reference (User) | ➖ | owner of the record |
| `lifecycle` | enum | ➖ | `lead`, `prospect`, `customer`, `churned` |

## Location

| Field | Type | Required | Description |
|-------|------|---|-------------|
| `id` | string | ✅ 🔁 | `loc_01HZXI` |
| `name` | string | ➖ | place name |
| `street`, `houseNumber` | string | ➖ | address |
| `postalCode`, `city` | string | ➖ | postcode, city |
| `country` | string | ➖ | ISO 3166-alpha-2, e.g. `DE` |
| `lat`, `lng` | number | ➖ | WGS84 coordinates |
| `geometry` | object | ➖ | GeoJSON object |

## File / media

| Field | Type | Required | Description |
|-------|------|---|-------------|
| `id` | string | ✅ 🔁 | `file_01HZXJ` |
| `name` | string | ✅ | file name |
| `mimeType` | string | ✅ | `image/png`, `application/pdf` |
| `size` | number | ✅ 🔁 | bytes |
| `storage` | enum | ➖ | `local`, `s3`, `webdav`, `nextcloud` |
| `url` | string | 🔁 | retrieval URL |
| `checksum` | string | ➖ | `sha256:…` |
| `width`, `height` | number | ➖ | for image/video |
| `duration` | duration | ➖ | for audio/video |
| `uploadedById` | reference (User) | ✅ 🔁 | uploader |

## Tag / label

| Field | Type | Required | Description |
|-------|------|---|-------------|
| `id` | string | ✅ 🔁 | `tag_01HZXK` |
| `name` | string | ✅ | display name |
| `slug` | string | ✅ | machine-readable |
| `color` | string | ➖ | `#2f6fed` |
| `scope` | enum | ➖ | `global`, `category`, `app` |

## Comment

| Field | Type | Required | Description |
|-------|------|---|-------------|
| `id` | string | ✅ 🔁 | `cmt_01HZXL` |
| `resourceType` | string | ✅ | `document`, `task`, `event`, `file` |
| `resourceId` | string | ✅ | ID of the object |
| `authorId` | reference (User) | ✅ | author |
| `body` | markdown | ✅ | content |
| `resolved` | boolean | ➖ | discussion resolved? |

## Notification

| Field | Type | Required | Description |
|-------|------|---|-------------|
| `id` | string | ✅ 🔁 | `ntf_01HZXM` |
| `userId` | reference (User) | ✅ | recipient |
| `kind` | enum | ✅ | `mention`, `assignment`, `mention_all`, `system` |
| `title` | string | ✅ | title |
| `body` | string | ➖ | short text |
| `resourceType` / `resourceId` | string | ✅ | jump target |
| `channel` | enum | ➖ | `inbox`, `email`, `push`, `webhook` |
| `readAt` | datetime \| null | ➖ | time read |

## Revision / version

| Field | Type | Required | Description |
|-------|------|---|-------------|
| `id` | string | ✅ 🔁 | `rev_01HZXN` |
| `resourceType` / `resourceId` | string | ✅ | object |
| `number` | number | ✅ | incrementing version number |
| `authorId` | reference (User) | ✅ | editor |
| `changes` | array[] | 🔁 | diff fields `{ field, from, to }` |
| `message` | string | ➖ | change comment |

## Integration / webhook

| Field | Type | Required | Description |
|-------|------|---|-------------|
| `id` | string | ✅ 🔁 | `int_01HZXO` |
| `kind` | enum | ✅ | `webhook`, `api_key`, `oauth_app`, `connector` |
| `targetUrl` | string | ➖ | for webhooks |
| `events` | array[] | ✅ | subscribed event names |
| `secret` | string | ➖ | signing secret |
| `scopes` | array[] | ➖ | permissions |
| `lastDelivery` | object | 🔁 | `{ status, code, at }` |

## Model relations

```
Team ──< User (members, roles)
  │
  ├──< Channel ──< Message ──< Comment
  │                 └──< File (attachments)
  ├── Space ──< Document ──< Block
  │                 └──< Revision
  ├── Calendar ──< Event ──> Location
  ├── Board ──< Task ──< Comment
  └── Contact ──> Location, ──> User (owner)

User ──< Notification ──> (Document | Task | Event | Message)
Integration ──> events: document.created | task.updated | message.created
```

## See also

- [data formats](formats.md)
- [standard fields](fields.md)
- [conventions](conventions.md)
- [data API](api.md)
- [components](../components/) — the `type` values of the blocks
