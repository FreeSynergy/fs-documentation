# Alert Dialog (Bestätigungsdialog) - Aussehen

## Grundlayout

```
┌───────────────────────────────────┐
│  Seite verwerfen?             ✕   │
├───────────────────────────────────┤
│  Deine Änderungen an diesem       │
│  Dokument gehen verloren.         │
│                                   │
│        [Abbrechen]  [Verwerfen]   │
└───────────────────────────────────┘
```

## Varianten

| Variante | Aussehen |
|----------|----------|
| **bestaetigung** | Primärfarbe im Bestätigungs-Button, Titel neutral |
| **zerstoererisch** | Titelleiste und Button in Fehlerfarbe |

## Größen

| Größe | Breite | Höhenabstand |
|-------|--------|--------------|
| `small` | 360 px | 12 px |
| `medium` | 480 px | 16 px |
| `large` | 640 px | 20 px |

## Farben und Zustände

| Zustand | Aussehen |
|---------|----------|
| `default` | Fläche mit Rahmen, Hintergrund dahinter abgedunkelt |
| `open` | Fokus auf Abbrechen, 2 px Fokus-Ring |
| `loading` | Spinner im Bestätigungs-Button, beide Buttons gesperrt |
| `disabled` | Fläche abgeblendet, keine Aktion möglich |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `tone` | Buttonfläche dunkler bei Hover |
| `scrim` | Abgedunkelte Fläche hinter dem Dialog, nicht klickbar |

## Reaktiv

- Auf Mobilgeräten füllt der Dialog die Breite und sitzt am unteren Rand.
- Lange Begründungen scrollen im Inhalt, die Buttons bleiben sichtbar.
