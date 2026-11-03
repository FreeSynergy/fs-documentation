# Bounce Out - Aussehen

## Grundlayout

Das Element staucht sich kurz an seiner Position, schnellt dann über die Position hinaus und verschwindet federnd aus der Fläche.

## Visueller Verlauf (Aussprung nach oben)

```
┌────────────────────────────────────────────┐
│   0 ms    [█████]      scale 1.00 (Ruhe)    │
│ 120 ms    [███]        scale 0.88 (Ausholen)│
│ 260 ms    [██] ↑       scale 0.50 (Absprung)│
│ 400 ms    (leer)       entfernt             │
└────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Squash-Away** | Erst stauchen, dann flach davonziehen (Standard) |
| **Jump-Away** | Kurzer Sprung nach oben, dann verschwinden |
| **Side-Flick** | Schnelles Wegschnippen zur Seite |
| **Shrink-Bounce** | Mit kleinem Überschwingen schrumpfend verschwinden |

## Dauer

- Typisch: 300–500 ms
- Standardwert: 400 ms

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Bounce In](../../entrance/bounce-in/description.md)
- [Zoom Out](../zoom-out/description.md)
