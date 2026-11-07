# Pipedrive - Structure & UI/UX

## Overview

Pipedrive shows the navigation bar on the left, the filter and action buttons at the top, and the active view in the middle: pipeline board, list or schedule. A clicked deal opens a detail area as an overlay above the list. Configuration dialogs appear as centered panels with a form.

## Window structure

### Pipeline board (deals)

```
+---------------------------------------------------------------------------+
| Logo | Left navigation | Filter bar | [Add] | Avatar | Setup            |
+---------------------------------------------------------------------------+
| Filter: Pipeline | Stage | Owner | Amount | Close period                 |
+---------------------------------------------------------------------------+
|  Stage A        |  Stage B        |  Stage C        |  Won    |  Lost     |
|  +------------+ |  +------------+ |  +------------+ |         |           |
|  | Deal 1     | |  | Deal 4     | |  | Deal 7     | |         |           |
|  | Amount     | |  | Amount     | |  | Amount     | |         |           |
|  | Close      | |  | Close      | |  | Close      | |         |           |
|  +------------+ |  +------------+ |  +------------+ |         |           |
|  Total: ...     |  Total: ...     |  Total: ...     |         |           |
+---------------------------------------------------------------------------+
```

### Deal detail area (overlay)

```
+---------------------------------------------------------------------------+
|  Deal title                     [Edit] [Duplicate] [Delete] x            |
+------------------------+--------------------------------------------------+
|  Fields:               |  Tabs: Overview | Activities | Files             |
|  Amount, Stage, Date   |  Products | Team & Access                        |
|  Owner, Source         |                                                    |
|  Custom fields         |  Activity log (emails, calls, tasks)              |
|                        |  [+ Add activity]                                 |
+------------------------+--------------------------------------------------+
```

### Company setup (admin)

```
+---------------------------------------------------------------------------+
|  Setup header (Back)                         [Save]                       |
+------------------+--------------------------------------------------------+
|  Setup navigation|  Settings form                                         |
|  - Pipelines     |  field by field, help text on the right               |
|  - Custom Fields |  table for field and user management                  |
|  - Users         |                                                        |
+------------------+--------------------------------------------------------+
```

## Areas

| Area | Position | Content |
|---------|----------|--------|
| Navigation bar | Left | Home, Activities, Deals, Mailbox, Products, Marketing, Reports, More |
| Header | Top right | "Add" action button, search field, avatar menu, setup icon |
| Filter bar | Below the header | Pipeline, stage, owner, amount, period, saved filters |
| Board area | Center | stage columns with deal tiles, column totals |
| List view | Center | table with columns, sorting, page numbers |
| Detail area | Overlay on the right or centered | fields, tabs, activity log, relationships |
| Messages | Top right | success, errors, sync status |

## UI/UX

### Design principles

- **Pipeline as main metaphor**: everything points to stage, amount and close date
- **Fewer fields, more context**: the standard field set is deliberately small; extensions via custom fields
- **Action directly on the object**: activities and emails visibly attached to the deal
- **Short paths**: create records via an action button from every view

### Color scheme and themes

- **Light, uniform** across all views; no selectable dark mode in the interface (version-dependent)
- **Stage colors** and status colors for Won/Lost are predefined
- **Accent color** in buttons and links, status green for completed activities
- **Icons** per activity type and module

### Typography

- **Tile fonts** with title, amount and date in a clear hierarchy
- **Tables** compact, numbers right-aligned, amounts in currency format
- **Forms** with labels above the field and help texts

### Interactions

- **Drag & drop**: drag a deal tile between stage columns; change column order in setup
- **Hover**: the tile shows actions (edit, duplicate, change owner)
- **Animations**: brief fade-in of the detail area, move transition of the tile, skeleton placeholders while loading
- **Inline editing**: amounts and selection fields editable directly in the list (version-dependent)
- **Autocomplete**: contact, company and deal search in relationship fields
- **Confirmation dialog** when moving to "Lost", with reason selection

### Responsive design

- **Desktop**: full board with all columns, horizontal scrolling with many stages
- **Tablet**: navigation bar reduced, board with fewer columns
- **Mobile**: card-style lists instead of the board, detail area full screen; for daily work the native apps are the recommended option
- **Setup areas** usable on small screens as stacked forms

### Accessibility

- **Tab order** follows navigation, filter bar, tiles, detail area
- **`Esc`** closes the detail area and dialogs
- **Arrow keys** in selection lists and autocomplete suggestions
- **Focus indicator** visible; contrast high in standard views
- **Screen reader**: areas are labeled, but board tiles remain dense; the alternative list view is simpler
- **Zoom**: browser zoom without cut-off controls

### Performance

- **Single page application**: module switch without full page rebuild
- **Loading in sections**: long deal lists are loaded in chunks
- **Caching**: contacts and organizations stored locally in the client, email sync in the background
- **Recommendation**: set filters instead of loading very many tiles at once; use custom fields sparingly

## See also

- [menu.md](menus.md) - Menu items by role
- [features.md](features.md) - Modules and automation
- [shortcuts.md](shortcuts.md) - Keyboard control
- [api.md](api.md) - REST API and webhooks
