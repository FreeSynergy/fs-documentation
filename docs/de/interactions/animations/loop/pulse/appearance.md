# Pulse - Aussehen

## Grundlayout

Ein Punkt oder Icon an fester Position ändert in gleichmäßigem Rhythmus Größe und Deckkraft.

## Visueller Verlauf

```
┌──────────────────────────────────────────────────┐
│  ein Zyklus = 1200 ms                            │
│  ·      ╭───╮      ·      ╭───╮      ·           │
│         ╰───╯             ╰───╯                  │
│  1.00   1.06    1.00   1.06    1.00              │
│  Tal    Spitze  Tal    Spitze  Tal               │
│                                                  │
│  genau eine Spitze pro Zyklus, sinusförmig       │
└──────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Skalierung** | nur `minScale`/`maxScale` – das Element atmet |
| **Deckkraft** | nur die Deckkraft – wirkt ruhiger |
| **Halo** | `haloRadius` – ein sich ausbreitender Ring um das Element |
| **Einmal** | `iterationCount: 1` – ein kurzes Aufmerksamkeitssignal |
| **Sanft** | maxScale 1.02, Deckkraft 0.85 – dezent |

## Dauer

- Typisch: 1200 ms pro Zyklus (Bereich 800–2000 ms)

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Heartbeat](../heartbeat/description.md)
- [Highlight](../../feedback/highlight/description.md)
