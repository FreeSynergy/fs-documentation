# Lift - Aussehen

## Grundlayout

Das Element verlässt seine Layout-Position nicht, sondern wird nur in der Darstellung angehoben. Der wachsende Schatten erzeugt den Eindruck einer Ebene über der Oberfläche.

## Visueller Verlauf

```
┌──────────────────────────────────────────────────────┐
│  0 ms         80 ms        160 ms        400 ms      │
│                                                      │
│  ┌──────┐    ┌──────┐     ┌──────┐     ┌──────┐     │
│  │ Karte│    │ Karte│     │ Karte│     │ Karte│     │
│  └──────┘    ▒▒▒▒▒▒▒▒    ░░░░░░░░      └──────┘     │
│   y = 0      y = -1      y = -2        y = 0         │
│   S = 0      S = 50 %    S = 100 %     Zeiger weg    │
└──────────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Standard** | 2 px Anhebung, Schatten 8/16 px (160 ms) |
| **Flach** | `nurSchatten: true` – Höhe bleibt, nur der Schatten wächst |
| **Kräftig** | `liftOffsetY: -4` für große Karten und Kacheln |
| **Fokus** | `ausloeser: focus` – hebt bei Tastaturfokus an, nicht bei Hover |

## Dauer

- Typisch: 120–200 ms
- Standardwert: 160 ms

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Press](../press/description.md)
- [Highlight](../highlight/description.md)
- [Card](../../../components/containers/card/description.md)
