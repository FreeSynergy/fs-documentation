# Bounce Out - Aussehen

## Grundlayout

Das Element staucht sich kurz an seiner Position zusammen, schießt dann darüber hinaus und federt von der Fläche weg.

## Visueller Verlauf (Ausgang mit Sprung nach oben)

```
┌────────────────────────────────────────────┐
│   0 ms    [█████]      Skalierung 1.00 (Ruhe)    │
│ 120 ms    [███]        Skalierung 0.88 (Zug)     │
│ 260 ms    [██] ↑       Skalierung 0.50 (Start)   │
│ 400 ms    (leer)       entfernt                  │
└────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Stauchen und weg** | erst stauchen, dann flach wegziehen (Standard) |
| **Sprung weg** | ein kurzer Sprung nach oben, dann verschwinden |
| **Seitlicher Schnipser** | ein schneller Schnipser zur Seite weg |
| **Schrumpfen mit Federn** | verschwinden beim Schrumpfen mit einem kleinen Überschwingen |

## Dauer

- Typisch: 300–500 ms
- Standardwert: 400 ms

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Bounce In](../../entrance/bounce-in/description.md)
- [Zoom Out](../zoom-out/description.md)
