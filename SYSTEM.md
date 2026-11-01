# FreeSynergy Documentation System

This document contains all important information for LLMs/agents working on the FreeSynergy documentation project.

## 📚 Project Structure and Conventions

### Directory Structure

```
fs-documentation/
├── docs/                    # Documentation source files
│   ├── de/                 # German documentation (primary)
│   │   ├── apps/           # programs, grouped by category
│   │   │   └── [category]/skins/[program]/   # 7 files per program
│   │   ├── components/     # UI elements: 10 categories + base class (see SYSTEM “UI Components”)
│   │   ├── gestures/       # touch gestures (description/attributes/appearance)
│   │   ├── animations/     # animations (description/attributes/appearance)
│   │   └── data/           # standardized data (standards, mappings, formats, models, fields, conventions, api)
│   └── en/                 # English documentation
│   └── [language]/         # Additional languages
├── .github/                # GitHub workflows and templates
├── mkdocs.yml             # MkDocs configuration
├── requirements.txt       # Python dependencies
├── LICENSE                # Apache 2.0 license
└── SYSTEM.md              # This file - system documentation
```

### Language Requirements

- **Primary language**: German (`de/`)
- All documentation must be created in **German** first
- English translations (`en/`) and French translations (`fr/`) are maintained as needed
- New languages can be added by creating subdirectories (e.g., `es/`, `it/`, etc.)

### Documentation Generation

- Built with **MkDocs** + **Material Theme**
- Live documentation: https://freesynergy.github.io/fs-documentation/

---

## 🗂️ Category Structure

All program documentation is organized in **categories** (categories) under `docs/[language]/apps/`.

### Existing Categories

```
docs/[language]/apps/
├── wiki/                  # Wiki systems
├── messenger/            # Instant messaging
├── marketing/            # Marketing & analytics tools
├── whiteboards/          # Digital whiteboards
├── helpdesk/             # Help desk systems
├── projectmanagement/    # Project management
├── contact/              # Contact management (CRM)
├── calendar/             # Calendar systems
├── desktop/              # Desktop applications
├── crm/                  # Customer relationship management
├── democracy/           # Democracy systems
├── maps/                 # Mapping systems
├── erp/                  # Enterprise resource planning
├── workflows/            # Workflow automation
└── [new categories]/     # Additional categories
```

### Folder Naming Conventions

- **Lowercase** with **German names** (e.g., `messenger`, `wiki`, `helpdesk`)
- **No spaces** - use hyphens or camelCase if needed
- **Consistent** across all language directories

### File Naming Conventions

Each program requires exactly **7 documentation files** (`index.md` plus the 6 core files):

| File | Purpose | German Description |
|------|---------|-------------------|
| `index.md` | Entry point | Übersicht + Links auf die 6 Dateien |
| `menu.md` | Menu structure | Alle Menüpunkte und Navigationsstruktur |
| `features.md` | Features | Funktionen, Editoren, Haupt-Features |
| `description.md` | Description | Was das Programm macht, Vorteile, Abgrenzung |
| `structure.md` | Structure | UI/UX, Fensterstruktur, Layout |
| `shortcuts.md` | Shortcuts | Alle Tastatur-Shortcuts |
| `api.md` | API | REST API, GraphQL, Webhooks, SDKs |

### Non-Program Documentation Areas

Areas outside `apps/` use their own, smaller file sets:

| Area | Location | Files per entry |
|------|----------|-----------------|
| UI components | `docs/de/components/<category>/<component>/` | `description.md`, `appearance.md`, `attributes.md`, `usage.md` (all four required; `examples.md` was merged into `usage.md`) |
| Gestures | `docs/de/gestures/<gesture>/` | `description.md`, `attributes.md`, `appearance.md` |
| Animations | `docs/de/animations/<category>/<animation>/` | `description.md`, `attributes.md`, `appearance.md` |
| Standardized data | `docs/de/data/` + `docs/de/data/<domain>/<standard>/` | Cross-cutting: `index.md`, `standards.md`, `mappings.md`, `formate.md`, `modelle.md`, `felder.md`, `konventionen.md`, `api.md`. Per standard: `index.md` (domain), `beschreibung.md`, `speicherung.md` (+ optional `beispiele.md`, `mapping.md`) |

