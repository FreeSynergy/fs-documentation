# Piwigo - Structure and UI/UX

## Visitor area

```
┌──────────────────────────────────────────────────────────────────────┐
│ Logo  Menu: Start pages | Albums | Tags | Calendar | Search | Login   │
├────────────────────────────┬─────────────────────────────────────────┤
│ Category tree (theme-dep.) │  Thumbnail grid, page numbering         │
│  ▸ Reisen                  │  ┌────┐┌────┐┌────┐┌────┐               │
│  ▸ Technik                 │  └────┘└────┘└────┘└────┘               │
│    ▸ Serverraum            │  Header: album name, description, count │
└────────────────────────────┴─────────────────────────────────────────┘
      Image page: large image | metadata block | comments | actions
```

- Image page: navigation back to the category, "next/previous", slideshow
- The admin area is its own mask with modules grouped on the left

## UI/UX

- Theme-dependent, the default theme "Bootstrap" is responsive
- Actions as text links/icons below the image, batch mask with checkboxes

## Interactions

- **Batch management**: grid with selection boxes → action bar at the bottom
- **Drag & drop** in "AddPictures" (upload plugin) and when sorting categories
- **Comment forms** with preview, moderation status
- **Animations**: slideshow transitions per theme, otherwise subtle

## Responsive design

| Width | Behaviour |
|-------|-----------|
| Desktop | Menu at the top, grid 4–6 columns |
| Tablet | Menu as toggle, 3–4 columns |
| Mobile | Single-column menu, 2-column grid, image page stacked |

## Accessibility

- Skip link and semantic headings in the default theme
- Alternative texts from image title/description, keyboard navigation in the slideshow
- Contrasts configurable per theme (CSS variables)

## Performance

- Generated preview sizes, optional cache and plugin caching
- Large galleries benefit from a `wait_for_images` cron and database indexes
