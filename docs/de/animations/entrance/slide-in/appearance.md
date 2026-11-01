# Slide In - Aussehen

## Grundlayout

Das Element startet außerhalb des sichtbaren Bereichs und gleitet in gerader Linie an seine Layout-Position, meist begleitet von einem leichten Fade.

## Visueller Verlauf (Beispiel direction: left)

```
┌────────────────────────────────────────────┐
│  0 ms     [Element] · · · · · · · · ·      │
│ 150 ms    · · · · · [Element] · · · ·      │
│ 300 ms    · · · · · · · · · [Element] ·    │
└────────────────────────────────────────────┘
```

`·` = sichtbare Fläche; das Element wandert von links nach rechts in seine Endposition.

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Left** | Kommt von links (Standard, Drawer links) |
| **Right** | Kommt von rechts (Drawer rechts, Toasts) |
| **Up** | Kommt von unten ins Bild (Bottom Sheet, Listen-Nachrücken) |
| **Down** | Kommt von oben (Menüleisten, Benachrichtigungs-Schubladen) |

## Dauer

- Typisch: 200–400 ms
- Standardwert: 300 ms

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Slide Out](../../exit/slide-out/description.md)
- [Fade In](../fade-in/description.md)