Every area has an `index.md` that lists all entries in a table and documents the shared attributes/configuration.

---

## 📋 Every Category with Examples

### 1. Wiki (Wiki-Systeme)

**Description**: Knowledge management and documentation platforms

**Programs**:
- **wikijs** - Modern, lightweight wiki with markdown support
- **xwiki** - Enterprise wiki with extensions and macros
- **mediawiki** - Wikipedia'swiki engine
- **tango.io** - Modern team knowledge base
- **notion** - All-in-one workspace (wiki features)
- **confluence** - Atlassian team collaboration
- **vscodium** - VS Code without telemetry (for local wiki hosting)
- **dokuwiki** - Simple file-based wiki
- **mediagoblin** - Federated media hosting platform
- **twiki** - Enterprise wiki with Perl backend
- **mdwiki** - Markdown-based wiki
- **wiki.md** - Simple markdown wiki
- **gollum** - GitHub-style wiki
- **bookstack** - Book-based documentation system
- **wiki.js** - Modern, powerful wiki platform

**What fits**: Any system for creating, editing, and organizing knowledge base articles, documentation, or collaborative writing.

---

### 2. Messenger (Instant Messaging)

**Description**: Communication and collaboration platforms

**Programs**:
- **outlook** - Microsoft email and collaboration
- **kontact** - KDE's personal information manager
- **thunderbird** - Mozilla email client
- **element** - Matrix-based secure messaging
- **discord** - Voice, video, and text chat
- **mastodon** - Decentralized social network
- **telegram** - Cloud-based messenger with bots
- **signal** - Private messaging with E2E encryption
- **whatsapp-web** - WhatsApp web interface
- **jabber/xmpp** - Open instant messaging protocol
- **skype** - Microsoft communication platform
- **rocketchat** - Open source team chat
- **mattermost** - Open source Slack alternative
- **irc** - Internet Relay Chat clients
- **wire** - Secure messaging platform

**What fits**: Any system for real-time communication, chat, email, or social networking.

---

---

### 3. Marketing (Marketing & Analytics)

**Description**: Marketing automation, CRM, and analytics tools

**Programs**:
- **mailchimp** - Email marketing platform
- **hubspot** - All-in-one CRM and marketing software
- **salesforce** - Customer relationship management
- **intercom** - Customer messaging platform
- **convertkit** - Email marketing for creators
- **mailgun** - Email delivery service
- **stripe** - Payment processing (marketing integrations)
- **google-analytics** - Web analytics service
- **hotjar** - User behavior analytics
- **mixpanel** - Product analytics
- **campaign-monitor** - Email marketing service
- **activecampaign** - marketing automation
- **klaviyo** - Email marketing for growing businesses
- **sendgrid** - Email delivery service
- **campaign-forgot** - Email campaign management

**What fits**: Any tool for email marketing, customer relationship management, analytics, or marketing automation.

---

### 4. Whiteboards (Whiteboard-Systeme)

**Description**: Collaborative digital whiteboards for brainstorming and planning

**Programs**:
- **mural** - Visual collaboration platform
- **miro** - Online whiteboard for team collaboration
- **excalidraw** - Collaborative whiteboard
- **figma** - Interface design tool with whiteboard features
- **jamboard** - Google's digital whiteboard
- **leantime** - Open source project management with whiteboard
- **stormboard** - Collaborative brainstorming tool
- **whimsical** - Visual collaboration for teams
- **gitmind** - Mind mapping tool
- **mindmeister** - Online mind mapping

**What fits**: Any collaborative whiteboard, mind mapping, or visual brainstorming tool.

---

### 5. Helpdesk (Help Desk & Support)

**Description**: Customer support and ticket management systems

**Programs**:
- **osTicket** - Open source help desk system
- **rt** - Request Tracker for ticket management
- **zammad** - Open source help desk
- **freshdesk** - Customer support software
- **zendesk** - Customer service platform
- **helpscout** - Customer support tool
- **civicrm** - Constituent relationship management
- ** GLPI** - IT asset management
- **sysaid** - IT service management
- **servertime** - Help desk software
- **kayako** - Customer support platform

