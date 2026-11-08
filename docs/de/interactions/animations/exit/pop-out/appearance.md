# Pop Out - Erscheinungsbild

## Grundaufbau

Das Element bleibt bis zum Ende der Animation an seiner Layoutposition und schrumpft nur in der
Darstellung. Erst wenn die Animation beendet ist, gibt es seinen Platz auf.

## Visueller Ablauf

```
┌──────────────────────────────────────────────────────┐
│   0 ms           50 ms          120 ms       200 ms  │
│                                                      │
│  [ Chip ]      [  Chip  ]      ▒▒ Chip ▒▒    (leer)  │
│  s = 1.00      s = 1.04        s = 0.45     s = 0    │
│  α = 1         α = 1           α = 0.6      α = 0    │
└──────────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|---------|-------------|
| **Standard** | Vorwegnahme 1.04, dann auf 0 schrumpfen (200 ms) |
| **Ohne Vorwegnahme** | `anticipation: 1` – sachlicher, weniger verspielt |
| **Schnell** | 120–180 ms für Badges und Zähler |
| **Platz bleibt** | `removeAfterEnd: false` – die Lücke bleibt (z. B. in einem Raster) |

## Dauer

- Typisch: 150–250 ms
- Standardwert: 200 ms

## Siehe auch

- [Übersicht Animationen](../../index.md)
- [Pop In](../../entrance/pop-in/description.md)
- [Scale Out](../scale-out/description.md)
- [Cascade](../../organization/cascade/description.md)
