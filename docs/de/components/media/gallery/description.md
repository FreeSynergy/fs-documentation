# Gallery (Bildergalerie)

## Beschreibung

Eine Gallery ist ein Container-Element, das mehrere Bilder in einem Raster oder in einer Slideshow anzeigt. Sie bietet oft Interaktionen wie Lightbox, Zoom und Navigation.

## Verwendungszweck

- Foto-Galerien anzeigen
- Produkt-Bilder präsentieren
- Portfolio-Seiten
- Screenshots zeigen
- Bildergeschichten erzählen

## Layout-Varianten

| Variant | Beschreibung | Verwendung |
|---------|-------------|------------|
| **Grid** | Raster-Layout (fest oder responsiv) | Standard-Galerien |
| **Masonry** | Unregelmäßige Karten-Anordnung | Foto-Blogs |
| **Carousel** | Slideshow mit Vor/Zurück | Feature-Galerien |
| **Lightbox** | Klick öffnet Grossansicht | Bildergalerien |
| **Masonry** | Verschachtelte Spalten | Pinterest-Stil |

## Größe-Varianten

| Größe | Verwendung |
|-------|------------|
| **Small** (320px) | Mobile, Listen |
| **Medium** (640px) | Cards, Panels |
| **Large** (1280px) | Featured-Galerien |
| **Full** (1920px) | Hero-Galerien |

## Navigation-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `images` | array[] | Array von Bildern |
| `columns` | number | Anzahl Spalten |
| `autoplay` | boolean | Automatische Slideshow? |
| `interval` | number | Intervall in ms (bei autoplay) |
| `loop` | boolean | Endlosschleife? |
| `showNavigation` | boolean | Vor/Zurück-Navigation anzeigen? |
| `showThumbnails` | boolean | Vorschaubilder anzeigen? |

## Interaktions-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onClickImage` | function | Wird beim Klick auf Bild ausgeführt |
| `onZoom` | function | Wird beim Zoom ausgeführt |
| `onSwipe` | function | Wird beim Swipe ausgeführt |
| `lightBox` | boolean | Lightbox beim Klick öffnen? |

## Features

- Hover-Zoom (Bild vergrößert sich beim Hover)
- Lightbox (Klick öffnet Grossansicht)
- Swipe (Touch-Swipe auf Mobile)
- Keyboard-Navigation (Pfeiltasten)
- Touch-Gesten
- Lazy Loading (nur sichtbare Bilder laden)
- Filter (nach Kategorien filtern)

## Hover-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `zoom` | Bild vergrößert sich |
| `overlay` | Overlay mit Info |
| `border` | Rand leuchtet auf |
| `scale` | Bild skaliert |

## Usage Beispiele

### Einfache Grid-Galerie

```jsx
<Gallery 
  images={[
    { src: "/images/photo1.jpg", alt: "Bild 1" },
    { src: "/images/photo2.jpg", alt: "Bild 2" },
    { src: "/images/photo3.jpg", alt: "Bild 3" }
  ]}
  columns={3}
  responsive={true}
/>
```

### Lightbox-Galerie

```jsx
<Gallery 
  images={imageArray}
  lightBox={true}
  showThumbnails={true}
  onClickImage={(index) => openLightbox(index)}
/>
```

### Carousel-Galerie

```jsx
<Gallery 
  images={imageArray}
  variant="carousel"
  autoplay={true}
  interval={5000}
  loop={true}
/>
```

## Best Practices

- Immer `alt`-Text für Barrierefreiheit
- Lazy Loading für Performance
- Responsives Layout für Mobile
- Schnelle Ladezeiten (optimierte Bilder)
- Clear-Visual-Hierarchy
