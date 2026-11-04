# Rich Text Editor - Appearance

## Base layout
A rich text editor is a WYSIWYG editor for formatted text.

```
┌─────────────────────────────────────────┐
│ [B] [I] [U] [ Strikes] [ Color]         │  ← toolbar
├─────────────────────────────────────────┤
│                                         │
│  (editor area)                          │
│                                         │
│  Here is the text...                    │
│                                         │
└─────────────────────────────────────────┘
```

## Variants

| Variant | Appearance |
|---------|------------|
| **wysiwyg** | formatting bar on top, text as in the printed layout |
| **wiki-syntax** | syntax field on the left, preview on the right (or as a tab) |

## Sizes

| Size | Height | Use |
|------|--------|-------------|
| Small | 200px | inline |
| Medium | 400px | standard |
| Large | 600px | featured |
| Full | 100% | full width |

## Colours and states

| State | Appearance |
|-------------|-------------------------------------------------------|
| `default` | light base, text area without border |
| `focus` | border in the primary colour, cursor visible |
| `unspeichert` | small dot on the edge, save button emphasised |
| `error` | red border, the affected spot underlined |
| `disabled` | grey base, bar greyed out |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `border` | the border lights up |
| `shadow` | stronger shadow |

## Responsive

- The formatting bar stays pinned at the top while scrolling; if it does not fit on one line,
  further tools move behind a `+` drop-down field.
- Below `small` screen width the `wiki-syntax` preview becomes a tab instead of a side column.
- The editor area grows with the text (`auto-resize`), `Full` fills the viewport height minus
  the bar.

## Toolbar buttons

| Button | Function |
|------------|--------------------|
| **B** | bold |
| **I** | italic |
| **U** | underlined |
| ** Strikes** | strikethrough |
| ** Color** | colour |
| ** Heading** | headings |
| ** List** | lists |
| ** Link** | links |
| ** Image** | images |
| ** Code** | code block |

## Placeholder

```
┌─────────────────────────────────────────┐
│ [B] [I] [U] ...                         │
├─────────────────────────────────────────┤
│  This is a placeholder...               │
└─────────────────────────────────────────┘
```
