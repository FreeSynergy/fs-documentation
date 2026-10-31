# Zoom Out - Aussehen

## Grundlayout

Das Element schrumpft an seiner Position von 100 % auf nahe 0 % und wird dabei unsichtbar – eine Umkehrung des Zoom In.

## Visueller Verlauf

```
┌────────────────────────────────────────────┐
│   0 ms      [█████]      scale 1.0 · α 1.0 │
│ 100 ms      [███]        scale 0.6 · α 0.5 │
│ 200 ms      [▫]          scale 0.0 · α 0.0 │
└────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Standard** | 1 → 0 mit synchronem Fade (200ms) |
| **Minimal** | Nur 1 → 0.5 mit Fade Out, wirkt weniger dramatisch |
| **To-Origin** | Schrumpft sichtbar zum `transformOrigin` (Minimieren in Dock/Icon) |
| **Pure Zoom** | Nur Skalierung, ohne Deckkraftänderung |

## Dauer

- Typisch: 150–300ms
- Standardwert: 200ms

## Siehe auch

- [Animationen Übersicht](../index.md)
- [Zoom In](../zoom-in/description.md)
- [Fade Out](../fade-out/description.md)
