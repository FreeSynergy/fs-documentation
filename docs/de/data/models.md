# Datenmodelle

Modelle beschreiben, **welche** Daten ein Programm verwaltet. Jedes Modell hat eine Standardform. Programme dürfen Felder ergänzen, aber keine Standardfelder entfernen oder umbenennen.

Legende: ✅ = Pflichtfeld, ➖ = optional, 🔁 = vom System gesetzt.

## User

| Feld | Typ | Pflicht | Beschreibung |
|-------|------|---|-------------|
| `id` | string | ✅ 🔁 | undurchsichtige ID, z. B. `user_01HZXA` |
| `username` | string | ✅ | eindeutiger Anmeldename |
| `displayName` | string | ✅ | Anzeigename |
| `email` | string | ✅ | Haupt-E-Mail-Adresse |
| `emailVerified` | boolean | ➖ | Adresse bestätigt? |
| `avatarUrl` | string \| null | ➖ | Bild-URL |
| `roles` | array[] | ✅ | `["admin", "editor"]` |
| `status` | enum | ✅ | `active`, `invited`, `disabled`, `deleted` |
| `locale` | string | ➖ | `de`, `en`, `fr` |
| `timezone` | string | ➖ | IANA, z. B. `Europe/Berlin` |
| `metadata` | object | ➖ | programmspezifische Felder |
| `createdAt` | datetime | ✅ 🔁 | Zeitpunkt der Anlage |
| `updatedAt` | datetime | ✅ 🔁 | letzte Änderung |
| `deletedAt` | datetime \| null | ➖ | Soft-Delete |

## Team

| Feld | Typ | Pflicht | Beschreibung |
|-------|------|---|-------------|
| `id` | string | ✅ 🔁 | `team_01HZXB` |
| `name` | string | ✅ | Name des Teams/der Organisation |
| `slug` | string | ✅ | URL-Pfad |
| `kind` | enum | ➖ | `workspace`, `org`, `department` |
| `parentId` | reference \| null | ➖ | übergeordnetes Team |
| `memberCount` | number | 🔁 | Anzahl der Mitglieder |
| `visibility` | enum | ➖ | `private`, `workspace`, `public` |

## Message

| Feld | Typ | Pflicht | Beschreibung |
|-------|------|---|-------------|
| `id` | string | ✅ 🔁 | `msg_01HZXC` |
| `channelId` | reference | ✅ | Kanal, Thread oder Mail-Ordner |
| `authorId` | reference (User) | ✅ | Verfasser |
| `body` | markdown | ✅ | Inhalt |
| `bodyFormat` | enum | ➖ | `markdown`, `html`, `plain` |
| `type` | enum | ➖ | `text`, `system`, `file`, `reaction` |
| `replyToId` | reference \| null | ➖ | bezogene Nachricht |
| `threadId` | reference \| null | ➖ | Wurzel des Threads |
| `attachments` | array[] (File) | ➖ | Anhänge |
| `reactions` | array[] | ➖ | `{ emoji, userIds }` |
| `mentions` | array[] | ➖ | erwähnte User-IDs |
| `editedAt` | datetime \| null | ➖ | Zeitpunkt der Bearbeitung |
| `createdAt` | datetime | ✅ 🔁 | Zeitpunkt des Versands |

## Dokument / Seite

| Feld | Typ | Pflicht | Beschreibung |
|-------|------|---|-------------|
| `id` | string | ✅ 🔁 | `doc_01HZXD` |
| `title` | string | ✅ | Titel |
| `slug` | string | ✅ | URL-Pfad, eindeutig innerhalb des Space |
| `spaceId` | reference | ✅ | Wiki-Bereich / Buch |
| `blocks` | array[] (Block) | ✅ | Inhalt als Blöcke |
| `status` | enum | ✅ | `draft`, `published`, `archived` |
| `currentRevision` | number | 🔁 | aktuelle Version |
| `authorId` | reference (User) | ✅ 🔁 | Ersteller |
| `lastEditorId` | reference (User) | 🔁 | letzte Bearbeitung |
| `tags` | array[] (Tag) | ➖ | Schlagwörter |
| `parentDocId` | reference \| null | ➖ | übergeordnete Seite |
| `visibility` | enum | ➖ | `public`, `workspace`, `private` |
| `publishedAt` | datetime \| null | ➖ | Veröffentlichung |

