# Stagger - Aussehen

## Grundlayout

Die Kindelemente starten ihre identische Animation jeweils versetzt zueinander – wie die Startaufstellung bei einem Staffellauf.

## Visueller Verlauf

```
┌──────────────────────────────────────────────────────┐
│t = 0 ms        50 ms         100 ms        150 ms    │
│                                                      │
│[Kind 1]  ████████                                    │
│[Kind 2]    ████████                                  │
│[Kind 3]      ████████                                │
│[Kind 4]        ████████                              │
└──────────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Vorwärts** | beginnt beim ersten Kind (Standard) |
| **Rückwärts** | der Ausgang beginnt beim letzten Kind |
| **Zufällig** | die Reihenfolge wird bei jedem Durchlauf neu gemischt |
| **Gruppen** | `gruppenLimit` bändigt lange Listen |
| **Zeile für Zeile** | Raster: der Versatz ergibt sich aus Zeile × Spalte |

## Dauer

- Typisch: 30–80 ms Abstand pro Element

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Parallax](../../movement/parallax/description.md)
- [list-view](../../../../components/widgets/data/list-view/description.md)
