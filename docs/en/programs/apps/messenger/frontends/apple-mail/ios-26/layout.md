# Apple Mail iOS 26 — Layout

✅ = seen in a screenshot · ⚠️ = inferred.

## Window structure

```
┌──────────────────────────────┐
│ 09:41            ▮▮ ≋ ▭     │ status bar
│ (‹)          [Select] (…)    │ floating round glass buttons
│ Inbox                        │ large title
│ iCloud · updated just now    │ subtitle
│ [● Primary] (🛒) (💬) (📣) … │ category chips (scroll sideways)
├──────────────────────────────┤
│ (av) Sender           09:15 ›│
│      Subject 🍳              │ list rows
│      preview, two lines …    │
│ ★(av) Sender          08:32 ›│ VIP star outside the row
│ ……                           │
│                              │
│ (≡)  ( 🔍 Search      🎙 ) (✎)│ floating bottom bar: filter · search · compose
└──────────────────────────────┘
```

## Regions

### Top bar
Floating circular buttons on the glass layer: back to mailboxes, "Select", more (…) ✅. No solid
navigation bar; content scrolls under it ✅. Our fit: `widgets/navigation/toolbar` (floating variant).

### Title block
Large bold title (mailbox name) with a small grey subtitle (account, last update) ✅.

### Category chips
A horizontal row of capsules: the active one is filled blue with icon and label, the others are grey
with icon only ✅. Our fit: `widgets/navigation/tabs` (chip variant) / `button-group`.

### Message list
Full-width rows with round avatar (photo or Memoji), sender in bold, time and chevron on the right,
subject, two lines of preview; hairline separators indented to the text ✅. VIP star sits in the left
margin ✅. Our fit: `widgets/data/list-view`.

### Bottom bar
Three floating elements: filter button, search capsule with microphone, compose button ✅.
Our fit: `primitives/fields/search-field` + `primitives/actions/button` (round).

### Message view
Top: back button with a counter capsule (e.g. inbox count), up/down arrows ✅. Line "1 email" and a
Summarize button ✅. Header: avatar, sender, "to" with chevron, time, flag ✅. Body below ✅.
Our fit: NEW `mail-view`.

### Sheets
Bottom sheets with rounded top corners for: message actions (2×2 tiles + list + colour row) ✅,
move to mailbox ✅, contact card (tinted with the contact's colour) ✅, about categories ✅.
Our fit: `widgets/overlays/drawer` (bottom sheet).

### Mailboxes screen
Large title "Mailboxes", subtitle "updated just now", a grouped card list; in edit mode tick boxes
and drag handles, "Done" as a filled blue capsule, "New mailbox" as a floating capsule ✅.

## Responsive / mobile
This version *is* the phone layout. On the Mac ✅ (current release): three columns — sidebar with
sections (Favourites, Smart Mailboxes, accounts), list with category tabs, reading pane — and a
toolbar of icon groups in glass capsules; window traffic lights top left ✅. iPad ⚠️ (not seen).
