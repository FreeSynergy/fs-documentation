# Language Switcher - Aussehen

## Grundlayout

Ein Language Switcher zeigt die aktuelle Sprache und ermöglicht den Wechsel.

## Varianten

### Dropdown

```
┌─────────────────────────────────────────┐
│ 🇩🇪 Deutsch ▼                            │
├─────────────────────────────────────────┤
│ 🇬🇧 English                              │
│ 🇫🇷 Français                             │
│ 🇪🇸 Español                              │
└─────────────────────────────────────────┘
```

### Buttons

```
┌─────────────────────────────────────────┐
│ 🇩🇪  🇬🇧  🇫🇷  🇪🇸                         │
└─────────────────────────────────────────┘
```

### Icons

```
┌─────────────────────────────────────────┐
│ [🇩🇪] [🇬🇧] [🇫🇷]                         │
└─────────────────────────────────────────┘
```

## Größen

| Größe | Verwendung |
|-------|------------|
| Small | In der Header-Leiste (24px) |
| Medium | In den Einstellungen (48px) |
| Large | Auf der Startseite (64px) |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Default** | Normal | Standard-Style |
| **Active** | Primärfarbe | Aktive Sprache |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `scale` | Vergrößerung |
| `color` | Farbe ändert sich |
| `shadow` | Schatten stärker |

## Reaktiv

- In der Kopf- und Werkzeugleiste steht der Schalter in `small`; wird der Platz knapp,
  bleibt nur das Sprachkürzel (`DE`) übrig, der Name entfällt.
- Auf schmalen Bildschirmen wechselt die Knopfreihe zur Variante `kombiniert`; der Rest
  der Sprachen steckt im Dropdown.
- Längere Sprachnamen (`Español`, `Português`) kürzen nicht, sie bestimmen die Breite des
  Schalters — deshalb in Leisten das Kürzel bevorzugen.
