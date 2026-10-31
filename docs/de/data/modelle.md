# Datenmodelle

Modelle beschreiben, **welche** Daten ein Programm verwaltet. Jedes Modell hat eine Standardform; Programme dürfen Felder ergänzen, aber keine Standardfelder entfernen oder umbenennen.

Legende: ✅ = Pflichtfeld, ➖ = optional, 🔁 = vom System gesetzt.

## User

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---|--------------|
| `id` | string | ✅ 🔁 | Opaque ID, z. B. `user_01HZXA` |
| `username` | string | ✅ | eindeutiger Anmeldename |
| `displayName` | string | ✅ | Anzeigename |
| `email` | string | ✅ | Haupt-E-Mail-Adresse |
| `emailVerified` | boolean | ➖ | Adresse bestätigt? |
| `avatarUrl` | string \| null | ➖ | Bild-URL |
| `roles` | array[] | ✅ | `["admin", "editor"]` |
| `status` | enum | ✅ | `active`, `invited`, `disabled`, `deleted` |
| `locale` | string | ➖ | `de`, `en`, `fr` |
| `timezone` | string | ➖ | IANA, z. B. `Europe/Berlin` |
| `metadata` | object | ➖ | programmeigene Felder |
| `createdAt` | datetime | ✅ 🔁 | Anlagezeitpunkt |
| `updatedAt` | datetime | ✅ 🔁 | Letzte Änderung |
| `deletedAt` | datetime \| null | ➖ | Soft-Delete |

## Team

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---|--------------|
| `id` | string | ✅ 🔁 | `team_01HZXB` |
| `name` | string | ✅ | Team-/Organisationsname |
| `slug` | string | ✅ | URL-Pfad |
| `kind` | enum | ➖ | `workspace`, `org`, `department` |
| `parentId` | reference \| null | ➖ | übergeordnetes Team |
| `memberCount` | number | 🔁 | Mitgliederanzahl |
| `visibility` | enum | ➖ | `private`, `workspace`, `public` |

## Message

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---|--------------|
| `id` | string | ✅ 🔁 | `msg_01HZXC` |
| `channelId` | reference | ✅ | Kanal, Thread oder Mail-Ordner |
| `authorId` | reference (User) | ✅ | Verfasser |
| `body` | markdown | ✅ | Inhalt |
| `bodyFormat` | enum | ➖ | `markdown`, `html`, `plain` |
| `type` | enum | ➖ | `text`, `system`, `file`, `reaction` |
| `replyToId` | reference \| null | ➖ | Bezugsnachricht |
| `threadId` | reference \| null | ➖ | Thread-Wurzel |
| `attachments` | array[] (File) | ➖ | Anhänge |
| `reactions` | array[] | ➖ | `{ emoji, userIds }` |
| `mentions` | array[] | ➖ | erwähnte User-IDs |
| `editedAt` | datetime \| null | ➖ | Bearbeitungszeitpunkt |
| `createdAt` | datetime | ✅ 🔁 | Sendezeitpunkt |

## Document / Page

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---|--------------|
| `id` | string | ✅ 🔁 | `doc_01HZXD` |
| `title` | string | ✅ | Titel |
| `slug` | string | ✅ | URL-Pfad, eindeutig im Space |
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
|------|-----|---|--------------|
| `id` | string | ✅ 🔁 | `blk_01HZXE` |
| `type` | string | ✅ | `text`, `heading`, `image`, `table`, `code`, `callout` |
| `props` | object | ✅ | typabhängige Attribute (siehe `attributes.md` der Komponente) |
| `content` | array[] \| markdown | ➖ | Kind-Blöcke oder Text |
| `order` | number | ✅ 🔁 | Sortierung |
| `align` | enum | ➖ | `left`, `center`, `right` |

## Event

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---|--------------|
| `id` | string | ✅ 🔁 | `evt_01HZXF` |
| `title` | string | ✅ | Termin-Titel |
| `start` | datetime | ✅ | Beginn |
| `end` | datetime | ✅ | Ende |
| `allDay` | boolean | ➖ | Ganztägig? |
| `timezone` | string | ✅ | IANA-Zeitzone |
| `locationId` | reference \| null | ➖ | Ort |
| `attendees` | array[] (User) | ➖ | Teilnehmer mit `response` |
| `recurrenceRule` | string \| null | ➖ | RRULE nach RFC 5545 |
| `calendarId` | reference | ✅ | Kalender |
| `status` | enum | ➖ | `confirmed`, `tentative`, `cancelled` |
| `reminders` | array[] | ➖ | `{ offset: "-PT15M" }` |

