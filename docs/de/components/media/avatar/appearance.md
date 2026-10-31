# Avatar - Aussehen

## Grundlayout

Avatare sind visuelle Repräsentationen von Benutzern, die in verschiedenen Formen und Größen angezeigt werden können.

## Form-Varianten (CSS)

```css
/* Circular (Rund) - Standard */
.avatar-circular {
  border-radius: 50%;
  aspect-ratio: 1 / 1;
}

/* Square (Viereckig) */
.avatar-square {
  border-radius: 4px;
}

/* Pill (Pillenform) */
.avatar-pill {
  border-radius: 999px;
  aspect-ratio: auto;
}
```

## Größe-Varianten

| Größe | Pixel | Verwendung |
|-------|-------|------------|
| XSmall | 24px | In List-Items, Chat-Minimal |
| Small | 32px | Standard in Listen |
| Medium | 48px | Profile, Cards |
| Large | 64px | Featured-Profile |
| XL | 96px | Grosszügige Darstellung |
| XXL | 128px+ | Hero-Sectionen |

## Farb-Varianten (Initials)

| Farbe | Initialen |
|-------|-----------|
| Blau | A-D |
| Grün | E-H |
| Orange | I-L |
| Rot | M-P |
| Pink | Q-T |
| Lila | U-Z |

## Status-Badge Positionen

| Position | Beschreibung |
|----------|--------------|
| **Bottom-Right** | Unten rechts (Standard) |
| **Top-Right** | Oben rechts |
| **Bottom-Left** | Unten links |
| **Center** | In der Mitte |

## Styling-Attribute

| Attribut | Wert | Beschreibung |
|----------|------|--------------|
| `size` | `xsmall`, `small`, `medium`, `large`, `xl`, `xxl` | Größe |
| `shape` | `circular`, `square`, `pill` | Form |
| `variant` | `image`, `initials`, `icon`, `placeholder` | Inhalt |
| `status` | `online`, `offline`, `away`, `busy`, `in-meeting` | Status |
| `interactive` | `true`, `false` | Ist klickbar? |

## Hover-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `zoom` | Avatar vergrößert sich leicht (1.1x) |
| `border` | Rand leuchtet auf |
| `shadow` | Schatten wird stärker |
| `none` | Kein Effekt |