**What fits**: Any help desk, ticketing system, or customer support management tool.

---

### 6. Project Management (Projektmanagement)

**Description**: Tools for managing projects, tasks, and teams

**Programs**:
- **trello** - Kanban-style project management
- **asana** - Work management platform
- **jira** - Issue and project tracking (Atlassian)
- **redmine** - Flexible project management web app
- **taiga** - Agile project management
- **monday.com** - Work operating system
- **clickup** - Productivity platform
- **linear** - Issue tracking and project management
- **nocalhost** - Cloud development platform
- **plantronics** - Audio and collaboration
- **toggl** - Time tracking
- **notion** - All-in-one workspace (project features)
- **coda** - Doc-based project management
- **smartsheet** - Work management and collaboration
- **wrike** - Project management software

**What fits**: Any project management, task tracking, or work collaboration tool.

---

### 7. Contact/CRM (Kontakt/CRM)

**Description**: Customer relationship management and contact management

**Programs**:
- **civicrm** - Constituent relationship management
- **suitecrm** - Open source CRM
- **odoo** - Business management software (CRM module)
- **frappe** - Modern ERP with CRM
- **metronic** - CRM system
- **pipedrive** - Sales pipeline management
- **lessonly** - Customer data platform
- **salesforce** - CRM platform
- **hubspot** - CRM platform
- **zoho-crm** - CRM software
- **insightly** - CRM and project management
- **pabbly-crm** - CRM software
- **capsule** - CRM for small businesses
- **sugarcrm** - CRM platform
- **roistat** - Marketing analytics and CRM

**What fits**: Any CRM, contact management, or customer relationship tool.

---

### 8. Calendar (Kalender)

**Description**: Calendar and scheduling systems

**Programs**:
- **google-calendar** - Google's calendar service
- **outlook-calendar** - Microsoft calendar
- **ical** - iCalendar format support
- **davical** - CalDAV server
- **nextcloud-calendar** - Calendar app for Nextcloud
- **kolab** - Groupware with calendar
- **caldav** - Calendar access protocol
- **sabredav** - CalDAV and CardDAV server
- **memacs** - Calendar data extraction
- **planner** - Task and calendar management
- **taskwarrior** - Task management with calendar
- **org-mode** - Emacs organization mode
- **todoist** - Task management with calendar
- **toodledo** - Task and time management
- **clockwork** - Calendar synchronization

**What fits**: Any calendar, scheduling, or time management system.

---

### 9. Desktop (Desktop-Applikationen)

**Description**: Desktop applications and software

**Programs with skin documentation** (`apps/desktop/skins/<program>/`):
- **homarr** - Homelab dashboard with widgets and Docker integration
- **heimdall** - Personal dashboard with server statistics (Laravel)
- **homer** - Static dashboard, YAML configuration only
- **dashy** - Highly configurable dashboard (Vue) with auth and widgets
- **homepage** - Static service dashboard with live widgets
- **gethomepage** - Service client library behind homepage
- **launchboard** - Commercial no-code homelab dashboard
- **synology-dsm** - Commercial NAS desktop portal (`SYNO.*` REST API)

**Programs**:
- **libreoffice** - Office suite
- **firefox** - Web browser
- **chrome** - Google Chrome
- **thunderbird** - Email client
- **krita** - Digital painting
- **gimp** - Image editor
- **inkscape** - Vector graphics editor
- **blender** - 3D creation suite
- **obs-studio** - Video recording and streaming
- **audacity** - Audio editor
- **shotcut** - Video editor
- **kdenlive** - Video editor
- **vlc** - Media player
- **mpv** - Media player
- **telegram-desktop** - Desktop messenger
- **element-desktop** - Desktop messaging
- **discord** - Desktop app
- **slack** - Desktop app
- **zoom** - Video conferencing
- **skype** - Communication platform

**What fits**: Any desktop application or software for productivity, creativity, or communication.

---

### 10. CRM (Customer Relationship Management)

**Description**: Customer relationship management systems

