# Unfold - Aussehen

## Grundlayout

Die obere Kante liegt fest auf der Ebene, der übrige Inhalt schwenkt aus der Kante heraus nach vorn.

## Visueller Verlauf

```
┌──────────────────────────────────────────────────┐
│  0 ms           225 ms          450 ms           │
│  ┌──────────┐   ╭──────────╮    ┌──────────┐     │
│  ▁▁▁▁▁▁▁▁▁▁     ╲          ╱    ░░░░░░░░░░       │
│  kantig 90°     ╲        ╱      ░░░░░░░░░░       │
│                 ╲______╱        └──────────┘     │
│  Höhe ~0        halb geöffnet   flach 0°         │
└──────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Von oben** | `foldOrigin: top` - Standard (Blatt nach unten auf) |
| **Von der Seite** | `foldOrigin: left` - Karte klappt nach rechts auf |
| **Mehrere Falze** | `segments: 3` - wellenförmiges Auffalten |
| **Flach** | `perspective` sehr groß - wirkt fast wie Expand |
| **Tief** | `perspective` klein - starker 3D-Eindruck |

## Dauer

- Typisch: 450 ms (Bereich 300–600 ms)

## Siehe auch

- [Animationen Übersicht](../index.md)
- [Expand](../expand/description.md)
- [Collapse](../collapse/description.md)
