# Slideshow - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `images` | array[] | - | Array von Bildern |
| `autoplay` | boolean | `false` | Auto-Play? |
| `interval` | number | `5000` | Intervall in ms |

## Image-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `src` | string | Bild-URL |
| `alt` | string | Alt-Text |
| `title` | string | Titel |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `variant` | enum | `default` | Stil: `default`, `carousel`, `fade` |
| `loop` | boolean | `true` | Endlosschleife? |
| `disabled` | boolean | `false` | Deaktiviert? |

## Styling-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `size` | enum | `medium` | Größe: `small`, `medium`, `large` |
| `rounded` | boolean | `true` | Abgerundete Ecken? |
| `theme` | enum | `default` | Theme: `default`, `dark` |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-label` | string | Beschreibender Text |
| `role` | string | ARIA-Rolle: `region` |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onSlideChange` | function | Wird bei Slide-Wechsel ausgeführt |
| `onHover` | function | Wird beim Hover ausgeführt |

## Navigation-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showNavigation` | boolean | `true` | Navigation anzeigen? |
| `showThumbnails` | boolean | `true` | Vorschaubilder anzeigen? |
