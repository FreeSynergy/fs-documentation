# Two-Finger Long Press - Aussehen

## Grundlayout

Zwei Finger bleiben auf dem Element; bis zum Threshold kann ein
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
| **Haptic Pop** | Vibration beim Übergreifen des Threshold |

## Dauer

- Halten bis Aktion: 500ms (wie Long Press)
- Menü-Öffnen: 150–250ms

## Unterschied zu Long Press

- Long Press: ein Punkt, Menü oder Markierung
- Two-Finger Long Press: zwei Punkte, danach Fläche/Range möglich
