# Alert Dialog - Appearance

## Base layout

```
┌───────────────────────────────────┐
│  Discard page?                ✕   │
├───────────────────────────────────┤
│  Your changes to this             │
│  document will be lost.           │
│                                   │
│         [Cancel]  [Discard]       │
└───────────────────────────────────┘
```

## Variants

| Variant | Appearance |
|---------|------------|
| **bestaetigung** | primary colour in the confirm button, neutral title |
| **zerstoererisch** | title bar and button in the error colour |

## Sizes

| Size | Width | Vertical spacing |
|------|-------|------------------|
| `small` | 360 px | 12 px |
| `medium` | 480 px | 16 px |
| `large` | 640 px | 20 px |

## Colours and states

| State | Appearance |
|-------|------------|
| `default` | surface with a border, background behind it darkened |
| `open` | focus on cancel, 2 px focus ring |
| `loading` | spinner in the confirm button, both buttons locked |
| `disabled` | surface dimmed, no action possible |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `tone` | the button surface gets darker on hover |
| `scrim` | darkened surface behind the dialog, not clickable |

## Responsive

- On mobile devices the dialog fills the width and sits at the bottom edge.
- Long justifications scroll inside the content, the buttons stay visible.
