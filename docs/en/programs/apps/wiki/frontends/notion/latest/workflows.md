# Notion (latest) · Workflows

Step-by-step workflows as the product intends them to be used. Each step reads "user does X → program shows Y". Only behaviour is described, nothing is copied (ADR 0013). S-numbers refer to [index.md](../index.md). Retrieval date of all help pages named here: 2026-11-13. What no official page states is marked **[nicht belegt]**.

Yes/no tests for these workflows: [acceptance.md](acceptance.md). Our gaps: [gaps.md](gaps.md).

Terms: a **page** is a tree of blocks; a **sub-page** is a page nested in a page; a **database** holds pages as rows; the **sidebar** is the page tree with the sections Private, Shared, Teamspaces, Favorites [S12].

---

## W1 Create a page

**Goal:** a new page at a chosen place.

1. User clicks the **+** next to **Private** or a teamspace in the sidebar → program creates a page there and opens it [S12].
2. Alternative: user hovers a page in the sidebar and clicks its **+** → program creates a page nested inside it [S12].
3. Alternative: user uses the new-item menu (top of the sidebar) or the 📝 button → program creates a page that defaults to Private unless a location is chosen; the 📝 button opens it in preview mode [S12].
4. Alternative: inside a page the user types `/page` (or uses the **Page** block) → program adds a sub-page [S11][S30]. `/link` or "Link to page" links an existing page instead [S28].
5. Alternative, from a template: Templates in the sidebar [S12], or `/template` [S11]. How a page is chosen and instantiated: **[nicht belegt]** in the pages read.
6. User types a title and content → the page keeps itself (see W2).

**Failure cases:** none described. Who may create in a teamspace: **[nicht belegt]**. **Undo:** delete the page (W7); Notion has no draft state for pages **[nicht belegt]**.

## W2 Edit

**Goal:** write and format without a save step.

1. User clicks into the text → program places the cursor in a block [S30].
2. User types; Markdown shortcuts convert while typing (`# `, `- `, `[] `, `> `, `**bold**`, `---`) [S11][S30].
3. User types `/` → program opens the block menu; typing narrows it (`/h1` + Enter) [S11][S30].
4. User presses Esc → the block is selected; arrow keys select others; Shift+arrows extend; Enter edits the block's text again [S11].
5. User opens the **⋮⋮** handle → program shows block actions: Turn into, Duplicate, Move to, Delete, Comment, Copy link to block [S30][S28].
6. User drags the handle → block moves; Option/Alt+drag duplicates [S11][S30].
7. Selecting blocks shows a word and character count [S30].
8. Saving: no save action exists in the help pages read; versions are recorded while editing (see W9). Whether a visible "saving" indicator exists: **[nicht belegt]** (no page describes it) [S30].
9. Two people on one page: text edits are merged automatically; non-text properties edited offline by two people keep only one value [S31]. Live-cursor display: **[nicht belegt]**.

**Failure cases:** page in Trash cannot be edited until restored [S14]. **Undo:** undo/redo exist (mobile menu is documented; desktop shortcut cmd/ctrl+Z is common but **[nicht belegt]** in the table read [S11]).

## W3 Publish

Notion pages are live as soon as typed for people who have access; there is no draft/publish step in the pages read **[nicht belegt]**. "Publish" is a tab in the Share dialog that makes a page reachable on the web (see W14) [S29].

## W4 Rename

1. User opens the page's **•••** menu in the sidebar (hover) → program shows Delete, Duplicate, Copy link, **Rename**, Move to [search summary 2026-11-13].
2. User types the new name → program shows it in the sidebar and title. Changing the title in the page itself: **[nicht belegt]** in pages read.
3. Links by mention: what happens to them on rename: **[nicht belegt]** [S28].

## W5 Move

**Goal:** put a page elsewhere.

1. User drags a sidebar entry onto another page → program nests it; dragging it out un-nests it [S12].
2. Alternative: **•••** → **Move to** (also `/moveto` and the block menu for blocks) → program opens a menu to choose another workspace or page [search summary][S11] ([dialogs.md](dialogs.md) D5).
3. Moving a page from Shared or a teamspace into Private removes the others' access [S12].
4. Moving across workspaces duplicates instead; links, relations, permissions and history can break in the copy [search summary].
5. Sidebar sections can be shown, hidden, reordered; a tab can be reset to the default [S12].

**Undo:** move it back; nothing more documented.

## W6 Duplicate

1. User opens **•••** → **Duplicate**, or `/duplicate`, or cmd/ctrl+D on selected blocks, or Option/Alt+drag [search summary][S11].
2. Program creates the copy next to the original. Naming of the copy: **[nicht belegt]**.
3. Public pages can be duplicated with the **Duplicate** button at the upper right, unless the owner turned "Duplicate as template" off [search summary].
4. Duplication is rate-limited to 50,000 blocks per hour [search summary].

## W7 Delete, trash, restore

1. User chooses **•••** in the sidebar or at the top right of the page, or drags the page into **Trash**, or selects the page block and presses Backspace/Delete → program moves the page to Trash, with its sub-pages [S14][S12]. No confirmation step is described **[nicht belegt]**.
2. Trash is at the bottom of the sidebar (iOS/Android: under **•••** at the top left of the sidebar) [S14].
3. User opens Trash → program lists deleted pages; search and filters by last editor, original location, teamspace [S14].
4. User opens a trashed page → program shows it read-only with **restore** and **delete permanently** [S14]; the curved arrow next to an entry restores it to where it was [search summary].
5. Pages stay 30 days by default, then are permanently deleted; Trash cannot be emptied in one go, pages are removed one by one; enterprise owners may change the period [S14].
6. Database properties: Settings → Edit properties → Deleted properties: arrow restores, trash can deletes for good [S14].
7. Accidental permanent deletion: contact support; backups of the last 30 days exist [S14].
8. Archive (beta, Business/Enterprise): archived pages stay readable, are hidden from search by default and show a banner; archiving a parent archives its sub-pages [S14].

