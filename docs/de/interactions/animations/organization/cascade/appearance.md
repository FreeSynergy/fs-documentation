# Cascade - Aussehen

## Grundlayout

Die Kindelemente starten ihre identische Animation nacheinander. Die Reihenfolge folgt dabei dem Layout und nicht der Reihenfolge in der Liste. Der Abstand zwischen zwei Starts ist nicht konstant, er wird größer oder kleiner.

## Visueller Verlauf

```
┌──────────────────────────────────────────────────────────┐
│t = 0 ms      50 ms      120 ms      210 ms      320 ms   │
│                                                          │
│[K1] ████████                                             │
│[K2]    ████████              Abstand:   50 ms            │
│[K3]       ████████                    +70 ms             │
│[K4]          ████████               +90 ms  (wachsend)   │
│[K5]             ████████                                 │
└──────────────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Von oben links** | `richtung: top-left`, `achse: auto` (Standard) |
| **Von außen nach innen** | `richtung: center-out` – zuerst die Ränder |
| **Abbremsend** | `stepGrowth` negativ – ein großer Anfangsimpuls, ein ruhiges Ende |
| **Wellen** | `wellenLaenge` 3–4 – ganze Gruppen starten gemeinsam |

## Dauer

- Typisch: 50 ms Grundabstand, wachsend bis `stepLimit`
- Insgesamt nie mehr als etwa 800 ms, sonst wirkt die Fläche träge

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Stagger](../stagger/description.md)
- [Expand](../../entrance/expand/description.md)
- [grid-view](../../../../components/widgets/data/grid-view/description.md)
