# Taiga - Structure and UI/UX

## Page structure

```
┌─────────────────────────────────────────────────────────────────┐
│ Project "API rework"   Backlog Kanban Issues Sprints Epics Wiki │
├─────────────────────────────────────────────────────────────────┤
│ Backlog (scrum)                                                  │
│ US#12 Login session   | Points: 3 | Sprint #4 👤Anna            │
│ US#13 Token refresh   | Points: 5 | —        👤Ben  [drag]      │
│ ── Sprint #4 ────────────────────────────────── (8/13 points)   │
│ US#11 Logout corner   | Points: 2 | ✔                           │
└─────────────────────────────────────────────────────────────────┘
Detail panel right (US#12): description, attachment, history,
subtasks, reviewer comments
```

- Header line = module tabs; boards with columns; drag interaction central everywhere

## UI/UX

- Taiga-typical: white/green accents, cards with point and status badges
- Filter chips above the boards; bulk edit via checkboxes

## Interactions

- **Drag & drop**: stories between sprints/columns, subtask order
- Inline pickers for status/points; quick-add row at the end of the list
- Live updates over a WebSocket channel (events service)

## Responsive design

- Web responsive; boards scrollable on mobile; no native app feel

## Accessibility

- Standard web accessibility; drag alternatives: sprint/status selection in the panel
- Colour status additionally labelled

## Performance

- Backlogs > 1,000 stories: use filters; the events service keeps the load low
