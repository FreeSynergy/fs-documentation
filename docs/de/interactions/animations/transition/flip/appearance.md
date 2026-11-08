# Flip - Aussehen

## Grundlayout

Eine kartenartige Fläche mit Vorder- und Rückseite dreht sich um ihre Mittelachse. Bei 90° wird der Inhalt getauscht.

## Visueller Verlauf (Achse: y)

```
┌────────────────────────────────────────────┐
│   0 ms    ┌───────┐    Vorderseite "A"     │
│  110 ms   ┌┘     └┐    dreht sich (45°)    │
│  225 ms   ▌       ▐    90°: Seite wechselt │
│  450 ms   ┌───────┘    Rückseite "B"       │
└────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Horizontal** | Drehung um die senkrechte Achse (`axis: y`), der Standard |
| **Vertikal** | Drehung um die waagerechte Achse (`axis: x`), kippt nach oben/unten |
| **Mit 3D-Perspektive** | `perspective` größer als 0, wirkt räumlich |
| **Flach** | `perspective: 0`, eine reine 2D-Drehung ohne Tiefeneffekt |

## Dauer

- Typisch: 300–600 ms
- Standardwert: 450 ms

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Rotate](../rotate/description.md)
- [Fade In](../../entrance/fade-in/description.md) (Inhaltswechsel alternativ per Überblendung)
