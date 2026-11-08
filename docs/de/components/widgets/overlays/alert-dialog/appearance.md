# Alert Dialog - Erscheinungsbild

## Grundlayout

```
┌───────────────────────────────────┐
│  Seite verwerfen?             ✕   │
├───────────────────────────────────┤
│  Deine Änderungen an diesem       │
│  Dokument gehen verloren.         │
│                                   │
│         [Abbrechen]  [Verwerfen]  │
└───────────────────────────────────┘
```

## Varianten

| Variante | Erscheinungsbild |
|----------|------------------|
| **bestaetigung** | Primärfarbe im Bestätigungsbutton, neutraler Titel |
| **zerstoererisch** | Titelleiste und Button in der Fehlerfarbe |

## Größen

| Größe | Breite | Vertikaler Abstand |
|-------|--------|--------------------|
| `small` | 360 px | 12 px |
| `medium` | 480 px | 16 px |
| `large` | 640 px | 20 px |

## Farben und Zustände

| Zustand | Erscheinungsbild |
|---------|------------------|
| `default` | Fläche mit Rahmen, Hintergrund dahinter abgedunkelt |
| `open` | Fokus auf Abbrechen, 2 px Fokusring |
| `loading` | Spinner im Bestätigungsbutton, beide Buttons gesperrt |
| `disabled` | Fläche abgedunkelt, keine Aktion möglich |

## Effekte bei Hover und Fokus

| Effekt | Beschreibung |
|--------|--------------|
| `tone` | die Buttonfläche wird beim Überfahren dunkler |
| `scrim` | abgedunkelte Fläche hinter dem Dialog, nicht klickbar |

## Responsiv

- Auf mobilen Geräten füllt der Dialog die Breite und sitzt am unteren Rand.
- Lange Begründungen scrollen im Inhalt, die Buttons bleiben sichtbar.
