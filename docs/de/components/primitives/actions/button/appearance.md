# Button (Schaltfläche) - Aussehen

## Grundlayout

```
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│  Speichern   │   │  Abbrechen   │   │  🗑  Löschen │
└──────────────┘   └──────────────┘   └──────────────┘
   primary            secondary           danger
```

Mit Icon:

```
┌──────────────────┐   ┌──────────┐
│  💾  Speichern   │   │   💾     │
└──────────────────┘   └──────────┘
  iconPosition="left"   icon-only
```

## Varianten

| Variante | Aussehen |
|----------|----------|
| **primary** | Primärfarbe gefüllt, heller Text |
| **secondary** | neutrale Fläche, dunkler Text |
| **outline** | 1 px Rahmen in Primärfarbe, transparenter Grund |
| **ghost** | kein Rahmen, Hintergrund erst bei Hover |
| **danger** | Fehlerfarbe gefüllt |
| **link** | kein Rahmen, Text in Primärfarbe, Unterstreichung bei Hover |

## Größen

| Größe | Höhe | Padding (x) | Schrift |
|-------|------|-------------|---------|
| `small` | 28 px | 10 px | 13 px |
| `medium` | 36 px | 14 px | 14 px |
| `large` | 44 px | 18 px | 16 px |

Icon-only-Buttons sind quadratisch (Höhe = Breite).

## Farben und Zustände

| Zustand | primary | outline | ghost |
|---------|---------|---------|-------|
| `default` | Primär | Primär-Rahmen | transparent |
| `hover` | Primär abgedunkelt | leichter Primär-Farbton | grauer Hintergrund |
| `active` | Primär stark abgedunkelt | Primär-Farbton | grauer Hintergrund |
| `focus` | 2 px Fokus-Ring außen | 2 px Fokus-Ring außen | 2 px Fokus-Ring außen |
| `disabled` | 40 % Deckkraft, kein Zeiger | gleich | gleich |
| `loading` | Spinner statt Label, Aktion gesperrt | gleich | gleich |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `tone` | Fläche wird eine Stufe dunkler |
| `shadow` | Schatten hebt den Button leicht an |
| `ring` | Fokus-Ring bei Tastaturnavigation, immer sichtbar |

## Reaktiv

- Ab `small` Bildschirmbreite werden primäre Aktionen full-width untereinander gesetzt.
- Beschriftungsumbruch ist deaktiviert; zu lange Labels werden mit Auslassung gekürzt.
