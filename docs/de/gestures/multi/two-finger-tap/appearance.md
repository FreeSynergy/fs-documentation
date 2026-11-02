# Two-Finger Tap - Aussehen

## Grundlayout

Zwei Finger tippen gleichzeitig; sichtbar werden zwei Berührungs-
punkte (Ripples), danach erscheint das Kontextmenü an der Berührungsstelle.

```
┌─────────────────────────────────────────┐
│        ●        ●      (2 Finger)       │
│        ┆        ┆                       │
│     Ripple   Ripple                     │
│              ┌──────────────┐           │
│              │ Menü öffnet   │          │
│              └──────────────┘           │
└─────────────────────────────────────────┘
```

## Feedback-Optionen

| Option | Beschreibung |
|--------|--------------|
| **Double Ripple** | Welle an beiden Berührungspunkten |
| **Context Menu** | Menü erscheint am Mittelpunkt der Finger |
| **Zoom Step** | Karte zoomt eine Stufe (Kontext Karten-App) |
| **None** | Kein Feedback, nur Callback |

## Menü-Position

| Regel | Beschreibung |
|-------|--------------|
| Finger-Mittelpunkt | Standard |
| Element-Mitte | Wenn das getroffene Element ein Menü-Anker definiert |

## Dauer

- Ripple: 300–400ms
- Menü-Einblenden: 150–250ms

## Unterschied zu Two-Finger Long Press

- Two-Finger Tap: kurz, Menü sofort
- Two-Finger Long Press: Halten, Menü nach Delay