## Block

Inhaltsbaustein eines Dokuments. `type` entspricht den [Komponenten](../components/).

| Feld | Typ | Pflicht | Beschreibung |
|-------|------|---|-------------|
| `id` | string | ✅ 🔁 | `blk_01HZXE` |
| `type` | string | ✅ | `text`, `heading`, `image`, `table`, `code`, `callout` |
| `props` | object | ✅ | typabhängige Attribute (siehe `attributes.md` der Komponente) |
| `content` | array[] \| markdown | ➖ | Kind-Blöcke oder Text |
| `order` | number | ✅ 🔁 | Sortierung |
| `align` | enum | ➖ | `left`, `center`, `right` |

## Event

| Feld | Typ | Pflicht | Beschreibung |
|-------|------|---|-------------|
| `id` | string | ✅ 🔁 | `evt_01HZXF` |
| `title` | string | ✅ | Titel des Termins |
| `start` | datetime | ✅ | Beginn |
| `end` | datetime | ✅ | Ende |
| `allDay` | boolean | ➖ | ganztägig? |
| `timezone` | string | ✅ | IANA-Zeitzone |
| `locationId` | reference \| null | ➖ | Ort |
| `attendees` | array[] (User) | ➖ | Teilnehmende mit `response` |
| `recurrenceRule` | string \| null | ➖ | RRULE nach RFC 5545 |
| `calendarId` | reference | ✅ | Kalender |
| `status` | enum | ➖ | `confirmed`, `tentative`, `cancelled` |
| `reminders` | array[] | ➖ | `{ offset: "-PT15M" }` |

## Task

| Feld | Typ | Pflicht | Beschreibung |
|-------|------|---|-------------|
| `id` | string | ✅ 🔁 | `task_01HZXG` |
| `title` | string | ✅ | Titel |
| `description` | markdown | ➖ | Beschreibung |
| `status` | enum | ✅ | `open`, `in_progress`, `done`, `archived` |
| `priority` | enum | ➖ | `low`, `normal`, `high`, `urgent` |
| `assigneeIds` | array[] (User) | ➖ | Zuständige |
| `dueAt` | datetime \| null | ➖ | Fälligkeit |
| `startAt` | datetime \| null | ➖ | Beginn |
| `progress` | number | ➖ | 0–100 |
| `boardId` | reference | ✅ | Projekt, Board, Liste |
| `order` | number | 🔁 | Position auf dem Board |
| `estimate` | duration \| null | ➖ | Aufwandsschätzung |

## Contact

| Feld | Typ | Pflicht | Beschreibung |
|-------|------|---|-------------|
| `id` | string | ✅ 🔁 | `con_01HZXH` |
| `firstName` | string | ✅ | Vorname |
| `lastName` | string | ✅ | Nachname |
| `displayName` | string | 🔁 | zusammengesetzt |
| `emails` | array[] | ➖ | `{ type, value }` |
| `phones` | array[] | ➖ | `{ type, value }` (E.164) |
| `organization` | string \| null | ➖ | Firma |
| `jobTitle` | string \| null | ➖ | Rolle im Unternehmen |
| `addresses` | array[] (Location) | ➖ | Adressen |
| `ownerId` | reference (User) | ➖ | Besitzer des Datensatzes |
| `lifecycle` | enum | ➖ | `lead`, `prospect`, `customer`, `churned` |

## Location

| Feld | Typ | Pflicht | Beschreibung |
|-------|------|---|-------------|
| `id` | string | ✅ 🔁 | `loc_01HZXI` |
| `name` | string | ➖ | Ortsname |
| `street`, `houseNumber` | string | ➖ | Adresse |
| `postalCode`, `city` | string | ➖ | Postleitzahl, Ort |
| `country` | string | ➖ | ISO 3166-alpha-2, z. B. `DE` |
| `lat`, `lng` | number | ➖ | WGS84-Koordinaten |
| `geometry` | object | ➖ | GeoJSON-Objekt |

## Datei / Medien

