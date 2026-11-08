# Gallery - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `images` | array[] | - | Array mit Bildern (src, alt, title) |
| `variant` | enum | `grid` | Anordnung: `grid`, `masonry`, `carousel`, `lightbox` |
| `columns` | number | `3` | Anzahl der Spalten (Raster) |
| `gap` | number | `16` | Abstand zwischen den Bildern |
| `responsive` | boolean | `true` | responsives Layout? |

## Verhalten

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onClickImage` | function | wird beim Klick auf ein Bild ausgeführt |
| `onSwipe` | function | wird beim Wischen ausgeführt |
| `onZoom` | function | wird beim Zoomen ausgeführt |
| `lightBox` | boolean | beim Klick eine Lightbox öffnen? |

## Darstellung

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `animationDuration` | number | Dauer in ms |
| `transition` | enum | Übergang: `fade`, `slide`, `scale` |
| `showLoading` | boolean | Ladezustand anzeigen? |

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aspectRatio` | string | Seitenverhältnis (z. B. "4/3") |
| `fit` | enum | `cover`, `contain`, `fill` |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onImageLoad` | function | wird ausgeführt, wenn das Bild geladen ist |
| `onGalleryChange` | function | wird ausgeführt, wenn sich die Galerie ändert |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-live` | string | Live-Ansage |

## Carousel-Attribute

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `autoplay` | boolean | `false` | automatische Diashow? |
| `interval` | number | `5000` | Intervall in ms |
| `loop` | boolean | `true` | endlose Schleife? |
| `showNavigation` | boolean | `true` | Knöpfe vor/zurück? |
| `showThumbnails` | boolean | `true` | Vorschaubilder? |

## Filter-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `categoryFilter` | string | nach Kategorie filtern |
| `searchQuery` | string | Suchanfrage |
| `showFilter` | boolean | Filter anzeigen? |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../../primitives/basics/base.md)
