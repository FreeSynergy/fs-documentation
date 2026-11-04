# LibrePhotos - Structure and UI/UX

## Interface

```
┌──────────────────────────────────────────────────────────────────────┐
│ Search 🔍 (semantic)              Filter ⚙   Upload ⬆    Avatar       │
├───────────┬──────────────────────────────────────────────────────────┤
│ Navigation│  Timeline grouped by date                                │
│ Search    │  12 June 2026   ┌──┐┌──┐┌──┐┌──┐                         │
│ Places    │                 └──┘└──┘└──┘└──┘                         │
│ Albums    │  11 June 2026   ┌──┐┌──┐                                 │
│ People    │                 └──┘└──┘                                 │
│ Deleted   ├──────────────────────────────────────────────────────────┤
│           │  Viewer / sidebar: EXIF, people, similar images          │
└───────────┴──────────────────────────────────────────────────────────┘
```

- The search overlay combines text, date range, people and places
- Viewer with left-hand navigation, EXIF on the right, "similar" below

## UI/UX

- Material-like interface, light/dark, fixed sidebar (collapsible)
- Grouping control for the timeline (day/month/year)

## Interactions

- **Shift+click** for range selection, the toolbar appears at the top
- **Click a face** → person page with the person's timeline
- **Share dialog** with user or link sharing
- **Animations**: skeleton tiles, gentle loading on scroll

## Responsive design

| Width | Behaviour |
|-------|-----------|
| Desktop | Sidebar + 4–6 column grid |
| Tablet | Sidebar as drawer, 3–4 columns |
| Mobile | Tab bar at the bottom, 2–3 columns, swipe viewer |

## Accessibility

- Keyboard in the viewer (`Esc`, arrows), focus rings in tiles
- Alternative texts can be added from the object recognition
- Icons labelled in the navigation bar

## Performance

- Scan pipeline asynchronous (Celery), search via database + vectors
- Thumbnail levels on disk; large libraries need enough CPU for the initial run
