# Wiki.js 3.1.1 — layout

Sources: `frontend/src/layouts/MainLayout.vue`, `frontend/src/components/HeaderNav.vue`, `NavSidebar.vue`, `PageActionsCol.vue`, `frontend/src/css/_theme.scss` (all at https://github.com/requarks/wiki/tree/3.1.1/frontend/src). Layout is partly set by the site's theme (see `themes/index.md`).

## Regions of the main layout

```
+------------------------------------------------------------------------+
| Header (w-header): logo/site title · search · create · library ·       |
|                    inbox (badge) · administration · login/account      |
+----------------+-------------------------------------------+-----------+
| Drawer         | Content                                   | Page      |
| (sidebar)      |  - page header, tags, last edited          | actions   |
|  - locale      |  - page body (view or editor)              | rail      |
|  - browse menu |  - Table of contents (position: theme)     | (48 px)   |
|  - nav tree    |                                            |           |
|  - Edit Nav    |                                            |           |
+----------------+-------------------------------------------+-----------+
```

The drawer is on the left by default. The theme setting `sidebarPosition` can put it on the right. The table of contents is placed by `tocPosition` (default `right`). The page rail width is `$rail-width: 48px` (`frontend/src/css/_theme.scss`). Sources: `backend/models/sites.ts` (theme defaults), `MainLayout.vue`.

## Header

| Element | Behaviour | Source |
|---------|-----------|--------|
| Home button | Goes to the site home page | `HeaderNav.vue` (`homePath`) |
| Search | Toggles a search row; aria label "Search..." | `HeaderNav.vue`, locale `common.header.search` |
| Create (+) | Opens the New Page menu with the active editors | `HeaderNav.vue`, locale `common.header.create`, `frontend/src/helpers/editors.js` |
| Library (museum icon) | Button labelled "Library"; target not checked | `HeaderNav.vue`, locale `common.header.library` |
| Inbox | Messages, watching, review queue; shows a badge | `HeaderNav.vue`, `routes.js` (`/_inbox/*`) |
| Administration (tools icon) | Admin area | `HeaderNav.vue`, locale `common.header.admin` |
| Login / Account | Login, or account menu with profile and logout | `HeaderNav.vue`, locale `common.header.login` |
| Locale selector | In the drawer, when the site has more than one locale | `MainLayout.vue` (`siteStore.locales.showMenu`) |

## Drawer (sidebar)

- Top: locale selector button and a "Browse" button (sitemap icon) that opens a browse menu (`NavBrowseMenu.vue`).
- Middle: the navigation tree (`NavSidebar.vue`). Items come from the site's navigation (admin "Navigation").
- Bottom: "Edit Nav" button, shown only to users who may edit navigation (`NavEditMenu.vue`, `NavEditOverlay.vue`).
- Narrow screens: the drawer becomes an overlay. The button to open it is at the bottom left of the screen, not the top (`MainLayout.vue` comment on `corner-btn`). Verified in source.
- The drawer has a "mini" variant with icon-only buttons (`sidebar-mini` class).

## Content area

- Page view with the title and body. Route `/:catchAll(.*)*` renders every page path through `pages/Index.vue`.
- Editor view: the same route with `/_edit/<path>`; `/_create/<editor>` for a new page.
- Version view: `/_version/:versionId`, read-only (`PageVersion.vue`).
- Error view: `/_error/:action?`.
- Live notes: `/n/:noteKey`, layout `LiveNoteLayout.vue`.
- Search results: `/_search`. Tag browser: `/_tags`. Public user page: `/_user/:userId`.

A breadcrumb component exists (`frontend/src/components/shared/WBreadcrumbs.vue`), but its use on the page view was not checked. The old page's breadcrumb claim is unverified.

## Page actions rail (right edge, 48 px wide)

From `PageActionsCol.vue`. Buttons are square and icon-only with an `aria-label`:

| Button | aria-label | Handler (function name in the file) |
|--------|-----------|-------|
| Page properties | "Page Properties" | `togglePageProperties`, side dialog `PagePropertiesDialog` |
| Page data | "Page Data" | `togglePageData`, side dialog `PageDataDialog` |
| History | "Page History" | `viewPageHistory` |
| Source | "Page Source" | `viewPageSource` |
| Actions (…) | "Page Actions" | menu with `convertPage` (`PageConvertDialog`) and `rerenderPage` (`RerenderPageDialog`), shown only when the user may write |
| Duplicate | "Duplicate Page" | `duplicatePage` |
| Rename / move | "Rename / Move Page" | `renamePage` (tree browser dialog) |
| Delete | "Delete Page" | `deletePage` (`PageDeleteDialog`) |

The Markdown, AsciiDoc and Visual editors have their own insert rail on the left of the editor, same width token (`$rail-width`). Whether the page rail is shown unchanged in editor mode was not checked. Sources: `PageActionsCol.vue`, `frontend/src/css/_theme.scss`.

## Editor layout

- Markdown and AsciiDoc: Monaco editor with a preview pane. Preview scroll is synchronised (`frontend/src/composables/previewScrollSync.js`).
- Visual: ProseMirror document with a block menu (slash) and a formatting toolbar (`frontend/src/editor/visual/bar.js`).
- Excalidraw and Feedback: component files exist (`EditorExcalidraw.vue`, `EditorFeedback.vue`, `EditorFeedbackConfigOverlay.vue`); their layout was not read.

Exact pane proportions and toolbar contents were not measured. Unverified.

## Accessibility notes from source

- Icon-only buttons carry `aria-label` (checked in `HeaderNav.vue`, `PageActionsCol.vue`).
- Keyboard focus and a "skip" mechanism were not checked. Unverified.

## Not verified

- Responsive breakpoints in pixels. The layout uses `composables/screen.js`; the numbers were not read.
- Print layout (`frontend/src/css/_print.scss` exists; not read).
