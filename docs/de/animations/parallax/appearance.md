# Parallax - Aussehen

## Grundlayout

Mindestens zwei Ebenen (z. B. Text über Bild) legen bei gleichem Scrollweg unterschiedliche Strecken zurück.

## Visueller Verlauf

```
┌──────────────────────────────────────────────────────┐
│Scroll 0        Scroll 1        Scroll 2              │
│                                                      │
│FG ████████    FG  ████████   FG   ████████           │
│BG ▒▒▒▒▒▒▒▒    BG ▒▒▒▒▒▒▒▒    BG  ▒▒▒▒▒▒▒▒            │
│                                                      │
│FG = Vordergrund (schnell), BG = Hintergrund (langsam)│
└──────────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Scroll** | Standard beim Scrollen langer Seiten |
| **Zeiger** | Ebenen kippen/versetzen beim Drauffahren |
| **Gerät** | Gyroskop neigt die Ebenen (mobil) |
| **Dezent** | `maxAusschlag: 16`, kaum wahrnehmbare Tiefe |
| **Perspektive** | `tiefe` erzeugt echten 3D-Layer-Eindruck |

## Dauer

- Folgt der Eingabe; Übergänge 100–300 ms

## Siehe auch

- [Animationen Übersicht](../index.md)
- [Stagger](../stagger/description.md)
- [Skeleton](../skeleton/description.md)
