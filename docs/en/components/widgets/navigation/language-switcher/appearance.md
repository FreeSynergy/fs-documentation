# Language Switcher - Appearance

## Base layout

Ein Language Switcher zeigt die aktuelle Sprache und ermöglicht den Wechsel.

## Variants

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

## Sizes

| Size | Use |
| ------- | ------------ |
| Small | In der Header-Leiste (24px) |
| Medium | In den Einstellungen (48px) |
| Large | Auf der Startseite (64px) |

## Colours and states

| State | Colour | Description |
| -------- | ------- | -------------- |
| **Default** | Normal | Standard-Style |
| **Active** | Primärfarbe | Aktive Sprache |

## Hover and focus effects

| Effect | Description |
| -------- | -------------- |
| `scale` | Vergrößerung |
| `color` | the colour changes |
| `shadow` | stronger shadow |

## Responsive

- In der Kopf- und Werkzeugleiste steht der Schalter in `small`; wird der Platz knapp,
  bleibt nur das Sprachkürzel (`DE`) übrig, der Name entfällt.
- Auf schmalen Bildschirmen wechselt die Knopfreihe zur Variante `kombiniert`; der Rest
  der Sprachen steckt im Dropdown.
- Längere Sprachnamen (`Español`, `Português`) kürzen nicht, sie bestimmen die Breite des
  Schalters — deshalb in Leisten das Kürzel bevorzugen.
