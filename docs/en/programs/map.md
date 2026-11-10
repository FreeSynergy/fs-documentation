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
| **Admin** | Every field, every setting, every command. The safety net. Looks like SAP Fiori (a public design system for dense business data). | Generated from the data type description, the same code for all programs |
| **Simple** | For people with little experience: few buttons, large, clear. | By hand, one style for all programs |
| **Apple style** | Rebuilt to measure after Apple's design language: spacing, line heights, font sizes, corners, glass, layout. | By hand, from a measurement sheet |
| **Windows style** | The same after Microsoft's Fluent design: flat surfaces, its spacing and corners. | By hand, from a measurement sheet |

The measurement sheets come from the public guidelines (Apple Human Interface Guidelines, Microsoft Fluent 2) and from
screenshots of the platforms' own apps that stay local and are never published. The exact rebuild also tests what the
GUI engine can do. Our own icons, texts and open fonts with similar measurements; none of theirs.

Apple style uses Apple's own apps as the template: rebuilt 1:1 first, then filled with functions, changed later if
needed. Windows style is also rebuilt 1:1, one Windows program per category, preferably one that does not exist on Linux,
so everyone profits from it in open software. Deliberately no Linux programs as templates: we have those already. Later a **FreeSynergy style** of our own, quite different from all of these (ADR 0066,
addition of 2026-11-09).

The analyses of well-known programs per category (`frontends/<program>/latest/`) stay the source for **functions**.

## Windows templates (approved by the owner, 2026-11-10)

The Windows style is rebuilt 1:1 from one Windows program per category, preferably one without a Linux counterpart.
No Linux program is a template. Measures and sources: `docs/en/components/styles/windows.md`.

| Category (program or facet) | Windows program | Notes |
|-----------------------------|-----------------|-------|
| People | Outlook | People view of the new Outlook for Windows |
| Mail (messenger) | Outlook | Mail module of the new Outlook |
| Calendar | Outlook | Calendar module of the new Outlook |
| Groups | Microsoft Teams | |
| Tasks | Microsoft To Do | |
| Files | File Explorer | |
| Gallery (facet of files) | Photos | Microsoft Photos |
| Videos | Media Player | Check which of the two players is meant: the new Media Player app, or Windows Media Player Legacy (optional feature) |
| Wiki | OneNote | |
| Maps | Google Earth | Google Earth Pro for Windows. Street View gets no frontend of its own |
| Whiteboard | Microsoft Whiteboard | **Open:** Microsoft's support page says the standalone Whiteboard apps for Windows retire on 2026-10-16 (Whiteboard stays in Teams and on the web, for work and school accounts). Needs a decision before the rebuild |
| Surveys | Microsoft Forms | **Open:** Forms is a web service without a Windows app |
| Resources | Excel | |
| Streaming | YouTube Studio | **Open:** YouTube Studio is a web service without a Windows app; its Live Control Room is the reference |
| Store | Microsoft Store | |
| Start | Start menu and Widgets | |
| Identity | Settings > Accounts, plus Windows Hello | A settings page, not a program |
| History | none | No template |

**Rule for templates (owner, 2026-11-10, always):** the template of a category is the program with the best features, UX and UI, whether open source, web only or discontinued. We look for what open source does **not** have; the open-source features come in on top. Research for whiteboard, surveys, studio/streaming and videos is running (all known programs per category, then a recommendation). **Gallery** shows local files and remote sources (YouTube, Vimeo, Odysee, PeerTube) through a provider interface, like AIs in People; **Studio** (facet of `fs-streaming`) is live production (OBS, Restream, StreamYard, vMix). ADR 0066.

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
| `fs-streaming` | stream (WHIP/WHEP) | files | Studio (live production and live cutting), Live | Media | OBS Studio, Restreamer, MediaMTX |
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

## Cross-cutting goals (owner, 2026-11-09)

1. **Command palette** over all programs; the commands come from the type descriptions (seen in Raycast, Linear).
2. **Input in plain language** for dates, tasks and contacts ("lunch with Ana Fri 1 pm"; Fantastical, Things, Todoist).
3. **Typed notes:** a tag turns a note into a data type with fields (Tana supertags, Frappe DocTypes; confirms ADR 0066).
4. **Screener:** someone new reaches you only after you let them in, for mail and chat (HEY).
5. **Guides recorded as commands** and the **wiki embeddable everywhere** (Tango; see wiki requirements).
6. **Deciding together** with the procedures in the democracy requirements (Polis, Loomio, systemic consensing,
   growing voting radius).