**Programs**:
- **civicrm** - Constituent relationship management
- **suitecrm** - Open source CRM
- **odoo** - Business management software
- **frappe** - Modern ERP with CRM
- **metronic** - CRM system
- **pipedrive** - Sales pipeline management
- **lessonly** - Customer data platform
- **salesforce** - CRM platform
- **hubspot** - CRM platform
- **zoho-crm** - CRM software
- **insightly** - CRM and project management
- **pabbly-crm** - CRM software
- **capsule** - CRM for small businesses
- **sugarcrm** - CRM platform
- **roistat** - Marketing analytics and CRM

**What fits**: Any CRM, contact management, or customer relationship tool.

---

### 11. Democracy (Demokratie-Systeme)

**Description**: Democratic decision-making and participation platforms

**Programs**:
- **liquid-feedback** - Participatory decision-making
- **democracy-app** - Digital democracy platform
- **polis** - Large-scale deliberation platform
- **circo** - Citizen participation platform
- **democracy-workflow** - Democratic workflows
- **polideo** - Video platform for democracy
- **decidim** - Participatory democracy platform
- **popular** - Citizen participation
- **consul** - Open source participatory platform
- **democracy-enabler** - Democracy tools

**What fits**: Any platform for democratic decision-making, voting, or citizen participation.

---

### 12. Maps (Kartensysteme)

**Description**: Mapping and GIS systems

**Programs**:
- **openstreetmap** - Collaborative map project
- **mapbox** - Customizable maps
- **leaflet** - Interactive maps library
- **cesium** - 3D globe and map engine
- **qgis** - GIS software
- **arcgis** - Geographic information system
- **google-maps** - Google Maps API
- **openlayers** - Maps library
- **carto** - Geospatial platform
- **maplibre** - Open source mapping
- **tangram** - Real-time 3D maps
- **mapnik** - Map rendering engine
- **geoserver** - Geospatial server
- **postgis** - Spatial database
- **mapbox-gl-js** - Interactive maps

**What fits**: Any mapping, GIS, or geospatial system.

---

### 13. ERP (Enterprise Resource Planning)

**Description**: Enterprise resource planning systems

**Programs**:
- **odoo** - All-in-one business software
- **frappe** - Modern ERP
- **sage** - Accounting and business management
- **SAP** - Enterprise software
- **oracle-erp** - Oracle ERP
- **infor-erp** - Infor ERP
- **microsoft-dynamics** - Business management solutions
- **netSuite** - Cloud ERP
- **acumatica** - Cloud ERP
- **iqz** - ERP system
- **axelor** - Open source ERP
- **erpnext** - Free and open source ERP
- **tryton** - Enterprise management system
- **ofbiz** - Apache OFBiz
- **dolibarr** - ERP/CRM for small businesses

**What fits**: Any ERP system for business management, finance, or operations.

---

### 14. Workflows (Workflow-Automatisierung)

**Description**: Workflow automation and integration platforms

**Programs**:
- **n8n** - Workflow automation tool
- **make** -formerly Integromat
- **zapier** - Automation platform
- **automate** - Workflow automation
- **node-red** - Flow-based programming
- **apache-airflow** - Workflow management
- **apache-airflow-composer** - Managed Airflow
- **luigi** - Workflow management
- **dagster** - Data orchestrator
- **prefect** - Workflow orchestration
- **kestra** - Modern workflow engine
- **temporal** - Workflow orchestration
- **caddy** - Web server with automation
- **traefik** - Reverse proxy
- **nifi** - Dataflow automation

**What fits**: Any workflow automation, integration, or orchestration platform.

---

## 📁 6-File-Per-Program Structure

Each program requires exactly 6 documentation files in German:

### 1. `menu.md` - Menüpunkte

**Purpose**: Document all menu items, navigation structure, and context menus

**Content requirements**:
- Complete list of all menu items
- Context menus and actions
- Navigation structure
- Menu organization by function
- Menu locations (top bar, sidebar, context menus)

**Example structure**:
```markdown
# Programmname - Menüpunkte

## Übersicht
[Beschreibung der Menüstruktur]

## Hauptmenüpunkte

### 1. [Menü-Name]
- **Funktion**: [Beschreibung]
- **Details**:
  - [Funktion 1]
  - [Funktion 2]
  - [Funktion 3]

## Kontext-Menüs
[Details zu Kontext-Menüs]

## Menüs nach Benutzerrolle
[Menüs für verschiedene Benutzerrollen]
```

