# Glow - Aussehen

## Grundlayout

Das Element steht still; um seine Kontur liegt ein weicher, farbiger Schein, der langsam an- und abschwillt.

## Visueller Verlauf

```
┌──────────────────────────────────────────────────────┐
│Frame 1        Frame 2        Frame 3        Frame 4  │
│                                                      │
│[■]            ~[■]~          ~~[■]~~        ~[■]~    │
│aus            schwach        hell           schwach  │
│                                                      │
│Intensität: 0 → 50 → 100 → 50 % (Endlos-Loop)         │
└──────────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Konstant** | Schein steht mit fester Intensität (Auswahl) |
| **Pulsierend** | Schein atmet im Loop (Live-Status, Präsenz) |
| **Kontur** | Schein folgt exakt der Elementform (SVG/Border-Radius) |
| **Rechteckig** | Schein als Weichzeichner-Rechteck, günstiger zu rendern |
| **Ein-/Ausstieg** | Schein baut sich beim Aktivieren weich auf und ab |

## Dauer

- Typisch: 1000–2000 ms pro Zyklus, Ein-/Ausstieg 200–400 ms

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Skeleton](../../loading/skeleton/description.md)
- [Typing](../../loading/typing/description.md)
