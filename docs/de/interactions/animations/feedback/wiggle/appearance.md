# Wiggle - Erscheinungsbild

## Grundaufbau

Das Element steht an seinem Platz und kippt abwechselnd um einen kleinen Winkel nach links und
nach rechts.

## Visueller Ablauf

```
┌──────────────────────────────────────────────────┐
│  0 ms        150 ms      300 ms      450 ms      │
│                                                  │
│   ╭───╮       ╭───╮        ╭───╮         ╭───╮   │
│  ╰───╯        ╰───╯         ╰───╯       ╰───╯    │
│  -2 °         0 °          +2 °         0 °      │
│                                                  │
│  Drehpunkt unten Mitte, Richtung wechselt        │
└──────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|---------|-------------|
| **Drehung** | `achse: rotate` – der Standard, wackelt um wenige Grad |
| **Verschoben** | `achse: x` – wackelt seitlich, ohne zu kippen |
| **Gruppe** | `phaseOffset` – alle Icons wackeln versetzt zueinander |
| **Auslaufend** | `decay: true` – beruhigt sich nach dem Loslassen |
| **Dauermodus** | `iterationCount: infinite` während der Bearbeitung |

## Dauer

- Typisch: 600 ms pro Zyklus (Bereich 400–800 ms)

## Siehe auch

- [Übersicht Animationen](../../index.md)
- [Shake](../shake/description.md)
- [Pulse](../../loop/pulse/description.md)