**Undo:** restore from Trash within the period.

## W8 Search

1. User clicks **Search** in the sidebar or presses cmd/ctrl+P (cmd/ctrl+K when no block has the cursor) → program opens the search window with recently visited pages listed [S26].
2. User types → results appear. Quotation marks demand an exact phrase [S26].
3. User picks sorting: Best matches, Last edited, Created (newest/oldest) [S26].
4. Filters: Title only, Created by, Teamspace, In (a page and its sub-pages), Date (Today, 7, 30 days, custom) [S26].
5. In-page search: cmd/ctrl+F [S26][S11].
6. Database search matches titles and property values, not page content; workspace search covers the content of database pages [S26].
7. Not searched: comments, mentions of people and pages, select tags (outside database search) [S26]. Trash search is inside Trash (W7) [S14].

## W9 Page history and versions

1. User opens **•••** at the top of the page → **Version history** (needs at least "Can edit") → program shows versions [S14][search summary].
2. A version is recorded every 10 minutes while editing and two minutes after the last edit; retention: 7 days Free, 30 Plus, 90 Business, any for Enterprise [search summary].
3. User opens a version → program shows it; **Restore** brings it back; blocks can be copied from the old version into the current page [S14][search summary].
4. Restoring a database restores its pages and properties, not the text inside [S14].
5. Compare side by side and version labels: **[nicht belegt]**.

## W10 Import

1. User opens **Settings → Import** in the sidebar, or types `/` and searches an importer, or **•••** → **More** → **Import** → program shows the source choices [S25] ([dialogs.md](dialogs.md) D6). Not on mobile.
2. Sources: plain text, Markdown, Word (.docx), CSV, HTML, PDF, ZIP; Evernote, Trello, Quip, Dropbox Paper, Hackpad, WorkFlowy, Google Docs; Confluence, Asana, Monday, Granola have their own guides [S25].
3. User chooses a file in the system file chooser or drops files; PDF, HTML, Markdown, Word, TXT accept several files in one session; CSV and ZIP use separate flows [S25]. The folder-picker wording: **[nicht belegt]**.
4. Program shows the import in **Settings → Import** under **In progress** / **Complete** with time, status, size [S25].
5. Results: CSV rows become pages, columns properties; Google Doc becomes one page; Evernote notebooks become pages and notes list items; PDF tables become simple tables [S25].
6. Limits: 5 MB per file on Free for Word, HTML, Markdown, CSV (50 MB paid); PDF 5 MB (20 MB paid); ZIP up to 5 GB but 10,000+ files likely fail; about 120 HTML/Markdown files per 12 hours [S25].
7. Failure: stuck import (wait, retry smaller); ZIP failure (remove hidden files, re-zip); garbled CSV (re-export UTF-8). CSV import adds rows, never updates [S25].

**Undo:** move the imported pages to Trash (W7). A dedicated undo for an import: **[nicht belegt]**.

## W11 Export

1. User opens **•••** at the top right → **Export** (admins may not see it) → program shows a dialog with the format and **Include subpages** [S27] ([dialogs.md](dialogs.md) D7).
2. Formats: Markdown & CSV, HTML (PDF also exists for pages) [S27][search summary].
3. Program downloads; uploaded files are included [S27].
4. Whole workspace: **Settings → General → Export all workspace content** → an e-mailed download link valid 7 days, with an `index.html` sitemap; desktop or web only [S27].
5. Failure: very large workspaces may fail — export top-level pages in batches with sub-pages [S27]. No scheduled backup exists [S27].

## W12 Links and backlinks

1. User types `@`, `[[` or `+` in text → program lists pages to mention [S28].
2. Alternative: `/link` or **Link to page** inserts a block; the page also appears in the sidebar below the current page like a sub-page [S28].
3. Link to a block: **⋮⋮** → **Copy link to block** [S28].
4. Pasting a URL offers "Paste as mention" with preview [S28].
5. Backlinks: select the backlinks count under the title (or under the properties of a database page) → program lists the pages that mention this one; only pages the user may see; private ones appear as "Private" [S28].
6. Page ••• → **Customize page** toggles the backlink and comment sections [search summary].

## W13 Attachments and media

1. User types `/image`, `/file`, `/pdf`, `/video`, `/audio`, `/embed` → program inserts a media block and offers upload or link [S11]. Drag-and-drop of files onto the page: **[nicht belegt]** in the pages read for this workflow (the older draft claims it).
2. Size limits per plan, preview, replace, delete of a file: **[nicht belegt]**.
3. Uploaded files are part of exports [S27].

## W14 Permissions (rough)

1. User clicks **Share** at the top of a page → program shows people and groups with an access dropdown; **Invite**, **Copy link**, tab **Publish** [S29][search summary].
2. Levels: Full access, Can edit, Can edit content (database pages), Can create (Business/Enterprise), Can comment, Can view [S29].
3. General access: only invited, everyone in the workspace, or anyone with the link; links can expire [S29].
4. Sub-pages inherit the parent's permissions and can be changed [S29].

## W15 Offline

1. Desktop/mobile app only: **•••** → toggle **Available offline** [S31]. Paid plans download recent and favourite pages automatically; sub-pages are not included [S31].
2. Offline the user can create pages and edit downloaded pages; embeds, AI, forms, buttons need a connection; sharing and permission changes are impossible [S31].
3. Settings → Offline lists downloaded pages and can stop them [S31].
