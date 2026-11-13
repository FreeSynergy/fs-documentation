# Confluence (Cloud, latest) · Acceptance checklist

Derived from [workflows.md](workflows.md). Every line is a click-through test with the answer **yes / no**. A frontend in this style passes only when every line without a note is "yes". Lines tied to something the vorbild leaves open (**[nicht belegt]**) are decisions for us; they are marked "ours" and must be decided, not copied. States and dialogs referred to: [states.md](states.md), [dialogs.md](dialogs.md).

## W1 Create

- [ ] A **Create** entry in the top area opens a choice of content kinds and templates.
- [ ] Choosing "page" opens an empty editor with a draft, no dialog in between.
- [ ] Choosing a template opens the editor pre-filled from it.
- [ ] A **+** next to the content heading of a space creates a draft in that space.
- [ ] Hovering a tree entry shows a **+**; using it creates the draft as a child of that entry.
- [ ] Without permission the entry points are absent or say why (ours: decide which).
- [ ] An untitled draft is listed with a placeholder name, not as an empty row.

## W2 Edit, drafts, auto-save

- [ ] `E` on a page opens the editor.
- [ ] Typing `# `, `1. `, `> `, `---` creates heading, list, quote, divider at once.
- [ ] `/` opens a quick-insert menu; choosing an entry inserts the block.
- [ ] Selecting text shows a toolbar for formatting (fixed or inline, switchable).
- [ ] Closing the editor without publishing keeps the text (no "save?" question).
- [ ] The **Drafts** list shows the kept draft; opening it resumes editing.
- [ ] A published page with unpublished edits shows a badge to viewers.
- [ ] "View changes" shows the unpublished edits against the published page.
- [ ] "Revert to previous version" discards the unpublished edits after confirmation.
- [ ] Deleting a never-published draft removes it for good.
- [ ] The author's draft is invisible to others until access is given.
- [ ] The save state is visible (ours: indicator not documented by the vorbild).

## W3 Publish / update

- [ ] **Publish…** on a new page opens a dialog with location, access, version comment, schedule.
- [ ] Confirming shows the page in view mode and adds a history entry with the comment.
- [ ] **Update** on a published page publishes without the full dialog.
- [ ] "Adjust update settings" opens the full dialog including notify watchers.
- [ ] Ctrl+Enter publishes; Ctrl+Shift+Enter publishes with a note.
- [ ] A scheduled publish shows the date and does not publish before it.

## W4 Rename (ours: no vorbild steps)

- [ ] The title can be changed in the editor and appears in tree, breadcrumbs and links' display text.
- [ ] A title already used in the space is refused with a message that names the clash.

## W5 Move, reorder

- [ ] Dragging a tree entry to another position reorders it; children move along.
- [ ] After a move, pages that linked to it still open it.
- [ ] A **Move** command opens a dialog with a tree tab and a search tab.
- [ ] **Start over** resets the tree in the dialog.
- [ ] Moving into another space lists only reachable spaces.
- [ ] Attachments and comments move with the page.
- [ ] A user without the right does not get the Move entry or gets a clear refusal.
- [ ] An item moved to the top level (hidden) leaves the tree but is still found by search.

## W6 Duplicate

- [ ] Duplicate asks for destination space and parent.
- [ ] "Include children" leads to a naming step.
- [ ] The copy is named with a prefix and keeps attachments and labels, not comments or history.
- [ ] Duplicate is not offered while editing.

## W7 Delete, trash, restore

- [ ] Before deleting, the details show incoming links and children.
- [ ] Delete asks once, then the item is gone from the tree and sits in the trash.
- [ ] Children of the deleted item move up one level.
- [ ] The trash lists the item with **Restore** and **Purge**.
- [ ] Restore with a taken name asks for a new name first.
- [ ] A restored item appears (at the space root) and can be found again.
- [ ] **Purge** removes one entry for good; **Purge All** removes all.
- [ ] Deleting a draft or a version never sends it to the trash.

## W8 Archive

- [ ] Archive takes an optional note and removes the item and its descendants from tree and quick search.
- [ ] Links to it still work and show an "archived" marker.
- [ ] An archived item cannot be edited, moved, duplicated or shared.
- [ ] The archived list restores it to the tree.

## W9 History

- [ ] The history lists versions with author, time and comment.
- [ ] Ticking two versions and choosing compare shows the differences; unchanged parts are collapsed.
- [ ] Restoring a version asks for a comment and keeps all later versions.
- [ ] Deleting a single version is permanent and says so.

## W10 Search

- [ ] A shortcut opens search from anywhere.
- [ ] Typing shows results; opening a result navigates to it.
- [ ] Archived content is not in quick search but can be included on request.
- [ ] A filter can be added to narrow results (ours: filter list must be decided).

## W11 Import

- [ ] Import is reachable from the new-draft's more-actions menu under "templates and import".
- [ ] The Word choice opens the system file chooser; several files can be chosen.
- [ ] One file gives a draft; several give pages under one restricted placeholder page.
- [ ] A file above the size limit is refused with the limit named.
- [ ] Unsupported images become visible placeholder text, not silent loss.
- [ ] Markdown / HTML / other-wiki import: ours (the vorbild pages read do not describe it).

## W12 Export

- [ ] A page can be exported to Word and to PDF from its menu.
- [ ] A space admin can export a space to PDF, CSV, HTML, XML.
- [ ] Unpublished content is not exported.

## W13 Links and backlinks

- [ ] Ctrl+K opens a link picker with internal items and an external address field.
- [ ] Pasting an internal address turns into a link showing the page's name.
- [ ] The details of a page list incoming and outgoing links.

## W14 Attachments

- [ ] Dropping a file on a page attaches it and shows it.
- [ ] Uploading the same name creates a new attachment version.
- [ ] The attachments view downloads one file or all as a zip.
- [ ] Deleting an attachment needs the right; a deleted file can be restored by an admin.

## W15 Permissions

- [ ] A draft has a lock control that changes who may see it.
- [ ] A restriction on a page blocks deleting for others.
- [ ] Archiving warns about inherited access.
