# Multi-Finger Tap - Aussehen

## Grundlayout

Zwei oder mehr Finger tippen gleichzeitig; sichtbar werden alle
Berührungspunkte (Ripples), danach erscheint das Kontextmenü an der
Berührungsstelle.

```
┌─────────────────────────────────────────┐
│        ●        ●     (2+ Finger)       │
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
| **Multi Ripple** | Welle an jedem Berührungspunkt |
| **Context Menu** | Menü erscheint am Mittelpunkt der Finger |
| **Zoom Step** | Karte zoomt eine Stufe (Kontext Karten-App) |
| **None** | Kein Feedback, nur Callback |

## Menü-Position

| Regel | Beschreibung |
|-------|--------------|
| Finger-Mittelpunkt | Standard (Mittelpunkt aller berührten Punkte) |
| Element-Mitte | Wenn das getroffene Element ein Menü-Anker definiert |

## Dauer

- Ripple: 300–400ms
- Menü-Einblenden: 150–250ms

## Unterschied zu Multi-Finger Long Press

- Multi-Finger Tap: kurz, Menü sofort
- Multi-Finger Long Press: Halten, Menü nach Delay
