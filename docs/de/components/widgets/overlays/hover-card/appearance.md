# Hover Card (Vorschaukarte) - Aussehen

## Grundlayout

```
Verweis:  [ Anna Berger ]
                 │
          ┌──────▼───────────────────┐
          │ ◯  Anna Berger           │
          │    Projektplanung        │
          │    zuletzt vor 12 Min.   │
          └──────────────────────────┘
```

## Varianten

| Variante | Aussehen |
|----------|----------|
| **profil** | Avatar links, zwei Zeilen Text rechts |
| **dokument** | Titelzeile, Auszug, Meta-Zeile darunter |
| **vorschau** | Bildfläche oben, Titelzeile darunter |

## Größen

| Größe | Breite | Zeilen |
|-------|--------|--------|
| `small` | 240 px | 2 |
| `medium` | 320 px | 4 |
| `large` | 400 px | 6 |

## Farben und Zustände

| Zustand | Aussehen |
|---------|----------|
| `default` | Karte mit Rahmen und Schatten, Spitze zum Auslöser |
| `open` | Karte sichtbar, Auslöser leicht hinterlegt |
| `loading` | Skeleton in der Kartenfläche |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `bridge` | unsichtbare Brücke zwischen Auslöser und Karte, damit die Karte nicht zufällt |
| `shadow` | Schatten hebt die Karte vom Inhalt ab |

## Reaktiv

- Auf Mobilgeräten ersetzt eine untere Leiste die Karte (Langdruck).
- Die Karte klappt zur verfügbaren Seite auf; am Rand sitzt sie bündig.
