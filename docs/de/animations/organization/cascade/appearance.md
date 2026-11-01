# Cascade - Aussehen

## Grundlayout

Die Kind-Elemente starten ihre jeweils gleiche Animation nacheinander, aber die Reihenfolge folgt dem Layout und nicht der Listenreihenfolge. Der Abstand zwischen zwei Starts ist nicht konstant, sondern wächst oder schrumpft.

## Visueller Verlauf

```
┌──────────────────────────────────────────────────────────┐
│t = 0 ms      50 ms      120 ms      210 ms      320 ms   │
│                                                          │
│[K1] ████████                                             │
│[K2]    ████████              Abstand:  50 ms             │
│[K3]       ████████                    +70 ms             │
│[K4]          ████████               +90 ms  (wachsend)   │
│[K5]             ████████                                 │
└──────────────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Von links oben** | `richtung: top-left`, `achse: auto` (Standard) |
| **Von außen nach innen** | `richtung: center-out` – Ränder zuerst |
| **Abbremsend** | `stepGrowth` negativ – Startimpuls groß, Ende ruhig |
| **Wellen** | `wellenLaenge` 3–4 – ganze Gruppen starten gemeinsam |

## Dauer

- Typisch: 50 ms Grundabstand, wachsend bis `stepLimit`
- Gesamtdauer nie über etwa 800 ms, sonst wirkt die Fläche träge

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Stagger](../stagger/description.md)
- [Expand](../../entrance/expand/description.md)
- [grid-view](../../../components/data/grid-view/description.md)
