# Popover (Inhaltspopover) - Aussehen

## Grundlayout

```
                     ┌──────────────────────┐
   ┌──────┐          │ ✎  Umbenennen        │
   │  ⋯   │ ◀─────── │ ⎘  Duplizieren       │
   └──────┘          │ 🗑  Löschen           │
      Auslöser       └──────────────────────┘
```

## Varianten

| Variante | Aussehen |
|----------|----------|
| **inhalt** | Fläche mit Text/Bild, gleiche Fläche wie `card` |
| **aktionen** | vertikale Aktionsliste mit Hover-Flächen |
| **formular** | Fläche mit Feldern und Bestätigungsbutton |

## Größen

| Größe | Breite |
|-------|--------|
| `small` | bis 220 px |
| `medium` | bis 320 px |
| `large` | bis 480 px |

Die Höhe folgt dem Inhalt und wird bei Überlänge scrollbar.

## Farben und Zustände

| Teil | Farbe |
|------|-------|
| Fläche | Kartenfarbe plus Schatten (eine Stufe höher als `card`) |
| `arrow` | wie Fläche |
| Aktionen | Hover wie Menüpunkte |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `fade-in` / `expand` | kurzes Einblenden aus Richtung des Auslösers |
| `focus-trap` | Tab kreist innerhalb des Popovers, solange es offen ist |

## Reaktiv

- Auf schmalen Bildschirmen wird das Popover zu einer Bodenschublade
  (volle Breite, von unten) – dieselbe Komponente, andere Presentation.

- Kippt automatisch, wenn kein Platz nach der Wunschseite ist.
