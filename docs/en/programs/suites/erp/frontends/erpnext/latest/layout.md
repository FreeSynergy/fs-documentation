# ERPNext - Structure and UI/UX

## Desk layout

```
┌──────────────────────────────────────────────────────────────────┐
│ ≡  🔍 Go to… (Ctrl+G)                         🔔 👤 Workspace ▾  │
├───────────┬──────────────────────────────────────────────────────┤
│ Workspaces│ Liste „Sales Orders“: Filter · ☑ Bulk-Actions        │
│ Selling   │  SO-2026-0042 | Kunde X | 12.400 € | ●Submitted     │
│ Stock     │  SO-2026-0043 | Kunde Y |  3.100 € | ○Draft         │
│ …         │ Form: Status-Kreispfad ●→○→○  Links (Delivery…)     │
│           │       Felder · Tags · Chatter (Comments/Timeline)    │
└───────────┴──────────────────────────────────────────────────────┘
```

- The status cycle path shows the document flow (Draft→Submitted→Invoiced…); linked documents as chips

## UI/UX

- Frappe Desk look (white/grey, blue accents); lists with list/card view
- Right-hand drawer for reports/charts from workspaces

## Interactions

- **Ctrl+G palette** as the main entry point; tags, assign to me, bookmark on forms
- Value setter (bulk change), report builder by click

## Responsive design

- Desktop-optimised; usable on mobile via browser, no native app feel

## Accessibility

- Standard web; palette reduces search clicks; status always labelled

## Performance

- Reports on large tables: index/query optimiser; do not share the scheduler with end users (separate workers)