| Feld | Typ | Pflicht | Beschreibung |
|-------|------|---|-------------|
| `id` | string | ✅ 🔁 | `file_01HZXJ` |
| `name` | string | ✅ | Dateiname |
| `mimeType` | string | ✅ | `image/png`, `application/pdf` |
| `size` | number | ✅ 🔁 | Bytes |
| `storage` | enum | ➖ | `local`, `s3`, `webdav`, `nextcloud` |
| `url` | string | 🔁 | Abruf-URL |
| `checksum` | string | ➖ | `sha256:…` |
| `width`, `height` | number | ➖ | für Bild/Video |
| `duration` | duration | ➖ | für Audio/Video |
| `uploadedById` | reference (User) | ✅ 🔁 | Hochladende Person |

## Tag / Label

| Feld | Typ | Pflicht | Beschreibung |
|-------|------|---|-------------|
| `id` | string | ✅ 🔁 | `tag_01HZXK` |
| `name` | string | ✅ | Anzeigename |
| `slug` | string | ✅ | maschinenlesbar |
| `color` | string | ➖ | `#2f6fed` |
| `scope` | enum | ➖ | `global`, `category`, `app` |

## Comment

| Feld | Typ | Pflicht | Beschreibung |
|-------|------|---|-------------|
| `id` | string | ✅ 🔁 | `cmt_01HZXL` |
| `resourceType` | string | ✅ | `document`, `task`, `event`, `file` |
| `resourceId` | string | ✅ | ID des Objekts |
| `authorId` | reference (User) | ✅ | Verfasser |
| `body` | markdown | ✅ | Inhalt |
| `resolved` | boolean | ➖ | Diskussion erledigt? |

## Notification

| Feld | Typ | Pflicht | Beschreibung |
|-------|------|---|-------------|
| `id` | string | ✅ 🔁 | `ntf_01HZXM` |
| `userId` | reference (User) | ✅ | Empfänger |
| `kind` | enum | ✅ | `mention`, `assignment`, `mention_all`, `system` |
| `title` | string | ✅ | Titel |
| `body` | string | ➖ | kurzer Text |
| `resourceType` / `resourceId` | string | ✅ | Sprungziel |
| `channel` | enum | ➖ | `inbox`, `email`, `push`, `webhook` |
| `readAt` | datetime \| null | ➖ | Zeitpunkt des Lesens |

## Revision / Version

| Feld | Typ | Pflicht | Beschreibung |
|-------|------|---|-------------|
| `id` | string | ✅ 🔁 | `rev_01HZXN` |
| `resourceType` / `resourceId` | string | ✅ | Objekt |
| `number` | number | ✅ | fortlaufende Versionsnummer |
| `authorId` | reference (User) | ✅ | Bearbeiter |
| `changes` | array[] | 🔁 | Diff-Felder `{ field, from, to }` |
| `message` | string | ➖ | Kommentar zur Änderung |

## Integration / Webhook

| Feld | Typ | Pflicht | Beschreibung |
|-------|------|---|-------------|
| `id` | string | ✅ 🔁 | `int_01HZXO` |
| `kind` | enum | ✅ | `webhook`, `api_key`, `oauth_app`, `connector` |
| `targetUrl` | string | ➖ | für Webhooks |
| `events` | array[] | ✅ | abonnierte Event-Namen |
| `secret` | string | ➖ | Signatur-Geheimnis |
| `scopes` | array[] | ➖ | Berechtigungen |
| `lastDelivery` | object | 🔁 | `{ status, code, at }` |

## Beziehungen zwischen Modellen

```
Team ──< User (Mitglieder, Rollen)
  │
  ├──< Channel ──< Message ──< Comment
  │                 └──< File (Anhänge)
  ├── Space ──< Document ──< Block
  │                 └──< Revision
  ├── Calendar ──< Event ──> Location
  ├── Board ──< Task ──< Comment
  └── Contact ──> Location, ──> User (Besitzer)

User ──< Notification ──> (Document | Task | Event | Message)
Integration ──> events: document.created | task.updated | message.created
```

## Siehe auch

- [Datenformate](formats.md)
- [Standardfelder](fields.md)
- [Konventionen](conventions.md)
- [Daten-API](api.md)
- [Komponenten](../components/) — die `type`-Werte der Blöcke
