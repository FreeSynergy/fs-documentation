# Message Bubble - Appearance

## Base layout

```
 Anna · 10:42                    🔒
┌──────────────────────────────┐
│ ↳ Re: Meeting at 3?          │
│ Yes, see you there.          │
│ 📎 agenda.pdf                │
└──────────────────────────────┘
 👍 2  ❤ 1                      ✓✓
```

## Variants

| Variant | Appearance |
|---|---|
| **incoming** | neutral surface, left, tail on the left |
| **own** | accent surface, right, status at the end |
| **compact** | no surface, single line with sender and excerpt |

## Sizes

| Size | Height | Use |
|---|---|---|
| `small` | auto | compact |
| `medium` | max 480 px | standard |
| `large` | max 640 px | wide windows |

## Colours and states

| State | Appearance |
|---|---|
| Default | surface of the sender side |
| Selected | accent outline |
| Edited | small "edited" mark |
| Deleted | muted text "message deleted" |
| Failed | error outline with retry hint |

## Hover and focus effects

| Effect | Description |
|---|---|
| `background` | slight highlight when actions are available |
| – | action bar is provided by the host |

## Responsive

- Maximum width 80 % of the container on narrow screens.
- Attachments scale down; the reaction bar wraps.
