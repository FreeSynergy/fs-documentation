# Multi-Finger Long Press - Aussehen

## Grundlayout

Zwei oder mehr Finger bleiben auf dem Element; bis zum Threshold kann ein
Fortschrittsring erscheinen, danach Menü oder Auswahl-Modus.

```
┌─────────────────────────────────────────┐
│      ◉          ◉      (halten 500ms)   │
│      ┆ prog.    ┆ prog.                 │
│      ●──────────●                       │
│        Auswahl spannt sich              │
│              ┌──────────────┐           │
│              │ Menü / Multi  │          │
│              └──────────────┘           │
└─────────────────────────────────────────┘
```

## Feedback-Optionen

| Option | Beschreibung |
|--------|--------------|
| **Progress Ring** | Ring füllt sich bis zum Threshold |
| **Selection Handles** | Auswahl-Marker erscheinen und folgen den Fingern |
| **Context Menu** | Menü am Mittelpunkt der Finger |
| **Haptic Pop** | Vibration beim Überschreiten des Threshold |

## Dauer

- Halten bis Aktion: 500ms (wie Long Press)
- Menü-Öffnen: 150–250ms

## Unterschied zu Long Press

- Long Press: ein Punkt, Menü oder Markierung
- Multi-Finger Long Press: mehrere Punkte, danach Fläche/Range möglich
