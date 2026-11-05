# Damselfly - Structure and UI/UX

## Surface

```
┌──────────────────────────────────────────────────────────────────────┐
│ 🔍 Search (text, "similar to…")   Filter ▾   Upload ⬆   Avatar/Admin  │
├──────────────┬───────────────────────────────────────────────────────┤
│ Folder tree  │ Tile grid (virtualised, grouped by date)              │
│ ▸ 2026       │ ┌───┐┌───┐┌───┐┌───┐                                  │
│ ▸ Trips      │ └───┘└───┘└───┘└───┘                                  │
│ Label /      │ Selection: checkboxes + action bar                    │
│ People       ├───────────────────────────────────────────────────────┤
│              │ Detail drawer right: preview, EXIF, labels, people    │
└──────────────┴───────────────────────────────────────────────────────┘
```

- Viewer in full screen with a "similar images" strip below it
- Filter pills show the active criteria and can be removed one by one

## UI/UX

- Bright, dense surface with a focus on result lists
- The status line shows indexing progress (pending tasks)

## Interactions

- **Similarity search**: "More like this" opens a new result list
- **Click a person** → person view with all their hits
- **Drag & drop** onto a folder = upload into that folder
- **Animations**: skeleton tiles, gentle lazy loading

## Responsive design

| Width | Behaviour |
|-------|-----------|
| Desktop | Folder tree + grid + detail drawer |
| Tablet | Folder tree collapsible, drawer as an overlay |
| Mobile | Navigation as a drawer, 2-column grid |

## Accessibility

- Keyboard works in the viewer and in dialogs, focus visibility in the tiles
- Alt texts come from the labels, captions instead of bare symbols
- Screen readers: status messages during indexing

## Performance

- pgvector for similarity search, a watcher for incremental indexing
- Preview sizes are generated on request and cached
