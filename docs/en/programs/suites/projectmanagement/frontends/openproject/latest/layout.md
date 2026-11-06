# OpenProject - Structure & UI/UX

## Overview

OpenProject uses a classic three-area layout: a narrow header with the project
selector, a left module bar, a large content area. Work packages extend this frame
with a right detail split (tab view) and an optional full-screen table.

## Window structure

### Main layout

```
+------------------------------------------------------------------+
| Bar: [Switch project v] [Search]         [Bell] [Avatar v]       |
+----------+-------------------------------------------------------+
| Module   |  Content (module)                                     |
| bar      |  +--------------------------------------------------+ |
|          |  | Filter bar / query tools                        | |
| Overview |  +--------------------------------------------------+ |
| Activity |  |                                                  | |
| Milestones| | Table / Gantt / board / wiki                   | |
| Work pkgs | |                                               | |
| Board    |  |                                                  | |
| Gantt    |  +--------------------------------------------------+ |
| Wiki ... |  | Pagination                                       | |
+----------+-------------------------------------------------------+
```

### Work package view with detail split

```
+------------------------------------------------------------------+
| Bar / module bar (as above)                                      |
+--------------------------------------------+---------------------+
|  Table or list view                       |  Detail split       |
|  [WP number] [Title] [Status] [Date]      |  Tabs:              |
|  [x] Order A  ...                         |  Details | Activi-  |
|  [ ] Order B  ...                         |  ties | Comments    |
|                                           |  Transition buttons |
+--------------------------------------------+---------------------+
```

### Area table

| Area | Position | Content |
|------|----------|---------|
| Header bar | top | project selector, global search, notifications, user menu |
| Module bar | left | modules of the selected project, expandable, collapsible on mobile |
| Query tools | above content | filters, sorting, grouping, column choice, saving |
| Main content | middle | table, Gantt, board, wiki content, meeting list |
| Detail split | right | work package details, activities, comments (collapsible) |
| Footer | bottom | version number, privacy/imprint links (configurable) |

## UI/UX

### Design principles

- **Modularity**: every topic is its own module with its own URL and its own menu item
- **Table centricity**: bulk editing via inline-editable tables instead of a flood of dialogs
- **Split screen instead of modal**: context stays visible when a work package is opened
- **Permission-driven UI**: actions that are not allowed are hidden, not merely disabled

### Colour scheme and themes

- **Light default UI** with a blue accent colour
- **Dark colour scheme** (dark mode) selectable; further custom themes via the instance settings (version-dependent)
- **Custom theme**: admins can adjust the instance's colour palette
- Status and priority colours are configurable via enumerations

### Interactions

- **Inline editing**: cells in tables directly editable, save with Tab/Enter (version-dependent)
- **Drag & drop**: Gantt bars, board cards, wiki structure (order version-dependent)
- **Tabs and expand/collapse**: detail split, filter bar and module bar are collapsible
- **Animations**: subtle transitions when opening the detail split, skeleton/loading indicators; no elaborate effects
- **Autocomplete**: user, version and project selection fields with suggestions

### Responsive design

- **Desktop**: full three-column layout with detail split
- **Tablet**: module bar collapsible, detail view as a full page
- **Mobile**: hamburger menu, tables reduce to a card layout, boards scroll horizontally
- Own native apps are missing; the web view is optimised for touch

## Accessibility

- **Focus control**: keyboard focus follows the tab order through bar, filters, table
- **Screen readers**: basic ARIA labels on filters and tables (expanded per version, state version-dependent)
- **Contrast**: dark scheme and configurable colours improve contrast; WCAG adjustments are a recurring roadmap topic
- **Scaling**: the UI scales with browser zoom without loss of function

## Performance

- **Server-side pagination**: tables and activities loaded chronologically in pages (default page 30, configurable, version-dependent)
- **Caching**: Rails asset caching plus an optional cache store (file/memcached); instance configuration recommended
- **Lazy loading**: activity stream and boards refresh via polling/WebSocket parts (version-dependent)
- **Free tip**: saved queries with narrow filters keep the table view fast
