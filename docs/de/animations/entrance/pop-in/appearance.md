# Pop In - Aussehen

## Grundlayout

Das Element behält seine Layout-Position und ändert nur Deckkraft und eigene Größe. Der Overshoot wirkt ausschließlich auf die Darstellung – angrenzende Elemente verschieben sich nicht.

## Visueller Verlauf

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
|----------|--------------|
| **Standard** | Overshoot 1.06, eine Nachschwingung (250 ms) |
| **Flach** | `overshoot: 1` – wächst ohne Überschießen (wirkt nüchtern) |
| **Schnell** | 150–200 ms für Badges und Zähler |
| **Von Ecke** | `origin: bottom-left` – wächst aus der Icon-Ecke heraus |

## Dauer

- Typisch: 200–300 ms
- Standardwert: 250 ms

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Pop Out](../../exit/pop-out/description.md)
- [Scale In](../scale-in/description.md)
- [Bounce In](../bounce-in/description.md)
