# Toolbar - Appearance

## Base layout

A toolbar is a row of buttons/icons for frequent actions.

## Variants

| Variant | Appearance |
|---------|------------|
| **standard** | single-row bar with icons |
| **kontext** | the bar swaps its buttons when the selection changes |
| **ribbon** | two or three rows with group headings |

### Horizontal (standard)
```
┌─────────────────────────────────────────────────────┐
│ [📄] [✏️] [✂️] [✔️] [❌] [🔍] [⚙️]                  │
└─────────────────────────────────────────────────────┘
```
### Floating
```
                    ┌─────────────────────────────┐
                    │ [📄] [✏️] [✂️] [✔️]        │
                    └─────────────────────────────┘
```
### Sidebar (left/right)
```
┌─────┬─────────────────────────────────────────────┐
│     │ [📄] [✏️] [✂️] [✔️] [❌] [🔍] [⚙️]         │
│     │                                             │
│     │                                             │
└─────┴─────────────────────────────────────────────┘
```

## Sizes

| Size | Icon size | Button size | Use |
|------|-----------|-------------|-----|
| Small | 16px | 32px | inline |
| Medium | 24px | 48px | standard |
| Large | 32px | 64px | featured |

## Colours and states

| State | Colour | Description |
|-------|--------|-------------|
| **Primary** | primary colour | main action |
| **Secondary** | secondary colour | secondary action |
| **Danger** | red | dangerous action |
| **Disabled** | grey | disabled action |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `color` | the colour changes |
| `background` | the background changes |
| `scale` | slight enlargement |
| `shadow` | a shadow appears |

## Responsive

- The bar is full width and stays at the top while scrolling (`geklebt`); the content of the
  group on the right slides away first.
- If the row no longer fits, the remaining buttons move behind a `+` drop-down field that
  keeps the groups.
- On touch devices the buttons are at least 44 px large; on large screens `icon and text`
  can be shown, on small ones only the icon.

## Button labelling

| Form | Description |
|------|-------------|
| **icon only** | standard, with a tooltip |
| **text only** | when no unambiguous icon exists |
| **icon and text** | new or ambiguous actions |

## Separator

```
┌─────────────────────────────────────────────────────┐
│ [📄] [✏️] [✂️] ───── [✔️] [❌] [🔍] [⚙️]            │
└─────────────────────────────────────────────────────┘
```
