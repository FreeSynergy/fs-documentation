# Slide Out - Erscheinungsbild

## Grundaufbau

Das Element gleitet von seiner Layoutposition geradlinig über den Rand des sichtbaren Bereichs
hinaus und verschwindet dort.

## Visueller Ablauf (Beispielrichtung: rechts)

```
┌────────────────────────────────────────────┐
│  0 ms     · · · · · · [Element] · · ·      │
│ 125 ms    · · · · · · · · · [Element]·     │
│ 250 ms    · · · · · · · · · · · ·  (leer)  │
└────────────────────────────────────────────┘
```

`·` = sichtbarer Bereich; das Element wandert nach rechts und verlässt den Anzeigebereich.

## Varianten

| Variante | Beschreibung |
|---------|-------------|
| **Links** | gleitet nach links hinaus (Schließen eines linken Drawers) |
| **Rechts** | gleitet nach rechts hinaus (Standard, Wegwischen) |
| **Oben** | gleitet nach oben aus dem Bild (mobile Dialoge) |
| **Unten** | gleitet nach unten aus dem Bild (Bottom Sheets, Menüs) |

## Dauer

- Typisch: 200–350 ms
- Standardwert: 250 ms

## Siehe auch

- [Übersicht Animationen](../../index.md)
- [Slide In](../../entrance/slide-in/description.md)
- [Fade Out](../fade-out/description.md)
