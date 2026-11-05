# Encryption State - Appearance

## Base layout

```
 🔒 MLS      🔒 OpenPGP      🔓 transport only      ⚠ not encrypted
```

## Variants

| Variant | Appearance |
|---|---|
| **icon** | 16 px lock glyph |
| **icon-text** | glyph and short kind name |
| **warning** | error-coloured surface with text "not encrypted" |

## Sizes

| Size | Height | Use |
|---|---|---|
| `small` | 16 px | bubble header |
| `medium` | 20 px | conversation header (default) |
| `large` | 24 px | detail panel |

## Colours and states

| State | Appearance |
|---|---|
| `encrypted` | neutral or success tone, closed lock |
| `transport-only` | warning tone, half-open lock |
| `unencrypted` | error tone, open lock, text |
| `unknown` | grey, question glyph |
| `focused` | focus ring of the theme |

## Hover and focus effects

| Effect | Description |
|---|---|
| `underline` | text underlined as for [link](../../basics/link/) |
| `tooltip` | explains the kind, see [tooltip](../../../widgets/overlays/tooltip/) |

## Responsive

- Below `small` width only the glyph is shown; the kind stays in the tooltip.
- The touch target is at least 44 px even when the glyph is 16 px.
