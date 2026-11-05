# Message Composer - Appearance

## Base layout

```
┌─────────────────────────────────────────┐
│ To   [Anna 🔒] [Ben ⚠] [ + ]            │
│ Subject  ___________________________    │
├─────────────────────────────────────────┤
│ Text of the message …                   │
├─────────────────────────────────────────┤
│ 📎 file.pdf   [😊] [@]        [ Send ]  │
└─────────────────────────────────────────┘
```

## Variants

| Variant | Appearance |
|---|---|
| **chat** | one line growing to a limit, send button at the end |
| **mail** | header rows above the editor |
| **reply** | one line, no toolbar |

## Sizes

| Size | Height | Use |
|---|---|---|
| `small` | 80 px | reply field |
| `medium` | 300 px | standard |
| `large` | 500 px | mail window |
| `full` | 100% | full area |

## Colours and states

| State | Appearance |
|---|---|
| Default | theme surface |
| Error | error outline at the faulty part |
| Sending | controls disabled, progress |

## Hover and focus effects

| Effect | Description |
|---|---|
| `background` | buttons hover |
| `cursor` | text cursor in the editor |

## Responsive

- Chat variant grows up to a maximum height, then scrolls.
- Attachments and emoji move into a toolbar row on narrow screens.
