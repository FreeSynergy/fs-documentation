# Wiki.js 3.1.1 — themes

Appearance is per site and is stored in the database, not in a theme file. The admin page is Admin → Theme (`frontend/src/pages/AdminTheme.vue`, route `:siteid/theme`). Defaults come from `backend/models/sites.ts`. Source tree: https://github.com/requarks/wiki/tree/3.1.1

No theme file format, theme marketplace or per-user theme was found in the 3.1.1 source. A user can only choose light or dark through the UI if the site allows it (not verified; the admin page has a site-wide `dark` switch).

## Settings (`theme` block of a site)

| Key | Type / values | Default | What it changes | Source |
|-----|---------------|---------|-----------------|--------|
| `dark` | boolean | `false` | dark colour scheme | `AdminTheme.vue` ("darkMode" toggle), `sites.ts` |
| `colorPrimary` | colour | `#1976D2` | `--color-primary` (buttons, links, accents) | `sites.ts`, `tailwind.css` |
| `colorSecondary` | colour | `#02C39A` | `--color-secondary` | same |
| `colorAccent` | colour | `#FF9800` | `--color-accent` | same |
| `colorHeader` | colour | `#000000` | `--color-header` (top bar) | same |
| `colorSidebar` | colour | `#1976D2` | `--color-sidebar` (drawer) | same |
| `baseFont` | `inter`, `opensans`, `montserrat`, `roboto`, `rubik`, `tajawal`, `user` | `roboto` | UI font | `AdminTheme.vue` (`fonts`), `sites.ts` |
| `contentFont` | same list | `roboto` | page body font | same |
| `contentWidth` | `full`, `centered` | `full` | width of page content | `AdminTheme.vue` (`widthOptions`), `sites.ts` |
| `sidebarPosition` | `left`, `right` | `left` | side of the drawer | `MainLayout.vue`, `sites.ts` |
| `tocPosition` | `off`, `left`, `right` (the admin list) | `right` | table of contents placement | `AdminTheme.vue` (`rightLeftOptions`), `sites.ts` |
| `codeBlocksTheme` | highlight.js style name (247 options in the admin list) | `github-dark` | code block colours | `AdminTheme.vue` (`codeThemes`), `sites.ts`, `highlight.js` 11.12.0 in `frontend/package.json` |
| `showPrintBtn` | boolean | `true` | print button | `sites.ts` |
| `showPageProgress` | boolean | `true` | reading progress bar | `sites.ts` |
| `pageTransitions` | boolean | `true` | view transitions between pages | `sites.ts` |
| `injectCSS` | text | empty | custom CSS added to every page | `sites.ts` |
| `injectHead` | text | empty | custom HTML in `<head>` | `sites.ts` |
| `injectBody` | text | empty | custom HTML at the end of `<body>` | `sites.ts` |

`injectCSS`, `injectHead`, `injectBody` are the way to add custom styling or markup. They are edited on the admin Theme page (`AdminTheme.vue`, fields at lines ~336 and ~352). Who may edit them and whether they are sanitised was not checked.

The UI font list includes `user`, which means each user's own font choice (`fontUserDefaults` locale string).

## Colour system

- Five brand colours (`primary`, `secondary`, `accent`, `header`, `sidebar`) are written at runtime as CSS custom properties `--q-<name>` (`frontend/src/helpers/cssVars.js`).
- Tailwind 4 tokens in `frontend/src/css/tailwind.css` map `--color-<name>` to those properties. Derived tints are `color-mix(...)` of the brand colour with white (`--color-primary-light`, `--color-primary-lighter`, `--color-secondary-lighter`, `--color-sidebar-light`).
- Fixed neutrals: `--color-white`, `--color-black`, `--color-cancel` (`#616161`), and a dark ramp `--color-dark` to `--color-dark-6` (`#0d1117`, `#343b48`, `#292f39`, `#1e232a`, `#161b22`, `#070a0d`). Source: `tailwind.css`.
- SCSS brand defaults in `frontend/src/css/_theme.scss` are the Quasar-era values (`$primary: #1976d2` and others). They are overwritten by the database values at runtime.
- `_palette.scss` holds the Material colour ramp used by older stylesheets.

### Dark mode

- Dark mode is the `body--dark` class on `<body>` (`frontend/CLAUDE.md`).
- A panel that is always dark in both themes uses `.w-dark-surface` (`frontend/CLAUDE.md`).
- `dark:` Tailwind variant keys off `body--dark` (`frontend/CLAUDE.md`).

## Typography

- Font families come from the six choices above. The font files are served from the instance (`frontend/public/_assets/…`). File list and licences were not checked. Unverified: whether the font files are shipped or loaded from a CDN.
- Headings, body, and code sizes: not extracted. The 3.1.1 stylesheets are `frontend/src/css/_base.scss`, `_page-contents.scss`, and `_page-contents-asciidoc.scss`. Not read in full.

## Spacing and layout metrics

| Metric | Value | Source |
|--------|-------|--------|
| Page rail width | `$rail-width: 48px` | `frontend/src/css/_theme.scss` (comment: width of the page actions rail and the editor insert rail; also the height of rail buttons, `h-12`) |
| Content width | `full` or `centered` (theme) | `sites.ts` |
| Drawer width | set in `MainLayout.vue` (`sidebarWidth`); value not extracted | `MainLayout.vue` |
| Spacing scale | Tailwind default is assumed; the file `tailwind.css` was not read for a custom scale | unverified |

## What can be rebuilt in a FreeSynergy frontend in this style

| Element | Rebuildable | Notes |
|---------|-------------|-------|
| Five brand colours plus neutral ramp | yes | Use the same five roles: primary, secondary, accent, header, sidebar. |
| Light and dark scheme | yes | Use a class on the root element; keep the "always-dark panel" rule. |
| Content width switch (full, centered) | yes | Behaviour only. |
| Drawer side (left or right) | yes | Behaviour only. |
| Table-of-contents position | yes | |
| Code block highlight theme | yes | Use any highlighter; name list not copied. |
| Six font choices | yes | Use our own font list. Check the licence of each font before shipping. |
| Custom CSS, head, body injection | yes, but as an admin feature | Keep it admin-only. |
| Exact pixel values, easing, shadows | not extracted | Do not copy; measure our own design. |

Rule for FreeSynergy: take the settings and the roles, not the CSS text. No stylesheet is copied (ADR 0013).
