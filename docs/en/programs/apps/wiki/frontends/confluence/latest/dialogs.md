# Confluence (Cloud, latest) · Dialogs

Every dialog found in the help pages read: purpose, fields, buttons, default button, behaviour on cancel. Sources: S-numbers as in [index.md](../index.md). Details the pages do not state are marked **[nicht belegt]**; in particular the **default button** and the **Esc / click-outside behaviour** are not described by Atlassian for any dialog read, so they are listed as **[nicht belegt]** and must be decided by us (see [gaps.md](gaps.md)).

## D1 Create panel (top bar **Create**) [S23]

- **Purpose:** choose what to create.
- **Fields/choices:** content kinds (Page, live doc, and others per [menus.md](menus.md)), template list on the right, **Create with Rovo** (drafts from a short prompt) [S23].
- **Buttons:** the kind entries and templates themselves open the editor.
- **Default / cancel:** **[nicht belegt]**.

## D2 Template browser (**Templates and import** tab) [S26][S31]

- **Purpose:** pick a template or import files.
- **Tabs:** templates, **Import**.
- **Buttons:** **Use template** (template preview) [S31 snippet].
- **Behaviour:** the browser closes when the user starts typing in the draft; reopen it via **Templates & import** [S26].
- **Default / cancel:** **[nicht belegt]**.

## D3 Publish dialog (new page) [S23]

- **Purpose:** publish a draft.
- **Fields:** **Location** (place in the tree), **Access** (who can view or edit), **Version comments**, notify-watchers option, **Schedule publish** (dropdown opening a date/time picker with **OK**, then **Schedule**) [S23].
- **Buttons:** **Publish** (becomes **Schedule** when a time is set) [S23]; a close/cancel control exists, its label is **[nicht belegt]**.
- **Publish as:** under ••• → More options: **Page** or **Blog** [S23].
- **Default / cancel:** primary action is **Publish** (as the confirming button); cancel behaviour **[nicht belegt]**, the draft remains (auto-saved) [S23].

## D4 Adjust update settings (published page) [S23]

- **Purpose:** review settings before updating.
- **Opened by:** caret next to **Update** → **Adjust update settings**.
- **Fields:** location, access, notify-watchers checkbox, version comment, scheduling, convert to blog post.
- **Buttons:** **Update** (schedule variant via the picker).
- **Cancel:** **[nicht belegt]**.

## D5 Move dialog [S24]

- **Purpose:** choose a new parent, possibly in another space.
- **Fields:** tab **Browse** (tree), tab **Search** (find a parent), destination space choice (other-space move; only accessible spaces listed).
- **Buttons:** **Start over** (resets the tree), **Move**.
- **Default:** **Move** after a target is selected. Cancel: **[nicht belegt]**.
- **Permission note:** destination needs view and add rights [S24].

## D6 Duplicate dialog [S24]

- **Purpose:** copy an item.
- **Fields:** destination space and parent; checkbox **Include children**; with children a second step (**Next**) for bulk naming, with optional inclusion of restrictions and labels.
- **Buttons:** **Next**, **Duplicate**.
- **Result naming:** "Duplicate of …" prefix; unique names required in a space.
- **Cancel:** **[nicht belegt]**.

## D7 Delete confirmation [S25]

- **Purpose:** confirm moving an item to the trash.
- **Opened by:** **More actions (•••)** → **Archive and Delete** → **Delete**.
- **Fields/buttons:** the confirmation texts and button labels are **[nicht belegt]** in the page read. The help says children move up to the nearest parent [S25], so the dialog may mention it (not verified).

## D8 Import dialog (Word / Google / OneDrive) [S26]

- **Purpose:** bring documents in.
- **Choices:** **Word document (.docx)**, **Google Doc**, **OneDrive**.
- **File selection:** the operating system's file chooser for Word files (**Open**); a connect-account step for Google/OneDrive and a document picker (**Select**).
- **Buttons:** **Open** / **Select**, **Finish**.
- **Limits:** see [workflows.md](workflows.md) W11.
- **Cancel:** closing the chooser aborts the selection; wording **[nicht belegt]**.

## D9 Archive dialog [S28]

- **Fields:** optional note (why archived). The note can be edited only by the person who archived.
- **Buttons:** confirm; label **[nicht belegt]**.
- **Scope:** parent and all nested items, all-or-nothing.

## D10 Restore-from-trash rename prompt [S25]

- **Purpose:** resolve a name clash.
- **Fields:** new name for the item. **Buttons:** **Restore** (after renaming). Cancel: **[nicht belegt]**.

## D11 Purge / Purge All [S25]

- **Purpose:** delete trash entries for good (items, versions, attachments).
- **Buttons:** **Purge**, **Purge All**. Confirmation wording: **[nicht belegt]**.

## D12 Version history panel and restore comment [search summary 2026-11-13]

- **Panel:** list of versions with checkboxes, **Compare selected versions**, **Restore this version**, **Delete**.
- **Restore step:** the default change comment can be edited → **OK**.
- **Cancel:** **[nicht belegt]**.

## D13 Keyboard shortcuts dialog [S12][S13]

- **Opened by:** Shift+? (view), Ctrl+/ or Cmd+/ (editing). Shows the shortcut list; close control **[nicht belegt]**.

