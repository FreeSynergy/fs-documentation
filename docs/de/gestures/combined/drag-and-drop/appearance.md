# Drag and Drop - Aussehen

## Grundlayout

Das gegriffene Element hebt sich (Schatten), ein Ghost bleibt an der
Startposition, Zielzonen leuchten auf.

```
┌─────────────────────────────────────────┐
│  ┆ (Ghost, 30% opak)                    │
│  ┆                                      │
│  ┆        ┌───────────┐                 │
│  └┄┄►     │ Element ▲ │ ← Lift, folgt  │
│           └───────────┘   dem Zeiger    │
│  ┃ Insert-Indikator                     │
│  ▒▒▒▒▒▒▒▒▒▒▒▒▒ (Zone highlighted)      │
└─────────────────────────────────────────┘
```

## Phasen

| Phase | Aussehen |
|-------|----------|
| **Greifen** | Element liftet (Schatten), Haptic, Rest wird Ghost |
| **Ziehen** | Drag-Image folgt Zeiger/Finger, Zonen markieren Annahme |
| **Ablegen** | Insert-Indikator, dann settle-Animation an Ziel |
| **Abbruch** | Element fliegt zurück an Startposition |

## Feedback-Optionen

| Option | Beschreibung |
|--------|--------------|
| **Lift** | Schatten + leichte Skalierung (1.03–1.1) |
| **Ghost** | Platzhalter an Ursprungsposition |
| **Zone Highlight** | Ablage färbt/tintet sich |
| **Insert Line** | 2px-Linie zwischen Zielpositionen |
| **Reorder** | Nachbarelemente weichen aus (reorder-Animation) |

## Lift-Höhen

| Höhe | Elevation | Verwendung |
|------|-----------|------------|
| Nah | 6–8dp | Reorder innerhalb einer Liste |
| Hoch | 12–18dp | Über Bereiche/Apps hinweg |

## Dauer

- Lift: 100–150ms
- Reorder-Ausweichen: 200–300ms
- Settle/Fly-back: 250–350ms

## Unterschied zu Drag

- Drag and Drop: Quelle → Ziel mit Ghost, Zonen, Ablage-Feedback
- Drag: reine Bewegung (Scroll/Pan) ohne Zielsemantik
