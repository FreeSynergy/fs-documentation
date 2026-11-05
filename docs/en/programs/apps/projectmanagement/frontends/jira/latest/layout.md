# Jira - Structure and UI/UX

## Page structure (board)

```
┌─────────────────────────────────────────────────────────────────────┐
│ Jira   Search…           Projects Filters Dashboards ⚙   👤         │
├──────────┬──────────────────────────────────────────────────────────┤
│ WEB-nav  │ Kanban board                                             │
│ Boards   │ ┌───────┬──────────┬───────────┬───────────┐             │
│ Backlog  │ │To Do  │In Progress│In Review │ Done      │             │
│ Reports  │ │WEB-14 │ WEB-12   │ WEB-13   │ WEB-9     │             │
│ …        │ │🐞 Bug │ 👤Anna   │          │           │             │
│          │ │SP 3   │          │          │           │             │
│          │ └───────┴──────────┴───────────┴───────────┘             │
│          │ Filter: assignee = currentUser()  [♻]                   │
└──────────┴──────────────────────────────────────────────────────────┘
```

- Issue detail as a full page or side panel; fields on the left, history/comments on the right

## UI/UX

- Atlassian design (blue/grey, Compass), high density; board filters at the top
- Drag & drop between columns and in the backlog (ranking)

## Interactions

- **Quick entry** (`c`), inline editing of many fields, issue links by type
- Live board updates for logged-in teams (commit auto-sync)

## Responsive design

- The web is responsive with caveats; the **Jira mobile app** (iOS/Android) for boards/issues

## Accessibility

- Atlassian accessibility (WCAG efforts documented); shortkeys replace mouse input (see [shortcuts.md](shortcuts.md))

## Performance

- Boards > 1k issues: column/query filters are mandatory; JQL with `ORDER BY Rank` is the standard path
