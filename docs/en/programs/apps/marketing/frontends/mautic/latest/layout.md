# Mautic - Structure and UI/UX

## Layout

```
┌─────────────────────────────────────────────────────────────────┐
│ Mautic UI  Search…                        ⚙ 👤                  │
├──────────┬──────────────────────────────────────────────────────┘
│ Contacts │ Contact view: fields on the left, activities
│ Campaigns│   on the right, points bar, tags (chips)
│ Emails   │ Campaign canvas: (trigger)─┬─(if/else)─(mail)
│ Forms    │                            └─(wait 3d)─(tag)
└──────────┴──────────────────────────────────────────────────────┘
Segment/list filters at the top; the CSV import master on the left
```

## UI/UX

- Standard admin look; the canvas is horizontal (a tree from the left)
- Contact detail = a chronicle log (a timeline of all interactions)

## Interactions

- Drag in the canvas (connect nodes); segment rules as dropdown chains
- Import master with preview/field assignment

## Responsive design

- Desktop; mobile maintenance is not intended (the API instead)

## Accessibility

- Standard HTML; forms/buttons tagged

## Performance

- The cron batches (campaigns, segment refresh) are the bottleneck → server tuning/queue
