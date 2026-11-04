# Coppermine - Structure and UI/UX

## Visitor area (standard theme)

```
┌──────────────────────────────────────────────────────────────────────┐
│ Gallery title  Menu: Home pages | Albums | Search | Login            │
├───────────────┬──────────────────────────────────────────────────────┤
│ Side block    │ Category/album overview with thumbnails              │
│ (blocks)      │ ┌────┐┌────┐┌────┐┌────┐                             │
│ last uploads  │ └────┘└────┘└────┘└────┘                             │
│ Bestsellers   │ Album header: title, description, image count, sort. │
└───────────────┴──────────────────────────────────────────────────────┘
   Image page: image centred | file info | rating | comments | navigation
```

- The admin surface "cuPCP" is a separate mask system with tab headers
- The page margins consist of blocks that are placed per theme

## UI/UX

- The standard theme is two-column, older themes have a fixed width
- Actions as text links below the image/thumbnail ("rotate", "edit", "move")

## Interactions

- **Bulk management**: a checkbox per thumbnail → action bar
- **Upload wizard**: multi-step dialog (album, files, description, keywords)
- **Rating**: stars directly on the image page, comment field beneath it
- **Animations**: barely any, lightbox plugins provide the transitions

## Responsive design

| Width | Behaviour |
|-------|-----------|
| Desktop | Two columns with blocks |
| Tablet | Blocks below the gallery (depending on theme) |
| Mobile | Single column only with a responsive theme; the standard theme scrolls horizontally (⚠) |

## Accessibility

- Limited: image alternatives come from the file titles, skip links are missing in the standard theme
- Forms are labelled, but keyboard guidance in the batch masks is weak
- Can be retrofitted via custom themes (the recommended route in skin projects)

## Performance

- Preview sizes are generated at upload time; rebuild them via the maintenance function
- No built-in page cache; caching has to happen via the web server/proxy
