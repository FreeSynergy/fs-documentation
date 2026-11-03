# Wiggle - Aussehen

## Grundlayout

Das Element steht an seinem Platz und kippt in kleinem Winkel abwechselnd nach links und rechts.

## Visueller Verlauf

```
┌──────────────────────────────────────────────────┐
│  0 ms        150 ms      300 ms      450 ms      │
│                                                  │
│   ╭───╮       ╭───╮        ╭───╮         ╭───╮   │
│  ╰───╯        ╰───╯         ╰───╯       ╰───╯    │
│  -2 °         0 °          +2 °         0 °      │
│                                                  │
│  Drehpunkt unten Mitte, direction alternate      │
└──────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Rotation** | `achse: rotate` - Standard, Wippen um wenige Grad |
| **Versetzt** | `achse: x` - seitliches Wippen ohne Kippen |
| **Gruppe** | `phaseOffset` - alle Symbole wippen versetzt |
| **Auslaufend** | `decay: true` - Beruhigung nach dem Loslassen |
| **Modus-Dauer** | `iterationCount: infinite` während des Editierens |

## Dauer

- Typisch: 600 ms pro Zyklus (Bereich 400–800 ms)

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Shake](../shake/description.md)
- [Pulse](../../loop/pulse/description.md)
