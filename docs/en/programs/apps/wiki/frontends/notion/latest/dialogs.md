# Notion (latest) · Dialogs

Every dialog or menu-window found in the help pages read: purpose, fields, buttons, default, cancel. S-numbers refer to [index.md](../index.md). Notion's pages do not describe default buttons or Esc/click-outside for any of them; these are **[nicht belegt]** and are for us to decide (see [gaps.md](gaps.md)).

## D1 Search window [S26]

- **Purpose:** find a page, jump to a recent page.
- **Fields:** search box; sort (Best matches, Last edited, Created); filters Title only, Created by, Teamspace, In, Date (Today, Last 7 days, Last 30 days, custom range).
- **Buttons:** result rows. On desktop Command Search can copy a result's link (cmd/ctrl+L, cmd+shift+C).
- **Default / cancel:** Enter on the first result is not documented; closing: **[nicht belegt]**.

## D2 Slash menu [S11][S30]

- **Purpose:** insert or change a block. **Field:** the typed word filters the list. **Default:** Enter takes the highlighted entry (stated in the shortcut page: type the command, press Enter). Cancel: **[nicht belegt]**.

## D3 Block menu (⋮⋮) [S30]

- **Entries:** Turn into, Duplicate, Move to, Delete, Comment, Copy link to block [S28]. Menu, no fields.

## D4 Page menu in the sidebar (•••) [search summary 2026-11-13]

- **Entries:** Delete, Duplicate, Copy link, Rename, Move to. Rename takes inline text; wording of the confirmation: **[nicht belegt]**.

## D5 Move to [search summary][S12]

- **Purpose:** choose a page or workspace to move into.
- **Fields:** a searchable list of pages/workspaces (exact layout **[nicht belegt]**).
- **Effect:** inside a workspace it moves; across workspaces it duplicates [search summary].

## D6 Import [S25]

- **Purpose:** bring files or other apps in.
- **Start:** Settings → Import, `/` importer, or page ••• → More → Import.
- **Choices:** source list (text, Markdown, Word, CSV, HTML, PDF, ZIP, Evernote, Trello, Google Docs, …).
- **File selection:** system file chooser (several files for PDF, HTML, Markdown, Word, TXT); CSV and ZIP flows differ. Field wording: **[nicht belegt]**.
- **Result list:** tabs **In progress** and **Complete** in Settings → Import (time, status, size).

## D7 Export [S27]

- **Opened by:** page ••• → Export.
- **Fields:** format (Markdown & CSV, HTML; PDF per the search summary), toggle **Include subpages**.
- **Buttons:** an export confirmation; label **[nicht belegt]**. Other options (content, page tree) are not described in the page read.

## D8 Export workspace [S27]

- **Opened by:** Settings → General → Export all workspace content.
- **Fields:** format; Include subpages for top-level pages. **Result:** e-mailed link, 7 days.

## D9 Share [S29]

- **Fields:** person/group rows with an access dropdown (Full access, Can edit, Can edit content, Can create, Can comment, Can view); invite by e-mail; general access (invited only, workspace, anyone with link); expiry for links.
- **Buttons:** **Invite**, **Copy link**, tab **Publish**. Default: **[nicht belegt]**.

## D10 Version history [S14]

- **Content:** the version list and a preview. **Button:** **Restore**. Cancel: leaving the view; **[nicht belegt]**.

## D11 Trash [S14]

- **Content:** list, search, filters (last editor, original location, teamspace). **Buttons:** restore (curved arrow), delete permanently on an opened page. No "empty all".

## D12 Deleted properties [S14]

- **Opened by:** Settings → Edit properties → Deleted properties. **Buttons:** arrow (restore), trash can (delete for good, cannot be undone).

## D13 Offline settings [S31]

- **Opened by:** Settings → Offline. **Content:** downloaded pages, search, stop access per page, switch off automatic download.

## D14 Customize page [search summary][S15]

