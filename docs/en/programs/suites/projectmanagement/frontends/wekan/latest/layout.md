# Wekan - Structure and UI/UX

## Page structure

```
┌───────────────────────────────────────────────────────────────────┐
│ Organisation ▾   Board "Sprint board"          Members  ⋮  ☰     │
├───────────────────────────────────────────────────────────────────┤
│ Swimlane "Q4"                                                     │
│  ┌─ To Do ──┬─ Doing ──┬─ Done ─┐                                 │
│  │ Card A 🏷│ Card C   │        │                                 │
│  └──────────┴──────────┴────────┘                                 │
│ Swimlane "Backlog"                                                │
│  ┌─ To Do ─────────────┐                                          │
│  │ Card B 📅11.11 👤   │                                          │
│  └─────────────────────┘                                          │
├───────────────────────────────────────────────────────────────────┤
│ Card "B": description · checklist · labels · custom fields        │
└───────────────────────────────────────────────────────────────────┘
```

- Swimlane headings as horizontal bands; card modal centred, activity on the right

## UI/UX

- functional, denser than Trello; swimlanes scroll horizontally
- colour accent per swimlane/label

## Interactions

- **drag & drop** cards between lists/swimlanes; checkbox bulk action limited
- real time: Meteor sync, cards move live for everyone
- quick-cards editor (title + Enter)

## Responsive design

- desktop-optimised; on mobile conditional scrolling (no own layout concept)

## Accessibility

- keyboard tabbing for forms; drag has no keyboard alternative (the card menu "move" acts as a substitute)

## Performance

- very large boards (>2k cards) slow down; swimlane/list archiving recommended
