# Textarea - Appearance

## Base layout
A textarea is a multi-line input field for text.

```
┌─────────────────────────────────────────┐
│ Message                                 │
├─────────────────────────────────────────┤
│                                         │
│  This is some text...                   │
│  Multi-line text                        │
│                                         │
│                                         │
└─────────────────────────────────────────┘
```

## Variants

| Variant | Appearance |
|---------|------------|
| **fix** | frame with a fixed height, a scrollbar inside |
| **mitwachsend** | the frame grows line by line, the ceiling becomes the scroll area |
| **chat** | borderless line above the bar, grows up to three lines |

## Sizes

| Size | Width/height | Use |
|------|--------------|-----|
| small | 200x100px | inline |
| medium | 300x150px | standard |
| large | 500x200px | featured |
| full | 100% | full width |

## Colours and states

| Status | Colour | Description |
|--------|--------|-------------|
| **default** | light | standard |
| **primary** | primary colour | primary |
| **active** | dark | active state |
| **disabled** | grey | deactivated |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `border` | the border lights up |
| `shadow` | shadow becomes stronger |

## Responsive

- The field fills the width of the container; the height stays limited as a percentage of
  the viewport (at most 60 %), so controls below it remain reachable.
- On narrow screens the resize handle (`drag`) is dropped, the height follows
  the content up to the ceiling.
- When sending in chat mode the field animates back down to one line (`collapse` transition
  via `expand`).

## Auto-resize

```
┌─────────────────────────────────────────┐
│ Message                                 │
├─────────────────────────────────────────┤
│  This is some text...                   │
│  Multi-line text                        │
│  New text                               │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    │
└─────────────────────────────────────────┘
```

## Validation states

| State | Description |
|-------|-------------|
| **valid** | green |
| **invalid** | red |
| **warning** | orange |
