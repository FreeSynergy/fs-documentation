# Message Status - Appearance

## Base layout

```
 sending   sent    delivered   read     failed
   ◷        ✓        ✓✓        ✓✓ (in colour)   ⚠
```

## Variants

| Variant | Appearance |
|---|---|
| **icon** | 16 px glyph; `read` uses the accent colour, `failed` the error colour |
| **icon-text** | glyph followed by a 12 px word |

## Sizes

| Size | Height | Use |
|---|---|---|
| `small` | 12 px | inside a bubble corner |
| `medium` | 16 px | list rows (default) |
| `large` | 20 px | detail panel |

## Colours and states

| State | Appearance |
|---|---|
| `sending` | neutral, clock glyph |
| `sent` | neutral, one check |
| `delivered` | neutral, two checks |
| `read` | accent colour, two checks |
| `failed` | error colour, warning glyph |

## Hover and focus effects

| Effect | Description |
|---|---|
| `tooltip` | state word and time, see [tooltip](../../../widgets/overlays/tooltip/) |
| – | no hover change of its own |

## Responsive

- On narrow screens only the `icon` variant is used.
- The glyph never wraps; it stays at the end of the time stamp.
