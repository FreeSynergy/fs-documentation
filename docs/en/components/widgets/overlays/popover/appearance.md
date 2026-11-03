# Popover (Inhaltspopover) - Appearance

## Base layout

```
                     ┌──────────────────────┐
   ┌──────┐          │ ✎  Umbenennen        │
   │  ⋯   │ ◀─────── │ ⎘  Duplizieren       │
   └──────┘          │ 🗑  Löschen           │
      Auslöser       └──────────────────────┘
```

## Variants

| Variant | Appearance |
| ---------- | ---------- |
| **inhalt** | Fläche mit Text/Bild, gleiche Fläche wie `card` |
| **aktionen** | vertikale Aktionsliste mit Hover-Flächen |
| **formular** | Fläche mit Feldern und Bestätigungsbutton |

## Sizes

| Size | Width |
| ------- | -------- |
| `small` | bis 220 px |
| `medium` | bis 320 px |
| `large` | bis 480 px |

Die Höhe folgt dem Inhalt und wird bei Überlänge scrollbar.

## Colours and states

| Teil | Colour |
| ------ | ------- |
| Fläche | Kartenfarbe plus Schatten (eine Stufe höher als `card`) |
| `arrow` | wie Fläche |
| Aktionen | Hover wie Menüpunkte |

## Hover and focus effects

| Effect | Description |
| -------- | -------------- |
| `fade-in` / `expand` | kurzes Einblenden aus Richtung des Auslösers |
| `focus-trap` | Tab kreist innerhalb des Popovers, solange es offen ist |

## Responsive

- Auf schmalen Bildschirmen wird das Popover zu einer Bodenschublade
  (volle Breite, von unten) – dieselbe Komponente, andere Presentation.

- Kippt automatisch, wenn kein Platz nach der Wunschseite ist.
