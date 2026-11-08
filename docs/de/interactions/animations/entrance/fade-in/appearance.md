# Fade In - Erscheinungsbild

## Grundaufbau

Das Element bleibt genau an seiner Layoutposition und wird nur über die Deckkraft sichtbar –
keine Bewegung und keine Größenänderung.

## Visueller Ablauf

```
┌────────────────────────────────────────────┐
│   0 ms            125 ms          250 ms   │
│                                            │
│  (unsichtbar)     ░░ Titel ░░     [Titel]  │
│    α = 0          α = 0.5         α = 1    │
└────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|---------|-------------|
| **Standard** | sanft von 0 auf 1 überblendet (250 ms) |
| **Schnell** | 100–150 ms für Hover, Tooltip, Mikro-Feedback |
| **Weich** | 350–400 ms mit `ease-out` für Overlays und Dialoge |
| **Blur Fade** | Einblenden kombiniert mit einer abklingenden Unschärfe |

## Dauer

- Typisch: 150–400 ms
- Standardwert: 250 ms

## Siehe auch

- [Übersicht Animationen](../../index.md)
- [Fade Out](../../exit/fade-out/description.md)
- [Slide In](../slide-in/description.md)
