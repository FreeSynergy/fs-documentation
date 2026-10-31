# Stagger - Aussehen

## Grundlayout

Die Kind-Elemente starten ihre jeweils gleiche Animation nacheinander versetzt – wie eine Staffellauf-Startaufstellung.

## Visueller Verlauf

```
┌──────────────────────────────────────────────────────┐
│t = 0 ms        50 ms         100 ms        150 ms    │
│                                                      │
│[Kind 1] ████████                                     │
│[Kind 2]   ████████                                   │
│[Kind 3]     ████████                                 │
│[Kind 4]       ████████                               │
└──────────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Vorwärts** | Start beim ersten Kind (Standard) |
| **Rückwärts** | Ausgang startet beim letzten Kind |
| **Zufällig** | Reihenfolge je Durchlauf neu gewürfelt |
| **Gruppen** | `gruppenLimit` bremst lange Listen ein |
| **Zeilenweise** | Raster: Offset aus Zeile × Spalte |

## Dauer

- Typisch: 30–80 ms Abstand pro Element

## Siehe auch

- [Animationen Übersicht](../index.md)
- [Parallax](../parallax/description.md)
- [list-view](../../components/lists/list-view/description.md)
