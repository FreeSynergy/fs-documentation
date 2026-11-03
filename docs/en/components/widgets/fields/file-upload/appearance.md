# File Upload - Appearance

## Base layout

A file upload is an element for choosing and uploading files.

## Variants

### File picker

```
┌─────────────────────────────────────────┐
│ [📁 Choose file]                        │
└─────────────────────────────────────────┘
```

### Drag & drop

```
┌─────────────────────────────────────────┐
│                                         │
│   Drop your file here                   │
│                                         │
└─────────────────────────────────────────┘
```

### Image preview

```
┌─────────────────────────────────────────┐
│  🖼️                                    │
│                                         │
│  [filename.jpg]      [✕]                │
└─────────────────────────────────────────┘
```

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
| **Primary** | primary colour | primary |
| **Active** | dark | active state |
| **Disabled** | grey | disabled |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `border` | the border lights up |
| `shadow` | the shadow becomes stronger |
| `background` | the background changes |

## Responsive

- The drop zone grows with the content: without a file it fills the full width,
  with a file list it becomes a list below the trigger.
- On narrow screens the preview and file name stack below each other,
  the remove button stays reachable at the top right.
- Below `small` screen width the drop zone is set to `Full` and the
  trigger becomes a full-width button.

## Progress indicator

```
┌─────────────────────────────────────────┐
│ file.jpg                                │
│ ▓▓▓▓▓▓▓▓▓▓░░░░░░  75%                  │
└─────────────────────────────────────────┘
```
