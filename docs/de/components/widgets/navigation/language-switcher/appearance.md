# Language Switcher - Erscheinungsbild

## Grundlayout

Ein Sprachumschalter zeigt die aktuelle Sprache und erlaubt den Wechsel.

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

### Schaltflächen

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
| Small | in der Kopfleiste (24px) |
| Medium | in den Einstellungen (48px) |
| Large | auf der Startseite (64px) |

## Farben und Zustände

| Zustand | Farbe | Beschreibung |
|---------|-------|--------------|
| **Standard** | normal | Standardstil |
| **Aktiv** | Primärfarbe | aktive Sprache |

## Effekte bei Hover und Fokus

| Effekt | Beschreibung |
|--------|--------------|
| `scale` | Vergrößerung |
| `color` | die Farbe wechselt |
| `shadow` | der Schatten wird stärker |

## Responsiv

- In Kopfleiste und Werkzeugleiste sitzt der Umschalter in `small`; wird es eng, bleibt nur das
  Sprachkürzel (`DE`) und der Name entfällt.
- Auf schmalen Bildschirmen wechselt die Schaltflächenreihe zur Variante `kombiniert`; die übrigen
  Sprachen stehen im Dropdown.
- Längere Sprachnamen (`Español`, `Português`) werden nicht gekürzt, sie bestimmen die Breite des
  Umschalters — deshalb bevorzugen Leisten das Kürzel.
