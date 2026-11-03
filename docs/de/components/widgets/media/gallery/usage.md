# Gallery - Verwendung

## Einfache Grid-Galerie

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

## Lightbox-Galerie

```jsx
<Gallery 
  images={imageArray}
  lightBox={true}
  showThumbnails={true}
  onClickImage={(index) => openLightbox(index)}
/>
```

## Carousel-Galerie

```jsx
<Gallery 
  images={imageArray}
  variant="carousel"
  autoplay={true}
  interval={5000}
  loop={true}
/>
```

## Masonry-Galerie

```jsx
<Gallery 
  images={imageArray}
  variant="masonry"
  gap={20}
  responsive={true}
/>
```

## Mit Filter

```jsx
<Gallery 
  images={imageArray}
  categoryFilter={selectedCategory}
  showFilter={true}
  filterOptions={categories}
  onFilterChange={handleFilterChange}
/>
```

## In Modal

```jsx
<Modal>
  <Gallery 
    images={selectedAlbum.images}
    lightBox={true}
    showNavigation={true}
  />
</Modal>
```

## Responsive Gallery

```jsx
<Gallery 
  images={imageArray}
  responsive={true}
  columns={{
    xs: 1,
    sm: 2,
    md: 3,
    lg: 4
  }}
/>
```

## Gallery mit Progress

```jsx
<Gallery 
  images={imageArray}
  showLoading={true}
  loadingState="skeleton"
  onImageLoad={(index) => console.log(index)}
/>
```

## Beispiele

## Beispiel 1: Portfolio-Galerie

```
┌─────────────────────────────────────────┐
│ 🎨 Meine Arbeit                         │
├─────────────────────────────────────────┤
│ ┌──────┐ ┌──────┐ ┌──────┐             │
│ │      │ │      │ │      │             │
│ │  🖼️  │ │  🖼️  │ │  🖼️  │             │
│ │      │ │      │ │      │             │
│ └──────┘ └──────┘ └──────┘             │
│ ┌──────┐ ┌──────┐ ┌──────┐             │
│ │      │ │      │ │      │             │
│ │  🖼️  │ │  🖼️  │ │  🖼️  │             │
│ │      │ │      │ │      │             │
│ └──────┘ └──────┘ └──────┘             │
└─────────────────────────────────────────┘
```

## Beispiel 2: Product Gallery

```
┌─────────────────────────────────────────┐
│ 📦 Produktname                          │
├─────────────────────────────────────────┤
│ ┌─────────────────────────────────────┐ │
│ │  🖼️                                │ │
│ │       Hauptbild                    │ │
│ └─────────────────────────────────────┘ │
├─────────────────────────────────────────┤
│ [🖼️] [🖼️] [🖼️] [🖼️]                   │
│   Kleine Vorschaubilder                 │
└─────────────────────────────────────────┘
```

## Beispiel 3: Photo Wall

```
┌─────────────────────────────────────────┐
│ 📸 Fotos                                │
├─────────────────────────────────────────┤
│ ┌────┐ ┌────────┐ ┌──┐                 │
│ │    │ │        │ │  │                 │
│ │ 🖼 │ │  🖼️   │ │🖼│                 │
│ │    │ │        │ │  │                 │
│ └────┘ └────────┘ └──┘                 │
│ ┌────────┐ ┌──┐ ┌────┐                 │
│ │        │ │  │ │    │                 │
│ │  🖼️   │ │🖼│ │ 🖼 │                 │
│ │        │ │  │ │    │                 │
│ └────────┘ └──┘ └────┘                 │
└─────────────────────────────────────────┘
```

## Beispiel 4: Carousel-Slideshow

```
┌─────────────────────────────────────────┐
│ [◀]      🖼️       [▶]                  │
│    Bild 1 von 10                        │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │
│ [●] [○] [○] [○] [○] ...                │
└─────────────────────────────────────────┘
```

## Beispiel 5: Lightbox-Modal

```
┌─────────────────────────────────────────┐
│ [✕]                                     │
│                                         │
│      🖼️                                │
│      (Großansicht)                     │
│                                         │
│   [◀]            [▶]                   │
│                                         │
│    Bild 1 von 20                       │
└─────────────────────────────────────────┘
```

## Beispiel 6: Gallery in Card

```
┌─────────────────────────────────────┐
│ 📸 Reise nach Italien               │
├─────────────────────────────────────┤
│ ┌──────┬──────┬──────┐              │
│ │      │      │      │              │
│ │ 🖼️  │ 🖼️  │ 🖼️  │              │
│ └──────┴──────┴──────┘              │
│                                     │
│ [Alle 12 Fotos anzeigen →]          │
└─────────────────────────────────────┘
```

## Beispiel 7: Social Photo Feed

```
┌─────────────────────────────────────────┐
│ 📷 Neueste Fotos                        │
├─────────────────────────────────────────┤
│ 👤 Alice:  🖼️  🖼️  🖼️                 │
│           ❤️ 23  💬 5                  │
│                                         │
│ 👤 Bob:   🖼️  🖼️                      │
│           ❤️ 45  💬 12                 │
└─────────────────────────────────────────┘
```

## Beispiel 8: Video Thumbnail Gallery

```
┌─────────────────────────────────────────┐
│ 🎥 Letzte Uploads                       │
├─────────────────────────────────────────┤
│ ┌──────┐ ┌──────┐ ┌──────┐             │
│ │[▶]   │ │[▶]   │ │[▶]   │             │
│ │ 🖼️  │ │ 🖼️  │ │ 🖼️  │             │
│ └──────┘ └──────┘ └──────┘             │
│ Video 1  Video 2  Video 3              │
└─────────────────────────────────────────┘
```