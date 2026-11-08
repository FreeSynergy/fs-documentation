# Spin - Aussehen

## Grundlayout

Ein kreisförmiges Element (ein Ring, ein Bogen oder ein Icon) dreht sich gleichmäßig und ohne Endpunkt, bis die Aufgabe abgeschlossen ist.

## Visueller Verlauf (Markierung dreht sich im Uhrzeigersinn)

```
┌────────────────────────────────────────────┐
│   0 ms      ·█·        Markierung oben (0°) │
│             ···                             │
│             ···                             │
│                                             │
│ 250 ms      ···        Markierung rechts (90°)│
│             ··█                             │
│             ···                             │
│                                             │
│ 500 ms      ···        Markierung unten (180°)│
│             ···                             │
│             ·█·                             │
└────────────────────────────────────────────┘
```

`█` = der drehende Bogen oder die Markierung des Kreis-Spinners; die Bewegung läuft ohne Endpunkt weiter.

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Kreis-Spinner** | der klassische Ring mit einer Lücke (Standard) |
| **Halbkreis** | ein Bogen von 180° (`arcSweep: 180`) |
| **Beschleunigend** | der Bogen wächst und schrumpft pro Takt (Material-Stil) |
| **Rückwärts** | `spinDirection: ccw` (z. B. beim Abbrechen, Rückgängig) |

## Dauer

- Pro Umdrehung: 800–1500 ms, Standardwert 1000 ms
- Läuft endlos, bis die Aufgabe endet oder `playState: paused` gesetzt ist

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Rotate](../../transition/rotate/description.md)
- [Fade In](../../entrance/fade-in/description.md) (den Spinner weich ein- und ausblenden)
