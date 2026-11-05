# Nextcloud Photos - Structure and UI/UX

## Interface

```
┌──────────────────────────────────────────────────────────────────────┐
│ ☰ Apps   [Photos]        🔍 Search             Avatar ▾               │
├──────────────────────────────────────────────────────────────────────┤
│ Sub-bar: Latest | Albums | Folders | Shared | Favourites             │
│ Chronology grid (column-filling, virtualised)                        │
│ ┌────┐┌────┐┌────┐┌────┐     Date divider "June 2026"                │
│ └────┘└────┘└────┘└────┘                                             │
│ Viewer: large image | left/right arrows | actions ⋮ (share, …)       │
└──────────────────────────────────────────────────────────────────────┘
```

- The viewer shares the mask with the Files app (preview overlay)
- The album page shows cover tiles, editing only for owners

## UI/UX

- Nextcloud design language (header, blue accent colour), light/dark
- Actions menu ⋮ per image/album instead of visible buttons

## Interactions

- **Drag & drop** of files into the chronology (= upload into the target folder)
- **Share dialog** with link, password, expiry, upload permission
- **Multi-selection** via `Ctrl`/`Shift` + click in the files view
- **Animations**: blending of the thumbnails, spinner for preview generation

## Responsive design

| Width | Behaviour |
|-------|-----------|
| Desktop | App bar + sub-bar, grid 5–8 columns |
| Tablet | App bar as icon bar, 3–5 columns |
| Mobile | App switch via ☰, grid 2–3 columns, swipe in the viewer |

## Accessibility

- Keyboard navigation in the viewer (`←`/`→`, `Esc`), focus rings in tiles
- Alternative texts from file names/metadata, menu items with text
- Screenreader announcements when the chronology loads more

## Performance

- Thumbnails generated and cached server-side (Redis/files preview cache)
- The chronology is paginated in blocks; large folders need a preview scan in the background
