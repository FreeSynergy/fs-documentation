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
