# Lift - Erscheinungsbild

## Grundaufbau

Das Element verlässt seine Layoutposition nicht, es wird nur in der Darstellung angehoben. Der
wachsende Schatten erzeugt den Eindruck einer Ebene über der Fläche.

## Visueller Ablauf

```
┌──────────────────────────────────────────────────────┐
│  0 ms         80 ms        160 ms        400 ms      │
│                                                      │
│  ┌──────┐    ┌──────┐     ┌──────┐     ┌──────┐      │
│  │ Karte│    │ Karte│     │ Karte│     │ Karte│      │
│  └──────┘    ▒▒▒▒▒▒▒▒    ░░░░░░░░      └──────┘      │
│   y = 0      y = -1      y = -2        y = 0         │
│   S = 0      S = 50 %    S = 100 %     Zeiger weg    │
└──────────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|---------|-------------|
| **Standard** | 2 px Anhebung, Schatten 8/16 px (160 ms) |
| **Flach** | `nurSchatten: true` – die Höhe bleibt, nur der Schatten wächst |
| **Stark** | `liftOffsetY: -4` für große Karten und Kacheln |
| **Fokus** | `ausloeser: focus` – hebt sich bei Tastaturfokus, nicht beim Hover |

## Dauer

- Typisch: 120–200 ms
- Standardwert: 160 ms

## Siehe auch

- [Übersicht Animationen](../../index.md)
- [Press](../press/description.md)
- [Highlight](../highlight/description.md)
- [Card](../../../../components/widgets/containers/card/description.md)
