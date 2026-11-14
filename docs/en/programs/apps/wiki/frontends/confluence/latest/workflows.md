# Confluence (Cloud, latest) · Workflows

Step-by-step workflows as the product intends them to be used. Each step reads "user does X → program shows Y". Only behaviour is described, nothing is copied (ADR 0013). Sources S-numbers refer to [index.md](../index.md). Retrieval date of all help pages named here: 2026-11-13. Anything not found in the official pages is marked **[nicht belegt]**.

The same workflows, as yes/no tests, are in [acceptance.md](acceptance.md). What our program cannot do yet is in [gaps.md](gaps.md).

Terms: a **content item** is a page, live doc, blog post, whiteboard, database or folder. The **content tree** is the page tree in the space sidebar.

---

## W1 Create a page (empty or from a template)

**Goal:** a new draft page at a chosen place. **Prerequisite:** the "Add content" permission in the space [S23].

Ways in (all lead to the editor with a draft):

1. User chooses **Create** in the top bar → program shows a panel with the content kinds (page, live doc, …) and a list of templates on the right [S23].
2. User chooses **Page** → program opens a blank draft in the editor [S23].
3. Alternative: user chooses a template in the panel → program opens a draft pre-filled from the template [S23][S31 snippet].
4. Alternative: user clicks the **+** next to the **Content** heading in the space sidebar → program opens a new draft in that space [S23].
5. Alternative: user hovers a page or folder title in the tree and clicks the **+** that appears → program creates the draft at that place (as a child) [S23].
6. User types a title and body → the draft saves itself (see W2).

**Failure cases:** without the permission the creation entry points are not offered [S23] (exact UI: **[nicht belegt]**). A draft without title shows as "Untitled" in lists [S23].
**Undo:** discard the draft (W2 step "discard") [S23].

## W2 Edit a page, drafts, auto-save

**Goal:** change text without losing work. **Prerequisite:** edit permission on the page.

1. User opens a published page and clicks **Edit** or presses `E` → program opens the editor [S23][S12].
2. User types; Markdown autoformat converts `# `, `1. `, `> `, `---` and similar while typing [S12] → program shows the formatted block at once.
3. User types `/` → program opens the quick-insert menu [S12]; the menu's full entry list is **[nicht belegt]** (only `/image` is named in the help read [S29 snippet]).
4. User selects text → program shows the inline toolbar, or the fixed top toolbar, depending on the setting in the toolbar's "..." menu [S15].
5. The editor saves on its own while typing [S23] → program shows no explicit "Save" action; the exact save indicator is **[nicht belegt]**.
6. User clicks **Close draft** → program leaves the editor and keeps the draft for later [S23].
7. Later: user opens **More actions (•••)** in the sidebar → **Drafts**, or finds the draft in the content tree where it was started → program lists the drafts [S23].
8. Unpublished edits of an already published page are auto-saved too, are visible to others who edit that page, and viewers see an "unpublished changes" badge next to the title [S23].
9. Discard: while editing, user opens **•••** → **Delete unpublished page** (new page) or **Revert to previous version** (published page) → program removes the draft or the unpublished edits **permanently** [S23][S25].

**Who sees a draft:** only the author, unless the author invites someone by notification or they open a shared link in the editor; the **lock icon** next to **Publish…** changes access [S23].
**Failure cases:** two people editing the same page: real-time collaboration exists for live docs (a help page with that title exists; not read); the conflict behaviour for pages is **[nicht belegt]** in the pages read (REST updates can return HTTP 409 when publishing approval is required [S9]).
**Undo:** editor Undo/Redo (Ctrl/Cmd+Z, Y) [S12]; reverting unpublished edits is permanent [S23]. Only pages and blog posts have drafts; live docs do not [S23].

## W3 Publish / update

**Goal:** make a draft visible, or publish changes.

1. User clicks **Publish…** (new page) or **Update** (published page) in the editor's top right → program opens the publish dialog (new page) or publishes directly (update); see [dialogs.md](dialogs.md) D3 [S23].
2. Optional: user opens the caret next to **Update** → **Adjust update settings** → program shows location, access, notify-watchers checkbox, version comment, schedule and convert-to-blog fields [S23].
3. Shortcut: Ctrl+Enter publishes, Ctrl+Shift+Enter publishes with note [S12]. (The help page for creating content names Cmd/Ctrl+Shift+Enter for opening the dialog [S23].)
4. User confirms → program shows the published page in view mode, adds a version to the history.
5. Scheduled publishing: user picks a date/time in the schedule control → **OK** → **Schedule** [S23].

**Failure cases:** a title already in use in the space prevents publishing until renamed (stated for duplicates [S24]). **Undo:** restore an earlier version (W9).

## W4 Rename

**Goal:** change a page title.

1. The help pages read give **no steps** for renaming [S23]. Title editing in the editor's title field is the usual place but is **[nicht belegt]** here.
2. Titles must be unique within a space [S24].
3. When restoring from the trash a name clash makes the program ask for a new name first [S25].

## W5 Move and reorder (page tree)

