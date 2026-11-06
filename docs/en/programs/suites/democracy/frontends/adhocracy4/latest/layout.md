# Adhocracy4 - Structure and UI/UX

## Project view

```
┌─────────────────────────────────────────────────────────────┐
│ Project „Platz am Kanal“   Phase: Brainstorming (until 20.11) │
│ [Project info | Ideas (142) | Map | Discussion]              │
├──────────────────────────────────────────────────────────────┤
│ Filter/Sorting   Idea cards: Title · Author (pseudonym)      │
│ (Map / List)     ▲ 31 ▼ 2 · Comments 7 · Moderation marker   │
│                  Detail: text, image, location pin, thread   │
└──────────────────────────────────────────────────────────────┘
```

- Phase bar at the top; map and list views can be switched
- Moderation markers as a colour band on the map

## UI/UX

- Friendly municipal tone (plenty of white space, large buttons), German texts throughout
- Pseudonym required for contributions (real-name option per procedure)

## Interactions

- Rating via ▲/▼ (one vote per person and module), comments threaded
- Place ideas on the city map by dragging

## Responsive design

- Fully responsive (taking part on the city map on mobile is common)

## Accessibility

- WCAG baseline; maps come with text-alternative lists

## Performance

- Large idea collections: map segmentation; rating counters computed server-side
