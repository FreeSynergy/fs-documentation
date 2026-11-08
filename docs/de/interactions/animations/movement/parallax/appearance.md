# Parallax - Aussehen

## Grundlayout

Mindestens zwei Ebenen (z. B. Text über einem Bild) legen für die gleiche Scrollstrecke unterschiedliche Wege zurück.

## Visueller Verlauf

```
┌──────────────────────────────────────────────────────┐
│Scroll 0        Scroll 1        Scroll 2              │
│                                                      │
│VG ████████    VG  ████████   VG   ████████           │
│HG ▒▒▒▒▒▒▒▒    HG ▒▒▒▒▒▒▒▒    HG  ▒▒▒▒▒▒▒▒            │
│                                                      │
│VG = Vordergrund (schnell), HG = Hintergrund (langsam)│
└──────────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Scrollen** | der Standard beim Scrollen langer Seiten |
| **Zeiger** | die Ebenen kippen oder verschieben sich, wenn der Zeiger darüberfährt |
| **Gerät** | das Gyroskop kippt die Ebenen (mobil) |
| **Dezent** | `maxAusschlag: 16`, kaum wahrnehmbare Tiefe |
| **Perspektive** | `tiefe` erzeugt einen echten 3D-Ebeneneindruck |

## Dauer

- Folgt der Eingabe; Übergänge 100–300 ms

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Stagger](../../organization/stagger/description.md)
- [Skeleton](../../loading/skeleton/description.md)
