# Make - Structure and UI/UX

## Scenario canvas

```
┌──────────────────────────────────────────────────────────────────┐
│ Scenario "Ticket→CRM"   [◀ Run once] [Start ▶]  History ⏱  💾    │
├────────┬─────────────────────────────────────────────────────────┤
│ List   │  (Webhooks) ──→ (Filter) ──┐                            │
│ scen.  │                            ├──(Router)──┐               │
│ Folders│                     (Zammad Search)   (Shopify…)        │
│        │                          │                │             │
│        │                     (Create Company)  (Add item)        │
│        │   Bubbles show records; arrows = data flows             │
└────────┴─────────────────────────────────────────────────────────┘
```

- Modules horizontal from left to right, routes branch out; click = module configuration

## UI/UX

- Color-coded app icons, "Instant preview" shows real records per module
- Mapping designer for fields (drag from source into target form)

## Interactions

- Drag: connect modules; right-click: insert error handling/sleep
- History dialog: execution → each bubble with input/output data (troubleshooting)

## Responsive design

- Desktop-heavy; mobile view for reading, but building scenarios → desktop

## Accessibility

- Standard web components; canvas editing primarily mouse-based

## Performance

- Scheduling intervals depend on the plan (Free 15 min, paid down to 1 min); high volume → batch optimization (group iterators)
