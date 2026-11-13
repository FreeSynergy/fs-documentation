# Confluence (Cloud, latest) · States

Every state a user can be in, what the user sees and what the user can do. Sources: S-numbers as in [index.md](../index.md). Visual details of a state that no official page describes are marked **[nicht belegt]**; they must not be invented when rebuilding.

## Overview

| State | What the user sees | What the user can do | Source |
|-------|--------------------|----------------------|--------|
| Empty space / empty tree | Space sidebar with space overview, pages, live docs, blogs, whiteboards entries; no pages below. Exact empty-state text: **[nicht belegt]** | Create via the **+** next to **Content**, or **Create** in the top bar | [S14][S23] |
| Empty list (Drafts, Starred, Recent, Trash) | Empty text of each list: **[nicht belegt]** | Leave; create content | – |
| Loading | **[nicht belegt]** (no help page describes skeletons or spinners) | wait | – |
| Reading a page (view mode) | Breadcrumbs (caret shows full path), header with "Last updated" (hover shows last editor), title area with owner/status/read time/views, body, floating action bar | Edit (`E`), comment, watch, share, favourite, open Details panel, open more-actions menu | [S15][S12] |
| Details panel open | Right panel: owner, views, read time, contributors, creator, status, classification, labels, linked files, attachments, Jira links, Smart Links | read, change labels/status, close | [S15] |
| Single item selected in the tree | Highlighted entry; hover shows **+** and a more-actions menu | open, **+** create child, drag, ••• menu | [S23][S24] |
| Multiple selection | Not documented for the page tree. Space admins with **Content manager** (Premium/Enterprise) select several items for archive or delete (500 / 100 limit) | bulk archive, bulk delete | [S28] |
| Dragging in the tree | Item is moved with its children; drop position decides the order. Drop-target highlight: **[nicht belegt]** | drop to reorder, release elsewhere to cancel (cancel behaviour **[nicht belegt]**) | [S24] |
| Editing a draft (new page) | Editor with title field, toolbar (fixed top or inline on selection), **Close draft**, lock icon, **Publish…**; breadcrumbs hidden | type, format, `/` insert, close draft, publish, discard | [S23][S15] |
| Editing a published page | Editor with **Update** instead of **Publish…**; unpublished edits auto-save; viewers see an "unpublished changes" badge | update, adjust update settings, view changes, revert | [S23] |
| Auto-saving | Saving happens as the user types; indicator text: **[nicht belegt]** | continue | [S23] |
| Unpublished changes pending | Badge next to the title for viewers; **View changes** and **Revert to previous version** under ••• for the editor | publish, review diff, revert (permanent) | [S23] |
| Conflict | For pages: **[nicht belegt]** in the pages read. For REST writes in spaces needing approval: HTTP 409 [S9]. Name clash on copy or restore: user must rename first | rename, retry | [S24][S25][S9] |
| Version being viewed (old version) | Page content of that version; **Restore this version** at the top | restore, compare, delete the version | search summary 2026-11-13, [S25] |
| Comparing versions | Two or more versions ticked; diff with large unchanged parts collapsed | read the diff, restore | search summary |
| Search open | Search field; quick search; results list. Archived content is excluded unless advanced search | open a result, filter, close | [S14], search summary |
| Search without results | **[nicht belegt]** | change term/filters | – |
| Trash view (space settings) | List of deleted items with **Restore** and **Purge**; **Purge All** at the top | restore (rename on clash), purge one, purge all | [S25] |
| Archived item | Banner with the archive note; "Archived" lozenge on links; editing, comments, likes, move, duplicate, share are disabled | restore (with Archive permission), read | [S28] |
| Hidden item | Not in the tree; still in search and reachable by URL | restore to tree by moving; **Space settings → Content → Hidden** lists them | [S24] |
| Import in progress | Import tab with chosen files; completion shows a **Finish** step. Progress display: **[nicht belegt]** | finish, close | [S26] |
| Import finished (one file) | Draft page or live doc ready to edit | edit, publish | [S26] |
| Import finished (many files) | Restricted placeholder page "Imported pages" with date/time and child pages | review privately, organise, set permissions | [S26] |
| Import error | Limit violations (size, count); unsupported images become placeholder text; shapes become placeholders. Message wording: **[nicht belegt]** | split the import, convert images | [S26] |
| Permission denied / no access | Menu entries (Delete, Duplicate, Archive, creation) are not offered; archived items without view rights are neither listed nor reachable by link | ask a space admin | [S23][S24][S25][S28] |
| Restricted page | Page restrictions block viewing or deleting; lock icon on drafts | change via the lock icon (editors) | [S23][S25] |
| Offline / connection lost | **[nicht belegt]** (offline mode and mobile behaviour are not verified, see [features.md](features.md)) | – | – |
| Locked (someone else editing) | **[nicht belegt]** for pages; live docs are edited together in real time (help page exists, not read) | – | – |
| Error (generic) | **[nicht belegt]** | – | – |

## Transitions that matter

| From | Action | To |
|------|--------|----|
| Reading | Edit / `E` | Editing a published page |
| Create | Page / template | Editing a draft |
| Editing a draft | Close draft | Draft kept (Drafts list) |
| Editing a draft | Publish… → Publish | Reading the new page |
| Editing a draft | Delete unpublished page | Draft gone (permanent) |
| Editing a published page | Update | Reading with a new version |
| Reading | Delete | Trash (restorable) |
| Trash | Restore | Space root, outside the sidebar |
| Trash | Purge | Gone, with versions and attachments |
| Reading | Archive | Archived |
| Archived | Restore | Tree of the space |
