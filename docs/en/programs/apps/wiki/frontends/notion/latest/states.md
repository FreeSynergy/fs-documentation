# Notion (latest) · States

Every state, what the user sees, what the user can do. S-numbers refer to [index.md](../index.md). Visual details no official page gives are **[nicht belegt]** and must not be invented.

| State | What the user sees | What the user can do | Source |
|-------|--------------------|----------------------|--------|
| Empty workspace / empty section | Sidebar sections Private, Shared, Teamspaces; Favorites appears only after the first favourite. Empty-state text: **[nicht belegt]** | create with **+**, new-item menu, 📝 | [S12] |
| Empty page | A page with a title and no blocks; hint text: **[nicht belegt]** | type, `/` for blocks | [S11] |
| Loading | **[nicht belegt]** | – | – |
| Error (generic) | **[nicht belegt]**; for failed imports and exports see below | contact support (documented for data loss) | [S14] |
| Reading/working on a page | Title, blocks, backlinks line under the title (when any), **Share**, **•••**; page style (font, small text, full width, table of contents) | edit directly; there is no separate view mode in the pages read | [S15][S28] |
| Preview mode | Page opened by the 📝 button | edit | [S12] |
| Single block selected | Esc selects the block; block highlighted | arrows move selection, Enter edits text, cmd/ctrl+D duplicate, Delete removes, cmd/ctrl+Shift+arrows move, `/` or cmd/ctrl+/ change type | [S11] |
| Multiple blocks selected | Drag from the margin, Shift+click or Shift+arrows; word and character count shown | duplicate, delete, move, change type, comment | [S11][S30] |
| Text selected | Inline formatting via shortcuts (bold, italic, link, comment) | format; cmd/ctrl+K adds a link | [S11] |
| Slash menu open | List of block types filtered by the typed word | choose, Esc leaves (Esc behaviour **[nicht belegt]**) | [S11] |
| Drag in sidebar | Page moves; dropping onto a page nests it; dropping on Trash deletes it | drop, drag out to un-nest | [S12] |
| Page in Trash | Opened read-only; cannot be edited until restored | restore, delete permanently | [S14] |
| Trash view | List with search and filters (last editor, location, teamspace); curved arrow restores | restore, open, delete one by one; no "empty all" | [S14] |
| Archived page (beta) | "Archived" banner; hidden from search by default | read | [S14] |
| Search open | Window with recently visited pages; filters and sort | type, filter, open result | [S26] |
| No search results | **[nicht belegt]** | change term or filter | – |
| Version history open | List of versions; an opened version | restore, copy blocks out | [S14] |
| Import running | **Settings → Import**, tab In progress, with time, status, size | wait; if stuck retry smaller | [S25] |
| Import done / failed | Tab Complete; failures: stuck, ZIP failure, garbled CSV (no message wording) | retry, re-export as UTF-8, remove hidden files | [S25] |
| Export running | Large export may fail; the workspace export arrives as an e-mailed link valid 7 days | export in batches | [S27] |
| Conflict (simultaneous edits) | Text: merged automatically. Non-text property: only one value survives | re-edit | [S31] |
| Offline | Downloaded pages can be edited; slash menu marks blocks that need a connection; sharing impossible; other pages not available | edit, wait for sync (WiFi recommended) | [S31] |
| Not downloaded and offline | **[nicht belegt]** | – | – |
| No permission | Levels: Full access, Can edit, Can comment, Can view; export hidden for admins in some cases; backlinks to private pages show "Private" | ask for access | [S29][S27][S28] |
| Locked | **[nicht belegt]** (no page lock state was found) | – | – |
| Rate limit reached (duplication) | 50,000 blocks per hour; message **[nicht belegt]** | wait | [search summary] |
