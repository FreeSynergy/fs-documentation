# Apple Mail iOS 26 — Interaction

✅ = seen · ⚠️ = inferred. Gestures belong to the frontend, not to the composer (ADR 0037).

## Hover and focus
- Not applicable on the phone. On the Mac: focus ring on the search field ✅; hover not seen ⚠️.
- Callout magnifier in Apple's help images is an illustration, not a UI feature ✅.

## Drag and drop
- Reorder smart mailboxes by their drag handles in edit mode ✅.
- Drag mails onto mailboxes ⚠️ (known on iPad/Mac, not seen).

## Gestures

### Finger
- **Swipe left on a row** → the row slides and reveals three round buttons with labels: More (grey),
  Flag (orange), Delete (red) ✅. A full swipe triggers the last action ⚠️.
- **Swipe right on a row** → mark read/unread ⚠️ (not seen).
- **Long press on a row** → lifted preview of the mail plus a menu (reply, reply all, forward, Mark,
  Notify Me, Mute) ✅.
- **Tap "Select"** → multi-select mode; then "Move" opens a sheet with a stacked preview ✅.
- **Tap a category chip** → filters the inbox ✅; chips scroll sideways ⚠️.
- **Tap up/down arrows** in an open mail → next/previous mail ✅.
- **Tap a sender** → contact card sheet ✅.
- **Tap a flag colour** in the action sheet → flag with that colour ✅.
- **Microphone in the search capsule** → dictate a search ✅.
- Swipe down to close a sheet; pull to refresh ⚠️.

### Mouse (macOS) ✅
- Toolbar buttons, menus, search suggestions dropdown; split view of sidebar/list/reading pane.

### Pen
- "Add sketch" from a nearby iPad into a Mac composer ✅ (attach menu) — pen input through Continuity.