## Function references (checked 2026-11-10, Sprint round 3)

Programs whose makers thought further than the rest. We take ideas, never code or looks (ADR 0025).

Checked by Thread F against web sources (Sprint round 3, 2026-11-10). Each program's sources are in its `index.md`
(linked in the last column). ✅ confirmed at a primary source · ⚠️ not fully confirmed (one search result, third party or
not readable) · ❌ gone. Corrections are marked **Corrected**. Not checked in this run: Immich.

| Area | Programs and their standout idea | Check (2026-11-10) |
|------|----------------------------------|--------------------|
| People | Monica: reminders, "last spoke", activities; a diary for life events; v3 announced for 2026 · Google Contacts: merge suggestions ("Merge & fix", within one account) · **Corrected:** Apple Contacts: NameDrop (iOS 17) | ✅ [people](apps/people/frontends/index.md) · Monica ⚠️ life events (README only) |
| Mail | HEY: Screener, Imbox/Feed/Paper Trail · Superhuman Mail: keyboard, split inbox (a split list, not a shared inbox) · Spark: team comments on a mail · Fastmail: masked addresses · Delta Chat: chat over e-mail | ✅ [messenger](apps/messenger/frontends/index.md) · Superhuman ⚠️ **Corrected:** Grammarly bought Superhuman Mail in 2025 and renamed the company Superhuman (one search result) |
| Chat | Zulip: a topic on every message · Signal: no standout function named; protocol docs (PQXDH, Double Ratchet) · Telegram: topics, scheduled messages · Discord: roles per channel; drop-in voice rooms ⚠️ (not verified) · Element: spaces, bridges | ✅ [messenger](apps/messenger/frontends/index.md) · Discord ⚠️ voice rooms |
| Calendar | Fantastical: plain-language input ⚠️ (details from a 2019 third-party guide) · Notion Calendar: time zones side by side, share free slots · Cal.com: booking pages · Reclaim, Motion: tasks placed into free time | ✅ [calendar](apps/calendar/frontends/index.md) · Fantastical ⚠️ |
| Tasks | Things 3: Today / This Evening / Someday, quick entry (⚠️ shortcuts not verified) · OmniFocus: perspectives, review (v4) · Todoist: filter language · Linear: triage, cycles; ⚠️ "speed" not verified · Taskwarrior: computed urgency (v3.5.0) | ✅ [tasks](apps/tasks/frontends/index.md) · Linear ⚠️ speed |
| Files | Dolphin: split view, terminal panel, places · **Corrected:** service menus only in KDE developer docs, not in the handbook · Finder: Quick Look · Everything: instant name search (NTFS journal, Windows only) · Dropbox: file requests (sender needs no account) · Seafile: client-side encrypted libraries ⚠️ (desktop client only; file names not encrypted) · Syncthing: device-to-device sync | ✅ [files](apps/files/frontends/index.md) · Dolphin ⚠️ service menus · Seafile ⚠️ |
| Gallery | Immich: plain-language search, faces, map, partner sharing (not checked yet) · Apple Photos: duplicates (album from macOS Ventura) · **Corrected:** text in images not confirmed (⚠️) | ✅ [gallery](apps/gallery/frontends/index.md) · Immich open · Apple Photos ⚠️ text |
| Wiki, notes | Tango: guides from clicks (**Corrected:** the product is tango.ai) · Tana: supertags with inheritance and table view · Obsidian: backlinks, canvas · Logseq: block references ⚠️ (forum source only) · Notion: databases in pages | ✅ [wiki](apps/wiki/frontends/index.md) · Logseq ⚠️ |
| Maps | Google Earth: 3D globe; projects (own maps, shareable), measuring, elevation profile (2026) · guided tours ⚠️ (confirmed only for the 2017 launch) · **Corrected:** Street View is a feature of Google Maps/Earth, not a program (decision open) · OsmAnd: offline; contour lines only with a paid plugin · Organic Maps · uMap · Felt: live co-editing | ✅ [maps](apps/maps/frontends/index.md) · Google Earth ⚠️ tours · OsmAnd ⚠️ contours |
| History | Day One: place and weather, "on this day" (also on the web since 2025-09) · ActivityWatch: automatic, local (v0.14.1) · Exist.io: correlations; service still online | ✅ [history](apps/history/frontends/index.md) |
| Resources, ERP | ERPNext/Frappe: DocTypes generate list and form · **Corrected:** SAP Fiori is a design system, not a program (not analysed) · Odoo: linked modules ⚠️ (indirect evidence) · Grocy: household stock · Snipe-IT: check-out and check-in (consumables are never returned) | ✅ [resources](apps/resources/frontends/index.md) · Odoo ⚠️ |
| Decisions | Polis: active (commits Nov 2026) · Loomio: active (v3.15.0) · LiquidFeedback: delegation ✅, **Corrected:** no release since core 4.2.2 (2021), a stall · Decidim: participation spaces with components (v0.32.2) · Consul: 2.6.1 · dieBasis procedures are procedures, not software (see democracy requirements) | ✅ [surveys](apps/surveys/frontends/index.md) · LiquidFeedback stalled |
| Whiteboard | tldraw ⚠️ "feel" is subjective; facts: React SDK, infinite canvas · Excalidraw: hand-drawn; **Corrected:** end-to-end encryption only in the hosted app, not in the npm package · FigJam: stamps, timer, voting with votes hidden until the end | ✅ [whiteboard](apps/whiteboard/frontends/index.md) · tldraw ⚠️ |
| Streaming | OBS Studio: scenes · YouTube Studio: live control room, analytics afterwards · StreamYard: guests in the browser · Ecamm Live: Mac only ⚠️ (third party) · Owncast: ActivityPub · PeerTube: AGPL-3.0, ActivityPub, P2P live | ✅ [streaming](apps/streaming/frontends/index.md) · Ecamm Live ⚠️ |
| Store | F-Droid: anti-feature labels, reproducible builds · Obtainium: installs straight from Git releases · Flathub: verified publishers (app-ID ownership check) | ✅ [store](apps/store/frontends/index.md) |
| Start | Raycast: one palette for everything · Alfred: palette, workflows (⚠️ macOS only not stated explicitly) · KDE Plasma: activities with own favourites, widgets, wallpaper, window rules; energy and panels apply to all (informal sources ⚠️) | ✅ [desktop](platform/desktop/frontends/index.md) · Alfred ⚠️ |
| Helpdesk | Chatwoot: all channels in one inbox, website widget · **Corrected:** Zammad has a CTI call log (Placetel, sipgate, generic CTI API), no own SIP; edit-conflict warning · Help Scout: customer sidebar | ✅ [helpdesk](apps/helpdesk/frontends/index.md) · Zammad corrected |
| CRM | Twenty: own objects and fields (license from a third-party source ⚠️) · Attio: enrichment | ✅ [crm](suites/crm/frontends/index.md) · Twenty license ⚠️ |
| Workflows | n8n: node canvas, code node (integration count inconsistent: 400+ vs 1500+) · Huginn: agents and events · Windmill: scripts become forms, endpoints and jobs · Apple Shortcuts: personal device tool · Power Automate: hosted product | ✅ [workflows](suites/workflows/frontends/index.md) · n8n count open |
| Marketing | Plausible: cookieless, funnels, stats API · Umami: cookieless, funnels, retention, journeys · Listmonk: newsletter manager (AGPL-3.0) | ✅ [marketing](apps/marketing/frontends/index.md) |

## Open points of this draft

1. **Marketing** (analysed: Matomo, Plausible, Mautic): own program with its own data, or a suite over messenger and
   people?
2. **Workflows** (analysed: n8n, Node-RED): a program that owns workflow definitions (candidate standard: CNCF
   Serverless Workflow, BPMN), or later?
3. **Helpdesk**: suite as proposed above, or own program?
4. **Groups, identity**: no reference programs analysed yet; Haiku researches candidates. History and store have their first analyses (2026-11-10).
5. **Styles**: the first four are fixed by the frontends: *Admin* (dense), *Simple* (large), *Apple* (round corners,
   glass), *Windows* (flat, Fluent spacing). Each with an icon set of our own. More can follow.