---

### 2. `features.md` - Funktionen

**Purpose**: Document features, editors, and capabilities

**Content requirements**:
- Main features and capabilities
- Editor features (if applicable)
- Feature comparison
- What the program CAN do
- What the program CANNOT do
- Editor types and differences
- Extension/plugin features

**Example structure**:
```markdown
# Programmname - Funktionen

## Übersicht
[Beschreibung der Hauptfunktionen]

## Hauptfunktionen

### 1. [Funktionsbereich]
- **Feature 1**: [Beschreibung]
- **Feature 2**: [Beschreibung]
- **Feature 3**: [Beschreibung]

## Editoren
[Beschreibung der verfügbaren Editoren]

## Vergleich der Editoren
[Tabelle oder Text Vergleich]

## Was Programmname NICHT kann
- [Nicht-Feature 1]
- [Nicht-Feature 2]
- [Nicht-Feature 3]
```

---

### 3. `description.md` - Beschreibung

**Purpose**: Describe what the program does and how it compares to alternatives

**Content requirements**:
- What the program does
- Key features and benefits
- Technical details (backend, database, authentication)
- Target audience
- Comparison to similar programs (3-5 comparisons)
- For whom the program is suitable

**Example structure**:
```markdown
# Programmname - Beschreibung

## Übersicht
[Kurzbeschreibung]

## Was Programmname macht
[Was das Programm genau macht]

## Vorteile
- **Feature 1**: [Beschreibung]
- **Feature 2**: [Beschreibung]

## Abgrenzung zu anderen Systemen
### Programmname vs. [Alternativ-1]
- [Unterschied 1]
- [Unterschied 2]

### Programmname vs. [Alternativ-2]
- [Unterschied 1]
- [Unterschied 2]

## Technische Details
- **Backend**: [Technologie]
- **Database**: [Datenbank]
- **Frontend**: [Frontend-Technologie]
- **Authentication**: [Auth-Methode]
- **Hosting**: [Hosting-Möglichkeiten]

## Für wen ist Programmname geeignet?
- [Zielgruppe 1]
- [Zielgruppe 2]
```

---

### 3. `structure.md` - Struktur & UI/UX

**Purpose**: Document UI structure, layout, and user experience

**Content requirements**:
- Window/viewport structure (ASCII diagram recommended)
- Main areas (sidebar, content, header, footer)
- UI components and their functions
- Color scheme and typography
- Interactions and animations
- Accessibility features
- Performance characteristics

**Example structure**:
```markdown
# Programmname - Struktur & UI/UX

## Übersicht
[Kurze Übersicht]

## Fenster-Struktur

### Hauptbereiche
```
[ASCII-Diagramm der UI-Struktur]
```

### [Bereichs-Name]
[Details zu diesem Bereich]

## UI/UX

### Design-Prinzipien
- [Prinzip 1]
- [Prinzip 2]

### Farbschema
- [Theme 1]
- [Theme 2]

### Interaktionen
- [Interaktion 1]
- [Interaktion 2]

## Zugänglichkeit
- [Feature 1]
- [Feature 2]

## Performance
- [Feature 1]
- [Feature 2]
```

---

### 4. `shortcuts.md` - Tastatur-Shortcuts

**Purpose**: Document all keyboard shortcuts

**Content requirements**:
- All keyboard shortcuts (Ctrl/Command combinations)
- Shortcuts by category (formatting, navigation, editing)
- Editor-specific shortcuts
- Mac vs Windows/Linux differences
- Quick navigation shortcuts

**Example structure**:
```markdown
# Programmname - Tastatur-Shortcuts

## Übersicht
[Kurze Übersicht]

## Allgemeine Shortcuts
| Shortcut | Funktion |
|----------|----------|
| `Ctrl+Shift+P` | [Funktion] |
| `Ctrl+,` | [Funktion] |

## Editor Shortcuts
### Formatierung
| Shortcut | Funktion |
|----------|----------|
| `Ctrl+B` | Fett |

## Navigation Shortcuts
| Shortcut | Funktion |
|----------|----------|
| `Ctrl+K` | [Funktion] |

## Mac Shortcuts
| Shortcut | Funktion |
|----------|----------|
| `Cmd+K` | [Funktion] |

## Zusammenfassung
[Zusammenfassung der Shortcuts]
```

