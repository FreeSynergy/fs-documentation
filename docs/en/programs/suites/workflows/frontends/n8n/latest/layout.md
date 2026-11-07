# n8n - Structure and UI/UX

## Editor structure

```
┌───────────────────────────────────────────────────────────────────┐
│ ‹ Workflows  "Sync Tickets→CRM"   [⋮] [Save] [Execute] [○ Active] │
├────────┬────────────────────────────────────────┬─────────────────┤
│ Nodes  │  Canvas                                │ Node panel      │
│ Palette│   (Webhook) → (IF) → (HTTP Request)    │ Resource: Zammad│
│ Search…│      ↘ (Error)                         │ Operation:      │
│        │      → (Create Ticket)                 │  create ticket  │
│        │                                        │ Fields …        │
│ Executions│  Zoom: -, 100%, +                  │ [Execute node]  │
└────────┴────────────────────────────────────────┴─────────────────┘
```

- Nodes as tiles with status icons; parameter form on the right; tab for test data output at the bottom

## UI/UX

- Dark default theme, large node icons with product logos
- Sticky notes/"Wait" badges on the canvas; undo rail

## Interactions

- **Tab** opens the node palette (fastest way), dragging creates connections
- Double-click a node → panel; right-click context menus (test/pin/disable)
- "Execute Workflow" shows the data path in color (item bubbles move through nodes)

## Responsive design

- Desktop tool; on mobile only viewing/configuration as a stopgap

## Accessibility

- Form panels keyboard-operable; canvas primarily mouse-based (zoom with `Ctrl+wheel`)

## Performance

- Queue mode decouples execution from the editor; large items >10 MB are split (binary handling)
