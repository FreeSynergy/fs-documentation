# Consul - Structure and UI/UX

## Page structure

```
┌──────────────────────────────────────────────────────────────────┐
│ City portal „Consul“   Home | Participation | Budget…            │
├──────────────────────────────────────────────────────────────────┤
│ Tiles for participation types (Proposals · Budget · Polls)       │
│ Proposal list: Title | Topic | Support counter | Discussion      │
│ Detail: text, map, [Support], comment threads                    │
│ Budget: section „250k€“ → project grid with ☑ selection           │
└──────────────────────────────────────────────────────────────────┘
```

## UI/UX

- Authority-friendly; supports shown as heart counters
- Phase and deadline banner per participation item

## Interactions

- Support (verification required), comments (threads), report (moderation)
- Budget grid: tick up to n projects (control logic inline)

## Responsive design

- Responsive (mobile use by citizens is standard)

## Accessibility

- Basic web standards; contrast depends on the theme

## Performance

- Large proposal lists need topic and status filters; API caching for statistics
