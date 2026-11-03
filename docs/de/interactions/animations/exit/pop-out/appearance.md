# Pop Out - Aussehen

## Grundlayout

Das Element bleibt bis zum Ende der Animation an seiner Layout-Position und schrumpft ausschließlich in der Darstellung. Erst wenn die Animation fertig ist, wird der Platz freigegeben.

## Visueller Verlauf

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
|----------|--------------|
| **Standard** | Ausholen 1.04, dann auf 0 schrumpfen (200 ms) |
| **Ohne Ausholen** | `anticipation: 1` – sachlicher, weniger verspielt |
| **Schnell** | 120–180 ms für Badges und Zähler |
| **Platz bleibt** | `removeAfterEnd: false` – Lücke bleibt bestehen (z. B. Raster) |

## Dauer

- Typisch: 150–250 ms
- Standardwert: 200 ms

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Pop In](../../entrance/pop-in/description.md)
- [Scale Out](../scale-out/description.md)
- [Cascade](../../organization/cascade/description.md)
