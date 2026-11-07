# Axelor - Structure and UI/UX

## UI layout

```
┌──────────────────────────────────────────────────────────────────┐
│ Axelor  Menüs ▾  Suche……                        🔔 🌐 👤         │
├──────────────────────────────────────────────────────────────────┤
│ Grid „Sale Orders“: Spalten sortierbar, ☑ Massenaktionen         │
│ Form „SO-2026-0012“: Status-Timeline (draft→confirmed→invoiced)  │
│   Feldgruppen · Panels (Linien, Calculi) · BPM-Aufgabenliste     │
│ Dashboards: KPI-Karten + Charts aus Builder-Konfiguration        │
└──────────────────────────────────────────────────────────────────┘
```

- Master view (grid) + detail form with "workflow bar"; kanban/calendar as alternative views

## UI/UX

- technical and sober; builder terms (model/action/view) appear in the UI
- BPM tasks as "Waiting for…" banner

## Interactions

- Tabbed forms, One2many editing, mass-update actions
- Workflow buttons (draft/confirm…) visible per BPM state

## Responsive design

- Web responsive; mobile usable for approvals/tasks

## Accessibility

- Standard web; grid keyboard navigation is essential

## Performance

- Large grids paginated server-side; keep BPM instances clean (archive)
