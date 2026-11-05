# GLPI - Structure and UI/UX

## Page structure

```
┌─────────────────────────────────────────────────────────────────┐
│ Assistance | Assets | Administration | Tools | Configuration     │
├───────────────┬─────────────────────────────────────────────────┤
│ Context tree  │ Object mask: ticket #9981 "VPN outage"          │
│ Categories    │ ┌ Tab ────────────────────────────────────────┐ │
│ ▸ Network     │ │ Properties | Links | Tasks                  │ │
│ ▸ Server      │ │ Follow-ups | Plans | Statistics             │ │
│               │ ├─────────────────────────────────────────────┤ │
│               │ │ Status: accepted  SLA: 6h (due 14:00)       │ │
│               │ │ Asset: srv-03 · Contract: maintenance 2026  │ │
│               │ │ [Add follow-up] [Mass actions]              │ │
└───────────────┴─────────────────────────────────────────────────┘
```

- On the left a hierarchy/filter tree per area, on the right tab masks with tables
- "Mass actions" bar below the tables (assign, delete, change)

## UI/UX

- Compact table density, many fields per mask; base theme + dark mode (newer versions)
- Masks follow the pattern: top row of header data → tabs → action bar

## Interactions

- **No drag & drop**; forms, popover pickers for users/assets
- **Live**: ❌ (page reload); planning/cron built in
- Knowledge base articles with a markdown editor

## Responsive design

| Area | Behaviour |
|------|-----------|
| Self-service portal | responsive (the main mobile use-case) |
| Agent/admin masks | desktop-optimised, scrollable on mobile |

## Accessibility

- HTML tables with labels; many fields in sequence — long screenreader runs
- Keyboard tabbing ok; colour codes (SLA due in red) additionally as text

## Performance

- Large inventories (100k+ assets) require clean indexes/PHP timeouts; generate reports via a cron template
