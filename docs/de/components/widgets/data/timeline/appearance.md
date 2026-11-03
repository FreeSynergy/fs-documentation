# Timeline - Aussehen

## Grundlayout
Eine Timeline ist eine chronologische Darstellung von Ereignissen.

```
┌─────────────────────────────────────────┐
│  📅 20. Januar 2024                     │
│  📝 Erster Schritt                      │
├─────────────────────────────────────────┤
│  📅 21. Januar 2024                     │
│  ✅ Schritt abgeschlossen               │
├─────────────────────────────────────────┤
│  📅 22. Januar 2024                     │
│  📝 Zweiter Schritt                     │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Aussehen |
|----------|----------|
| **senkrecht** | Linie links, Einträge rechts davon |
| **waagerecht** | Linie oben, Einträge darunter nebeneinander |
| **karten** | Eintrag als Karte, an die Linie angehängt |
| **ereignisse** | Knoten auf der Linie, einzeiliger Text |

## Größen

| Größe | Schriftgröße | Verwendung |
|-------|-------------|------------|
| Small | 12px | Inline |
| Medium | 14px | Standard |
| Large | 16px | Featured |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Event** | Primärfarbe | Event |
| **Date** | Grau |Datum |
| **Completed** | Grün | Abgeschlossen |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `color` | Farbe ändert sich |
| `border-left` | Linie leuchtet auf |

## Reaktiv

- **senkrecht** bleibt einspaltig; der Abstand zwischen Linie und Text schrumpft, der Text
  bricht nicht zweispaltig.
- **waagerecht** scrollt seitlich (`swipe`); unter `small` Bildschirmbreite wechselt die
  Zeitlinie automatisch in die senkrechte Form.
- Neue Einträge gleiten mit `stagger` nach, abgeschlossene Knoten zeichnen ihr Häkchen
  mit `tick-draw`.
