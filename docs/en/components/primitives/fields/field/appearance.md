# Field - Appearance

## Base layout

```
vertikal:                     horizontal:

Username *                    Username *
┌────────────────────────┐    ┌────────────────────────┐
│                        │    │                        │
└────────────────────────┘    └────────────────────────┘
Sign in with your             (field to the right of the label)
email address
```

Error state:

```
Email *
┌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┐
│ ✕  broken@doma.in     │
└╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┘
⚠ This email is not valid.
```

## Variants

| Variant | Appearance |
|---------|------------|
| **vertikal** | label above the field, help text below the field |
| **horizontal** | label with a fixed width on the left, field on the right |
| **inline** | label and field in one line, no help text |

## Sizes

| Size | Label font | Help text |
|------|------------|-----------|
| `small` | 12 px | 11 px |
| `medium` | 14 px | 12 px |
| `large` | 16 px | 14 px |

The enclosed field keeps its own size.

## Colours and states

| Part | Colour |
|------|--------|
| label | primary text |
| required marking `*` | error colour |
| help text | secondary text |
| error state | field border and text in the error colour |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `expand` | help text/error fades in, the block grows down cleanly |
| – | hover belongs to the field, not to the wrapper |

## Responsive

- Below a narrow width, `horizontal` switches to `vertikal` automatically.
