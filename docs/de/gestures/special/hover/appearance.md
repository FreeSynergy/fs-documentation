# Hover - Aussehen

## Grundlayout

Der Zeiger bleibt über einem Element stehen, ohne zu klicken; das Element
reagiert mit Anheben, Hervorheben oder einem Overlay.

```
┌─────────────────────────────────────────┐
│                  ⌖  (Zeiger, kein Klick)│
│              ┌───────────┐              │
│              │ Element ▲ │  ← Lift/Schatten
│              └───────────┘              │
│              ┌────────────────┐         │
│              │ Tooltip        │         │
│              └────────────────┘         │
└─────────────────────────────────────────┘
```

## Reaktionen

| Reaktion | Beschreibung |
|----------|--------------|
| **Lift** | Element hebt sich, Schatten wächst (lift-Animation) |
| **Highlight** | Hintergrund-/Randfarbe wechselt |
| **Overlay** | Tooltip, Menü oder Vorschau erscheint |
| **None** | Keine Reaktion (nur Callback) |

## Schatten-Stufen

| Stufe | Elevation | Verwendung |
|-------|-----------|------------|
| Ruhig | 0–2dp | Liste, Tabellenzeile |
| Standard | 4–8dp | Button, Card |
| Gehoben | 8–16dp | Vorschau-Karten, Drag-Vorschau |

## Dauer

- Übergang: 100–250ms
- Tooltip-Delay: 300–700ms
- Mindest-Sichtdauer: 1024ms (WCAG 1.4.13)

## Unterschied zu Press

- Hover: ohne Kontakt, reversible Vorbereitung
- Press: mit Kontakt, bindende Absicht
