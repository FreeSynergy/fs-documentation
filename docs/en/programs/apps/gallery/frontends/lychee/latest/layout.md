# Lychee - Structure and UI/UX

## Interface

```
┌──────────────────────────────────────────────────────────────────────┐
│ ☰ Albums  🔍 Search   ⬆ New             Favourites  Shared  Avatar    │
├──────────────────────────────────────────────────────────────────────┤
│ Album tiles (cover + title + count)                                  │
│ ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐                          │
│ └────────┘ └────────┘ └────────┘ └────────┘                          │
│ Album view: grid of captures, header with album actions ⋮            │
│ Lightbox: large image | left/right navigation | EXIF overlay (i)     │
└──────────────────────────────────────────────────────────────────────┘
```

- Nested albums as their own level, back button at the top left
- Selection mode with checkboxes and bulk actions

## UI/UX

- Reduced, dark default interface, focus on the image areas
- Context menu per album/capture via ⋮ or right-click

## Interactions

- **Drag & drop**: files straight into the album, progress bar
- **Right-click**: album/photo actions
- **Share dialog**: link with a parameter bar (password, expiry, permissions)
- **Animations**: blending when opening, gentle lazy loading

## Responsive design

| Width | Behaviour |
|-------|-----------|
| Desktop | Tiles 4–6 columns, lightbox with sidebars |
| Tablet | 3 columns, operated via ⋮ |
| Mobile | 2 columns, lightbox edge-to-edge, swipe gestures |

## Accessibility

- Keyboard navigation in the lightbox (`←`/`→`, `Esc`, `i`)
- Alt texts from titles/descriptions, focus rings in tiles
- Actions additionally with text in menus

## Performance

- Several preview sizes, the client chooses the suitable level
- Albums are loaded paginated; large albums stay smooth
