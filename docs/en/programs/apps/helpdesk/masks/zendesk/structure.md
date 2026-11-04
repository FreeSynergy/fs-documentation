# Zendesk - Structure and UI/UX

## Page structure (agent workbench)

```
┌──────────────────────────────────────────────────────────────────┐
│ 🔍 Search…                   Zendesk          [App] [Avatar]     │
├───────────┬──────────────────────────────┬───────────────────────┤
│ Views     │ Ticket list (view)           │ Ticket #9031          │
│ ▸ Mine…   │ #9031 VPN…  open  ●4h SLA   │ Customer: Beta GmbH   │
│ ▸ Unassigned                            │ [Solve][Pending][Hold]│
│ Tickets   │ #9032 Drucker new           │ [Public reply ▾]      │
│ Users     │ …                           │ [Internal note]       │
│ Orgs      │                             │ ── Conversation ──    │
│ Reporting │                             │ 📎 Attachments        │
│           │                             ├───────────────────────┤
│           │                             │ Sidebar: Fields, Apps │
└───────────┴──────────────────────────────┴───────────────────────┘
```

- Three zones: navigation | list | ticket with conversation + right sidebar (custom fields, apps, context)

## UI/UX

- Zendesk "Garden" design: white/yellow accents (brand blue), high contrast, much whitespace
- Live: WebSocket updates (the ticket list/status change without reload)

## Interactions

- **Drag & drop**: attachments; macros by click; batch actions via checkboxes
- **Macros**: one click fills reply + actions
- **App panel** on the right (marketplace apps render their own UI)

## Responsive design

- The web app is partly responsive; for mobile: the **Zendesk mobile agent app** (iOS/Android), client portal responsive

## Accessibility

- WCAG tasks officially documented (Zendesk accessibility statement); screenreader tests available for support
- Shortcuts (see [shortcuts.md](shortcuts.md)) as a mouse alternative for core actions

## Performance

- Client-side SPA-like; large views cached server-side, > 1k hits are paginated
