# Wiki.js 3.1.1 — menus

Sources: `frontend/src/routes.js` and components named below, at https://github.com/requarks/wiki/tree/3.1.1/frontend/src. The old page's menu list (Pages, Editor, Trash, Media, Users, Groups, Access, Settings, Appearance, Extensions, Logs, Search) is replaced by the list below, because those names do not match the 3.1.1 UI.

## Top header menu

| Entry | Who sees it | Target | Source |
|-------|-------------|--------|--------|
| Home | everyone | site home page | `HeaderNav.vue` |
| Search | everyone | search row, then `/_search` | `HeaderNav.vue` |
| Create (+) → New Page | users with write rights | pick an active editor, then `/_create/<editor>` | `HeaderNav.vue`, `helpers/editors.js` |
| Library | not checked | not checked | `HeaderNav.vue` |
| Inbox | logged-in users | `/_inbox/messages`, `/_inbox/watching`, `/_inbox/review/:id?` | `routes.js` |
| Administration | users with admin access | `/_admin` | `HeaderNav.vue`, `routes.js` |
| Login | guests | `/login` | `HeaderNav.vue` |
| Account | logged-in users | `/_profile/*` and logout | `HeaderNav.vue` |

## Drawer menus

| Menu | Content | Source |
|------|---------|--------|
| Locale | list of site locales | `locale-selector-menu` in `MainLayout.vue` |
| Browse | tree browser for folders and pages | `NavBrowseMenu.vue` |
| Edit Nav | navigation editing: add, edit, delete items | `NavEditMenu.vue`, `NavEditItemMenu.vue`, `NavEditOverlay.vue` |

## Page actions rail

Listed in `layout.md`. The "Actions (…)" button opens a menu that contains `Convert Page` and `Rerender Page`, each shown only when the user has write rights. Source: `PageActionsCol.vue`.

Other items in the rail: Duplicate, Rename / Move, Delete, and the view buttons Page Properties, Page Data, History, Source.

## Profile menu (`/_profile/*`)

| Section | Route | Source |
|---------|-------|--------|
| Info | `/_profile/info` | `routes.js` |
| Avatar | `/_profile/avatar` | `routes.js` |
| Authentication (passwords, 2FA, passkeys) | `/_profile/auth` | `routes.js` |
| Groups | `/_profile/groups` | `routes.js` |
| Live notes | `/_profile/notes` | `routes.js` |
| Access tokens | `/_profile/tokens` | `routes.js` |
| Notifications | `/_profile/notifications` | `routes.js` |

## Inbox (`/_inbox/*`)

| Tab | Route | Content |
|-----|-------|---------|
| Messages | `/_inbox/messages` | notifications |
| Watching | `/_inbox/watching` | pages the user watches |
| Review | `/_inbox/review/:submissionId?` | suggested edits and approvals (reviewers) |

## Administration (`/_admin/*`)

Every section below is a route in `frontend/src/router/routes.js`. Per-site sections take a `:siteid` segment. Permission checks are on the server (`permissions: ['access:admin']` is the example seen in `backend/api/pages.ts`).

| Group | Sections (route name) |
|-------|-----------------------|
| Overview | Dashboard (`dashboard`), Sites (`sites`) |
| Site (`:siteid/…`) | General, Approvals, Analytics, Blocks, Comments, Editors, Locale, Login, Navigation, Storage, Theme |
| Accounts | Auth (`auth`), Groups (`groups`), Users (`users`), SCIM (`scim`) |
| Integration | API (`api`), MCP (`mcp`), Webhooks (`webhooks`) |
| System | Audit, Extensions, Icons, Instances, Mail, Metrics, Notifications, Rendering, Scheduler, Search, Security, System, Terminal, Utilities, Flags |

## Context menus

| Context | Items | Source |
|---------|-------|--------|
| Editor insert (Monaco, Markdown) | bold, italic, header level, and Monaco's own context actions | `EditorMarkdown.vue` (`editor.addAction`) |
| Visual editor block menu | slash menu items | `frontend/src/editor/visual/slash.js` |
| Code block menu | code block actions | `frontend/src/components/EditorCodeBlockMenu.vue` |
| Emoji menu | emoji picker | `frontend/src/components/EditorEmojiMenu.vue` |
| Tab block (visual) | new tab, remove tab, remove tab set | locale `editor.visual.tabs.*` |

## Menus by role

Menus are filtered on the client and checked again on the server. Examples verified in source:

| Menu item | Requirement | Source |
|-----------|-------------|--------|
| Rerender Page, Convert Page | `write:pages` | `PageActionsCol.vue` |
| Administration | admin access | `HeaderNav.vue`, `routes.js` |
| Edit Nav | rights to edit navigation | `MainLayout.vue` (`showEditNav`) |
| Create (+) | write rights for at least one active editor | `HeaderNav.vue` (not read line by line) |

Guests (not logged in) see suggested-edit actions instead of editing actions (locale `common.actions.suggestEdits`).

## Not verified

- The full list of entries under the Library button.
- Exact item order in each menu.
- Whether the Trash lives in the admin area only. The locale string says deleted pages can be restored "from the administration area".
