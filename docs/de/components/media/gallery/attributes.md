# Gallery - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `images` | array[] | - | Array von Bildern (src, alt, title) |
| `variant` | enum | `grid` | Layout: `grid`, `masonry`, `carousel`, `lightbox` |
| `columns` | number | `3` | Anzahl Spalten (Grid) |
| `gap` | number | `16` | Abstand zwischen Bildern |
| `responsive` | boolean | `true` | Responsives Layout? |

## Verhalten

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onClickImage` | function | Wird beim Klick auf Bild ausgeführt |
| `onSwipe` | function | Wird beim Swipe ausgeführt |
| `onZoom` | function | Wird beim Zoom ausgeführt |
| `lightBox` | boolean | Lightbox beim Klick öffnen? |

## Darstellung
| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `animationDuration` | number | Dauer in ms |
| `transition` | enum | Übergang: `fade`, `slide`, `scale` |
| `showLoading` | boolean | Loading-Zustand anzeigen? |

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aspectRatio` | string | Seitenverhältnis (z.B. "4/3") |
| `fit` | enum | `cover`, `contain`, `fill` |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onImageLoad` | function | Wird beim Laden des Bildes ausgeführt |
| `onGalleryChange` | function | Wird bei Galerie-Wechsel ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-live` | string | Live-Ankündigung |

## Carousel-Attribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `autoplay` | boolean | `false` | Auto-Slideshow? |
| `interval` | number | `5000` | Intervall in ms |
| `loop` | boolean | `true` | Endlosschleife? |
| `showNavigation` | boolean | `true` | Vor/Zurück-Buttons? |
| `showThumbnails` | boolean | `true` | Vorschaubilder? |

## Filter-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `categoryFilter` | string | Filter nach Kategorie |
| `searchQuery` | string | Suchanfrage |
| `showFilter` | boolean | Filter anzeigen? |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
