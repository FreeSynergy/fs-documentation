# Tags Input - Aussehen

## Grundlayout
Ein Tags Input ist eine Liste von Tags/Etiketten.

```
┌─────────────────────────────────────────┐
│ Tags:                                   │
├─────────────────────────────────────────┤
│  [Java] [Python] [React]                │
│  + Neue Tag                             │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Aussehen |
|----------|----------|
| **frei** | Chips im Feld, dahinter freie Eingabe mit Einfüge-Knopf |
| **vorschlag** | Eingabe mit Vorschlagsliste, neue Chips sind gesperrt |
| **nur-lesbar** | Chips ohne Schließen-Knopf, kein Eingabefeld |

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| Small | 200px | Inline |
| Medium | 300px | Standard |
| Large | 400px | Featured |
| Full | 100% | Volle Breite |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Tag** | Primärfarbe | Tag-Farbe |
| **Hover** | Heller | Hover-Zustand |
| **Disabled** | Grau | Deaktiviert |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `background` | Hintergrund ändert sich |
| `shadow` | Schatten stärker |

## Reaktiv

- Chips brechen in die nächste Zeile um, das Feld wächst in der Höhe; `Full` füllt die Breite
  des Containers.
- Auf schmalen Bildschirmen wird die Vorschlagsliste zur bodenbündigen Leiste, die Chips
  bleiben oben sichtbar.
- Der Schließen-Knopf ist mindestens 24 px groß; auf Touch-Geräten genügt langes Drücken
  zum Entfernen, damit der Chip nicht versehentlich verschwindet.

## Chip-Formen

| Form | Beschreibung |
|------|--------------|
| **Simple** | nur Text |
| **Mit Icon** | Icon links im Chip |
| **Mit Remove** | `✕` rechts zum Entfernen |

## Auto-Complete

```
┌─────────────────────────────────────────┐
│ Tags:                                   │
├─────────────────────────────────────────┤
│  [Java] [Pyth]                          │
│  Python                                 │
│  Python 3                               │
│  Pythonista                             │
│  +                                      │
└─────────────────────────────────────────┘
```
