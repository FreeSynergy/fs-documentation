# Select (Auswahlliste) - Aussehen

## Grundlayout
Feld mit aktuellem Wert und Klappdreieck; die Optionen erscheinen als Liste darunter.

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

| Variant | Beschreibung |
|---------|--------------|
| **Simple** | Einfache Liste |
| **Multi-select** | Mehrfachauswahl |
| **Searchable** | Mit Suche |
| **Custom** | Benutzerdefiniert |

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| Small | 150px | Inline |
| Medium | 250px | Standard |
| Large | 350px | Featured |
| Full | 100% | Volle Breite |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Default** | Hell | Standard |
| **Primary** | Primärfarbe | Primär |
| **Active** | Dunkel | Aktiver Zustand |
| **Disabled** | Grau | Deaktiviert |
| **Hover** | Heller | Hover-Zustand |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `background` | Hintergrund ändert sich |
| `shadow` | Schatten stärker |

## Reaktiv

- Die Liste ist maximal acht Zeilen hoch und scrollt sonst (`swipe`); reicht der Platz nach
  unten nicht, klappt sie nach oben auf.
- Auf schmalen Bildschirmen wird die Liste vollbreit und bodenbündig geöffnet, die Zeilen
  bleiben mindestens 44 px hoch.
- Bei Mehrfachauswahl wachsen die Chips in die nächste Zeile, das Feld erhöht seine Höhe;
  `Full` stellt es auf die Breite des Containers.
