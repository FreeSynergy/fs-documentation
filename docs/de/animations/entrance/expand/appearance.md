# Expand - Aussehen

## Grundlayout

Von einer Linie ausgehend wächst der Slot nach unten; der Inhalt bleibt unskaliert und wird freigelegt.

## Visueller Verlauf

```
┌──────────────────────────────────────────────────┐
│  0 ms            150 ms          300 ms          │
│  ╭────────╮      ┌────────┐      ┌────────┐      │
│  Höhe = 0        ░░░░░░░░░░      ░░░░░░░░░░      │
│                  └────────┘      ░░░░░░░░░░      │
│                  Höhe 50 %       └────────┘      │
│  Inhalt wird                     Höhe = Inhalt   │
│  freigelegt, nicht skaliert                      │
└──────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Vertikal** | `dimension: height` - Standard bei Akkordeons |
| **Horizontal** | `dimension: width` - Panel klappt nach rechts auf |
| **Mit Scroll** | `maxHeight` begrenzt, Rest scrollbar |
| **Mit Fade** | `innerFade` blendet Kind-Elemente zusätzlich ein |
| **Lazy** | `deferRender` - Inhalt erscheint erst beim Öffnen |

## Dauer

- Typisch: 300 ms (Bereich 200–400 ms)

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Collapse](../../exit/collapse/description.md)
- [Unfold](../unfold/description.md)
