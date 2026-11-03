# Image - Usage

## A simple image

```jsx
<Image
  src="/images/photo.jpg"
  size="medium"
  alt="Description"
/>
```

## Circular image

```jsx
<Image
  src="/images/profile.jpg"
  shape="circular"
  size="large"
  alt="Profile picture"
/>
```

## With a hover effect

```jsx
<Image
  src="/images/product.jpg"
  interactive={true}
  hoverEffect="zoom"
  onClick={() => openProductDetails()}
/>
```

## Lazy loading

```jsx
<Image
  src="/images/large-photo.jpg"
  size="full"
  loading="lazy"
  alt="Large photo"
/>
```

## Background image

```jsx
<Card
  backgroundImage="/images/banner.jpg"
  backgroundSize="cover"
  backgroundPosition="center"
>
  <h2>Title</h2>
  <p>Description</p>
</Card>
```

## Responsive image

```jsx
<Image
  src="/images/photo.jpg"
  responsive={true}
  srcSet={[
    { size: '320w', src: '/images/photo-small.jpg' },
    { size: '640w', src: '/images/photo-medium.jpg' },
    { size: '1280w', src: '/images/photo-large.jpg' }
  ]}
  sizes="(max-width: 640px) 100vw, (max-width: 1280px) 50vw, 33vw"
/>
```

## With a fallback

```jsx
<Image
  src="/images/optional.jpg"
  alt="Optional"
  onErrorFallback="/images/default.jpg"
/>
```

## In a list item

```jsx
<ListItem>
  <Image src={item.image} shape="circular" size="small" />
  <span>{item.title}</span>
</ListItem>
```

## Grid layout

```jsx
<ImageGrid columns={3} gap={16}>
  {images.map((img, index) => (
    <Image
      key={index}
      src={img.src}
      alt={img.alt}
      fit="cover"
      onClick={() => openLightbox(index)}
    />
  ))}
</ImageGrid>
```

## Examples

## Example 1: profile pictures in a list

```
┌─────────────────────────────────────────┐
│ 🧑‍🤝‍🧑 Participants                      │
├─────────────────────────────────────────┤
│ 🖼️ Alice                              │
│ 🖼️ Bob                                │
│ 🖼️ Carol                              │
│ 🖼️ Dave                               │
└─────────────────────────────────────────┘
```

## Example 2: product gallery

```
┌─────────────────────────────────────────┐
│ 🛍️ Product detail                       │
├─────────────────────────────────────────┤
│ ┌─────────────────────────────────────┐ │
│ │                                     │ │
│ │         🖼️                         │ │
│ │         product image               │ │
│ │                                     │ │
│ └─────────────────────────────────────┘ │
│                                         │
│ [🖼️] [🖼️] [🖼️] [🖼️]                   │
│ thumbnails                              │
└─────────────────────────────────────────┘
```

## Example 3: hero image

```
┌─────────────────────────────────────────┐
│                                         │
│      🖼️                                │
│      hero image                        │
│                                         │
│     Title                               │
│     Description                         │
│                                         │
└─────────────────────────────────────────┘
```

## Example 4: feed with images

```
┌─────────────────────────────────────────┐
│ 📱 Latest posts                         │
├─────────────────────────────────────────┤
│ 👤 Alice                                │
│ 🖼️                                    │
│ Very nice photo! ❤️ 23 💬 5            │
│                                         │
│ 👤 Bob                                  │
│ 🖼️  🖼️                                │
│ Holiday memories ❤️ 45 💬 12           │
└─────────────────────────────────────────┘
```

## Example 5: card with an image

```
┌─────────────────────────────────────┐
│ 📝 Article                          │
├─────────────────────────────────────┤
│ 🖼️                                │
│                                     │
│ Title of the article                │
│ Short description...                │
│                                     │
│ [Read more →]                       │
└─────────────────────────────────────┘
```

## Example 6: avatar grid

```
┌─────────────────────────────────────┐
│ 👥 Team                             │
├─────────────────────────────────────┤
│ 🖼️  🖼️  🖼️  🖼️                    │
│ 🖼️  🖼️  🖼️  🖼️                    │
│ 🖼️  🖼️  🖼️  🖼️                    │
└─────────────────────────────────────┘
```

## Example 7: gallery with a lightbox

```
┌─────────────────────────────────────┐
│ 📸 Photos                           │
├─────────────────────────────────────┤
│ ┌──────┬──────┬──────┐              │
│ │      │      │      │              │
│ │ 🖼️  │ 🖼️  │ 🖼️  │              │
│ └──────┴──────┴──────┘              │
│ [Show all 24 photos]                │
└─────────────────────────────────────┘
```

## Example 8: background image

```
┌─────────────────────────────────────┐
│                                     │
│      🖼️ (background image)          │
│      text over the image            │
│                                     │
└─────────────────────────────────────┘
```