## D14 Space export dialog [S16]

- **Opened by:** **Space settings → General → Export space** (space admins).
- **Choices:** format PDF, CSV, HTML or XML; selected pages possible (see [features.md](features.md)). Other fields **[nicht belegt]**.

## D15 Share dialog [S12]

- **Opened by:** **Share** button, Ctrl+Alt+S. Fields and buttons: **[nicht belegt]** in the pages read.

## D16 Page restrictions

- **[nicht belegt]**. The lock icon next to **Publish…** changes access for drafts [S23]; the dialog fields are not described in the pages read.

## Additions 2026-11-14 (S32 to S34, S23, S25, S28)

These were read on 2026-11-14. Where one of the entries D1 to D16 above says **[nicht belegt]**, the pages read still do not state it unless named here.

## D17 Share dialog (replaces D15) [S32][S33]

- **Opened by:** **Share** button at the top of the content, Ctrl+Alt+S / Cmd+Opt+S [S12].
- **Fields:** search field for people and groups (suggestions), permission choice view or edit where it applies, a notify checkbox, optional message [S32]. For restrictions the same dialog has the sections **General access** and **Specific access** (search, **Can edit** / **Can view**, per entry a menu with **Remove**) and a tab for access requests [S33].
- **Buttons:** **Share** (send), link icon (copy link), **Save** (after changing General access), **Remove all**, **Remove**, **Approve**, **Deny** [S32][S33].
- **Errors:** teams are not compatible with Share; invitations to outsiders may go to an administrator for approval, a refused request is mailed to the sender only [S32].
- **Undo:** removing a person with **Remove** [S33]; withdrawing a share otherwise **[nicht belegt]**. Cancel behaviour **[nicht belegt]**.

## D18 Share to Slack [S32]

- **Opened by:** the Slack option of the Share dialog. **Buttons:** **Sign in**, **Add new workspace**, **Share**. **Fields:** workspace, channel or person, optional message. Cancel and errors **[nicht belegt]**.

## D19 Access requests (restrictions) [S33]

- **Buttons:** **Approve** (adds the person to Specific access and tells them), **Deny** (removes the request for everybody, the requester is not told). Closing keeps the request open [S33].

## D20 Quick search drawer and Advanced search [S34]

- **Opened by:** `/` or the search field in the top bar. **Content:** names of pages, blog posts, whiteboards, slides, people, files and spaces, newest first; at the end **Advanced**. Enter or **Advanced** opens the results page.
- **Filters on the results page:** Spaces (with archived spaces), Contributors, Type (pages, live docs, blog posts, whiteboards, slides, attachments, comments), Last modified, Labels, Pages under, **Search titles only**. Several contributors or labels are an OR [S34].
- **Errors:** the text shown for "no results" is **[nicht belegt]**.

## D21 Recent drawer [S34]

- Tabs **Visited**, **Worked on**, **Drafts**, **Starred**; a field filters by characters in the title (no full text) [S34]. The home page "Recent" part has the tabs **All**, **Worked on**, **Owned by me**.

## D22 Show details panel (before a delete) [S25]

- Shows incoming links, labels, outgoing links and content information. Not a confirmation: closing it changes nothing [S25].

## D23 Archive note dialog [S28]

- Fields: optional note. Buttons: **Archive** (first time), **Add** / **Update** (later, via the banner or the Archived list). Only the person who archived may change the note [S28].

## D24 Revert to previous version [S23]

- Shows the unpublished changes first and then discards them for good; the help says they cannot be recovered. A cancel control: **[nicht belegt]**.

## Dialog-Inventar

Machine-readable list for `scripts/menue-vergleich` (one dialog per line; indentation = parts of the dialog). Names are the names used in the help; where the help gives no name, the name of the button that opens it is used and the line says so in the section above.

- Create panel {de: Erstellen-Fenster}
- Template browser {de: Vorlagen-Fenster}
- Publish dialog {de: Veröffentlichen-Dialog}
  - Schedule publish
- Adjust update settings {de: Aktualisierungs-Einstellungen}
- Move dialog {de: Verschieben-Dialog}
  - Browse
  - Search
- Duplicate dialog {de: Duplizieren-Dialog}
- Delete confirmation {de: Löschen-Bestätigung}
- Show details {de: Details anzeigen}
- Restore from trash {de: Aus dem Papierkorb wiederherstellen}
- Purge {de: Endgültig löschen}
- Purge All
- Import dialog {de: Import-Dialog}
- Archive dialog {de: Archivieren-Dialog}
- Archive note {de: Archiv-Notiz}
- Version history {de: Versionsverlauf}
  - Restore this version
  - Compare selected versions
- Revert to previous version
- Keyboard shortcuts dialog {de: Tastenkürzel-Dialog}
- Space export dialog {de: Space-Export-Dialog}
- Share dialog {de: Teilen-Dialog}
  - General access
  - Specific access
  - Access requests
- Share to Slack
- Quick search {de: Schnellsuche}
- Advanced search {de: Erweiterte Suche}
- Recent drawer {de: Zuletzt-Fenster}
- Attachment properties {de: Anhang-Eigenschaften}
- Page restrictions {de: Seiteneinschränkungen}
