# Google Analytics - Structure and UI/UX

## Layout

```
┌─────────────────────────────────────────────────────────────────┐
│ GA   property ▾  home ▾                🔍    👤                   │
├──────────┬──────────────────────────────────────────────────────┤
│ Reports  │ KPI cards: active users | sessions | engagement      │
│ Overv..  │ Chart blocks (7/28 days)                             │
│ Lifecy.. │ Explore tabs: free table | funnel | path             │
│ Explorer │ Segment overlays (comparison lines)                  │
│ Admin    │ Audience management (Ads activation)                 │
└─────────────────────────────────────────────────────────────────┘
```

## UI/UX

- Material look, guided KPI cards; the explorer is the "power user" counterpart
- Data lag: the realtime report is minute-accurate, standard reports up to 24 h

## Interactions

- Date range/segment buttons at the top; right-click on a bar → drilldown
- Drag metrics into the "free table"

## Responsive design

- Desktop-centred; mobile views read-only (the "Google Analytics" app)

## Accessibility

- Standard Material components; charts with numeric summaries

## Performance

- Huge properties: the sampling notice is visible; the BigQuery export for alternative analyses
