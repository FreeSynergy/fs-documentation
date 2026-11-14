# Confluence (Cloud, latest) · Menus

Sources: S-numbers refer to [index.md](../index.md). Items marked "unverified" were in the earlier draft and could not be confirmed.

## Top bar [S14]

| Menu | Items / function |
|------|------------------|
| Search | Find pages, live docs, spaces |
| Create | Page, live doc, database, Loom video, whiteboard, slides; blog post via shortcut [S12] |
| Chat | Rovo chat |
| Notifications | Notification list |
| Help | Online help, what's new, keyboard shortcuts (help icon > Keyboard shortcuts) [S13] |
| Your profile and settings | Personal space, Confluence settings, feedback |

## Sidebar [S14]

For you · Recent (filters: Today, Worked on, Owned by me) · Starred · Spaces (recent and starred) · Apps · More · Teams · Drafts · Company Hub (conditional) · Customize sidebar

## Page "•••" menu [S15][S16]

| Item | Source |
|------|--------|
| Watch settings | [S15] |
| Version history (view changes) | [S15] |
| Find and replace | [S15] |
| Export > Export to Word | [S16] |
| Export > Export to PDF | [S16] |
| Templates and import | [S15] |
| Archive and delete | [S15] |

Unverified from the earlier draft: Permissions, Print. Move, Duplicate (copy) and Delete are verified since 2026-11-13, see "Context menus by object type" below [S23][S24][S25].

## Space "•••" menu (next to the space name) [S14][S16]

| Item | Function |
|------|----------|
| Space settings | Opens space settings (available items depend on permissions) |
| Space settings > General > Features | Choose space sidebar items |
| Space settings > General > Export space | Formats PDF, CSV, HTML, XML (space admins) |

Unverified: "Change the theme" for a space (S17 describes space inheritance only), "Organise the content", "Space statistics", "Space backup".

## Floating action bar [S15]

Comments panel · Details panel · Emoji reactions · Loom · Atlassian Intelligence (Premium and Enterprise).

## Blog post menu

Unverified in detail. Only the blog post create shortcut is documented [S12].

## Comment menu

Unverified.

## Dashboard, Saved, Created, Mentions

Not present as named menu items in the Cloud navigation docs read. "Saved" maps to Starred; "Created" maps to Recent with the "Owned by me" filter [S14]. "Dashboard" and "Mentions" as menu names: unverified.

## Context menus by object type (added 2026-11-13)

Atlassian does not describe a right-click menu for the page tree. The menus are **More actions (•••)** menus. Sources: S-numbers as in [index.md](../index.md); the new sources are listed there. A right-click menu as such: **[nicht belegt]**.

### Published page, view mode [S23][S25][S28]

Star · Watch settings · Preview · Find and replace · View changes (only with unpublished edits) · Revert to previous version (only with unpublished edits) · Version history · Move · Duplicate (not while editing) · Convert to live doc · Templates and import · Export (Word, PDF) · Archive · Archive and Delete → Delete (by permission).

### Draft page, editor [S23]

Preview · Find and replace · Move · Templates and import · Convert to live doc · Delete unpublished page / Delete draft. More options → **Publish as** Page or Blog.

### Content tree entry (page, folder) [S23][S24][S28]

Hover: **+** (create child) and ••• . ••• on a draft offers **Delete**. Other entries of the tree menu (move, archive, delete): **[nicht belegt]** as exact list; dragging reorders.

### Folder

Created via **+**; moves like a page [S23]. Own menu entries: **[nicht belegt]**.

### Space (••• next to the space name) [S25][S28][S24]

Space settings → Content → Trash, Archived, Hidden, Reorder; Content manager (Premium/Enterprise); General → Features, Export space; Space access; Attachments.

### Trash entry [S25]

Restore · Purge. Header: Purge All.

### Archived item [S28]

Restore (needs Archive permission). Banner shows the note.

### Version in history [search summary 2026-11-13][S25]

Restore this version · Delete · tick box for Compare.

### Attachment [S27]

Download · Download all (zip) · Properties (rename, comment, MIME type, move, label) · Delete · upload new version (same name) or from preview.

### Imported placeholder "Imported pages" [S26]

A normal restricted page; children can be organised, moved and have permissions set.

### Selected text in the editor [S15]

Inline toolbar (if chosen) with formatting, link, comment. Exact buttons: **[nicht belegt]**.

### Comment [S12]

Comment panel, next/previous comment shortcuts exist; the comment's own menu: **[nicht belegt]**.

## Role-based menus

Access is set by permissions. Which menus appear for which role is not documented in the sources read (unverified).

## Menü-Inventar

Machine-readable inventory for `scripts/menue-vergleich` (format: [menue-vergleich](../../../../../../../../docs/menue-vergleich.md), nested list, indentation = depth). Names are Atlassian's menu names; `{de: ...}` is our own translation. Shortcuts: Windows first, then Mac (both in one bracket, comma separated); source S12 unless noted. Shortcuts whose key is `[`, `]` or `,` (sidebar toggle, comments panel, previous comment, inline comments) are left out here because they would break the bracket syntax; they are in [shortcuts.md](shortcuts.md). Re-read 2026-11-14 on the pages S14, S15, S16, S23 to S28 (index.md); items without a source stay out of the list. Atlassian names no `id`, so none is given.

