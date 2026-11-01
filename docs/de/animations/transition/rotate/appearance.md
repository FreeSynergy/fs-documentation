# Rotate - Aussehen

## Grundlayout

Ein Element dreht sich einmalig um seinen Drehpunkt auf einen festen Zielwinkel und verharrt danach in der neuen Ausrichtung.

## Visueller Verlauf (Chevron, angle: 180)

```
┌────────────────────────────────────────────┐
│   0 ms      ▾          zugeklappt (0°)      │
│ 150 ms      ◄          halbe Drehung (90°)  │
│ 300 ms      ▴          aufgeklappt (180°)   │
└────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Quarter** | Drehung um 90° (Icons, Karussell-Pfeile) |
| **Half** | Drehung um 180° (Chevron, Sortierrichtung) |
| **Full** | volle 360°-Drehung als einmaliges Quittieren |
| **Corner-Pivot** | Drehpunkt an einer Ecke (`transformOrigin`), klapptartiger Effekt |

## Dauer

- Typisch: 200–500 ms
- Standardwert: 300 ms

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Flip](../flip/description.md)
- [Spin](../../loop/spin/description.md)
