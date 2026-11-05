# Zammad - Structure and UI/UX

## Ticket mask

```
┌──────────────────────────────────────────────────────────────────────┐
│ Icon bar │ Filter/links         │ Ticket #1231 "Printer offline" ⋮   │
│ ▦ 🎫 👥 📚 ⚙│ Saved filters          ├──────────┬───────────────────────┤
│          │ Open tickets         │ Article  │ Attributes              │
│          │ Overdue              │ ┌──────┐ │ Status: open            │
│          │ Shared               │ │Cust..│ │ Owner: Anna             │
│          │                      │ │"New… │ │ Group: Support          │
│          │                      │ └──────┘ │ Priority: high          │
│          │                      │ Reply    │ Tags: drucker, hw       │
│          │                      │ editor   │ Customer: Beta GmbH     │
│          │                      │ [📎 😃 ✉→]│ Org: Beta GmbH           │
└───────────────────────────────────┴──────────┴───────────────────────┘
```

- Middle: a chronology of customer articles and notes, reply editor at the bottom
- Right: attributes and history, left: filter navigation

## UI/UX

- Zammad "tile" design, light/dark themes, accent colours chosen by the admin
- Full-text search (⌕) opens an overlay with live hits
- Drag & drop: attachments into the editor, filters on the left by click

## Interactions

- **Bulk selection**: checkboxes on the left → "edit mask" with state/owner/tags actions
- **Text-block picker**: `#` in the editor opens the block list
- **Number overlay**: the SLU ticker at the top right shows upcoming deadlines
- **Animations**: articles fade in; live updates via WebSocket without reload

## Responsive design

| Width | Behaviour |
|-------|-----------|
| Desktop | Three columns |
| Tablet | Attributes as an expandable panel |
| Mobile | Single column, navigation as a drawer |

## Accessibility

- Keyboard palette (`Ctrl+Shift+K`) for navigation/actions
- Editor with standard keyboard/screenreader support; live regions for new articles
- Colour status additionally with text (open/…, closed)

## Performance

- Elasticsearch keeps search < 1 s with > 1 million articles; the WebSocket channel keeps the masks current
