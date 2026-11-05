# Asana - Structure and UI/UX

## Page structure

```
┌──────────────────────────────────────────────────────────────────┐
│ Asana  🔍 Search…                          [+] [🔔] [👤]            │
├────────────────┬─────────────────────────────────────────────────┤
│ My tasks       │ Project "Website" – view: list ▾ timeline       │
│ Today          │ ▸ Section Launch                                │
│ Today+7        │   ☐ Copy final  👤Anna 📅 31.10 🔗2                │
│ Projects       │   ☐ Switch hosting 👤Ben                         │
│ Portfolios     │ ▸ Section Legal                                 │
│ Workloads      │   ☐ Imprint …                                   │
│ Goals          │      Right-click → task panel right             │
└────────────────┴─────────────────────────────────────────────────┘
```

- Task panel (right) with tab character: details | comments | dependencies

## UI/UX

- Asana design (coral/violet accents), calm typography, high consistency
- Tabs per view; drag for order and dependencies (timeline)

## Interactions

- **Quick entry** by typing into lists (Enter = the next task)
- `Tab`+name assigns quickly; comments with @ and Ctrl+Enter
- Partially live: new comments/notifications push into the inbox

## Responsive design

- The web is responsive; the mobile apps are fully functional (the timeline is limited)

## Accessibility

- WCAG reports published; keyboard mode `?` (see [shortcuts.md](shortcuts.md))

## Performance

- Large portfolios (10k tasks) load section by section; the workload charts cache
