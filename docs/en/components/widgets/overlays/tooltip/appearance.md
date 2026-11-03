# Tooltip (Kurzinfo) - Appearance

## Base layout

```
        ┌────────────────────┐
        │ Einstellungen      │   placement = top
        └─────────┬──────────┘
                  ▼
              ┌───────┐
              │  ⚙   │
              └───────┘
```

## Variants

| Variant | Description |
| ---------- | -------------- |
| **top** | über dem Element |
| **right** | rechts neben dem Element |
| **bottom** | unter dem Element |
| **left** | links neben dem Element |
| **auto** | freie Wahl, kippt bei Randnähe |

## Sizes

| Size | Schrift | max. Breite |
| ------- | --------- | ------------- |
| `small` | 11 px | 180 px |
| `medium` | 12 px | 240 px |
| `large` | 14 px | 300 px |

## Colours and states

| Teil | Colour |
| ------ | ------- |
| Fläche | dunkle Fläche, im hellen Theme dunkelgrau, im dunklen heller |
| Text | hoher Kontrast zur Fläche |
| `arrow` | gleiche Farbe wie die Fläche |

## Hover and focus effects

| Effect | Description |
| -------- | -------------- |
| `fade-in` | Einblenden nach `delay` (Standard 400 ms) |
| `fade-out` | kurzes Ausblenden, wenn der Zeiger das Element verlässt |

## Responsive

- Der Tooltip bleibt innerhalb des Viewports und kippt automatisch auf die
  Gegenseite.

- Bei `prefers-reduced-motion` ohne Animation sofort sichtbar.
