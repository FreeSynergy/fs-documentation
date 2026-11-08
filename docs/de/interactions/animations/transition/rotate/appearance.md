# Rotate - Aussehen

## Grundlayout

Ein Element dreht sich einmal um seinen Drehpunkt auf einen festen Zielwinkel und bleibt danach in der neuen Ausrichtung.

## Visueller Verlauf (Winkelpfeil, Winkel: 180)

```
┌────────────────────────────────────────────┐
│   0 ms      ▾          eingeklappt (0°)    │
│ 150 ms      ◄          halbe Drehung (90°) │
│ 300 ms      ▴          ausgeklappt (180°)  │
└────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Viertel** | eine Drehung um 90° (Icons, Karussellpfeile) |
| **Halb** | eine Drehung um 180° (Winkelpfeil, Sortierrichtung) |
| **Voll** | eine volle Drehung um 360° als einmalige Bestätigung |
| **Ecken-Drehpunkt** | der Drehpunkt an einer Ecke (`transformOrigin`), wirkt wie eine Klappe |

## Dauer

- Typisch: 200–500 ms
- Standardwert: 300 ms

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Flip](../flip/description.md)
- [Spin](../../loop/spin/description.md)