## Task

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---|--------------|
| `id` | string | ✅ 🔁 | `task_01HZXG` |
| `title` | string | ✅ | Titel |
| `description` | markdown | ➖ | Beschreibung |
| `status` | enum | ✅ | `open`, `in_progress`, `done`, `archived` |
| `priority` | enum | ➖ | `low`, `normal`, `high`, `urgent` |
| `assigneeIds` | array[] (User) | ➖ | Bearbeiter |
| `dueAt` | datetime \| null | ➖ | Fälligkeit |
| `startAt` | datetime \| null | ➖ | Beginn |
| `progress` | number | ➖ | 0–100 |
| `boardId` | reference | ✅ | Projekt, Board, Liste |
| `order` | number | 🔁 | Position im Board |
| `estimate` | duration \| null | ➖ | Aufwandsschätzung |

## Contact

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---|--------------|
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
|------|-----|---|--------------|
| `id` | string | ✅ 🔁 | `loc_01HZXI` |
| `name` | string | ➖ | Ortsname |
| `street`, `houseNumber` | string | ➖ | Adresse |
| `postalCode`, `city` | string | ➖ | PLZ, Ort |
| `country` | string | ➖ | ISO 3166-alpha-2, z. B. `DE` |
| `lat`, `lng` | number | ➖ | WGS84-Koordinaten |
| `geometry` | object | ➖ | GeoJSON-Objekt |

## File / Media

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---|--------------|
| `id` | string | ✅ 🔁 | `file_01HZXJ` |
| `name` | string | ✅ | Dateiname |
| `mimeType` | string | ✅ | `image/png`, `application/pdf` |
| `size` | number | ✅ 🔁 | Bytes |
| `storage` | enum | ➖ | `local`, `s3`, `webdav`, `nextcloud` |
| `url` | string | 🔁 | Abruf-URL |
| `checksum` | string | ➖ | `sha256:…` |
| `width`, `height` | number | ➖ | bei Bild/Video |
| `duration` | duration | ➖ | bei Audio/Video |
| `uploadedById` | reference (User) | ✅ 🔁 | Hochlader |

## Tag / Label

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---|--------------|
| `id` | string | ✅ 🔁 | `tag_01HZXK` |
| `name` | string | ✅ | Anzeigename |
| `slug` | string | ✅ | maschinenlesbar |
| `color` | string | ➖ | `#2f6fed` |
| `scope` | enum | ➖ | `global`, `category`, `app` |

## Comment

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---|--------------|
| `id` | string | ✅ 🔁 | `cmt_01HZXL` |
| `resourceType` | string | ✅ | `document`, `task`, `event`, `file` |
| `resourceId` | string | ✅ | ID des Objekts |
| `authorId` | reference (User) | ✅ | Verfasser |
| `body` | markdown | ✅ | Inhalt |
| `resolved` | boolean | ➖ | Diskussion erledigt? |

## Notification

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---|--------------|
| `id` | string | ✅ 🔁 | `ntf_01HZXM` |
| `userId` | reference (User) | ✅ | Empfänger |
| `kind` | enum | ✅ | `mention`, `assignment`, `mention_all`, `system` |
| `title` | string | ✅ | Titel |
| `body` | string | ➖ | Kurztext |
| `resourceType` / `resourceId` | string | ✅ | Sprungziel |
| `channel` | enum | ➖ | `inbox`, `email`, `push`, `webhook` |
| `readAt` | datetime \| null | ➖ | Lesezeitpunkt |

## Revision / Version

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---|--------------|
| `id` | string | ✅ 🔁 | `rev_01HZXN` |
| `resourceType` / `resourceId` | string | ✅ | Objekt |
| `number` | number | ✅ | hochzählende Versionsnummer |
| `authorId` | reference (User) | ✅ | Bearbeiter |
| `changes` | array[] | 🔁 | Diff-Felder `{ field, from, to }` |
| `message` | string | ➖ | Änderungskommentar |

## Integration / Webhook

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---|--------------|
| `id` | string | ✅ 🔁 | `int_01HZXO` |
| `kind` | enum | ✅ | `webhook`, `api_key`, `oauth_app`, `connector` |
| `targetUrl` | string | ➖ | bei Webhooks |
| `events` | array[] | ✅ | abonnierte Event-Namen |
| `secret` | string | ➖ | Signatur-Geheimnis |
| `scopes` | array[] | ➖ | Berechtigungen |
| `lastDelivery` | object | 🔁 | `{ status, code, at }` |

## Modell-Beziehungen

```
Team ──< User (Mitglieder, Rollen)
  │
  ├──< Channel ──< Message ──< Comment
  │                 └──< File (Anhänge)
  ├── Space ──< Document ──< Block
  │                 └──< Revision
  ├── Calendar ──< Event ──> Location
  ├── Board ──< Task ──< Comment
  └── Contact ──> Location, ──> User (owner)

User ──< Notification ──> (Document | Task | Event | Message)
Integration ──> events: document.created | task.updated | message.created
```

## Siehe auch

- [Datenformate](formate.md)
- [Standardfelder](felder.md)
- [Konventionen](konventionen.md)
- [Daten-API](api.md)
- [Komponenten](../components/) — `type`-Werte der Blöcke
