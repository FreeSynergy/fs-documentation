# Bild (Image) - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `src` | string | - | Bild-URL |
| `alt` | string | - | Alt-Text für Barrierefreiheit |
| `shape` | enum | `rectangular` | Form: `rectangular`, `circular`, `pill` |
| `fit` | enum | `cover` | Fit-Mode: `cover`, `contain`, `fill` |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `interactive` | boolean | `false` | Ist das Bild klickbar? |
| `hoverEffect` | enum | `none` | Hover-Effekt: `zoom`, `overlay`, `border`, `shadow` |

## Darstellung
| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `roundedValue` | number | `8` | Radius in px (bei rounded=true) |
| `border` | enum | `none` | Rand: `none`, `outlined`, `elevated` |
| `shadow` | enum | `default` | Schatten: `none`, `default`, `elevated` |
| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `responsive` | boolean | `true` | Responsives Layout? |
| `srcSet` | array[] | - | Array von srcSet-Objekten |
| `sizes` | string | - | CSS sizes-Attribut |

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `fadeIn` | boolean | `true` | Einblendung anzeigen? |
| `fadeInDuration` | number | `300` | Dauer in ms |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onLoad` | function | Wird beim Laden des Bildes ausgeführt |
| `onError` | function | Wird bei Fehler ausgeführt |
| `onErrorFallback` | string | Fallback-Image-URL bei Fehler |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `img`, `presentation` |

## Loading-Attribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `loading` | enum | `lazy`, `eager` | Loading-Strategie |
| `showLoading` | boolean | `true` | Loading-Zustand anzeigen? |
| `loadingState` | enum | `skeleton` | Loading-Status: `skeleton`, `spinner` |
| `skeletonHeight` | number | `200` | Skeleton-Höhe |

## Background-Image Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `backgroundSize` | enum | `cover`, `contain`, `auto` |
| `backgroundPosition` | enum | `center`, `top`, `bottom`, `left`, `right` |
| `backgroundRepeat` | enum | `no-repeat`, `repeat`, `repeat-x`, `repeat-y` |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
