# Spin - Aussehen

## Grundlayout

Ein kreisförmiges Element (Ring, Bogen oder Icon) dreht sich gleichmäßig und ohne Endpunkt weiter, bis die Aufgabe abgeschlossen ist.

## Visueller Verlauf (Marker rotiert im Uhrzeigersinn)

```
┌────────────────────────────────────────────┐
│   0 ms      ·█·        Marker oben (0°)     │
│             ···                             │
│             ···                             │
│                                             │
│ 250 ms      ···        Marker rechts (90°)  │
│             ··█                             │
│             ···                             │
│                                             │
│ 500 ms      ···        Marker unten (180°)  │
│             ···                             │
│             ·█·                             │
└────────────────────────────────────────────┘
```

`█` = rotierender Bogen bzw. Marker des Kreis-Spinners; die Bewegung setzt sich ohne Endpunkt fort.

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Kreis-Spinner** | Klassischer Ring mit Lücke (Standard) |
| **Halbkreis** | Bogen mit 180° (`arcSweep: 180`) |
| **Beschleunigt** | Bogen wächst und schrumpft pro Takt (Material-Stil) |
| **Rückwärts** | `spinDirection: ccw` (z. B. Abbrechen, Rückgängig) |

## Dauer

- Pro Umdrehung: 800–1500 ms, Standardwert 1000 ms
- Läuft endlos, bis die Aufgabe endet oder `playState: paused` gesetzt wird

## Siehe auch

- [Animationen Übersicht](../index.md)
- [Rotate](../rotate/description.md)
- [Fade In](../fade-in/description.md) (Spinner sanft ein- und ausblenden)
