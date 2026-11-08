# Reorder - Aussehen

## Grundlayout

Alle betroffenen Elemente bleiben in ihrem Container. Ihre Positionsänderung wird nicht als Neuberechnung gezeigt, sondern als Bewegung verfolgt. Das gezogene Element liegt leicht erhoben (Schatten), die anderen weichen seitlich oder senkrecht aus.

## Visueller Verlauf

```
┌──────────────────────────────────────────────────────┐
│  0 ms (neu sortiert)   160 ms          320 ms        │
│                                                      │
│  A A                    A _ B              A B C     │
│  B B        ->          B A                A B C     │
│  C C                    C C                A B C     │
│                                                      │
│  B wandert nach oben, A nach unten; C bleibt stehen  │
└──────────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Standard** | alle verdrängten Elemente wandern gleichzeitig (320 ms) |
| **Nur Verschiebung** | `messung: transform` – die günstigste Variante ohne Neuberechnung |
| **Mit Einrasten** | `einrasten: 2` – das Element rastet leicht über und federt zurück |
| **Nach Filterung** | entfernte Elemente per [Fade Out](../../exit/fade-out/description.md), der Rest rückt per Reorder nach |

## Dauer

- Typisch: 250–400 ms
- Standardwert: 320 ms

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Stagger](../../organization/stagger/description.md)
- [Rubber Band](../../feedback/rubber-band/description.md)
- [Drag (Geste)](../../../gestures/swipe/drag/description.md)
