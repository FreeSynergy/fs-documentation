# Programs (Apps)

Programs are organised into **categories**. Programs whose user interface is replicated or connected in FreeSynergy receive a **skin documentation**: seven files per program.

## Categories

| Category | Content | Skin documentation |
|-----------|--------|--------------------|
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

## Skin schema

Each skin documentation is located in `apps/<category>/masks/<program>/` and contains:

| File | Content |
|-------|--------|
| `index.md` | Overview and links |
| `menu.md` | Menu items, context menus, role menus |
| `features.md` | Functions, integrations, what it CANNOT do |
| `description.md` | Description, advantages, differentiation, technical details |
| `structure.md` | Window structure (ASCII), UI/UX, accessibility |
| `shortcuts.md` | All keyboard shortcuts (always separate) |
| `api.md` | API type, authentication, endpoints, examples, rate limits, SDKs |

Reference examples: [Wiki/Skins](apps/wiki/frontends/), [Messenger/Skins](apps/messenger/frontends/), [Desktop/Skins](platform/desktop/frontends/).

## Cross-references to system areas

| Area | Relation to programs |
|---------|---------------------|
| [Components](../components/) | UI elements used in the interfaces |
| [Gestures](../interactions/gestures/) | Interactions in touch interfaces |
| [Animations](../interactions/animations/) | Transitions and feedback in the interfaces |
| [Standardised data](../data/) | Fields, models and the API pattern of all programs |

## Adding new programs

1. Choose the category and level (levels and examples: see `conventions/doku-standard.md` in the project root)
2. Create the directory `apps/<category>/masks/<program>/`
3. Write the seven files according to the schema above (write the German version first)
4. Add the entry to `apps/<category>/masks/index.md`
5. Name missing functions explicitly — invent nothing
