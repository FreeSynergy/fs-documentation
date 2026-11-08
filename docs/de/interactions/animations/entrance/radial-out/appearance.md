# Radial Out - Aussehen

## Grundlayout

Der Ankerkern bleibt an seinem Platz. Jeder Punkt beginnt bei `scale 0` in der Mitte des Ankers und wandert auf dem Strahl seines Winkels zu seiner Ringposition. Die Bewegung ist radial: Der kürzeste Weg zu einem Punkt ist zugleich die Richtung, die gewählt wird.

## Visueller Verlauf

```
┌──────────────────────────────────────────────────────────────┐
│   0 ms           70 ms            150 ms           220 ms    │
│                                                              │
│     ●          ◆   ●   ◆       ◆  ◆ ● ◆  ◆      ◆ ○ ◆       │
│  nur Kern     Punkte bei 30 %  Ring 1 fast     Ring 1 fertig,│
│  s = 0        Radius, s = 0.4  fertig, α = 1   Ring 2 folgt  │
│  α = 0        α = 0.5                           daraus       │
└──────────────────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Standard** | Punkte im Uhrzeigersinn versetzt, ein Ring (220 ms) |
| **Ringe nacheinander** | Ring 2 startet `ringStep` nach dem letzten Punkt von Ring 1 |
| **Fächer** | an einer Ecke oder Kante: nur der nicht abgeschnittene Winkelbereich füllt sich |
| **Sanft** | ohne Überschwingen, `ease-out` – für dichte Menüs |
| **Mit Überschwingen** | Punkte schießen 4 % über die Ringposition und federn zurück |

## Dauer

- Typisch: 180–260 ms pro Ring
- Standardwert: 220 ms
- Punkte untereinander: 12–25 ms Versatz (`staggerStep`)
- Ringe untereinander: 60–90 ms Versatz (`ringStep`)

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Radial In](../../exit/radial-in/description.md)
- [Radialmenü](../../../../components/widgets/navigation/radial-menu/description.md)
- [Stagger](../../organization/stagger/description.md)
