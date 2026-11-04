# osTicket - Structure and UI/UX

## Page structure

```
Agent list:
┌────────────────────────────────────────────────────────────┐
│ Dashboard | Tickets | Customers | Knowledge | Files | Admin│
│ Filter: [all ▾][Status: open ▾]         [+ New ticket]     │
├────┬──────────┬──────────────────┬────────┬────────────────┤
│ ☐   | #4711    | Payment failed   | Beta   | 2 h ago       │
│ ☐   | #4712    | Printer offline  | Alpha  | yesterday     │
├────┴──────────┴──────────────────┴────────┴────────────────┤
│ Ticket #4711                              [⋯ Actions ▾]    │
│ From: b@example.org  To: support@…  Status: open (SLA:4h)  │
│ ── Thread ─────────────────────────────────────────────────│
│ [Answer] [Forward] [Note]  <editor>  [Attachment]          │
│ Internal note ☐   [Close ticket]                           │
└────────────────────────────────────────────────────────────┘
```

## UI/UX

- Functional table style, grey/blue default; no themes without template work
- The masks are click-path heavy (many forms, few overlays)

## Interactions

- **No drag & drop**, no live updates (refresh manually)
- Answer/note editor: simple rich text (HTML)
- Ticket actions as a dropdown with dialogs

## Responsive design

- The portal is responsive (Bootstrap-like breakpoints since v1.10+), the agent UI only limitedly — use the portal or API clients for mobile use

## Accessibility

- Classic HTML forms, tab order ok; colour signals (SLA due) additionally as text
- Screenreader: table headings present, but the masks are long — the ARIA build-out is incomplete

## Performance

- MySQL LIKE search scales badly; separating archive/instance is recommended
