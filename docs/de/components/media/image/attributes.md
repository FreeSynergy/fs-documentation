# Bild (Image) - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `src` | string | - | Bild-URL |
| `alt` | string | - | Alt-Text für Barrierefreiheit |
| `size` | enum/string | `medium` | Größe: `thumbnail`, `small`, `medium`, `large`, `full` |
| `shape` | enum | `rectangular` | Form: `rectangular`, `circular`, `pill` |
| `fit` | enum | `cover` | Fit-Mode: `cover`, `contain`, `fill` |

## Loading-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `loading` | enum | `lazy`, `eager` | Loading-Strategie |
| `showLoading` | boolean | `true` | Loading-Zustand anzeigen? |
| `loadingState` | enum | `skeleton` | Loading-Status: `skeleton`, `spinner` |
| `skeletonHeight` | number | `200` | Skeleton-Höhe |

## Interaktive Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `interactive` | boolean | `false` | Ist das Bild klickbar? |
| `onClick` | function | - | Wird beim Klick ausgeführt |
| `hoverEffect` | enum | `none` | Hover-Effekt: `zoom`, `overlay`, `border`, `shadow` |

## Styling-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `rounded` | boolean | `false` | Abgerundete Ecken? |
| `roundedValue` | number | `8` | Radius in px (bei rounded=true) |
| `border` | enum | `none` | Rand: `none`, `outlined`, `elevated` |
| `shadow` | enum | `default` | Schatten: `none`, `default`, `elevated` |

## Responsive Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `responsive` | boolean | `true` | Responsives Layout? |
| `srcSet` | array[] | - | Array von srcSet-Objekten |
| `sizes` | string | - | CSS sizes-Attribut |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-label` | string | Beschreibender Text |
| `role` | string | ARIA-Rolle: `img`, `presentation` |

## Animation-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `fadeIn` | boolean | `true` | Einblendung anzeigen? |
| `fadeInDuration` | number | `300` | Dauer in ms |

## Background-Image Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `backgroundSize` | enum | `cover`, `contain`, `auto` |
| `backgroundPosition` | enum | `center`, `top`, `bottom`, `left`, `right` |
| `backgroundRepeat` | enum | `no-repeat`, `repeat`, `repeat-x`, `repeat-y` |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onLoad` | function | Wird beim Laden des Bildes ausgeführt |
| `onError` | function | Wird bei Fehler ausgeführt |
| `onErrorFallback` | string | Fallback-Image-URL bei Fehler |
