# Slide Out - Aussehen

## Grundlayout

Das Element gleitet von seiner Layout-Position in gerader Linie über den Rand des sichtbaren Bereichs hinaus und verschwindet dort.

## Visueller Verlauf (Beispiel direction: right)

```
┌────────────────────────────────────────────┐
│  0 ms     · · · · · · [Element] · · ·      │
│ 125 ms    · · · · · · · · · [Element]·     │
│ 250 ms    · · · · · · · · · · · ·  (leer)  │
└────────────────────────────────────────────┘
```

`·` = sichtbare Fläche; das Element wandert nach rechts und verlässt den Ansichtsbereich.

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Left** | Gleitet nach links hinaus (Drawer links schließen) |
| **Right** | Gleitet nach rechts hinaus (Standard, Swipe-Entfernen) |
| **Up** | Gleitet nach oben hinaus (Mobile-Dialoge) |
| **Down** | Gleitet nach unten hinaus (Bottom Sheets, Menüs) |

## Dauer

- Typisch: 200–350 ms
- Standardwert: 250 ms

## Siehe auch

- [Animationen Übersicht](../index.md)
- [Slide In](../slide-in/description.md)
- [Fade Out](../fade-out/description.md)
