# Notion (latest) · Acceptance checklist

Derived from [workflows.md](workflows.md). Each line is a click-through test: **yes / no**. Lines marked "ours" are points the vorbild leaves open; we decide them. States and dialogs: [states.md](states.md), [dialogs.md](dialogs.md).

## W1 Create

- [ ] A **+** next to the Private section creates a page and opens it.
- [ ] Hovering a sidebar entry shows a **+** that creates a nested page.
- [ ] A new-item menu creates a page; with no location chosen it is private.
- [ ] `/page` inside a page adds a sub-page that shows in the sidebar under it.
- [ ] A template can be chosen when creating (ours: flow undocumented).
- [ ] The new page shows an empty title and accepts typing at once.

## W2 Edit

- [ ] Typing `# `, `- `, `[] `, `> `, `---` creates heading, bullet, to-do, toggle, divider immediately.
- [ ] `/` opens a block menu; typing `h1` and Enter makes a heading.
- [ ] Esc selects the block; arrows move the selection; Enter returns to editing.
- [ ] The **⋮⋮** handle opens Turn into, Duplicate, Move to, Delete, Comment, Copy link.
- [ ] Dragging the handle moves a block; Alt/Option+drag copies it.
- [ ] Selecting blocks shows a word count.
- [ ] Nothing has to be saved; after closing and reopening the text is there (ours: define save indicator).
- [ ] Two editors changing different text both survive.

## W3 Publish

- [ ] A page is visible to those with access without a publish step (ours: decide if we keep drafts).
- [ ] Sharing to the web is a separate action in the share dialog.

## W4 Rename

- [ ] The sidebar menu has **Rename**; the new name shows in sidebar and title.
- [ ] Renaming does not break mentions of the page (ours: not documented, decide and test).

## W5 Move

- [ ] Dragging a page onto another nests it; dragging it out un-nests it.
- [ ] A **Move to** command opens a page chooser and moves the page there.
- [ ] Moving into Private from Shared removes others' access (and tells the user, ours).
- [ ] Sidebar sections can be shown, hidden and reordered; reset restores the default.

## W6 Duplicate

- [ ] **Duplicate** in the page menu creates a copy.
- [ ] Cmd/Ctrl+D duplicates selected blocks.
- [ ] A public page can be duplicated through a button, unless the owner switched it off.

## W7 Delete, trash, restore

- [ ] Delete from the sidebar menu, from the page menu, by dragging to Trash, and by Backspace on a selected page block.
- [ ] Deleting a page also removes its sub-pages from the tree.
- [ ] Trash lists the page; filters by editor, location, teamspace work.
- [ ] A page in Trash opens read-only and cannot be edited.
- [ ] Restore puts the page back where it was.
- [ ] Entries must be removed one at a time; no "empty all" exists.
- [ ] After the retention period the page is gone for good.

## W8 Search

- [ ] A shortcut and a sidebar entry open search.
- [ ] The window lists recently visited pages before typing.
- [ ] Quotes make an exact phrase search.
- [ ] Sort and filters (title only, creator, in, date) work.
- [ ] In-page search (Cmd/Ctrl+F) finds text inside the page.
- [ ] Comments and mentions of pages are not found (documented limit).

## W9 History

- [ ] The page menu opens version history for editors only.
- [ ] A version can be opened and restored.
- [ ] Blocks can be copied out of an old version.
- [ ] Retention shows what the plan allows (ours: decide).

## W10 Import

- [ ] Import is reachable from Settings, from the page menu, and from the slash menu.
- [ ] Choosing a source opens a system file chooser; several files can be chosen for text-like types.
- [ ] A running import is visible in an In progress list and moves to Complete.
- [ ] A file above the limit is refused with the limit named (ours: wording).
- [ ] CSV rows become pages with properties.
- [ ] A stuck import can be retried in smaller batches.
- [ ] ZIP with hidden files is handled or the user is told to remove them.

## W11 Export

- [ ] Page menu **Export** offers format and **Include subpages**.
- [ ] The export includes uploaded files.
- [ ] A workspace export arrives as a link valid seven days.

## W12 Links and backlinks

- [ ] `@`, `[[` and `+` open a page picker.
- [ ] A backlinks entry under the title lists mentioning pages; private ones show "Private".
- [ ] **Copy link to block** produces an anchor for one block.
- [ ] Pasting a URL offers a mention with preview.

## W13 Attachments

- [ ] `/image` and `/file` insert a media block with upload.
- [ ] Uploaded files appear in exports.
- [ ] Size limit and replace behaviour (ours: undocumented).

## W14 Permissions

- [ ] Share shows people with an access dropdown, an invite field, copy link, publish tab.
- [ ] Sub-pages inherit the parent's access and can be changed.

## W15 Offline

- [ ] A page can be made available offline in the app.
- [ ] Offline edits of downloaded pages sync when online.
- [ ] Sharing and permission changes are refused offline.
