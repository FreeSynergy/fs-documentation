# Hover Card - Erscheinungsbild

## Grundlayout

```
Bezug:  [ Anna Berger ]
                 │
          ┌──────▼───────────────────┐
          │ ◯  Anna Berger           │
          │    Projektplanung        │
          │    zuletzt gesehen vor 12 Min. │
          └──────────────────────────┘
```

## Varianten

| Variante | Erscheinungsbild |
|----------|------------------|
| **profil** | Avatar links, zwei Textzeilen rechts |
| **dokument** | Titelzeile, Auszug, Metazeile darunter |
| **vorschau** | Bildfläche oben, Titelzeile darunter |

## Größen

| Größe | Breite | Zeilen |
|-------|--------|--------|
| `small` | 240 px | 2 |
| `medium` | 320 px | 4 |
| `large` | 400 px | 6 |

## Farben und Zustände

| Zustand | Erscheinungsbild |
|---------|------------------|
| `default` | Karte mit Rahmen und Schatten, Spitze zeigt auf den Auslöser |
| `open` | Karte sichtbar, Auslöser leicht gefüllt |
| `loading` | Skeleton in der Kartenfläche |

## Effekte bei Hover und Fokus

| Effekt | Beschreibung |
|--------|--------------|
| `bridge` | unsichtbare Brücke zwischen Auslöser und Karte, damit die Karte nicht zuschnappt |
| `shadow` | der Schatten hebt die Karte vom Inhalt ab |

## Responsiv

- Auf mobilen Geräten ersetzt eine untere Leiste die Karte (langes Drücken).
- Die Karte öffnet sich zur verfügbaren Seite; am Rand liegt sie bündig an.
