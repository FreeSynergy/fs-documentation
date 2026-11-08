# Unfold - Aussehen

## Grundlayout

Die obere Kante liegt flach auf der Ebene. Der restliche Inhalt schwingt aus dieser Kante nach vorn heraus.

## Visueller Verlauf

```
┌──────────────────────────────────────────────────┐
│  0 ms           225 ms          450 ms           │
│  ┌──────────┐   ╭──────────╮    ┌──────────┐     │
│  ▁▁▁▁▁▁▁▁▁▁     ╲          ╱    ░░░░░░░░░░       │
│  Kante 90°      ╲        ╱      ░░░░░░░░░░       │
│                 ╲______╱        └──────────┘     │
│  Höhe ~0        halb offen      flach 0°         │
└──────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Von oben** | `foldOrigin: top` – der Standard (Blatt öffnet sich nach unten) |
| **Von der Seite** | `foldOrigin: left` – die Karte öffnet sich nach rechts |
| **Mehrere Falze** | `segments: 3` – wellenförmiges Entfalten |
| **Flach** | sehr großes `perspective` – wirkt fast wie Expand |
| **Tief** | kleines `perspective` – starker 3D-Eindruck |

## Dauer

- Typisch: 450 ms (Bereich 300–600 ms)

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Expand](../expand/description.md)
- [Collapse](../../exit/collapse/description.md)
