# Press - Erscheinungsbild

## Grundaufbau

Das Element bleibt an seiner Position im Layout und schrumpft nur in der Darstellung. Der
gedrückte Zustand hält, bis der Nutzer loslässt; erst dann kehrt die Größe zurück.

## Visueller Ablauf

```
┌──────────────────────────────────────────────────────┐
│  0 ms         60 ms        120 ms        300 ms      │
│                                                      │
│  [ OK ]      [  OK  ]     [  OK  ]     [ OK ]        │
│  s = 1.00    s = 0.98     s = 0.97     s = 1.00      │
│             Finger drauf   gehalten     losgelassen  │
└──────────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|---------|-------------|
| **Standard** | `pressScale: 0.97` für Schaltflächen und Zeilen |
| **Deutlich** | `pressScale: 0.94` für große Flächen und Karten |
| **Nur Farbe** | `pressScale: 1` mit `pressOpacity` – ganz ohne Bewegung |
| **Mit Rückfedern** | `releaseOvershoot: 1.02` – das Element federt beim Loslassen zurück |

## Dauer

- Typisch: 100–150 ms beim Herunterdrücken, 120–180 ms beim Zurückkehren
- Standardwert: 120 ms

## Siehe auch

- [Übersicht Animationen](../../index.md)
- [Lift](../lift/description.md)
- [Ripple](../ripple/description.md)
- [Elastic](../elastic/description.md)
