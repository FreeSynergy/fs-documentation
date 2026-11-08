# Map of the programs

**Status: draft (2026-11-08); the layers and the four frontends are decided (ADR 0066, 2026-11-09), the program table is still open.** This page puts every program, facet and suite in
one place, together with the data types each one owns and the frontends it gets. It is the starting point of round 3:
first we agree on this map, then on the data types and interfaces, and only then do we build.

## The layers, from the bottom up

| Layer | What it is | Who defines it |
|-------|------------|----------------|
| **Basic type** | A small value with fixed rules: e-mail address, phone number, name, address, date. Same everywhere. | Once, for all programs |
| **Data type** | A thing made of basic types, owned by exactly one program: `Person`, `Event`, `Task`. Follows a standard. | The owning program (ADR 0050) |
| **Interface** | What a program can do with its data types: commands such as create, change, find, suggest. | The owning program |
| **Component** | Each basic type has fixed components: *input*, *display*, *compact* (in a line), *cell* (in a list). A data type gets its components from its basic types. | Once, in `fs-components` |
| **Style** | The look: spacing, corners, glass or solid, fonts, **an icon set of our own**. Reusable by any frontend. | Once per style, 5–10 in total |
| **Frontend** | One way to use a program or facet, built from components in one style. | Per program or facet |
| **Facet** | A part of a program that looks like an app of its own (ADR 0061). | The program |
| **Suite** | Several programs together for one purpose. | Across programs |

The backend announces, for each data type, its fields, their basic types and its commands. A frontend never decides
what an e-mail address is; it only decides where it shows the e-mail component.

## Four frontends for every program (ADR 0066)

| Frontend | Purpose | Built how |
|----------|---------|-----------|
| **Admin** | Every field, every setting, every command. The safety net. | Generated from the data type description, the same code for all programs |
| **Simple** | For people with little experience: few buttons, large, clear. | By hand, one style for all programs |
| **Apple style** | Rebuilt to measure after Apple's design language: spacing, line heights, font sizes, corners, glass, layout. | By hand, from a measurement sheet |
| **Windows style** | The same after Microsoft's Fluent design: flat surfaces, its spacing and corners. | By hand, from a measurement sheet |

The measurement sheets come from the public guidelines (Apple Human Interface Guidelines, Microsoft Fluent 2) and from
screenshots of the platforms' own apps that stay local and are never published. The exact rebuild also tests what the
GUI engine can do. Our own icons, texts and open fonts with similar measurements; none of theirs.

The analyses of well-known programs per category (`frontends/<program>/latest/`) stay the source for **functions**.

## Basic types (first list)

| Basic type | Standard | Used by |
|------------|----------|---------|
| Text, multi-line text | – | all |
| Formatted text | RFC 9073 `STYLED-DESCRIPTION`, own text model (ADR 0031) | wiki, tasks, messages |
| E-mail address | RFC 5322, JSContact `EmailAddress` | people, messenger, identity, groups |
| Phone number | E.164, JSContact `Phone` | people |
| Online service, handle | JSContact `OnlineService` | people, messenger |
| Link | RFC 3986, JSContact `Link` | all |
| Name of a person | JSContact `Name` with `components[]` | people, identity |
| Postal address | JSContact `Address` | people, maps, resources |
| Place | `geo:` URI (RFC 5870), GeoJSON | maps, calendar, people, files |
| Date, date and time, time zone | RFC 3339, JSCalendar `LocalDateTime`, IANA zones | calendar, tasks, history |
| Duration, recurrence | JSCalendar `Duration`, `RecurrenceRule` | calendar, tasks |
| Language | BCP 47 (RFC 5646) | all |
| Quantity, money | UCUM, ISO 4217 | resources |
| Colour | CSS Color 4 | all |
| Picture, sound, video | AS2 `Image`/`Audio`/`Video`, media types | people, files, messenger |
| Public key | OpenPGP fingerprint, JSContact `CryptoKey` | people, identity |
| Status, priority, choice | JSCalendar enums, own lists | tasks, surveys |
| Keywords | JSContact `keywords`, JSCalendar `keywords` | all |
| Reference to an object | AS2 `id` (IRI) | all; shows the target's *compact* component |

## Programs

