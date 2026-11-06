# Trello - Structure and UI/UX

## Page structure

```
┌─────────────┬─────────────┬─────────────┬────────────────────────┐
│ ← Workspace     Board "Editorial"      Members ☹☹☹  ☰ ⋮          │
├─────────────┬─────────────┬─────────────┬────────────────────────┤
│ Ideas       │ Doing       │ Review      │ Done                   │
│┌─────────┐  │┌─────────┐  │┌─────────┐  │┌─────────┐             │
││✎ Title  │  ││✎ Title  │  ││✎ Title  │  ││✓ Done   │             │
││🏷🔴 📅     │  ││🏷🟡 👤     │  ││📅 late   │  │└─────────┘             │
│└─────────┘  │└─────────┘  │└─────────┘  │                        │
│ [+ Card]    │             │             │                        │
└─────────────┴─────────────┴─────────────┴────────────────────────┘
```

- Lists scroll horizontally; a card is an overlay (modal) with the activity feed on the right

## UI/UX

- Playful base design (background images, card colours) — deliberate lightness
- The card preview shows labels, due date and checklist progress

## Interactions

- **Drag & drop** (card ↔ list, list ↔ position), long-press on mobile
- Create a card with `C` (see [shortcuts.md](shortcuts.md)), checklists are collapsible
- Live: cards move for all participants almost simultaneously

## Responsive design

- Web is responsive; the mobile app is fully functional (board look); table/timeline views are desktop-heavy

## Accessibility

- Keyboard control is well covered (shortcuts overlay `?`); drag alternative: card menu "Move"
- Labels always carry text; colours are an additional code

## Performance

- Very large boards (>500 cards) slow the drag fluidity; archiving lists helps
