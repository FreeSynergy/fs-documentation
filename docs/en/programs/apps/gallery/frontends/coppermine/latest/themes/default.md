# Coppermine latest — Theme "default"

Moved from `layout.md` (ADR 0012). Values are described, not copied (ADR 0013).

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
