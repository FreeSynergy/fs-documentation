# Sharetribe - Structure and UI/UX

## Marketplace layout

```
┌──────────────────────────────────────────────────────────────────┐
│ Marketplace "Neighborhood"   [Search…]  [+ Post ad]  Account     │
├──────────────────┬───────────────────────────────────────────────┤
│ Filter: category │  (map view with listing pins)                 │
│ price · location │  or list: tiles with image/price/rating       │
│ period           │  Listing detail: gallery · price tiers        │
│                  │   [Inquire] calendar availability · reviews   │
└──────────────────┴───────────────────────────────────────────────┘
```

- Inquiry/booking as a multi-step flow (choose date → message → confirmation)
- Chat + transaction status centrally in the account

## UI/UX

- light marketplace template (default-templates), customizable (branding)
- Trust signals: verification badge, review count, response rate

## Interactions

- Map ⇄ list in sync; price filter with histogram
- Provider dashboard: listing editor, calendar blocks, payout status

## Responsive design

- responsive; mobile search is the main channel (map focused)

## Accessibility

- standard web; template base is WCAG-oriented

## Performance

- search index (Elasticsearch-like in SaaS) fast; map tiles cluster
