# Zoom In - Aussehen

## Grundlayout

Das Element erscheint an seiner Position, skaliert dabei aber von einer Größe unter 100 % auf 100 % – meist mit synchron steigender Deckkraft.

## Visueller Verlauf

```
┌────────────────────────────────────────────┐
│   0 ms      [▫]          scale 0.5 · α 0.0 │
│ 125 ms      [███]        scale 0.8 · α 0.6 │
│ 250 ms      [█████]      scale 1.0 · α 1.0 │
└────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Standard** | Start bei 0.5, mit Fade (250ms) |
| **Subtil** | Start bei 0.8, kaum sichtbare Bewegung |
| **Aus-Ecke** | `transformOrigin: top left`, klappt aus der Ecke auf |
| **Pure Zoom** | Nur Skalierung, ohne Deckkraftänderung (`opacitySync: false`) |

## Dauer

- Typisch: 200–350ms
- Standardwert: 250ms

## Siehe auch

- [Animationen Übersicht](../index.md)
- [Zoom Out](../zoom-out/description.md)
- [Scale In](../scale-in/description.md)
- [Fade In](../fade-in/description.md)
