# Press - Aussehen

## Grundlayout

Das Element bleibt an seiner Position im Layout und schrumpft nur in der Darstellung. Der gedrückte Zustand hält an, bis der Nutzer loslässt; erst dann kehrt die Größe zurück.

## Visueller Verlauf

```
┌──────────────────────────────────────────────────────┐
│  0 ms         60 ms        120 ms        300 ms      │
│                                                      │
│  [ OK ]      [  OK  ]     [  OK  ]     [ OK ]       │
│  s = 1.00    s = 0.98     s = 0.97     s = 1.00      │
│             Finger runter   gehalten   losgelassen   │
└──────────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Standard** | `pressScale: 0.97` für Buttons und Zeilen |
| **Deutlich** | `pressScale: 0.94` für große Flächen und Karten |
| **Nur Farbe** | `pressScale: 1` mit `pressOpacity` – ganz ohne Bewegung |
| **Mit Rückprall** | `releaseOvershoot: 1.02` – elementfedert beim Loslassen zurück |

## Dauer

- Typisch: 100–150 ms Absteigen, 120–180 ms Rückkehr
- Standardwert: 120 ms

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Lift](../lift/description.md)
- [Ripple](../ripple/description.md)
- [Elastic](../elastic/description.md)
