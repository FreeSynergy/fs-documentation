# Gallery - Verwendung

## Einfache Raster-Galerie

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

## In einem Modal

```jsx
<Modal>
  <Gallery
    images={selectedAlbum.images}
    lightBox={true}
    showNavigation={true}
  />
</Modal>
```

## Responsive Galerie

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

## Galerie mit Ladeanzeige

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
│ 🎨 Meine Arbeiten                       │
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

## Beispiel 2: Produktgalerie

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
│   kleine Vorschaubilder                 │
└─────────────────────────────────────────┘
```

## Beispiel 3: Fotowand

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

## Beispiel 4: Carousel-Diashow

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
│      (große Ansicht)                    │
│                                         │
│   [◀]            [▶]                    │
│                                         │
│    Bild 1 von 20                        │
└─────────────────────────────────────────┘
```

## Beispiel 6: Galerie in einer Karte

```
┌─────────────────────────────────────┐
│ 📸 Reise nach Italien               │
├─────────────────────────────────────┤
│ ┌──────┬──────┬──────┐              │
│ │      │      │      │              │
│ │ 🖼️  │ 🖼️  │ 🖼️  │              │
│ └──────┴──────┴──────┘              │
│                                     │
│ [alle 12 Fotos anzeigen →]          │
└─────────────────────────────────────┘
```

## Beispiel 7: Foto-Feed in sozialen Medien

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

## Beispiel 8: Video-Vorschaugalerie

```
┌─────────────────────────────────────────┐
│ 🎥 Neueste Uploads                      │
├─────────────────────────────────────────┤
│ ┌──────┐ ┌──────┐ ┌──────┐             │
│ │[▶]   │ │[▶]   │ │[▶]   │             │
│ │ 🖼️  │ │ 🖼️  │ │ 🖼️  │             │
│ └──────┘ └──────┘ └──────┘             │
│ Video 1  Video 2  Video 3              │
└─────────────────────────────────────────┘
```
