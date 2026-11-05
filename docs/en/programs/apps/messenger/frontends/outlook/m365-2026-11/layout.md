# Outlook m365-2026-11 — Layout

✅ = seen in a screenshot · ⚠️ = inferred. Desktop = new Outlook for Windows and web (same UI).

## Window structure

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│ [logo] Outlook        [ Search ……………… ]      ◇ ☑ 🔔 ⚙ 💡 (avatar)   [next event] │ title bar
├──┬───────────────────────────────────────────────────────────────────────────────┤
│  │ ≡  Home  View  Help                                                          │ ribbon tabs
│A │ [New mail ▾] Delete Archive Report Sweep Move… ↶ ↶↶ ↷ QuickSteps Read … [AI] │ ribbon (1 line)
│P ├───────────────┬────────────────────────┬────────────────────────────────────┤
│P │ Favourites    │ Focused | Other   ⚲ ⇅  │ Subject                      ⧉ ✕  │
│  │  Inbox     11 │ ▾ Pinned               │ ┌ AI summary card ────────────────┐ │
│R │  Invoices     │   row (pinned)         │ └─────────────────────────────────┘ │
│A │ ▾ account 1   │ ▾ Today                │ sender · to · time   ↶ ↶↶ ↷ …     │
│I │  Inbox     11 │   row  row  row        │ body                               │
│L │  Drafts …     │ ▾ Yesterday            │                                    │
│  │ ▸ account 2   │   row + [date · RSVP]  │                                    │
│  │ + Add account │                        │                                    │
└──┴───────────────┴────────────────────────┴────────────────────────────────────┘
  app rail          folder pane              message list              reading pane
```

## Regions

### Title bar
Product name, a wide **search field** in the centre, then icon buttons: premium offer, My Day / to-do,
notifications (bell with dot), settings, tips, profile picture; at the far right an
**upcoming-event chip** ("next meeting in 30 min", with a 1/2 pager when there are several) ✅.
Our fit: `widgets/navigation/toolbar` + `primitives/fields/search-field` + `widgets/data/avatar`.

### App rail (far left)
A narrow icon column switching between Mail, Calendar, Copilot, People, Groups, To Do, Word, Excel,
PowerPoint, OneDrive and "more apps" ✅. This is the suite switcher (ADR 0038 suite context).
Our fit: `widgets/navigation/sidebar` (collapsed) — in FreeSynergy the shell, not the messenger ⚠️.

### Ribbon
Three tabs on desktop (Home, View, Help) ✅; the composer adds Message, Insert, Format text, Options ✅.
Single-line "simplified" ribbon; groups separated by thin dividers; overflow under "…" and a chevron
to expand to the classic two-line ribbon ✅. Split buttons (New mail ▾, Send ▾, Delete ▾) ✅.
Classic Outlook: full ribbon with File, Home, Send/Receive, Folder, View, Help (+ add-in tabs) ✅.
Our fit: `widgets/navigation/toolbar` (ribbon variant with `tabs`).

### Folder pane
Collapsible sections: **Favourites** (cross-account), then one tree per account with Inbox, Drafts,
Sent Items, Deleted Items, Junk Email, Archive, Notes, user folders, search folders, "snoozed" folder ✅;
unread counters right-aligned ✅; "Add account" link at the bottom ✅; can be hidden from the View tab ✅.
Our fit: `widgets/data/tree-view` + `primitives/feedback/badge`.

### Message list
Header with Focused / Other tabs, a selection-mode toggle, filter and sort icons ✅. Collapsible
groups (Pinned, Today, Yesterday, This month) ✅. A row: avatar, sender, subject (blue when unread),
time, preview line, optional chips (meeting with RSVP, category tag), status icons (pin, flag,
calendar, @, attachment), expand chevron for the conversation, blue left bar for unread ✅.
Selected row: light blue background ✅; flagged/highlighted row: pale yellow background ✅.
Our fit: `widgets/data/list-view` (rows `With Avatars`/`With Badges`) + `widgets/navigation/tabs`.

### Reading pane
Subject line with pop-out and close; optional AI summary card; per message a header (avatar with
presence, sender, recipients, time) with reply / reply all / forward / more; body; meeting
response block for invitations ✅. Can be placed right, bottom or hidden ⚠️ (View → reading pane
option seen ✅, positions not seen).
Our fit: NEW `mail-view` + `widgets/containers/panel`.

### Composer (inline or pop-out)
Inline in the reading pane or as its own window ✅: Send split button, From selector, To/Cc (Bcc on
demand) with chips, subject, "draft saved at" note, body; zoom, pop-out and discard icons on the right ✅.
Our fit: NEW `composer` + `rich-text-editor` + `tags-input` (recipients).

### Status bar (classic only)
Item counts, unread counts, reminders, offline indicator, view switches and zoom slider; each item can
be shown/hidden from a context menu ✅.

### Settings dialog
A large modal with three columns: categories (Accounts, Files, General, Mail, Calendar, People,
Copilot) with a settings search box, sub-pages, content; Save / Discard at the bottom ✅.
Our fit: App shell settings (`sidebar` + `field` + `switch` + `select`).

## Responsive / mobile
Phone app ✅: coloured header (or picture theme) with account title, bell and search; Focused/Other
segmented toggle and a filter button; single-column list; floating **"New email" button** with an
expand chevron for other new items; bottom navigation (Mail, Calendar, Feed, Apps — or Mail, Search,
Calendar in another state) ✅. Toast-like note at the bottom ("new design", with an action) ✅.
Tablet/web older state shows the same three panes with a coloured top bar ✅.