**Goal:** put an item somewhere else. **Prerequisites:** same space: space admin (roles off) or "Manage all content in space" (roles on). Other space: additionally view content, view the item and add items in the destination [S24].

Reorder / move by drag:
1. User expands branches in the content tree → program shows children.
2. User drags an item to a new position → program reorders; moving a parent moves its children; incoming links stay valid [S24].

Move by dialog (same space):
1. User opens the item's action menu in the top-right toolbar → **Move** → program opens the Move dialog [S24] ([dialogs.md](dialogs.md) D5).
2. User uses the **Browse** tab (tree) or the **Search** tab to find the new parent; **Start over** resets the tree [S24].
3. User clicks **Move** → program moves the item with attachments, comments and children [S24].

Move to another space: from the breadcrumb's down caret or **More actions (...)** → **Move** → pick the destination space (only spaces the user can access appear) → parent → **Move** [S24].

Hide from the tree: move the item to root level next to the space home; hidden items are still found by search and by URL; list them under **Space settings → Content → Hidden** (reordering under **Content → Reorder**) [S24].

**Undo:** move it back [S24] (no undo button **[nicht belegt]**).

## W6 Duplicate (copy)

1. User opens **More actions (...)** → **Duplicate** (not offered while editing) → program opens the dialog for destination space and parent [S24] (D6).
2. Optional: **Include children** → **Next** → bulk naming (optionally labels and restrictions) → **Duplicate** [S24].
3. Program creates a copy named with a "Duplicate of" prefix; it keeps attachments, labels and restrictions, but not comments, version history, watchers or stars [S24].

**Failure:** name clash in the target space: the copy cannot be published until renamed [S24].

## W7 Delete, trash, restore, purge

**Goal:** remove content with a way back.

1. Before deleting: user opens **Show details** to see incoming links and child items [S25].
2. User opens **More actions (•••)** next to **Share** → **Archive and Delete** → **Delete** → program asks to confirm and moves the item to the space trash [S25] (D7). The entry is offered only to those with permission; page restrictions can block it [S25].
3. Children move up to the nearest parent; to keep them under a chosen parent, move them first [S25].
4. Restore (space admin): **Space settings → Content → Trash** → **Restore** next to the item → program asks for a new name if the old one is taken. Restored items lose inherited permissions and land at the space root outside the sidebar; find them via **Reorder** [S25].
5. Purge (space admin): **Purge** for one item or **Purge All** → program removes items, their versions and their attachments for good [S25].
6. Drafts, unpublished changes and single versions are deleted permanently and never reach the trash [S25].

**Undo:** restore from the trash until purged.

## W8 Archive

1. User opens **More actions (•••)** → **Archive** → optionally writes a note → confirms [S28].
2. Program removes the item (and all nested items, all-or-nothing) from tree and quick search; links still work and show an "Archived" lozenge [S28].
3. Archived items cannot be edited, commented, liked, moved, duplicated or shared [S28].
4. Find them under **Space settings → Content → Archived**; restore there [S28].
5. Warning: if the item inherited access from its parent, archiving can widen who sees it; set restrictions first [S28].
6. Bulk archive/delete: **Content manager** in space settings (Premium/Enterprise): max 500 per archive action, 100 per delete [S28].

## W9 Page history and versions

1. User opens **More actions → Version history** → program shows the version list [S15][S23].
2. Compare: user ticks the boxes of the versions → **Compare selected versions** → program shows the differences with large unchanged parts hidden [search summary, 2026-11-13].
3. Restore: **Restore this version** beside a version (or at the top of an opened old version) → program offers to edit the default change comment → **OK**; later versions are kept [search summary, 2026-11-13].
4. Delete a version: from the history, **Delete** — permanent, not restorable [S25].
5. Archived items cannot be compared or reverted [search summary].

**Failure:** none described. **Undo:** restoring creates a new version; the previous state is itself in history.

## W10 Search

1. User opens search in the top bar, or presses Alt+Shift+Z (Win) / Ctrl+Opt+Z (Mac) [S12][S14] → program shows the search field with results.
2. Quick search leaves out archived content; an advanced search can include it [search summary 2026-11-13].
3. Filters: "Add a filter" narrows results in CQL-powered views; the macro filters named are space, content type, last modified, contributor [search summary]. The exact filter list of the main search page is **[nicht belegt]**.
4. The sidebar's **Recent** has filters Today / Worked on / Owned by me [S14].

## W11 Import

Paths and dialogs (files come from a system file chooser):
1. User opens a blank page or live doc → **More actions** next to **Share** → **Templates and import** → **Import** tab [S26].
2. User picks **Word document (.docx)**, **Google Doc** or **OneDrive** [S26].
3. Word: system file chooser → select .docx files → **Open** → **Finish** [S26] (D8).
4. Google/OneDrive: connect the account if asked, choose documents, **Select/Open**, **Finish** [S26].
5. Result: one file becomes a draft page or live doc; several files become separate pages under a restricted placeholder page "Imported pages" with date and time [S26].
6. Limits: 5 MB per document (without attachments), bulk up to 30 files and 50 MB, 10 MB per file; only supported image types are kept, others become placeholder text; shapes become placeholders [S26].
7. Import of Markdown, HTML, other wikis, Notion: **[nicht belegt]** in the page read (the page links to separate articles). Pasting formatted text into the editor is the way for web content [S26]. A folder import: **[nicht belegt]**.
8. The template browser closes when the user starts typing; reopen it via **Templates & import** in the draft's more-actions menu [S26].

