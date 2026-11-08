# Pop In - Erscheinungsbild

## Grundaufbau

Das Element behält seine Layoutposition und ändert nur Deckkraft und eigene Größe. Das
Überschwingen wirkt nur auf die Darstellung – benachbarte Elemente verschieben sich nicht.

## Visueller Ablauf

```
┌──────────────────────────────────────────────────────┐
│   0 ms          100 ms          180 ms       250 ms  │
│                                                      │
│  (leer)        ▒▒ Chip ▒▒      [ Chip ]     [ Chip ] │
│  s = 0.80      s = 1.06        s = 0.98     s = 1.00 │
│  α = 0         α = 0.8         α = 1        α = 1    │
└──────────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|---------|-------------|
| **Standard** | Überschwingen 1.06, ein Nachschwingen (250 ms) |
| **Flach** | `overshoot: 1` – wächst ohne Überschwingen (wirkt nüchterner) |
| **Schnell** | 150–200 ms für Badges und Zähler |
| **Aus der Ecke** | `origin: bottom-left` – wächst aus der Ecke des Icons |

## Dauer

- Typisch: 200–300 ms
- Standardwert: 250 ms

## Siehe auch

- [Übersicht Animationen](../../index.md)
- [Pop Out](../../exit/pop-out/description.md)
- [Scale In](../scale-in/description.md)
- [Bounce In](../bounce-in/description.md)
