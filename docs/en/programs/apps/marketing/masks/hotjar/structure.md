# Hotjar - Structure and UI/UX

## Layout

```
Site selection ▾   Period ▾
├ Heatmaps:     Page overlay (red = hot) over DOM screenshot,
│               device switch (desktop/mobile), click list
├ Recordings:   Table list (thumbnail, page count, duration,
│               rage-click badge) → player (timeline, mouse path,
│               DOM reconstruction, masked fields "•••")
├ Surveys:      Question editor left, preview phone right
└ Goal funnel:  Stage bars with drop-off rates
```

## UI/UX

- Visual only: overlays/thumbnails instead of columns of numbers
- Guided creation ("which page? which period?")

## Interactions

- Toggle heatmap layers (click/move/scroll)
- Replay player: play/pause, speed, mouse trail on/off

## Responsive design

- The web dashboard is responsive; recordings are kept separate per device type

## Accessibility

- Standard web; videos/overlays cannot be replaced accessibly (the reports as a text export)

## Performance

- Recording sampling limits the data volume; the player loads DOM fragments afterwards
