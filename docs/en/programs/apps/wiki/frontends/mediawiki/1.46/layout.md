# MediaWiki 1.46 — Layout (Vector 2022, default skin)

Sources: Vector 2022 templates and components in the REL1_46 skin repository (https://github.com/wikimedia/mediawiki-skins-Vector/tree/REL1_46): `includes/templates/skin.mustache`, `Header.mustache`, `MainMenu.mustache`, `PageTools.mustache`, `includes/SkinVector22.php`, `includes/Components/*`. Layout dimensions from `resources/skins.vector.styles/variables.less`.

The layout below is the structure of the rendered page. Positions are described as Vector places them on a desktop screen. Verified against the template, not against a screenshot.

## Regions (top to bottom, left to right)

```
+-------------------------------------------------------------------------+
| Header: [menu toggle] [logo]   [search box]   [appearance] [languages] [user links] |
+-----------+-------------------------------------------------------------+
| Main menu | Site notice                                                  |
| (sidebar, | Page titlebar: <h1 title>        [TOC toggle]               |
| pinnable) | Page toolbar: views (Read | Edit | History ...) | tools menu  |
|           | +--------------------------------------------------------+ |
| TOC       | | Subtitle / user messages                                | |
| (pinnable,| | Body (mw-body / vector-body), wikitext rendered          | |
| left of   | | Categories (below the body)                              | |
| content)  | | Language list (optional, bottom of content)              | |
|           | +--------------------------------------------------------+ |
|           | Footer (info, copyright, links)                               |
+-----------+-------------------------------------------------------------+
  Bottom dock (optional, fixed at the bottom); sticky header (appears on scroll)
```

## Named parts (template partials)

| Part | Template | What it holds | Notes |
|------|----------|---------------|-------|
| Header | `Header.mustache` | Logo, search, personal tools, language entry | Language button is shown when the ULS extension is loaded and languages are shown in the header (`SkinVector22.php`, `shouldHideLanguages`) |
| Main menu | `MainMenu.mustache`, `MainMenuPinned.mustache`, `MainMenuDropdown.mustache` | Navigation sidebar | Pinned or hidden per preference `vector-main-menu-pinned` |
| Search | `SearchBox.mustache` | Search input with suggestions (typeahead) | Search input carries access key `f` (see `shortcuts.md`) |
| Titlebar | `PageTitlebar.mustache` | Page title, tagline, subtitle | |
| Toolbar | `PageToolbar.mustache` | Views (read, edit, history) and actions | Labels of the p-tb and p-cactions menus revised in `VectorComponentPageTools.php` |
| Tools | `PageTools.mustache` | Tools menu, pinned to the right when enabled | Preference `vector-page-tools-pinned` |
| Appearance | `Appearance.mustache` | Text size, width, theme | Preferences `vector-font-size`, `vector-limited-width`, `vector-theme` (`doc/configuration/configuration.md`) |
| TOC | `TableOfContents.mustache` | Section list of the current page | Pinnable; collapses when the page has at least 28 sections by default (`wgVectorTableOfContentsCollapseAtCount` = 28, `configuration.md`) |
| Body | `skin.mustache` `#bodyContent` | Rendered page HTML | Sections are anchor targets |
| Categories | `html-categories` slot | Category list under the body | |
| Footer | `Footer.mustache` | Info and links | |
| Sticky header | `StickyHeader.mustache` | Header that stays on scroll | Only present when `data-vector-sticky-header` is set |
| Bottom dock | `BottomDock.mustache` | Optional bottom bar | |

## Widths and spacing (Vector 2022 variables)

| Variable | Value | Meaning |
|----------|-------|---------|
| `@max-width-page-container` | 1596px (`unit(1596px / 16, rem)`) | Outer container limit |
| `@max-width-content-container` | 948px | Article column limit (default; limited-width preference) |
| `@padding-horizontal-page-container-desktop` | 44px | Side padding on desktop |
| `@height-header` | 50px | Sticky header height |
| `@max-width-search` | 500px | Search box limit |
| `@grid-column-gap` / `@grid-row-gap` | 24px | Layout gaps |
| `@scroll-margin-heading` | 75px | Offset when jumping to a heading |
| `@min-width-supported` | 300px | Below this width the layout scrolls horizontally |
| `@font-size-browser` | 16 | Base assumption for px-to-rem |

Source: `resources/skins.vector.styles/variables.less`.

## Responsive behaviour

- Vector 2022 has a responsive variant behind an experimental flag (`wgVectorResponsive`), documented as experimental and not to be relied on (`configuration.md`).
- Narrow screens: the main menu and TOC become drawers or hide (behaviour from `skin.js`, `pinnableElement.js`; exact breakpoints unverified).

## What our frontend needs from this

- A three-column desktop grid with a pinnable left navigation and an optional right tools rail.
- A header with search, language and user area.
- A toolbar row with view tabs and a tools menu.
- A content column with a 948px-equivalent maximum width.
- A sticky header on scroll (optional).

Items marked "unverified" in this file were not checked against a rendered page.
