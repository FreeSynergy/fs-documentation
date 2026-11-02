# Reorder - Aussehen

## Grundlayout

Alle betroffenen Elemente bleiben in ihrem Behälter; ihre Position wird nicht neu berechnet dargestellt, sondern als Bewegung nachgefahren. Das gezogene Element liegt dabei leicht erhöht (Schatten), die anderen weichen seitlich oder vertikal aus.

## Visueller Verlauf

```
┌──────────────────────────────────────────────────────┐
│  0 ms (neu sortiert)     160 ms          320 ms      │
│                                                      │
│  A A                    A _ B              A B C     │
│  B B        ->          B A                A B C     │
│  C C                    C C                A B C     │
│                                                      │
│  B wandert nach oben, A rückt nach unten; C bleibt    │
└──────────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Standard** | alle versetzten Elemente wandern gleichzeitig (320 ms) |
| **Nur Verschiebung** | `messung: transform` – billigste Variante, keine Neuberechnung |
| **Mit Einrasten** | `einrasten: 2` – Element setzt leicht über und federt zurück |
| **Nach Filtern** | entfernte Elemente per [Fade Out](../../exit/fade-out/description.md), die übrigen rücken per Reorder nach |

## Dauer

- Typisch: 250–400 ms
- Standardwert: 320 ms

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Stagger](../../organization/stagger/description.md)
- [Rubber Band](../../feedback/rubber-band/description.md)
- [Drag (Geste)](../../../gestures/single/drag/description.md)
