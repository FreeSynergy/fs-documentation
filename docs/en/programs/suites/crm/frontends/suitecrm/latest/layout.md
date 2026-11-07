# SuiteCRM - Structure & UI/UX

## Overview

SuiteCRM 7.x shows a menu bar at the top, below it the module view (list, detail, form) and, if needed, a filter panel on the left. SuiteCRM 8 places an Angular application around the same views: its own header, a module menu via a dropdown, and content in its own panel area. The basic logic stays the same: list → detail → edit.

## Window structure

### List view (SuiteCRM 7.x)

```
+--------------------------------------------------------------------------+
| Logo | Main menu (Home, Activities, Leads, Opportunities, ...) | Admin | User |
+--------------------------------------------------------------------------+
| Breadcrumb: Leads > all Leads   [Search] [Sort] [Page size]              |
+------------------+-------------------------------------------------------+
| Filter panel     |  List (table)                                         |
| - Field filters  |  [ ] Name      Company    Stage      Owner      ...   |
| - Saved          |  [x] Meyer AG  ...        Proposal   ...              |
|   filters        |  [ ] ...                                              |
| - Mass actions   |                                                       |
| - Field selection|  [Browse results: < 1 2 3 >]                          |
+------------------+-------------------------------------------------------+
```

### Detail view with subpanels

```
+--------------------------------------------------------------------------+
|  Record title (name)             [Edit] [Duplicate] [Delete]             |
+--------------------------------------------------------------------------+
|  Field area (2 columns)                                                  |
|  Status: New          Phone: ...          Email: ...        Industry: ... |
+--------------------------------------------------------------------------+
|  Subpanel: Contacts          | Subpanel: Notes        | Subpanel: History |
|  [+ Add entry]               | [+ Note]               | (timestamp)       |
+--------------------------------------------------------------------------+
```

### SuiteCRM 8 (Angular shell)

```
+--------------------------------------------------------------------------+
|  App header: module menu / module search    |   Personal menu             |
+--------------------------------------------------------------------------+
|  Home area with cards (modules)                                          |
|  +-------------------+   +-------------------+   +-------------------+   |
|  | Leads             |   | Opportunities     |   | Cases             |   |
|  +-------------------+   +-------------------+   +-------------------+   |
|  Content panel: embedded view of the selected module                     |
+--------------------------------------------------------------------------+
```

## Areas

| Area | Position | Content |
|---------|----------|--------|
| Main menu bar | Top | modules as dropdowns, admin menu, user menu |
| Breadcrumb / title bar | Below the menu bar | current area, search, view options |
| Filter panel | Left | field filters, saved filters, mass actions, column selection |
| List | Center | table with sort and selection checkboxes, pagination |
| Detail area | Center | field pairs, status, relationships |
| Subpanels | Below the fields | linked records of other modules |
| Dashlets | Home page | small panels with tasks, activities, charts |
| Messages | Top center | success and error messages after saving |

## UI/UX

### Design principles

- **Module mindset**: every data type follows the same three-step sequence: list, detail, form
- **Administrators instead of developers**: Studio and the filter panel make customization possible without code
- **Data first**: dense tables, many columns, few decorative elements
- **Horizontal menus with dropdowns** instead of a permanent sidebar (7.x)

### Color scheme and themes

- **Default theme "SuiteP"** (7.x) with a light table area and a blue menu bar
- **SuiteCRM 8** ships its own modern theme for the Angular shell (name version-dependent)
- **Theme per user**: switchable in personal settings (if installed)
- **Own themes** via theme directories and CSS; no dark mode out of the box in 7.x (version-dependent in 8.x)

### Typography

- **Tables and forms** in the system font, 12 to 14 pixels
- **Field labels** bold, values normal; required fields marked with an asterisk
- **Charts** in dashlets with labeled axes

### Interactions

- **Hover**: row highlighting in lists; icon buttons appear on hover
- **Click**: a row opens the detail view; Edit opens a form with Save or Cancel
- **Drag & drop**: only on the dashboard to sort dashlets, not in lists
- **Animations**: sparing; expanding/collapsing the filter panel and subpanels, progress bars for imports
- **Form validation**: client and server checks, error message above the field
- **Autocomplete**: person and company search in relationship fields

### Responsive design

- **Desktop**: full width with filter panel and many columns
- **Tablet**: menu bar stays, fewer columns
- **Mobile**: switchable responsive or compact theme, menus as collapsible menus, subpanels stacked
- **SuiteCRM 8** is responsive from the ground up, more so than 7.x; older views may scroll horizontally on small screens

### Accessibility

- **Tab order** follows the form and table structure; checkboxes and buttons can be operated with the space bar
- **Esc** cancels dialogs and popups (version-dependent)
- **Screen reader**: labels present, but tables with many columns are dense for screen readers; ARIA support is better in 8.x than in 7.x
- **Contrast and font size** scalable via browser zoom
- **Keyboard shortcuts**: none specific to the application, see [shortcuts.md](shortcuts.md)

### Performance

- **Server-side caching** of metadata and templates, caches in the installation directory (`cache/`)
- **Pagination** (default 10 to 30 rows) and optional column selection keep lists fast
- **Full-text search** can be slow on large data sets; database indexes and maintenance jobs help
- **Recommendation**: run the scheduler via `cron.php`, clear the cache after updates, disable unused modules

## See also

- [menu.md](menus.md) - Menu items by role
- [features.md](features.md) - Modules and automation
- [shortcuts.md](shortcuts.md) - Keyboard control
- [api.md](api.md) - REST and SOAP
