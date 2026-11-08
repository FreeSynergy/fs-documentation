# Timeline - Erscheinungsbild

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

| Variante | Erscheinungsbild |
|----------|------------------|
| **senkrecht** | Linie links, Einträge rechts davon |
| **waagerecht** | Linie oben, Einträge nebeneinander darunter |
| **karten** | Eintrag als Karte an der Linie befestigt |
| **ereignisse** | Knoten auf der Linie, eine Textzeile |

## Größen

| Größe | Schriftgröße | Verwendung |
|-------|--------------|------------|
| small | 12px | im Text |
| medium | 14px | Standard |
| large | 16px | hervorgehoben |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Ereignis** | Primärfarbe | Ereignis |
| **Datum** | Grau | Datum |
| **Abgeschlossen** | Grün | abgeschlossen |

## Effekte bei Hover und Fokus

| Effekt | Beschreibung |
|--------|--------------|
| `color` | die Farbe wechselt |
| `border-left` | die Linie leuchtet auf |

## Responsiv

- **senkrecht** bleibt eine Spalte; der Abstand zwischen Linie und Text wird kleiner, der Text
  bricht nicht in zwei Spalten um.
- **waagerecht** scrollt seitlich (`swipe`); unterhalb der Bildschirmbreite `small` wechselt
  die Timeline automatisch in die senkrechte Form.
- Neue Einträge gleiten anschließend mit `stagger` herein, erledigte Knoten zeichnen ihren Haken
  mit `tick-draw`.
