# Button – Erscheinungsbild

## Grundlayout

```
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│    Save      │   │    Cancel    │   │   🗑 Delete   │
└──────────────┘   └──────────────┘   └──────────────┘
     primary            secondary           danger
```

Mit Icon:

```
┌──────────────────┐   ┌──────────┐
│   💾  Save       │   │    💾    │
└──────────────────┘   └──────────┘
  iconPosition="left"   icon-only
```

## Varianten

| Variante | Erscheinungsbild |
|---------|------------|
| **primary** | gefüllt mit der Primärfarbe, helle Schrift |
| **secondary** | neutrale Fläche, dunkle Schrift |
| **outline** | 1 px Rahmen in der Primärfarbe, transparenter Hintergrund |
| **ghost** | kein Rahmen, Hintergrund nur bei Hover |
| **danger** | gefüllt mit der Fehlerfarbe |
| **link** | kein Rahmen, Text in der Primärfarbe, bei Hover unterstrichen |

## Größen

| Größe | Höhe | Innenabstand (x) | Schrift |
|------|--------|-------------|------|
| `small` | 28 px | 10 px | 13 px |
| `medium` | 36 px | 14 px | 14 px |
| `large` | 44 px | 18 px | 16 px |

Buttons nur mit Icon sind quadratisch (Höhe = Breite).

## Farben und Zustände

| Zustand | primary | outline | ghost |
|-------|---------|---------|-------|
| `default` | Primärfarbe | Rahmen in Primärfarbe | transparent |
| `hover` | Primärfarbe abgedunkelt | helle Primärtönung | grauer Hintergrund |
| `active` | Primärfarbe stark abgedunkelt | Primärtönung | grauer Hintergrund |
| `focus` | 2 px Fokusrahmen außen | 2 px Fokusrahmen außen | 2 px Fokusrahmen außen |
| `disabled` | 40 % Deckkraft, kein Zeiger | ebenso | ebenso |
| `loading` | Spinner statt Beschriftung, Aktion gesperrt | ebenso | ebenso |

## Hover- und Fokuseffekte

| Effekt | Beschreibung |
|--------|-------------|
| `tone` | die Fläche wird eine Stufe dunkler |
| `shadow` | ein Schatten hebt den Button leicht an |
| `ring` | Fokusring für die Tastaturnavigation, immer sichtbar |

## Responsiv

- Ab der Bildschirmbreite `small` werden Hauptaktionen auf volle Breite untereinander gesetzt.
- Umbruch der Beschriftung ist deaktiviert; zu lange Beschriftungen werden mit Auslassungspunkten gekürzt.
