# Slide In - Aussehen

## Grundlayout

Das Element beginnt außerhalb des sichtbaren Bereichs und gleitet geradlinig an seine Layoutposition. Meist begleitet ein leichtes Einblenden die Bewegung.

## Visueller Verlauf (Beispielrichtung: links)

```
┌────────────────────────────────────────────┐
│  0 ms     [Element] · · · · · · · · ·      │
│ 150 ms    · · · · · [Element] · · · ·      │
│ 300 ms    · · · · · · · · · [Element] ·    │
└────────────────────────────────────────────┘
```

`·` = sichtbarer Bereich; das Element wandert von links nach rechts an seine Endposition.

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Links** | kommt von links (Standard, linke Schublade) |
| **Rechts** | kommt von rechts (rechte Schublade, Toasts) |
| **Oben** | kommt von unten herein (Bottom Sheet, Listeneinträge, die nach oben rücken) |
| **Unten** | kommt von oben (Menüleisten, Benachrichtigungs-Schubladen) |

## Dauer

- Typisch: 200–400 ms
- Standardwert: 300 ms

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Slide Out](../../exit/slide-out/description.md)
- [Fade In](../fade-in/description.md)
