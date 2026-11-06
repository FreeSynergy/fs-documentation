# Redmine - Structure & UI/UX

## Overview

Redmine shows a vertical standard layout: a narrow header line with tabs and search,
below it a breadcrumb and project tab bar, then the content area with a form or table.
Right margin columns for project info and actions are module-specific. The UI follows a
functional, content-centred style without single-page mechanics.

## Window structure

### Main layout

```
+----------------------------------------------------------------+
| Redmine | My page | Projects | Administration            [Search] |
+----------------------------------------------------------------+
| Project name > (breadcrumb)                                    |
| [Overview][Activity][Issues][Time][Wiki] ...                   |
+----------------------------------------------------------------+
|                                                              |
|  Content area (table, form, issue view)                      |
|                                                              |
|  +--------------------------------------------------------+  |
|  | Filter bar / column headers                           |  |
|  | Issue list with status, tracker, assignee, date       |  |
|  +--------------------------------------------------------+  |
|  | Pagination (pages 1..n, hit counter)                  |  |
|                                                              |
+---------------------------------------------+----------------+
|                                              | Margin column  |
+----------------------------------------------+---------------+
| Footer line: Redmine version, theme note                     |
+-------------------------------------------------------------+
```

### Issue detail view

```
+-------------------------------------------------------------+
| #1234 Title of the issue         [Edit] [Delete]            |
+---------------------------------------------+---------------+
| Journal (comments, field changes)           | Details block |
| - by Anna, 2 days ago: status New -> In     | Tracker       |
|   Progress                                  | Status        |
| - note field (Textile/Markdown)             | Priority      |
|                                             | Assignee      |
| Save note                                   | Version       |
+---------------------------------------------+---------------+
```

### Area table

| Area | Position | Content |
|------|----------|---------|
| Header line | top | main tabs, user menu, search field |
| Breadcrumb + tabs | below it | project path, module tabs, project-internal actions |
| Content area | middle | lists, forms, issue detail, wiki text |
| Margin column | right | details block (issue), project info, "links" |
| Footer line | bottom | version and theme note (changeable per theme) |

## UI/UX

### Design principles

- **Content before decoration**: tabular density, small type, many fields per screen
- **Server-rendered**: every action is a page call; state lives in URLs (deep-linkable)
- **One theme, many adjustments**: base layout stable, presentation entirely swappable via CSS

### Colour scheme and themes

- Default theme "Classic" (light, grey-blue), further themes in the theme folder (`public/themes/`)
- No dark mode in the core; dark schemes as theme plugins (version-dependent)
- Status/priority colours can be adjusted via CSS or themes

### Interactions

- **Forms with inline validation**: errors appear at the top of the page
- **Autocomplete** for user/project/version fields while typing
- **No drag & drop in the core**: sorting via column headers and forms (Gantt actions only as a plugin)
- **Animations**: practically none; page changes happen without transitions
- **Popups**: small JS popups for the time-tracking quick form; otherwise normal pages

### Responsive design

- **Responsive since Redmine 3.x**: viewport breakpoints for lists and forms
- **Mobile**: tabs wrap, tables scroll; operation usable, but dense tables take getting used to
- Own mobile apps are plugin/third-party territory

## Accessibility

- **Skip link "skip to content"** at the top of the page
- **Tab order** follows the DOM order; forms fully operable by keyboard
- **No consistent ARIA improvements**: screen readers get the table structure, but few roles/labels (retrofitting version-dependent)
- **Contrast**: standard Classic is weak; for WCAG an adjusted theme is advisable

## Performance

- **Server-side pagination**: standard 25/30 rows per page, configurable via settings
- **Column choice** reduces the load time of large issue lists
- **Caching**: Rails fragment caching; scaling primarily via the app server and database caching
- **Scales poorly**: cross-project queries and reports without restrictive filters slow down large instances
