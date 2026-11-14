# Notion - Menu Items

> **Status 2026-11-14:** Everything below rests on official help pages (S-numbers as in [index.md](../index.md)). The unverified "Earlier draft" of this file (Workspace, Pages, Users, Integrations, Resources, Preferences, a shortcut table) was removed from `latest/` on 2026-11-14; the folder [2026-11-07](../2026-11-07/menus.md) is frozen and was not touched.

## Verified menus and context menus

Right-click: the help pages mention right-click only for deleting sub-pages and blocks [S14]. A full right-click menu is **[nicht belegt]**.

### Sidebar [S12]

Search · Home (Recents, Favorites, Teamspaces; also Shared and Private sections) · Chats with Notion AI · Meetings · Inbox (top right) · Library · Templates · Trash · Settings · new-item menu and 📝 button · workspace switcher · **+** next to Private/teamspaces and on hover per page · collapse (<<), resize by dragging the edge, section headings hide/show a section; items in each tab can be shown, hidden, reordered and reset.

### Context menu: page entry in the sidebar (••• on hover) [search summary 2026-11-13][S14]

Delete · Duplicate · Copy link · Rename · Move to. Dragging onto another page nests; dragging onto Trash deletes.

### Page menu (••• at the top right of the page)

Export [S27] · Version history (needs Can edit) [S14] · Customize page: Font (Default, Serif, Mono), Small text, Full width, Table of contents, backlinks and comments toggles [S15][search summary] · Available offline (desktop and mobile) [S31] · More → Import [S25] · Delete [S14]. Top bar of the page: **Share** [S29].

### Context menu: block (⋮⋮ handle, or right-click on desktop) [S30][S14][S28]

Turn into (also into a page) · Duplicate · Move to · Delete · Comment · Copy link to block. Colour via `/color`.

### Context menu: sub-page block / media block (••• on the block) [S14]

Delete. Further items: **[nicht belegt]**.

### Context menu: page in Trash [S14]

Restore (curved arrow in the list) · Delete permanently (on the opened page).

### Context menu: sidebar section, Favorites

Show, hide, reorder items and reset a tab [S12]. Adding to Favorites via menu: **[nicht belegt]** wording (Favorites section exists).

### Context menu: database row / property

Delete a property, restore under Settings → Edit properties → Deleted properties [S14]. Other database menus: **[nicht belegt]** (databases are out of scope for the wiki workflows).

### Context menu: selected text

Formatting via shortcuts (bold, italic, underline, strikethrough, code, link, comment) [S11]. The floating toolbar's buttons: **[nicht belegt]**.

### Context menu: mention / link

Paste URL → "Paste as mention" [S28]. Hover preview [S28].

### Context menu: Search result (desktop Command Search)

cmd+L or cmd+shift+C copies the result's link [S26].

### Settings paths [S25][S27][S31]

Settings → Import · Settings → General → Export all workspace content · Settings → Offline.

## Additions 2026-11-14 (re-read of S12, S14, S15, S25, S26, S29, S30 and S32 to S35)

- **Home** shows the sections Upcoming events, Recents, Favorites, Agents, Teamspaces, Shared pages, Private pages, Notion apps; at the bottom My Tasks, Library, Marketplace, Help, Trash [S12]. Names as listed on the page; the Agents and Marketplace parts depend on the plan: **[nicht belegt]**.
- **Section menu (••• beside Private, Shared, a teamspace):** Sort (Manual, Last edited), Show (a number of pages up to all), Move section (up, down) [S12].
- **Page menu (••• at the top right):** Appearance & layout (Default, Serif, Mono; Small text; Full width; Page discussions; Table of contents and inline comments by name), Use with AI, More (Present, Translate, Import, Export, Turn into wiki), Version history, Move to, Duplicate, Archive (beta, plans) and Delete [S14][S15][S25][S30].
- **Block handle menu (⋮⋮):** Turn into, Color, Copy link to block, Duplicate, Move to, Delete, Comment, Suggest edits, Edit with AI, Ask AI, Word and character count [S30][S14]. The slash words `/duplicate`, `/delete`, `/turn`, `/color` do the same from the keyboard [S30].
- **Share menu:** tabs Share and Publish; invite a person or group with an access level; General access: only people invited, everyone at the workspace (toggle Hide in search), anyone on the web with the link (Link expires); Request edit access; Page-level access rules (business plans) [S29].
- **Search window:** sort Best matches, Last edited newest/oldest, Created newest/oldest; filters Title only, Created by, Teamspace, In, Date [S26].
- **Trash:** search and filters Last edited by, In, Teamspace; no "empty all"; kept 30 days by default [S14].
- **Right click:** only "Delete" is named for blocks and pages; **[nicht belegt]** beyond that [S14].

## Menü-Inventar

Machine-readable inventory for `scripts/menue-vergleich`, format of [menue-vergleich](../../../../../../../../docs/menue-vergleich.md). Names as on Notion's help pages (read 2026-11-14), `{de: ...}` our own translation. Shortcuts: macOS first, then Windows/Linux, only where a help page names them for the entry; Notion's own writing "cmd/ctrl" is split into two. Items without a documented shortcut have no bracket. No `id`: Notion names none.

