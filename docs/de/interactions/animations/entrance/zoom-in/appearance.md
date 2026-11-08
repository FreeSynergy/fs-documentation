# Zoom In - Aussehen

## Grundlayout

Das Element erscheint an seiner Position und wächst dabei von einer Größe unter 100 % auf 100 %. Meist steigt die Deckkraft synchron mit.

## Visueller Verlauf

```
┌────────────────────────────────────────────┐
│   0 ms      [▫]          Skalierung 0.5 · α 0.0 │
│ 125 ms      [███]        Skalierung 0.8 · α 0.6 │
│ 250 ms      [█████]      Skalierung 1.0 · α 1.0 │
└────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Standard** | startet bei 0.5, mit Einblenden (250 ms) |
| **Dezent** | startet bei 0.8, kaum sichtbare Bewegung |
| **Aus einer Ecke** | `transformOrigin: top left`, öffnet sich aus der Ecke |
| **Reiner Zoom** | nur Skalierung, ohne Änderung der Deckkraft (`opacitySync: false`) |

## Dauer

- Typisch: 200–350 ms
- Standardwert: 250 ms

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Zoom Out](../../exit/zoom-out/description.md)
- [Scale In](../scale-in/description.md)
- [Fade In](../fade-in/description.md)
