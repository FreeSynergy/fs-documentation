# Outlook m365-2026-11 — Interaction

✅ = seen in a screenshot · ⚠️ = inferred or known from the product, not seen.
Gestures belong to the frontend, not to the composer (ADR 0037).

## Hover and focus
- **Contact hover card**: pointing at a person (sender, recipient) opens a card with photo, presence,
  role and department, quick actions (mail, chat, external profile), contact details (mail, phone,
  location), the manager line ("reports to") and links to more ✅ (seen in an older web state).
- Hover on a list row shows quick actions (flag, delete, pin, read/unread) ⚠️ — the classic menu
  "Set Quick Actions" ✅ shows that these hover buttons are configurable.
- Grammar suggestion popover on an underlined word in the composer: explanation, one-tap fix,
  ignore, more, open the full editor ✅.
- Selected row: light blue fill; focused tab: underline in accent colour ✅.
- Tooltips on icon-only ribbon buttons ⚠️.

## Drag and drop
- Drag mails onto folders to move them ⚠️ (known; not seen).
- Drag files into the composer to attach ⚠️.
- Classic: "drag your favourite folders here" hint above the folder pane ✅ — favourites are filled by drag.

## Gestures

### Finger
- Mobile list: swipe left/right on a row for configurable actions (archive, delete, flag, snooze,
  read) ⚠️ — known from the product, **not in the screenshots**.
- Mobile: tap the floating "New email" button; tap its chevron for other new items ✅.
- Mobile: Focused/Other segmented toggle and filter button ✅.
- Pull to refresh ⚠️.

### Mouse
- Right-click on a row opens the long context menu ✅ (see [menus](menus.md)).
- Split buttons: left part runs the default, the arrow opens the choices ✅.
- Expand chevron on a row unfolds the conversation ✅.
- Classic: "quick click" on the flag column sets a pre-chosen flag ✅ (menu entry seen).
- Slider for undo-send delay in settings ✅.

### Pen
- Not seen ⚠️.
