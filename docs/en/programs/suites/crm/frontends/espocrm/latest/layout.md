# EspoCRM - Structure and UI/UX

## Page structure

```
┌──────────────────────────────────────────────────────────────────┐
│ 🔍 Search…                   EspoCRM            [🔔][👤][⚙]     │
├──────────┬──────────────────────────────┬────────────────────────┤
│ Menu     │ List (records)               │ Detail page            │
│ Dashboard│ ⌲ Leads  [Filter][⋮][+Add]   │ Andrea Berg            │
│ Streams  │ ☐ Berg   +49…   open         │ [⋮][Edit]             │
│ Calls    │ ☐ Klein  …                   │ Left: fields          │
│ Leads    │                              │ Right: Streams tabs   │
│ Opp.     │                              │ Calls|Meetings|Tasks  │
│ Accounts │                              │ Emails                │
└──────────┴──────────────────────────────┴────────────────────────┘
```

- SPA with tab sheets (list → detail → related), lists with filter presets and mass ⋮ actions

## UI/UX

- Calm, clear SPA; standard color scheme, dark theme optional
- Pipeline kanban with drag & drop for opportunity stages

## Interactions

- **Kanban drag** for the pipeline, list checkboxes for mass actions
- Record header: follow bell, print, click-to-dial (extension)
- Live result lists (debounced search), no full WebSocket (streams poll)

## Responsive design

- Lists/detail responsive down to mobile (lean forms); portlet dashboards stack

## Accessibility

- Keyboard-accessible tables, filters with labels; full-text search prominent
- Drag alternatives: the stage can also be changed via a field

## Performance

- Very fast; large lists (100k+) with indexing + "Select All" guard
