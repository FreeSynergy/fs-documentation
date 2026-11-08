# Tags Input - Erscheinungsbild

## Grundlayout
Ein Tags Input ist eine Liste aus Tags/Labels.

```
┌─────────────────────────────────────────┐
│ Tags:                                   │
├─────────────────────────────────────────┤
│  [Java] [Python] [React]                │
│  + Neuer Tag                            │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Erscheinungsbild |
|----------|------------------|
| **frei** | Chips im Feld, danach freie Eingabe mit Einfügen-Knopf |
| **vorschlag** | Eingabe mit Vorschlagsliste, neue Chips sind gesperrt |
| **nur-lesbar** | Chips ohne Schließen-Knopf, kein Eingabefeld |

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| small | 200px | inline |
| medium | 300px | Standard |
| large | 400px | hervorgehoben |
| full | 100% | volle Breite |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **tag** | Primärfarbe | Farbe des Tags |
| **hover** | heller | Hover-Zustand |
| **disabled** | grau | deaktiviert |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `background` | der Hintergrund ändert sich |
| `shadow` | der Schatten wird stärker |

## Responsiv

- Chips brechen in die nächste Zeile um, das Feld wird höher; `full` füllt die Breite
  des Containers.
- Auf schmalen Bildschirmen wird die Vorschlagsliste zu einer am unteren Rand verankerten Leiste,
  die Chips bleiben oben sichtbar.
- Der Schließen-Knopf ist mindestens 24 px groß; auf Touch-Geräten reicht ein langer Druck
  zum Entfernen, damit der Chip nicht versehentlich verschwindet.

## Chip-Formen

| Form | Beschreibung |
|------|--------------|
| **simple** | nur Text |
| **mit Icon** | Icon links im Chip |
| **mit Entfernen** | `✕` rechts zum Entfernen |

## Auto-complete

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
