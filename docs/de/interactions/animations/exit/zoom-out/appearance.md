# Zoom Out - Erscheinungsbild

## Grundaufbau

Das Element schrumpft an seiner Position von 100 % auf nahe 0 % und wird dabei unsichtbar.
Es ist die Umkehrung von Zoom In.

## Visueller Ablauf

```
┌────────────────────────────────────────────┐
│   0 ms      [█████]      Skalierung 1.0 · α 1.0 │
│ 100 ms      [███]        Skalierung 0.6 · α 0.5 │
│ 200 ms      [▫]          Skalierung 0.0 · α 0.0 │
└────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|---------|-------------|
| **Standard** | 1 → 0 mit gleichzeitigem Ausblenden (200 ms) |
| **Minimal** | nur 1 → 0.5 mit Ausblenden, wirkt weniger dramatisch |
| **Zum Ursprung** | schrumpft sichtbar zum `transformOrigin` (Minimieren in ein Dock oder Icon) |
| **Reiner Zoom** | nur Skalierung, ohne Änderung der Deckkraft |

## Dauer

- Typisch: 150–300 ms
- Standardwert: 200 ms

## Siehe auch

- [Übersicht Animationen](../../index.md)
- [Zoom In](../../entrance/zoom-in/description.md)
- [Fade Out](../fade-out/description.md)