- Sidebar {de: Seitenleiste}
  - Search [cmd+K, ctrl+K] {de: Suche}
  - Home {de: Start}
  - Chats with Notion AI
  - Meetings
  - Inbox {de: Eingang}
    - Mark all as read
    - Archive all
    - Archive read
  - Library
  - Templates {de: Vorlagen}
  - Trash {de: Papierkorb}
  - Settings {de: Einstellungen}
  - Marketplace
  - My Tasks
  - New item menu {de: Neu-Menü}
  - Workspace switcher {de: Workspace-Wechsler}
    - Settings
    - Log out
  - Collapse sidebar [cmd+\, ctrl+\] {de: Seitenleiste ein-/ausklappen}
- Section menu (Private, Shared, teamspace) {de: Bereichsmenü}
  - Sort {de: Sortieren}
    - Manual
    - Last edited
  - Show
  - Move section
    - Move up
    - Move down
  - Leave teamspace
- Home section menu (••• at Home) {de: Menü des Bereichs Start}
  - Show
  - Move up
  - Move down
  - Hide section
  - Customize sidebar
- Page in the sidebar, ••• on hover {de: Seite in der Seitenleiste}
  - Delete {de: Löschen}
  - Duplicate {de: Duplizieren}
  - Copy link [cmd+L, ctrl+L] {de: Link kopieren}
  - Rename {de: Umbenennen}
  - Move to {de: Verschieben nach}
  - Remove from Favorites
  - Add subpage (+ on hover) {de: Unterseite hinzufügen}
- Page menu, ••• at the top right {de: Seitenmenü}
  - Appearance & layout
    - Default
    - Serif
    - Mono
    - Small text
    - Full width
    - Page discussions
    - Table of contents
  - Use with AI
  - More
    - Present
    - Translate
    - Import
    - Export
      - PDF
      - HTML
      - Markdown & CSV
    - Turn into wiki
  - Version history {de: Versionsverlauf}
  - Move to {de: Verschieben nach}
  - Duplicate {de: Duplizieren}
  - Archive {de: Archivieren}
  - Delete {de: Löschen}
- Page top bar {de: Seitenkopf}
  - Share {de: Teilen}
  - Favorite (star)
- Block handle menu (⋮⋮) {de: Blockmenü}
  - Turn into [cmd+/, ctrl+/] {de: Umwandeln in}
  - Color
  - Copy link to block
  - Duplicate [cmd+D, ctrl+D] {de: Duplizieren}
  - Move to {de: Verschieben nach}
  - Delete [backspace] {de: Löschen}
  - Comment [cmd+shift+M, ctrl+shift+M] {de: Kommentar}
  - Suggest edits
  - Edit with AI
  - Ask AI
  - Word and character count
- Sub-page or media block, ••• {de: Unterseiten- oder Medienblock}
  - Delete {de: Löschen}
- Slash menu (/) {de: Schrägstrich-Menü}
  - Text
  - Page {de: Seite}
  - To-do list
  - Heading 1
  - Heading 2
  - Heading 3
  - Bulleted list
  - Numbered list
  - Toggle list
  - Divider
  - Quote
  - Link to page
  - Mention
  - Date or reminder
  - Equation
  - Emoji
  - Image
  - PDF
  - Web bookmark
  - Video
  - Audio
  - Code
  - File
  - Embed
  - Duplicate
  - Move to
  - Delete
  - Table of contents
  - Template button
  - Breadcrumb
  - Turn into
  - Color
- Text selection toolbar {de: Textauswahl-Leiste}
  - Bold [cmd+B, ctrl+B] {de: Fett}
  - Italic [cmd+I, ctrl+I] {de: Kursiv}
  - Underline [cmd+U, ctrl+U] {de: Unterstrichen}
  - Strikethrough [cmd+shift+S, ctrl+shift+S] {de: Durchgestrichen}
  - Inline code [cmd+E, ctrl+E] {de: Inline-Code}
  - Link [cmd+K, ctrl+K]
  - Comment [cmd+shift+M, ctrl+shift+M]
  - Color [cmd+shift+H, ctrl+shift+H] {de: Farbe}
  - Mention [@]
- Trash entry {de: Papierkorb-Eintrag}
  - Restore {de: Wiederherstellen}
  - Delete permanently {de: Endgültig löschen}
- Share menu {de: Teilen-Menü}
  - Share tab
    - Invite
    - Copy link
    - Access level
      - Full access
      - Can edit
      - Can edit content
      - Can create
      - Can comment
      - Can view
    - Remove
  - Publish tab
  - General access
    - Only people invited
    - Everyone at the workspace
    - Anyone on the web with link
  - Request edit access
  - Page-level access
- Search window {de: Suchfenster}
  - Sort
    - Best matches
    - Last edited, newest first
    - Last edited, oldest first
    - Created, newest first
    - Created, oldest first
  - Filter
    - Title only
    - Created by
    - Teamspace
    - In
    - Date
  - Copy result link [cmd+L, ctrl+L]
  - Open result in new tab [cmd+click, ctrl+click]
- Settings paths {de: Einstellungspfade}
  - Import
  - Offline
  - General
    - Export all workspace content
  - Security
  - Teamspaces
  - Emoji