- **Content:** Font (Default, Serif, Mono), Small text, Full width, Table of contents; toggles for backlinks and comments.

## Additions 2026-11-14 (S25, S26, S29, S30, S32 to S34; S14, S12, S15 re-read)

Notion's pages state no default button and no Esc behaviour for any dialog; only the slash menu closes with Esc [S11]. That stays **[nicht belegt]**.

## D15 Export dialog, fields [S32]

- **Opened by:** page ••• → More → Export (PDF), or ••• → Export (HTML, Markdown & CSV); mobile ••• → More → Export.
- **Fields:** Format (PDF, HTML, Markdown & CSV); Include content, Page format and Scale percent (PDF only); Include subpages; Create folders for subpages. **Button:** Export.
- **Rules:** subpages in a PDF need a business plan; guests need Full access; an Enterprise setting "Disable export" hides the entry; databases export their current view; form views cannot be exported [S32].
- **Errors:** a failed PDF is advised to be exported as HTML; very large exports arrive as an e-mailed link; on Windows ZIP paths over 260 characters fail (turn off folders for subpages) [S32]. **Undo:** **[nicht belegt]**.

## D16 Import, buttons and limits [S25]

- **Buttons by source:** Import (Evernote), Continue (Trello), Connect Google account and Select (Google Docs), Merge with CSV (in a database), Convert Zip to pages. Target: a teamspace, Private or an existing database; CSV columns are mapped to properties.
- **Limits:** desktop and web only; Free 5 MB per file, paid 50 MB (PDF 20 MB), ZIP up to 5 GB; one CSV at a time. **Errors:** named per source (Trello "Unrecognized URL", Google Docs "Import failed" and others); an import only adds rows, it does not update (duplicates possible). **Undo:** **[nicht belegt]**.

## D17 Page icon and cover [S15]

- **Icon picker:** tabs Emoji, Icon, Upload; a random button; checkbox Add to workspace Emoji library (for an upload); Remove. **Cover:** Add cover, Change cover; gallery, Upload, Link, search in an image service. Dialog titles, formats, size limits, errors, undo: **[nicht belegt]**.

## D18 Share dialog, details [S29]

- Tabs **Share** and **Publish**; **Invite**; **Copy link**; access dropdown per entry with **Remove**; **General access** (Only people invited; Everyone at the workspace with Hide in search; Anyone on the web with link with Link expires); **Request edit access** for a person without rights. Errors on guest invitations: organisation domain, domain not allowed, guests blocked, guest limit [S29]. A confirmation on Remove and undo: **[nicht belegt]**.

## D19 Favorites, lock and move [S33][S12]

- Favorites: a star on the page; remove by clicking it again or ••• → Remove from Favorites [S12][S33]. Page menu: Lock page [S33]. Move to: a workspace dropdown moves a page between workspaces, subpages follow into Private [S33]. Layout of the Move to dialog: **[nicht belegt]**.

## Dialog-Inventar

Machine-readable list for `scripts/menue-vergleich`, one dialog per line. Names as in the help; where the help names none, the opening entry is used (see the sections above).

- Search window {de: Suchfenster}
- Slash menu {de: Schrägstrich-Menü}
- Mention menu {de: Erwähnungs-Menü}
- Block menu {de: Blockmenü}
- Page menu in the sidebar {de: Seitenmenü in der Seitenleiste}
- Move to {de: Verschieben nach}
- Import {de: Import}
- Export {de: Export}
- Export workspace {de: Workspace exportieren}
- Share {de: Teilen}
  - Publish tab
  - General access
- Version history {de: Versionsverlauf}
- Trash {de: Papierkorb}
- Deleted properties {de: Gelöschte Eigenschaften}
- Offline settings {de: Offline-Einstellungen}
- Customize page {de: Seite anpassen}
- Page icon picker {de: Seitensymbol-Auswahl}
- Cover dialog {de: Titelbild-Dialog}
