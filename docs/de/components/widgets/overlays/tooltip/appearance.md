# Tooltip (Kurzinfo) - Aussehen

## Grundlayout

```
        ┌────────────────────┐
        │ Einstellungen      │   placement = top
        └─────────┬──────────┘
                  ▼
              ┌───────┐
              │  ⚙   │
              └───────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **top** | über dem Element |
| **right** | rechts neben dem Element |
| **bottom** | unter dem Element |
| **left** | links neben dem Element |
| **auto** | freie Wahl, kippt bei Randnähe |

## Größen

| Größe | Schrift | max. Breite |
|-------|---------|-------------|
| `small` | 11 px | 180 px |
| `medium` | 12 px | 240 px |
| `large` | 14 px | 300 px |

## Farben und Zustände

| Teil | Farbe |
|------|-------|
| Fläche | dunkle Fläche, im hellen Theme dunkelgrau, im dunklen heller |
| Text | hoher Kontrast zur Fläche |
| `arrow` | gleiche Farbe wie die Fläche |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `fade-in` | Einblenden nach `delay` (Standard 400 ms) |
| `fade-out` | kurzes Ausblenden, wenn der Zeiger das Element verlässt |

## Reaktiv

- Der Tooltip bleibt innerhalb des Viewports und kippt automatisch auf die
  Gegenseite.

- Bei `prefers-reduced-motion` ohne Animation sofort sichtbar.
