# Tree View - Appearance

## Base layout
A tree view is a hierarchical directory structure with collapse/expand.

```
┌─────────────────────────────────────────┐
│ ▶ Folder 1                              │
│   └─ File 1                             │
│   └─ File 2                             │
├─────────────────────────────────────────┤
│ ▶ Folder 2                              │
│   └─ File 3                             │
│   └─ File 4                             │
└─────────────────────────────────────────┘
```

## Variants

| Variant | Appearance |
|---------|------------|
| **einfach** | triangle and name, one indent per level |
| **icon** | type symbol between triangle and name |
| **kästchen** | checkbox on the left, half tick on a partial selection |
| **verschiebbar** | cursor for dragging, the target is marked as a line |

## Sizes

| Size | Width | Use |
|------|-------|-----|
| small | 200px | inline |
| medium | 300px | standard |
| large | 400px | featured |
| full | 100% | full width |

## Colours and states

| Status | Colour | Description |
|--------|--------|-------------|
| **Default** | light | standard |
| **Hover** | lighter | hover state |
| **Active** | primary colour | active state |
| **Disabled** | grey | disabled |
| **Selected** | dark | selected node |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `background` | the background changes |
| `border` | the border lights up |

## Responsive

- The indent is 16 px per level; on narrow screens 12 px so that deep
  trees stay readable without sideways scrolling.
- Names that are too long are shortened in the middle so the extension stays visible on
  the right.
- Expanding animates with `expand`; the scroll position of the node you clicked stays
  in the same place while it happens.

## Expand/collapse

```
├─ ▼ Folder 1
│   ├─ ▸ Subfolder
│   ├─ ─ File 1
│   └─ ─ File 2
└─ ▸ Folder 2
```
