# Tooltip - Erscheinungsbild

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
| **auto** | freie Wahl, klappt um, wenn es nah an einem Rand ist |

## Größen

| Größe | Schrift | max. Breite |
|-------|---------|-------------|
| `small` | 11 px | 180 px |
| `medium` | 12 px | 240 px |
| `large` | 14 px | 300 px |

## Farben und Zustände

| Teil | Farbe |
|------|-------|
| Fläche | dunkle Fläche, dunkelgrau im hellen Design, heller im dunklen |
| Text | hoher Kontrast zur Fläche |
| `arrow` | gleiche Farbe wie die Fläche |

## Effekte bei Hover und Fokus

| Effekt | Beschreibung |
|--------|--------------|
| `fade-in` | blendet nach `delay` ein (Standard 400 ms) |
| `fade-out` | kurzes Ausblenden, wenn der Zeiger das Element verlässt |

## Responsiv

- Der Tooltip bleibt im sichtbaren Bereich und klappt automatisch auf die andere Seite.

- Bei `prefers-reduced-motion` erscheint er sofort, ohne Animation.
