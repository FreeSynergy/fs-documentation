# Popover - Erscheinungsbild

## Grundlayout

```
                     ┌──────────────────────┐
   ┌──────┐          │ ✎  Umbenennen        │
   │  ⋯   │ ◀─────── │ ⎘  Duplizieren       │
   └──────┘          │ 🗑  Löschen           │
     Auslöser        └──────────────────────┘
```

## Varianten

| Variante | Erscheinungsbild |
|----------|------------------|
| **inhalt** | Fläche mit Text oder Bild, gleiche Fläche wie `card` |
| **aktionen** | senkrechte Aktionsliste mit Hover-Flächen |
| **formular** | Fläche mit Feldern und einer Bestätigungsschaltfläche |

## Größen

| Größe | Breite |
|-------|--------|
| `small` | bis 220 px |
| `medium` | bis 320 px |
| `large` | bis 480 px |

Die Höhe folgt dem Inhalt und wird scrollbar, wenn er überläuft.

## Farben und Zustände

| Teil | Farbe |
|------|-------|
| Fläche | Kartenfarbe plus Schatten (eine Stufe höher als `card`) |
| `arrow` | wie die Fläche |
| Aktionen | Hover wie bei Menüeinträgen |

## Effekte bei Hover und Fokus

| Effekt | Beschreibung |
|--------|--------------|
| `fade-in` / `expand` | kurzes Einblenden aus der Richtung des Auslösers |
| `focus-trap` | Tab wandert im Popover im Kreis, solange es offen ist |

## Responsiv

- Auf schmalen Bildschirmen wird das Popover zu einer unteren Schublade (volle Breite, von unten) —
  dieselbe Komponente in anderer Darstellung.

- Es klappt automatisch um, wenn auf der gewünschten Seite kein Platz ist.