---

### 5. `api.md` - API-Dokumentation

**Purpose**: Document the API for program integration

**Content requirements**:
- API overview
- Authentication methods
- Main API endpoints
- Request/response examples
- Rate limits
- Webhooks
- SDKs and client libraries
- Code examples (curl, Python, JavaScript)

**Example structure**:
```markdown
# Programmname - API Dokumentation

## Übersicht
[Kurze Übersicht]

## Authentifizierung
[Beschreibung der Authentifizierungsmethoden]

### Header
```
[Header-Beispiel]
```

### URL Format
```
[URL-Format]
```

## Endpunkte

### [Endpoint-Gruppe]
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/endpoint` | [Beschreibung] |
| POST | `/endpoint` | [Beschreibung] |

## Beispiele

### [Beispiel-Typ]
```bash
[curl-Beispiel]
```

### Python Example
```python
[Python-Beispiel]
```

## Rate Limits
- [Limit 1]
- [Limit 2]

## Webhooks
[Beschreibung der Webhooks]

## SDKs und Client-Bibliotheken
- **JavaScript**: [Library]
- **Python**: [Library]

## Siehe auch
- [menu.md](menu.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (diese Datei)
```

---

## 🧩 UI Components (`docs/de/components/<category>/<component>/`)

Ten categories, each with its own `index.md`; every component lives in a directory of its own:

| Category | Contains | Example components |
|----------|----------|--------------------|
| `basics/` | base class and the smallest building blocks | `base.md`, `label`, `separator`, `link`, `kbd` |
| `actions/` | single actions and groups of actions | `button`, `button-group`, `floating-action-button` |
| `navigation/` | menus, bars, path navigation, command palette | `menu`, `tabs`, `breadcrumb`, `command` |
| `containers/` | boxes and layout surfaces | `card`, `panel`, `accordion`, `split-view`, `wizard`, `scroll-area` |
| `overlays/` | surfaces with their own focus lifetime | `modal`, `drawer`, `popover`, `tooltip`, `context-menu`, `alert-dialog`, `hover-card` |
| `feedback/` | state made visible | `alert`, `toast`, `progress`, `spinner`, `skeleton`, `badge`, `empty-state` |
| `fields/` | entering and choosing values | `field`, `text-input`, `select`, `combobox`, `date-picker`, `otp-input` |
| `data/` | presenting data | `table`, `list-view`, `tree-view`, `timeline`, `chart`, `description-list` |
| `media/` | playing and showing media | `media-player` (parent of `audio`/`video`), `image`, `icon`, `carousel` |
| `special/` | composites with their own data model | `embed`, `code-editor`, `whiteboard`, `map-view`, `dashboard` |

**Inheritance model.** `basics/base.md` is the parent class: it defines the inherited
attributes (`id`, `label`, `visible`, `enabled`, `size`, `theme`, `rounded`, `variant`,
`state`, `tabIndex`, `onClick`/`onFocus`/`onBlur`, `gesture`, `animation`, ARIA), the size
scale, the state names, the fixed section order and the naming convention
(`-input`, `-picker`, `-editor`, `-view`, `-menu`/`-bar`). A component's `attributes.md`
lists **only its own** attributes and ends with the section `Geerbt von` pointing at the
base class. Real inheritance is expressed in the `Erbt von` row of the profile table
(e.g. `audio` → `media-player`, `context-menu` → `menu`).

**File set per component** (fixed order of sections):

| File | Sections |
|------|----------|
| `description.md` | profile table → Beschreibung → Verwendungszweck → Varianten → Features → Abgrenzung → Best Practices → Siehe auch |
| `appearance.md` | Grundlayout → Varianten → Größen → Farben und Zustände → Hover- und Fokus-Effekte → Reaktiv |
| `attributes.md` | Hauptattribute → Verhalten → Darstellung → Events → Barrierefreiheit → (component specific) → Geerbt von |
| `usage.md` | Anwendung → Beispiele → Szenarien (the former `examples.md` is merged here) |

**Profile table (Steckbrief).** `description.md` starts with a Markdown table (no YAML
frontmatter, deliberately) carrying `Kategorie`, `Erbt von`, `Varianten`, `Zustände`,
`Gesten`, `Animationen`, `Verwandt`, `Rolle`, `Status`. It makes the cross references to
`gestures/` and `animations/` machine readable and is the input for the generators.

**Tools** (stdlib only, each supports a dry run without `--apply`):

| Tool | Purpose |
|------|---------|
| `tools/gen_component_indexes.py` | writes `components/index.md`, every category `index.md` and the `mkdocs.yml` nav block (between `# BEGIN/END components nav`) from the profile tables; `--check` fails on drift |
| `tools/check_components.py` | validates the standard: required files, profile fields, required sections, table cell counts, dead links, attributes that belong in the base class, near-duplicate components, pages missing from the nav |
| `tools/gen_usage_pages.py` | creates missing `usage.md` from the component's own description and attribute tables |
| `tools/add_steckbrief.py` | inserts/refreshes the profile table and the `Siehe auch` section; `--blank-lines` normalises blank lines between Markdown blocks |
| `tools/standardize_sections.py` | renames section headings to the standard names, merges duplicates, reorders sections, repairs attribute tables whose header lacks the `Default` column |
| `tools/standardize_components.py` | earlier migration: `examples.md` → `usage.md`, strip inherited attributes |
| `tools/restructure_components.py` | the one-off move into the ten categories plus the merges, rewriting every internal link |

CI runs `check_components.py` and `gen_component_indexes.py --check` before the site build,
so numbers and navigation cannot drift again.

Relative links inside a component directory use **three** levels for areas outside
`components/` (`../../../gestures/`) and two levels for a sibling category
(`../../feedback/toast/`); links inside the same category use one level (`../menu/`).

## 🖱️ Interaction Areas (Gestures and Animations)

### Gestures (`docs/de/gestures/<gesture>/`)

tap, double-tap, long-press, swipe, drag, pinch, spread, rotate, shake

Each gesture: `description.md`, `attributes.md`, `appearance.md`. Shared attributes are listed in `gestures/index.md` (`onTap` … `onShake`, thresholds, `enabled`).

### Animations (`docs/de/animations/<category>/<animation>/`)

Eight category directories, each with its own `index.md`, each animation in a directory of its own:

| Category | Animations |
|----------|-----------|
| `entrance/` | fade-in, slide-in, zoom-in, scale-in, bounce-in, pop-in, expand, unfold (8) |
| `exit/` | fade-out, slide-out, zoom-out, scale-out, bounce-out, pop-out, collapse (7) |
| `feedback/` | shake, wiggle, ripple, press, lift, tick-draw, highlight, elastic, rubber-band (9) |
| `loop/` | spin, pulse, heartbeat, glow (4) |
| `loading/` | progress, skeleton, typing, dots (4) |
| `transition/` | flip, rotate, morph, cross-fade, cross-slide, reorder (6) |
| `movement/` | parallax (1) |
| `organization/` | stagger, cascade (2) |

Total: **41 animations**, three files each (`description.md`, `attributes.md`, `appearance.md`).

Within the categories, entrance and exit are **families** (mirrored pairs): `fade-in`/`fade-out`, `slide-in`/`slide-out`, `zoom-in`/`zoom-out`, `scale-in`/`scale-out`, `bounce-in`/`bounce-out`, `pop-in`/`pop-out`, `collapse`/`expand`, `rotate`/`spin`, `pulse`/`heartbeat` are documented separately but described as one family driven by `direction` — the 41 documents could collapse to 32 family documents. `animations/index.md` keeps the category table, the tree, the family table and a prioritised list of candidate additions (not yet created).

Relative links inside an animation directory therefore use two levels: `../../index.md` for the animation overview, `../../<category>/<animation>/description.md` for an animation in another category, `../../../components/…` for areas outside `animations/`.

Shared attributes: `animation`, `duration`, `timingFunction`, `delay`, `iterationCount`, `direction`, `fillMode`, `playState`, plus `respectReducedMotion`.

Note: `gestures/shake` (input: user shakes the device) and `animations/shake` (output: element wobbles as feedback) are deliberately separate documents.

## 📦 Standardized Data (`docs/de/data/`)

| File | Content |
|------|---------|
| `index.md` | Overview, models table, data types, basic rules |
| `standards.md` | Which existing external standard covers which data area; each entry carries a verification status (✅ verified at RFC Editor / w3.org / schema.org, ⚠️ unverified, ❌ proven absent) |
| `mappings.md` | Our fields ↔ standard fields (JSContact RFC 9553, JSCalendar RFC 8984, vCard RFC 6350, ActivityStreams 2.0, schema.org); naming conflicts and open gaps |
| `formate.md` | JSON, NDJSON, YAML, TOML, CSV/TSV, XML, MessagePack, Parquet, Markdown frontmatter, ICS, VCF, GeoJSON, JSON Schema |
| `modelle.md` | User, Team, Message, Document, Block, Event, Task, Contact, Location, File, Tag, Comment, Notification, Revision, Integration |
| `felder.md` | ID, time, naming, communication, enums, permissions, metadata fields; null rules |
| `konventionen.md` | Naming, file sets, versioning, JSON Schema pattern, validation, i18n, accessibility data |
| `api.md` | Shared CRUD pattern, response envelope, pagination, filters, error format, sync, webhooks, SDKs |

Program `api.md` files document program-specific deviations from this pattern.

## 🔗 Cross-Linking Requirements

### Within a Program's Documentation

All 6 files should include cross-links to each other:

**In `menu.md`**:
- Link to features, description, structure, shortcuts, and api

**In `features.md`**:
- Link to menu, description, structure, shortcuts, and api

**In `description.md`**:
- Link to menu, features, structure, shortcuts, and api

**In `structure.md`**:
- Link to menu, features, description, shortcuts, and api

**In `shortcuts.md`**:
- Link to menu, features, description, structure, and api

**In `api.md`**:
- Link to all other files in the program's documentation

### Between Categories

- Link related programs across categories
- Link to related documentation in other languages
- Link to main documentation index

### Between Languages

- Each language directory should mirror the structure of others
- Cross-link between language versions where applicable

---

## 📝 Content Requirements by File Type

| Requirement | menu.md | features.md | description.md | structure.md | shortcuts.md | api.md |
|-------------|---------|-------------|----------------|--------------|--------------|--------|
| German language | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Cross-links | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Examples | Optional | Optional | Optional | Optional | ✅ | ✅ |
| Code snippets | Optional | Optional | Optional | Optional | Optional | ✅ |
| ASCII diagrams | Optional | Optional | Optional | ✅ | Optional | Optional |
| Tables | ✅ | ✅ | Optional | ✅ | ✅ | ✅ |
| Comparison tables | Optional | Optional | ✅ | Optional | Optional | Optional |

---

## 🚀 Adding a New Program

### Step-by-Step Process

1. **Determine the correct category** for the program

2. **Create the folder structure**:
   ```bash
   docs/[language]/apps/[category]/skins/[program-name]/
   ```

3. **Create the 7 required files**:
   - `index.md`
   - `menu.md`
   - `features.md`
   - `description.md`
   - `structure.md`
   - `shortcuts.md`
   - `api.md`

4. **Follow the template structure** from existing programs (reference: `docs/de/apps/wiki/skins/mediawiki/`)

5. **Add cross-links** in all files

6. **Update the category `skins/index.md`** with the new program entry

7. **Update the mkdocs.yml** navigation section if needed

8. **Test the documentation** locally with MkDocs

---

## 📚 Additional Notes

### Language Support

- German (`de/`) is the primary language
- English (`en/`) translations are maintained as needed
- French (`fr/`) translations are maintained as needed
- Other languages can be added by creating new subdirectories

### Documentation Maintenance

- Keep documentation up to date
- Update documentation when the program updates
- Fix broken links
- Add missing information

### Quality Standards

- Use clear, concise German
- Include examples where helpful
- Use tables for comparison and organization
- Include cross-links for easy navigation
- Follow the 6-file structure consistently

---

## 📞 Support

For questions or issues with the documentation:
- Check existing documentation
- Review similar programs' documentation
- Contact the FreeSynergy team

---

**Last Updated**: 2026-10-31
**Version**: 1.0
