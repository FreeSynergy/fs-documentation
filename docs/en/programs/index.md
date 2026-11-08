# Programs

**One engine per topic. As many faces as there are people.**

Every app you see in FreeSynergy stands on a strong engine that knows its topic inside out: people, messages, tasks, files, appointments. On top of that engine you choose how it looks and how much it shows. Underneath, all engines speak the same open interfaces, so your contacts, your calendar and your messages work together without you setting anything up. You never have to learn how it is built. But if you want to know, here it is.

## How it is built

```
  Suites        Groupware · Project management · CRM · ERP · Helpdesk · Democracy
                (several programs put together for one purpose)
                        │ uses
  ┌─────────────────────┴──────────────────────────────────────────────┐
  │ Program  fs-people                       Program  fs-messenger     │  ← owns the data and one open standard
  │   Facets   Contacts · Users · AIs · …      Facets   Mail · Chat    │  ← look like apps of their own
  │     Frontends  simple · classic · full …     Frontends  …          │  ← how it looks; switch any time
  │     Admin frontend (every setting)           Admin frontend        │  ← the safety net
  └─────────────────────┬──────────────────────────────────────────────┘
                        │ built from
  Components    calendar grid · file manager · charts · chat …
```

FreeSynergy sorts everything by **purpose**, not by what a tool looks like. To people, everything is simply an **app**. Behind the apps there are a few kinds of building blocks, and the difference between them is what lets FreeSynergy be simple for one person and complete for a company at the same time. (ADR 0021, 0049, 0061)

## The kinds

| Kind | What it is | Has its own data? | Example |
|------|------------|-------------------|---------|
| **Program** | The engine for one topic. It owns the data and the rules, and one open standard. | Yes | `fs-people`, `fs-messenger`, `fs-tasks` |
| **Facet** | A part of a program that looks like an app of its own: own name, own logo, own menu entry, a fixed filter on the program's data. The program defines its facets. | No | Contacts, Users, AIs and Partners in `fs-people`; Mail and Chat in `fs-messenger` |
| **Frontend** | One way of looking at a program or a facet: very simple, classic, familiar, or complete. Many per program and per facet; you can switch. | No | A simple contact list; a full contact manager |
| **Admin frontend** | The frontend with *every* setting. Each program and each facet has one. | No | "Contacts – Settings" |
| **Component, workbench** | A piece of screen that shows something without knowing what the data means. Frontends are built from them. | No | A calendar grid, a file manager |
| **Suite** | Several programs put together for one purpose. | No (uses the programs') | Groupware, project management, CRM |

A facet is the opposite of a suite: a suite brings several programs together; a facet shows one part of one program.

## Why we make these differences

**People look for what they need, not for how it is built.** Someone wants their contacts, not "people records with the role contact". Someone wants e-mail, and does not need to know that the same engine also carries chats from Matrix. Facets give each need its own app, with a name that says what it is.

**One engine keeps everything together.** Because Contacts and Users are both `fs-people`, a person you know and the account they sign in with are the same record. Because Mail and Chat are both `fs-messenger`, a conversation can move from one to the other. Separate programs would copy the data and drift apart.

**Frontends let everyone choose.** The engine can do far more than any one screen shows. One person wants three buttons, another wants every detail, a third wants something that feels like the program they already know. All of them work on the same data, and can switch at any time.

**The admin frontend is the safety net.** A simple frontend hides settings on purpose. If something gets switched off by mistake, the admin frontend has every setting, so you, or someone who helps you, can always put it right. That is why every program and every facet must have one. In desktop menus, admin frontends are grouped under *Settings*, so the main menu stays short.

## In the store

[FreeSynergy.Store](platform/releases.md) lists every facet as an app with its own logo. Installing an app installs the program behind it; installing a second facet of the same program adds only its menu entry and frontends.

## Planned facets

| Program | Facets (proposed) |
|---------|-------------------|
| `fs-people` | Contacts, Users, AIs, Partners (leads, customers, suppliers), Team, Members |
| `fs-messenger` | Mail, Chat, possibly Forum |
| `fs-files` | Gallery, Music, Videos, Documents |
| `fs-tasks` | To-dos, Tickets |
| `fs-calendar` | Calendar, Booking (with `fs-resources`) |

## Categories

| Category | Content | Analysed programs |
|----------|---------|-------------------|
| [Wiki](apps/wiki/) | Wiki and knowledge systems | complete (7 programs) |
| [Messenger](apps/messenger/) | Chat, e-mail, social networks | complete (7 programs) |
| [Desktop](platform/desktop/) | Desktop programs, dashboards, start pages | complete (12 programs) |
| [Whiteboards](apps/whiteboard/) | Collaborative whiteboards | complete (6 programs) |
| [Helpdesk](apps/helpdesk/) | Tickets and support | complete (8 programs) |
| [Project management](suites/projectmanagement/) | Tasks, boards, projects | complete (8 programs) |
| [Contacts](apps/people/) | Contact management | complete (4 programs) |
| [CRM](suites/crm/) | Customer relationships | complete (6 programs) |
| [Calendar](apps/calendar/) | Appointments and planning | complete (6 programs) |
| [Maps](apps/maps/) | Maps and geodata | complete (7 programs) |
| [ERP](suites/erp/) | Resource planning | complete (6 programs) |
| [Workflows](suites/workflows/) | Automation and integration | complete (6 programs) |
| [Democracy](suites/democracy/) | Participation platforms | complete (6 programs) |
| [Marketing](apps/marketing/) | Marketing and analytics | complete (6 programs) |
| [Marketplaces](suites/marketplace/) | Marketplace software and third-party marketplaces | complete (6 programs) |
| [Photo galleries](apps/gallery/) | Image and video collections | complete (8 programs) |
| [Streaming](apps/streaming/) | Encoders, media servers, multistreaming | complete (10 programs) |


How each category's well-known programs are analysed (functions only, nothing copied, ADR 0012, 0013) is described in the frontends index of each category, for example [Wiki](apps/wiki/frontends/index.md).

## Cross-references to system areas

| Area | Relation to programs |
|---------|---------------------|
| [Components](../components/) | UI elements used in the interfaces |
| [Gestures](../interactions/gestures/) | Interactions in touch interfaces |
| [Animations](../interactions/animations/) | Transitions and feedback in the interfaces |
| [Standardised data](../data/) | Fields, models and the API pattern of all programs |

