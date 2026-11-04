# Sidebar - Appearance

## Base layout

```
┌─────────────┐
│  Logo/Title │
├─────────────┤
│  📩 Mail    │
│  📅 Calend. │
│  👥 Contacts│
├─────────────┤
│  📝 Wiki    │
│  💬 Chat    │
│  📋 Tasks   │
├─────────────┤
│  ─────────  │
│  👤 User    │
│  ⚙️ Settings│
└─────────────┘
```

## Variants

| Variant | Appearance |
| ---------- | ---------- |
| **angeheftet** | full width with names, content moves next to it |
| **ikonenleiste** | narrow strip with icons, no text |
| **einklappbar** | wide, collapse button in the header; collapsed like `ikonenleiste` |

## Sizes

| Size | Width | Icon | Font | Use |
|------------|-------|------|------|-------------------|
| desktop | 240 px | 20 px | 14 px | standard |
| collapsed | 64 px | 20 px | – | icon bar |
| mobile | 100 % | 20 px | 14 px | overlay (drawer) |

Spacing per item: 12 px above/below, 16 px on the left; group indent 8 px.

## Colours and states

| Element | Colour | Note |
|---------|--------|------|
| background | `--sidebar-bg` | usually darker than the main content |
| text | `--sidebar-text` | contrast against the background |
| hover | `--sidebar-hover` | subtle emphasis |
| active | `--sidebar-active` | clear marking |
| divider | `--sidebar-divider` | separator between groups |

## Hover and focus effects

| Effect | Description |
| -------- | -------------- |
| `background` | the item gets a filled area, the text stays readable |
| `ring` | focus ring during keyboard navigation |
| `tooltip` | the name appears on hover in the icon bar |
| `indicator` | narrow bar on the left edge of the active item |

## Responsive

| Breakpoint | Behaviour |
| ------------ | ----------- |
| Desktop (>768px) | full sidebar visible |
| Tablet (480-768px) | optionally collapsed or a drawer |
| Mobile (<480px) | drawer or bottom navigation |

The bar scrolls independently (`scroll-area`), the header and footer stay in place.
- When collapsing, the width shrinks; the text disappears first, the icons stay in the
  same place (`expand`/`collapse`).
- Below 480 px the bar becomes an overlay with no remaining width; the content is no
  longer pushed aside.