| Program | Owns (standard) | Uses | Facets (proposed) | Suites | Analysed programs (functions) |
|---------|-----------------|------|-------------------|--------|-------------------------------|
| `fs-people` | `Person` (JSContact `Card`) | groups, files | Contacts, Users, AIs, Partners, Team, Members | Groupware, CRM, Democracy | GNOME Contacts, KAddressBook, Monica, Nextcloud Contacts |
| `fs-groups` | `Group`, membership (AS2, SCIM) | people | Groups | all | **none analysed** |
| identity (`fs-identity`) | account, sign-in (Kanidm wrapper) | people | Users (with people) | all | **none analysed** |
| `fs-messenger` | `Message`, conversation (AS2, JMAP Mail, MIMI) | people, files | Mail, Chat, Assistant, possibly Forum | Groupware, CRM, Helpdesk | Thunderbird, Element, Telegram, Kontact, Apple Mail, Outlook, Discord, Mastodon |
| `fs-calendar` | `Event` (JSCalendar) | people, maps, resources | Calendar, Booking | Groupware, Project mgmt | Merkuro, Google Calendar, Nextcloud Calendar, Outlook Calendar, Planner, DAViCal |
| `fs-tasks` | `Task` (JSCalendar, RFC 9253) | people, calendar, groups | To-dos, Tickets | Project mgmt, Helpdesk | Planka, OpenProject, Taiga, Trello, Wekan, Redmine, Jira, Asana |
| `fs-files` | `Document`, file (AS2) | people, groups | Files, Gallery, Music, Videos, Documents | Media, all | Nautilus, Dolphin, Seafile, Nextcloud Files; gallery: Immich, PhotoPrism, Lychee, Piwigo |
| `fs-wiki` | text, page (own spec, ADR 0031) | files, people | Wiki, Notes | Groupware, Democracy | Wiki.js, MediaWiki, XWiki, Notion, Confluence |
| `fs-maps` | place (GeoJSON) | people, calendar | Maps | Groupware | Organic Maps, OsmAnd, uMap, QGIS |
| `fs-history` | activity (AS2) | all | Timeline | Project mgmt | **none analysed** |
| `fs-resources` | resource, need (gap, own spec) | people, calendar | Inventory, Booking (with calendar) | ERP, Project mgmt, Democracy | ERP: Dolibarr, ERPNext, Odoo, Tryton |
| `fs-surveys` | `Question`, vote (AS2, gap) | people, groups | Polls, Votes | Democracy, Project mgmt | Decidim, Polis, LiquidFeedback, Consul, adhocracy+ |
| `fs-whiteboard` | board (gap, own spec) | files | Whiteboard | Project mgmt | Excalidraw, tldraw, draw.io, OpenBoard |
| `fs-streaming` | stream (WHIP/WHEP) | files | Studio, Live | Media | OBS Studio, Restreamer, MediaMTX |
| `fs-store` (the store) | catalog entry, package (TUF) | – | Store | – | **none analysed** |
| desktop | – (start page, uses all) | all | Start | – | Homarr, Dashy, Homepage, Heimdall |

Platform without its own frontend: `fs-objects` (keeping objects), `fs-hub` (sharing between programs on a device),
`fs-interfaces` (contracts), `fs-components` (components and styles), `fs-release`, `fs-capnpc`.

## Suites

| Suite | Programs |
|-------|----------|
| Groupware | people, messenger, calendar, wiki, maps, files |
| Project management | tasks, history, resources, surveys, whiteboard, wiki, groups |
| Democracy | surveys, groups, wiki, messenger, tasks, resources |
| Helpdesk | tasks (Tickets), messenger, people, wiki — analysed: Zammad, osTicket, GLPI, Request Tracker |
| CRM | people (Partners), messenger, tasks, calendar — analysed: EspoCRM, SuiteCRM, CiviCRM |
| ERP | resources, people, tasks — analysed: Dolibarr, ERPNext, Odoo |
| Media | files (Gallery), streaming |
| Marketplace | later |

## Open points of this draft

1. **Marketing** (analysed: Matomo, Plausible, Mautic): own program with its own data, or a suite over messenger and
   people?
2. **Workflows** (analysed: n8n, Node-RED): a program that owns workflow definitions (candidate standard: CNCF
   Serverless Workflow, BPMN), or later?
3. **Helpdesk**: suite as proposed above, or own program?
4. **Groups, identity, history, store**: no reference programs analysed yet; Haiku researches candidates.
5. **Styles**: the first four are fixed by the frontends: *Admin* (dense), *Simple* (large), *Apple* (round corners,
   glass), *Windows* (flat, Fluent spacing). Each with an icon set of our own. More can follow.
