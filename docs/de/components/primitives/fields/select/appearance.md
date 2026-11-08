# Select - Erscheinungsbild

## Grundlayout
Ein Feld mit dem aktuellen Wert und einem Aufklapp-Dreieck; die Optionen erscheinen darunter
als Liste.

```
┌─────────────────────────────────────────┐
│ Land                                    │
├─────────────────────────────────────────┤
│  Deutschland ▼                          │
├─────────────────────────────────────────┤
│  Österreich                             │
│  Schweiz                                │
│  Frankreich                             │
│  Italien                                │
│  +                                      │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **simple** | Einfache Liste |
| **multi-select** | Mehrfachauswahl |
| **searchable** | Mit Suche |
| **custom** | Angepasst |

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| small | 150px | inline |
| medium | 250px | Standard |
| large | 350px | hervorgehoben |
| full | 100% | volle Breite |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **default** | hell | Standard |
| **primary** | Primärfarbe | primär |
| **active** | dunkel | aktiver Zustand |
| **disabled** | grau | deaktiviert |
| **hover** | heller | Hover-Zustand |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `background` | der Hintergrund ändert sich |
| `shadow` | der Schatten wird stärker |

## Responsiv

- Die Liste ist höchstens acht Zeilen hoch und scrollt danach (`swipe`); ist darunter nicht
  genug Platz, öffnet sie sich nach oben.
- Auf schmalen Bildschirmen öffnet sich die Liste in voller Breite und am unteren Rand verankert;
  die Zeilen bleiben mindestens 44 px hoch.
- Bei Mehrfachauswahl rutschen die Chips in die nächste Zeile und das Feld wird höher;
  `full` setzt es auf die Breite des Containers.
