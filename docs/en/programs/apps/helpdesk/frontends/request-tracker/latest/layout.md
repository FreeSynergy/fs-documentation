# Request Tracker - Structure and UI/UX

## Page structure

```
┌────────────────────────────────────────────────────────────────┐
│ RT   Create | New Search | Saved | Logs | Tools | Admin        │
├──────────────┬─────────────────────────────────────────────────┤
│ Saved        │ Query result (table)                            │
│ Searches     │ ID  | Subject         | Queue | Status | Owner  │
│ ▸ Mine       │ 4711| VPN bricht ab   | netz  | open   | anna   │
│ ▸ Overdue    │ 4712| Drucker         | hw    | new    |        │
│              ├─────────────────────────────────────────────────┤
│              │ Ticket #4711  Status: open  Queue: netz         │
│              │ [Reply][Correspond][Comment] Status▼ Owner▼     │
│              │ History | Attachments | Links                   │
└──────────────┴─────────────────────────────────────────────────┘
```

- Basic pattern: query → result table → update page (reply/correspond/comment side by side)
- Sidebar with personal saved searches

## UI/UX

- Functionally dense 2000s-era aesthetics; templates adaptable (`share/html`)
- No themes in the modern sense; RT 5 MUI modernises cautiously

## Interactions

- **No drag & drop / no live updates**
- Status/owner as inline links/selects on the update page
- Batch updates via the result table (checkboxes)

## Responsive design

- The web UI is only limitedly mobile; the typical mobile path = mail clients (ingest/reply via email)

## Accessibility

- html tables/forms, access keys in some language versions; screenreaders find it demanding due to many small tables, but it is fundamentally operable

## Performance

- The query engine depends on SQL index strength; saved searches do not cache — large instances need DB tuning
