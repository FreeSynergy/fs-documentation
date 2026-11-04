# Plausible - Structure and UI/UX

## Dashboard single page

```
┌──────────────────────────────────────────────────────────────┐
│ Domain ▾  period ▾  [compare ⊘]               Settings       │
├──────────────────────────────────────────────────────────────┤
│ KPI row: visits | views/visit | bounce rate | time           │
│ Time-series area (daily bars)                                │
│ Source segmenter: search | social | direct | email | Ads     │
├──────────────────────────────┬───────────────────────────────┤
│ Top pages (list+%)           │ Countries / devices / browsers│
└──────────────────────────────┴───────────────────────────────┘
```

## UI/UX

- Radically reduced: one page, no drilldown level below the lists
- Percentages instead of columns of raw numbers; bars proportional

## Interactions

- Clicking a source category filters the whole page
- Period picker with a comparison period (previous period/custom)

## Responsive design

- Fully responsive (fast on mobile too)

## Accessibility

- Plain lists/bars, high contrast

## Performance

- Aggregate tables instead of visit logs → very fast loading