- Top bar {de: Kopfleiste}
  - Search [Alt+Shift+Z, Ctrl+Opt+Z] {de: Suche}
  - Create {de: Erstellen}
    - Page [Win+Alt+C, Ctrl+Opt+C] {de: Seite}
    - Live doc [Ctrl+Shift+D, Ctrl+Shift+D] {de: Live-Dokument}
    - Database {de: Datenbank}
    - Loom video
    - Whiteboard
    - Slides {de: Folien}
    - Create with Rovo
    - Blog post [Ctrl+Alt+Shift+B, Cmd+Opt+Shift+B] {de: Blogbeitrag}
  - Chat [Ctrl+Win+., Cmd+.]
  - Notifications [Ctrl+Alt+O, Cmd+Opt+O] {de: Benachrichtigungen}
  - Help {de: Hilfe}
    - Keyboard shortcuts [Shift+?, Shift+?] {de: Tastenkürzel}
  - Your profile and settings {de: Profil und Einstellungen}
- Sidebar {de: Seitenleiste}
  - Expand/Collapse {de: Ein-/Ausklappen}
  - For you
  - Recent [Ctrl+Alt+G, Cmd+Opt+G] {de: Zuletzt}
    - Today
    - Worked on
    - Owned by me
  - Starred [Ctrl+Alt+8, Cmd+Opt+8] {de: Markiert}
  - Spaces
  - Apps
  - More
  - Teams
  - Drafts {de: Entwürfe}
  - Company Hub
  - Customize sidebar
  - Home [Ctrl+Alt+H, Cmd+Opt+H] {de: Start}
- Space sidebar {de: Space-Seitenleiste}
  - Content area plus button (+) {de: Neue Seite im Space}
  - Go to space overview [Ctrl+Alt+V, Cmd+Opt+V]
  - More actions (•••) neben dem Space-Namen
    - Space settings {de: Space-Einstellungen}
      - General
        - Features
        - Export space {de: Space exportieren}
      - Content
        - Trash {de: Papierkorb}
        - Archived {de: Archiviert}
        - Hidden {de: Ausgeblendet}
        - Reorder {de: Neu ordnen}
      - Content manager
      - Space access
      - Attachments {de: Anhänge}
- Page, view mode, More actions (•••) {de: Seite in der Ansicht}
  - Star [Ctrl+Alt+F, Ctrl+Opt+F] {de: Markieren}
  - Watch settings [Ctrl+Alt+W, Cmd+Opt+W] {de: Beobachten}
  - Preview {de: Vorschau}
  - Find and replace [Ctrl+F, Cmd+F] {de: Suchen und ersetzen}
  - View changes {de: Änderungen ansehen}
  - Revert to previous version {de: Auf vorherige Version zurücksetzen}
  - Version history {de: Versionsverlauf}
    - Compare selected versions
    - Restore this version {de: Diese Version wiederherstellen}
    - Delete {de: Löschen}
  - Move {de: Verschieben}
  - Duplicate {de: Duplizieren}
  - Convert to live doc
  - Templates and import
  - Export
    - Export to Word
    - Export to PDF
  - Archive {de: Archivieren}
  - Archive and delete
    - Delete {de: Löschen}
  - Automations
  - Apps
- Page, view mode, toolbar and header
  - Edit [E, E] {de: Bearbeiten}
  - Share [Ctrl+Alt+S, Cmd+Opt+S] {de: Teilen}
  - Show details [Ctrl+Shift+I, Ctrl+Shift+I]
  - Breadcrumbs
    - Move {de: Verschieben}
- Page, editor (draft or edit mode)
  - Publish… [Ctrl+Enter, Cmd+Enter] {de: Veröffentlichen}
  - Publish with note [Ctrl+Shift+Enter, Cmd+Shift+Enter]
  - Update
    - Adjust update settings
  - Close draft {de: Entwurf schließen}
  - Lock icon (page restrictions) {de: Seiteneinschränkungen}
  - More actions (•••)
    - Preview
    - Find and replace [Ctrl+F, Cmd+F]
    - Move
    - Templates and import
    - Convert to live doc
    - Delete unpublished page {de: Unveröffentlichte Seite löschen}
    - Delete draft {de: Entwurf löschen}
    - Revert to previous version
    - More options
      - Publish as
        - Page
        - Blog
      - Publish
  - Toolbar menu (…)
    - Fixed at the top
    - In-line
- Content tree entry (page, folder) {de: Seitenbaum-Eintrag}
  - Plus button (+) on hover {de: Unterseite anlegen}
  - More actions (•••)
    - Delete (draft only) {de: Löschen}
    - Archive {de: Archivieren}
  - Drag to reorder {de: Ziehen zum Umordnen}
- Floating action bar
  - Comments panel
  - Details [Ctrl+Shift+I, Ctrl+Shift+I]
  - Emoji reaction
  - Create a Loom video
  - Atlassian Intelligence
- Trash entry (Space settings > Content > Trash) {de: Papierkorb-Eintrag}
  - Restore {de: Wiederherstellen}
  - Purge {de: Endgültig löschen}
  - Purge All {de: Alles endgültig löschen}
- Archived item {de: Archivierter Inhalt}
  - Restore
  - Add note / Edit note
  - View
  - Delete
  - Export to PDF
  - Export to Word
  - Watch / Unwatch
  - Star / Unstar
  - Edit restrictions
  - View history
- Attachment {de: Anhang}
  - Download
  - Download All
  - Properties {de: Eigenschaften}
  - Delete {de: Löschen}
  - Version list
    - Delete {de: Löschen}
- Comment {de: Kommentar}
  - Comment [Ctrl+Alt+C, Cmd+Opt+C]
  - Next comment [Ctrl+., Ctrl+.]
  - Previous comment
  - Next unread comment [Ctrl+Shift+U, Cmd+Shift+U]
  - Toggle inline comments
  - Select comment [Ctrl+Alt+E, Cmd+Opt+E]
