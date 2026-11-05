# Matomo - Structure and UI/UX

## Layout

```
┌─────────────────────────────────────────────────────────────────┐
│ Matomo  website ▾  period ▾                  ⚙ 👤                │
├────────────┬────────────────────────────────────────────────────┤
│ Visits     │ Visitor log: one row per visit, action tree        │
│ Behaviour  │   (pages → clicks → search)                        │
│ Acquisition│ Bar charts (daily aggregates), sparklines          │
│ Goals      │ Segment bar (top, applies to all reports)          │
└────────────┴────────────────────────────────────────────────────┘
Widget grid on the dashboard; drilldown per row
```

## UI/UX

- Functionally dense (the classic analytics table UI); a dark mode exists
- Hovering shows the visit's "actions" sub-tree — the unique selling point

## Interactions

- Click on rows → drilldown columns; create segments via a click combinator
- Report download (CSV/JSON/PNG) per report

## Responsive design

- The web is responsive; reports on mobile are read-only

## Accessibility

- Table/link basics; charts with data counterparts

## Performance

- The visits table is large → the archive plugin + cron; database partitioning above 100 million rows
