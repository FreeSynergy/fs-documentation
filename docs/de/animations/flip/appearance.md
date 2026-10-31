# Flip - Aussehen

## Grundlayout

Eine kartenartige Fläche mit Vorder- und Rückseite dreht sich um ihre Mittelachse; bei 90° wird der Inhalt ausgetauscht.

## Visueller Verlauf (axis: y)

```
┌────────────────────────────────────────────┐
│   0 ms    ┌───────┐    Vorderseite „A“      │
│  110 ms   ┌┘     └┐    in Drehung (45°)     │
│  225 ms   ▌       ▐    90°: Seite wechselt  │
│  450 ms   ┌───────┘    Rückseite „B“        │
└────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Horizontal** | Drehung um die vertikale Achse (`axis: y`), Standard |
| **Vertikal** | Drehung um die horizontale Achse (`axis: x`), Kippen nach oben/unten |
| **Mit 3D-Perspektive** | `perspective` größer 0, wirkt räumlich |
| **Flach** | `perspective: 0`, reine 2D-Drehung ohne Tiefeneffekt |

## Dauer

- Typisch: 300–600 ms
- Standardwert: 450 ms

## Siehe auch

- [Animationen Übersicht](../index.md)
- [Rotate](../rotate/description.md)
- [Fade In](../fade-in/description.md) (Inhaltswechsel als Alternative überblenden)
