# Salesforce - Structure and UI/UX

## Page structure (Lightning)

```
┌───────────────────────────────────────────────────────────────────┐
│ ☁ App launcher ▾  Tabs: Accounts Contacts Leads Opps …  🔍 👤 ⚙  │
├──────────────────────────────────────┬────────────────────────────┤
│ List view                            │ Record detail              │
│ [Filter ▾][⋯][+ New]                 │ Andrea Berg   [⋯][Edit]    │
│ ☐ Beta GmbH   Owner: Anna            │ Path: ▸Qualify▸Present     │
│ ☐ Alpha AG    Owner: Ben             │ Detail fields (sections)   │
│                                      │ Related lists: Activities, │
│                                      │   Contacts, Opportunities  │
│                                      │ Sidebar: Notes/Knowledge/Apps │
└──────────────────────────────────────┴────────────────────────────┘
```

- Record pages are built from page layouts/Lightning pages — different per profile/record type

## UI/UX

- Lightning Design System (SLDS), themer per tenant; high density, but consistent
- Kanban views for opportunities; master-detail lists

## Interactions

- **Drag & drop**: stage on the kanban, list column resize, file attachments
- **Quick actions** (buttons in the header), toast notifications
- Live: platform events for internal real-time widgets (no general live refresh)

## Responsive design

- Lightning app (mobile) mirrors object detail and list pages; fully responsive web UI
- Salesforce mobile app with offline capabilities (sales/service)

## Accessibility

- Salesforce documents WCAG 2.1 support for Lightning; core masks tested with screen readers
- Shortcuts see [shortcuts.md](shortcuts.md)

## Performance

- Paginate lists (25/50/100); reports with more than 2k rows need indexes and filters that limit the data — on the API side, respect the limits
