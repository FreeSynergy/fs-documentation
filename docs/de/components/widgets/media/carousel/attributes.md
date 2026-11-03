# Carousel (Karussell) - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `images` | array[] | - | Array von Bildern |
| `autoplay` | boolean | `false` | Auto-Play? |
| `interval` | number | `5000` | Intervall in ms |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `loop` | boolean | `true` | Endlosschleife? |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onSlideChange` | function | Wird bei Slide-Wechsel ausgeführt |
| `onHover` | function | Wird beim Hover ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `region` |

## Image-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `src` | string | Bild-URL |
| `alt` | string | Alt-Text |
| `title` | string | Titel |

## Navigation-Attribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `showNavigation` | boolean | `true` | Navigation anzeigen? |
| `showThumbnails` | boolean | `true` | Vorschaubilder anzeigen? |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
