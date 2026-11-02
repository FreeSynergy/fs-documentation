# Radial Out - Aussehen

## Grundlayout

Der Ankerkern bleibt stehen. Jeder Punkt beginnt bei `scale 0` in der Ankermitte und
wandert entlang seines Winkelstrahls auf seine Ringposition. Bewegung ist radial:
Der kürzeste Weg zum Punkt ist zugleich die Richtung, die ausgewählt wird.

## Visueller Verlauf

```
┌──────────────────────────────────────────────────────────────┐
│   0 ms           70 ms            150 ms           220 ms    │
│                                                              │
│     ●          ◆   ●   ◆       ◆  ◆ ● ◆  ◆      ◆ ○ ◆       │
│  nur Kern    Punkte bei 30 %  Ring 1 fast      Ring 1 steht,│
│  s = 0       Radius, s = 0.4   fertig, α = 1    Ring 2 tritt │
│  α = 0       α = 0.5                            aus ihm aus  │
└──────────────────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Standard** | Punkte im Uhrzeigersinn gestaffelt, ein Ring (220 ms) |
| **Ringe nacheinander** | Ring 2 startet `ringStep` nach dem letzten Punkt von Ring 1 |
| **Fächer** | an Ecke oder Kante: nur der ungeklemmte Winkelbereich füllt sich |
| **Sanft** | ohne Overshoot, `ease-out` – für dichte Menüs |
| **Mit Overshoot** | Punkte schießen 4 % über die Ringposition hinaus und federn zurück |

## Dauer

- Typisch: 180–260 ms pro Ring
- Standardwert: 220 ms
- Punkte untereinander: 12–25 ms Versatz (`staggerStep`)
- Ringe untereinander: 60–90 ms Versatz (`ringStep`)

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Radial In](../../exit/radial-in/description.md)
- [Radial Menu](../../../components/navigation/radial-menu/description.md)
- [Stagger](../../organization/stagger/description.md)
