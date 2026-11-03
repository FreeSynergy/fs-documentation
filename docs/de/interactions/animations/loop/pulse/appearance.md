# Pulse - Aussehen

## Grundlayout

Ein Punkt oder Icon in fester Position ändert Größe und Deckkraft im gleichmäßigen Rhythmus.

## Visueller Verlauf

```
┌──────────────────────────────────────────────────┐
│  Ein Zyklus = 1200 ms                            │
│  ·      ╭───╮      ·      ╭───╮      ·           │
│         ╰───╯             ╰───╯                  │
│  1.00   1.06    1.00   1.06    1.00              │
│  Tal    Peak    Tal    Peak    Tal               │
│                                                  │
│  genau ein Peak pro Zyklus, sinusförmig          │
└──────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Skala** | nur `minScale`/`maxScale` - Element atmet |
| **Deckkraft** | nur Opacity - wirkt ruhiger |
| **Halo** | `haloRadius` - expandierender Ring um das Element |
| **Einmalig** | `iterationCount: 1` - kurzes Aufmerksamkeitssignal |
| **Sanft** | maxScale 1.02, Deckkraft 0.85 - dezent |

## Dauer

- Typisch: 1200 ms pro Zyklus (Bereich 800–2000 ms)

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Heartbeat](../heartbeat/description.md)
- [Highlight](../../feedback/highlight/description.md)
