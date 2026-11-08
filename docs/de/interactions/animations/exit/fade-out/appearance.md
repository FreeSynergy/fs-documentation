# Fade Out - Aussehen

## Grundlayout

Das Element bleibt an seiner Layoutposition und wird nur über die Deckkraft unsichtbar. Eine Verschiebung im Layout findet nicht statt.

## Visueller Verlauf

```
┌────────────────────────────────────────────┐
│   0 ms            100 ms          200 ms   │
│                                            │
│   [Titel]         ░░ Titel ░░  (unsichtbar)│
│   α = 1           α = 0.5         α = 0    │
└────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Standard** | sanft ausblenden, das Element bleibt im DOM |
| **Schnell** | 100–150 ms für Mikro-Feedback und kleine Elemente |
| **Mit Entfernen** | nach dem Ausblenden aus dem DOM entfernen (`removeOnEnd`) |
| **Unscharf ausblenden** | beim Ausblenden wird die Unschärfe größer |

## Dauer

- Typisch: 150–300 ms
- Standardwert: 200 ms

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Fade In](../../entrance/fade-in/description.md)
- [Zoom Out](../zoom-out/description.md)
