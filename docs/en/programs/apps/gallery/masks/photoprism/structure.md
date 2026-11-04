# PhotoPrism - Structure and UI/UX

## Interface

```
┌──────────────────────────────────────────────────────────────────────┐
│ 🔍 Search + filter chips (label, person, place, period)  ⚙  ☰  Avatar │
├──────────┬───────────────────────────────────────────────────────────┤
│ Side-    │  Mosaic (virtual, sizes per zoom level)                    │
│ bar      │  ┌────┐┌────┐┌────┐┌────┐                                 │
│ Search   │  └────┘└────┘└────┘└────┘   Selection: tick + toolbar      │
│ Albums   │  ┌────┐┌────┐┌────┐┌────┐                                 │
│ Folders  │  └────┘└────┘└────┘└────┘                                 │
│ Labels   ├───────────────────────────────────────────────────────────┤
│ Faces    │ Detail panel on the right: preview, EXIF, label, album,   │
└──────────┴───────────────────────────────────────────────────────────┘
```

- Two modes: mosaic (compact view) and list/folder view
- The detail panel opens on the right, fullscreen viewer with `Esc`

## UI/UX

- Light and dark interface, adjustable tile size and sorting
- Filters as chips above the list, each removable at any time
- The selection toolbar appears at the first tick

## Interactions

- **Clicking a label/person** sets the corresponding search filter
- **Drag & drop** of files onto a folder/album (= upload)
- **Share dialog**: link with password, expiry, download right, watermark (Plus)
- **Animations**: subtle transitions when filtering, skeleton tiles while loading

## Responsive design

| Width | Behaviour |
|-------|-----------|
| Desktop | Sidebar + mosaic + detail panel |
| Tablet | Sidebar as drawer, detail as overlay |
| Mobile | Bottom navigation, single-column mosaic |

## Accessibility

- Keyboard control in the viewer (`Esc`, arrows), focus visibility in tiles
- Alt texts from label suggestions, labels instead of pure symbol colours
- Screenreader: live region when the hit count changes

## Performance

- Index update incremental; search from the database plus vectors
- Preview levels are cached server-side, large collections are virtualised
