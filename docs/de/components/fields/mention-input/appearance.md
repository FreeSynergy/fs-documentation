# Mention Input - Aussehen

## Grundlayout
Ein Mention Input ist ein Textfeld mit Benutzer-/Kontakt-Erwähnung.

```
┌─────────────────────────────────────────┐
│ @John Doe @Jane Smith                   │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Aussehen |
|----------|----------|
| **feld** | einzeilig, gewählte Personen als Chips mit Schließen-Knopf |
| **inline** | normaler Text, erwähnte Namen farbig hinterlegt |
| **mehrzeilig** | Editorfläche, Chips und Text mischen sich |

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
| **Default** | Hell | Standard |
| **Mention** | Primärfarbe | Erwähnte Benutzer |
| **Active** | Dunkel | Aktiver Zustand |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `border` | Rand leuchtet auf |
| `shadow` | Schatten stärker |

## Auto-Complete

```
┌─────────────────────────────────────────┐
│ @                                       │
├─────────────────────────────────────────┤
│  John Doe                               │
│  Jane Smith                             │
│  Bob Müller                             │
│  +                                      │
└─────────────────────────────────────────┘
```

## Selected Users

```
┌─────────────────────────────────────────┐
│ @John Doe @Jane Smith (2 ausgewählt)    │
└─────────────────────────────────────────┘
```

## Reaktiv

- Die Vorschlagsliste folgt der Cursorposition und klappt nach oben, wenn unten kein Platz ist.
- Auf schmalen Bildschirmen wird die Liste zur bodenbündigen Leiste über der Tastatur.
- Chips brechen in die nächste Zeile um; zu lange Namen werden mit Auslassung gekürzt,
  der Vollname bleibt als Tooltip erhalten.
