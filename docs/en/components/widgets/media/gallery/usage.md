# Gallery - Usage

## Simple grid gallery

```jsx
<Gallery
  images={[
    { src: "/images/photo1.jpg", alt: "Image 1" },
    { src: "/images/photo2.jpg", alt: "Image 2" },
    { src: "/images/photo3.jpg", alt: "Image 3" }
  ]}
  columns={3}
  responsive={true}
/>
```

## Lightbox gallery

```jsx
<Gallery
  images={imageArray}
  lightBox={true}
  showThumbnails={true}
  onClickImage={(index) => openLightbox(index)}
/>
```

## Carousel gallery

```jsx
<Gallery
  images={imageArray}
  variant="carousel"
  autoplay={true}
  interval={5000}
  loop={true}
/>
```

## Masonry gallery

```jsx
<Gallery
  images={imageArray}
  variant="masonry"
  gap={20}
  responsive={true}
/>
```

## With a filter

```jsx
<Gallery
  images={imageArray}
  categoryFilter={selectedCategory}
  showFilter={true}
  filterOptions={categories}
  onFilterChange={handleFilterChange}
/>
```

## In a modal

```jsx
<Modal>
  <Gallery
    images={selectedAlbum.images}
    lightBox={true}
    showNavigation={true}
  />
</Modal>
```

## Responsive gallery

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

## Gallery with progress

```jsx
<Gallery
  images={imageArray}
  showLoading={true}
  loadingState="skeleton"
  onImageLoad={(index) => console.log(index)}
/>
```

## Examples

## Example 1: portfolio gallery

```
┌─────────────────────────────────────────┐
│ 🎨 My work                              │
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

## Example 2: product gallery

```
┌─────────────────────────────────────────┐
│ 📦 Product name                         │
├─────────────────────────────────────────┤
│ ┌─────────────────────────────────────┐ │
│ │  🖼️                                │ │
│ │       main image                   │ │
│ └─────────────────────────────────────┘ │
├─────────────────────────────────────────┤
│ [🖼️] [🖼️] [🖼️] [🖼️]                   │
│   small preview images                  │
└─────────────────────────────────────────┘
```

## Example 3: photo wall

```
┌─────────────────────────────────────────┐
│ 📸 Photos                               │
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

## Example 4: carousel slideshow

```
┌─────────────────────────────────────────┐
│ [◀]      🖼️       [▶]                  │
│    image 1 of 10                        │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │
│ [●] [○] [○] [○] [○] ...                │
└─────────────────────────────────────────┘
```

## Example 5: lightbox modal

```
┌─────────────────────────────────────────┐
│ [✕]                                     │
│                                         │
│      🖼️                                │
│      (large view)                      │
│                                         │
│   [◀]            [▶]                   │
│                                         │
│    image 1 of 20                       │
└─────────────────────────────────────────┘
```

## Example 6: gallery in a card

```
┌─────────────────────────────────────┐
│ 📸 Trip to Italy                    │
├─────────────────────────────────────┤
│ ┌──────┬──────┬──────┐              │
│ │      │      │      │              │
│ │ 🖼️  │ 🖼️  │ 🖼️  │              │
│ └──────┴──────┴──────┘              │
│                                     │
│ [show all 12 photos →]              │
└─────────────────────────────────────┘
```

## Example 7: social photo feed

```
┌─────────────────────────────────────────┐
│ 📷 Latest photos                        │
├─────────────────────────────────────────┤
│ 👤 Alice:  🖼️  🖼️  🖼️                 │
│           ❤️ 23  💬 5                  │
│                                         │
│ 👤 Bob:   🖼️  🖼️                      │
│           ❤️ 45  💬 12                 │
└─────────────────────────────────────────┘
```

## Example 8: video thumbnail gallery

```
┌─────────────────────────────────────────┐
│ 🎥 Recent uploads                       │
├─────────────────────────────────────────┤
│ ┌──────┐ ┌──────┐ ┌──────┐             │
│ │[▶]   │ │[▶]   │ │[▶]   │             │
│ │ 🖼️  │ │ 🖼️  │ │ 🖼️  │             │
│ └──────┘ └──────┘ └──────┘             │
│ Video 1  Video 2  Video 3              │
└─────────────────────────────────────────┘
```
