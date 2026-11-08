# Expand - Erscheinungsbild

## Grundaufbau

Ausgehend von einer einzelnen Zeile wächst der Bereich nach unten. Der Inhalt bleibt unskaliert
und wird nach und nach sichtbar.

## Visueller Ablauf

```
┌──────────────────────────────────────────────────┐
│  0 ms            150 ms          300 ms          │
│  ╭────────╮      ┌────────┐      ┌────────┐      │
│  Höhe = 0        ░░░░░░░░░░      ░░░░░░░░░░      │
│                  └────────┘      ░░░░░░░░░░      │
│                  Höhe 50 %       └────────┘      │
│  Inhalt wird                     Höhe = Inhalt   │
│  aufgedeckt, nicht skaliert                      │
└──────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|---------|-------------|
| **Vertikal** | `dimension: height` – der Standard für Akkordeons |
| **Horizontal** | `dimension: width` – der Bereich öffnet sich nach rechts |
| **Mit Scroll** | `maxHeight` begrenzt die Höhe, der Rest ist scrollbar |
| **Mit Fade** | `innerFade` blendet zusätzlich die Kindelemente ein |
| **Verzögert** | `deferRender` – der Inhalt erscheint erst beim Öffnen |

## Dauer

- Typisch: 300 ms (Bereich 200–400 ms)

## Siehe auch

- [Übersicht Animationen](../../index.md)
- [Collapse](../../exit/collapse/description.md)
- [Unfold](../unfold/description.md)
