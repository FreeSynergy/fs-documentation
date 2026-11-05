# Immich - Structure and UI/UX

## Timeline

```
┌──────────────────────────────────────────────────────────────────────┐
│ Navigation  │ Search (🔍 semantic)      │ Upload ⬆  │ Avatar          │
│ Photos      ├───────────────────────────┴────────────────────────────┤
│ Albums      │ 2026  ▾   [Year][Month][All]                           │
│ Explore     │ ┌──┐┌──┐┌──┐┌──┐┌──┐┌──┐   virtual grid                │
│ Favourites  │ └──┘└──┘└──┘└──┘└──┘└──┘   (lazy-load, date groups)    │
│ Shared      │ Selection toolbar appears at the top                   │
│ Trash       │ ▣ Selection  ♥  ⤓  🗑  ⑂ Share                          │
└─────────────┴────────────────────────────────────────────────────────┘
```

- Viewer: full screen with a thumbnail bar on the left, EXIF panel on the right, video with a timeline
- Selection mode: click + `Shift` for a range, toolbar with bulk actions

## UI/UX

- Dark and light theme, accent colour, touch swipe gestures in the viewer
- The virtual grid keeps large libraries (100k+ captures) smooth
- Upload overlay with progress and a duplicate warning

## Interactions

- **Drag & drop**: drag files straight into the timeline
- **Person search**: clicking a face opens the person page with their timeline
- **Sharing an album**: dialog with user selection or a link (password/expiry optional)
- **Animations**: fade-in of the thumbnails, skeleton placeholders while loading

## Responsive design

| Width | Behaviour |
|-------|-----------|
| Desktop | Navigation bar + multi-column grid |
| Tablet | Navigation bar collapsible, grid 3–4 columns |
| Mobile | Bottom tab bar, grid 2–3 columns, swipe viewer |

## Accessibility

- Keyboard control in the viewer (arrows, `Esc`), focus rings in the grid
- Alternative texts can be retrofitted from the ML tagging, screen-reader labels in dialogs
- Colour-coded states are additionally labelled (favourite = symbol + text)

## Performance

- Derivatives (thumbnail/preview/webp) server-side, the client loads the size-appropriate variant
- Jobs run asynchronously; search via PostgreSQL full-text + pgvector/CLIP embeddings