**Undo:** discard the imported draft, or move the imported pages to the trash (W7).

## W12 Export

1. Page: **More actions** → **Export** → **Export to Word** / **Export to PDF** [S16].
2. Space (space admin): **Space settings → General → Export space** → format PDF, CSV, HTML or XML [S16].
3. Only published content is exported; limits are in [features.md](features.md) [S16].

## W13 Links and backlinks

1. User presses Ctrl/Cmd+K or clicks the **Link** button → program shows a picker for internal items (page, live doc, whiteboard, database, blog post, slides) or an external URL [S30 snippet].
2. Pasting a URL of the same site makes the item's name the link text [S30 snippet]. Anchors: page URL plus `#anchor` [S30 snippet].
3. Incoming links: **Show details** → **Content information** lists incoming and outgoing links, also before a delete [S25].
4. Moving an item keeps incoming links valid [S24].

## W14 Attachments

1. Upload: drag a file onto the page, use the toolbar's "Add image, video, or file" icon, or type `/image` [S29 snippet]. Needs the "Add attachments" permission.
2. A file with the same name as an existing attachment becomes a new version [S27][S29].
3. Manage: **Show details → Attachments** (download single or zip); file properties allow rename, comment, labels, move [S27].
4. Delete needs "Delete attachment"; deleting a single version also needs space admin; deleted files can be restored by space admins from the trash, versions cannot [S27].
5. Space-wide view: **Space settings → Attachments** [S27].

## W15 Permissions and restrictions (rough)

1. Space level: space admins set permissions under **Space settings → Space access** (includes an Archive permission) [S28].
2. Page level: the **lock icon** in the editor (drafts) and restrictions on published pages; restrictions can block deletion and survive archiving [S23][S25][S28]. The restriction dialog itself is **[nicht belegt]**.
3. **Share** next to the more-actions menu shares an item (shortcut Ctrl+Alt+S) [S12].

## Update 2026-11-14 (S32 to S34, S23, S28)

### W10a Search in detail [S34]

1. User presses `/` or clicks the search field → program opens the drawer with names of pages, blog posts, whiteboards, slides, people, files and spaces, newest first.
2. User picks a hit (a person opens a profile); with no hit, Enter or **Advanced** opens the results page.
3. User sets filters (Spaces, Contributors, Type, Last modified, Labels, Pages under, titles only) → program lists hits with highlight, date and breadcrumbs. Contributors and labels combine as OR.
4. **Failure:** the "no results" text and indexing delays are **[nicht belegt]**. **Undo:** not applicable.

### W15a Share and restrict in detail [S32][S33]

1. **Share:** user clicks **Share** → program shows the dialog. User searches and picks people or groups, chooses view or edit where offered, ticks notify, adds a message, clicks **Share** → program sends the invitation. The link icon copies the link; the link alone gives no access [S32].
2. **Failure (Share):** teams cannot be shared with; an invitation to an outsider may wait for administrator approval and a refusal is mailed to the sender only; outsiders get access to the whole site and billing starts [S32].
3. **Restrict, edit only:** the same dialog; user sets **Anyone in this space** from **Can edit** to **Can view** and adds editors under **Specific access** [S33].
4. **Restrict, fully:** user sets General access to **Restricted** and adds people or groups with **Can edit** / **Can view**; **Save** → program applies. Viewing restrictions are inherited by children, editing restrictions are not; a child shows "Restricted by a parent" [S33].
5. **Remove:** the per-person menu → **Remove**, or **Remove all** → program drops the entry [S33]. Free plans have no restrictions [S33].
6. **Access requests:** a person without access asks; owner, creator, last editor and space admin get a flag and **Approve** or **Deny**; Deny is silent to the requester [S33].
7. **Failure:** content missing in tree and macros for lack of access; "You don't have permission" (details **[nicht belegt]**) [S33]. **Undo:** set the earlier state again; a dedicated undo **[nicht belegt]**.

### W9a Revert unpublished changes [S23]

1. User opens **More actions → Revert to previous version** → program shows the unpublished changes, then, after confirming, deletes them and shows the last published version. The help says they cannot be recovered. A version can also be deleted from the history; that renumbers the versions and is not recoverable either.

### W8a Archive permissions [S28]

1. Own items: any user who can see them; space-wide: the space-admin-granted Archive permission (**Space settings → Space access → Groups or Users → Edit**, tick Archive, **Save all**). **Restore** (banner or Archived list) needs the same permission and puts the item back in its tree [S28].

### W5a Trash restore places the page at the top [S25]

1. After **Restore** (space admin, **Space settings → Content → Trash**) the page loses inherited permissions and sits at the top level of the space, not at the old place; **Space settings → Content → Reorder** finds it. A name clash must be fixed by renaming first [S25].
