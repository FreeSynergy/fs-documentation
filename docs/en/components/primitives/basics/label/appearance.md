# Label - Appearance

## Base layout

```
ueber-feld:        inline:            versteckt:

Username           Username ─┐        (no visible text,
┌──────────────┐   ┌─────────────┴──┐  but present as text)
│              │   │                │
└──────────────┘   └────────────────┘
```

## Variants

| Variant | Appearance |
|---------|------------|
| **ueber-feld** | text above the element, gap of 4–6 px |
| **inline** | text on the left, aligned to the baseline of the element |
| **versteckt** | invisible (1 px, clip), kept in the reading flow |
| **pflicht** | additional "*" in the error colour plus the text "required" |

## Sizes

| Size | Font |
|------|------|
| `small` | 12 px |
| `medium` | 14 px |
| `large` | 16 px |

## Colours and states

| Part | Colour |
|------|--------|
| text | primary text |
| disabled relationship | secondary text, 60 % opacity |
| required marking | error colour |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| – | the label itself does not react; clicking the label focuses the field |

## Responsive

- Labels that are too long may wrap; they never cover the field.
