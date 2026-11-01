# Bild (Image) - Verwendung

## Einfaches Bild

```jsx
<Image 
  src="/images/photo.jpg" 
  size="medium" 
  alt="Beschreibung"
/>
```

## Circular Image

```jsx
<Image 
  src="/images/profile.jpg" 
  shape="circular" 
  size="large"
  alt="Profilbild"
/>
```

## mit Hover-Effekt

```jsx
<Image 
  src="/images/product.jpg" 
  interactive={true}
  hoverEffect="zoom"
  onClick={() => openProductDetails()}
/>
```

## Lazy Loading

```jsx
<Image 
  src="/images/large-photo.jpg" 
  size="full" 
  loading="lazy"
  alt="Großes Foto"
/>
```

## Background Image

```jsx
<Card 
  backgroundImage="/images/banner.jpg"
  backgroundSize="cover"
  backgroundPosition="center"
>
  <h2>Titel</h2>
  <p>Beschreibung</p>
</Card>
```

## Responsive Image

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

## mit Fallback

```jsx
<Image 
  src="/images/optional.jpg"
  alt="Optional"
  onErrorFallback="/images/default.jpg"
/>
```

## In List-Item

```jsx
<ListItem>
  <Image src={item.image} shape="circular" size="small" />
  <span>{item.title}</span>
</ListItem>
```

## Grid-Layout

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

## Beispiele

## Beispiel 1: Profil-Bilder in Liste

```
┌─────────────────────────────────────────┐
│ 🧑‍🤝‍🧑 Teilnehmer                       │
├─────────────────────────────────────────┤
│ 🖼️ Alice                              │
│ 🖼️ Bob                                │
│ 🖼️ Carol                              │
│ 🖼️ Dave                               │
└─────────────────────────────────────────┘
```

## Beispiel 2: Produkt-Galerie

```
┌─────────────────────────────────────────┐
│ 🛍️ Produktdetail                        │
├─────────────────────────────────────────┤
│ ┌─────────────────────────────────────┐ │
│ │                                     │ │
│ │         🖼️                         │ │
│ │         Produktbild                 │ │
│ │                                     │ │
│ └─────────────────────────────────────┘ │
│                                         │
│ [🖼️] [🖼️] [🖼️] [🖼️]                   │
│ Vorschaubilder                          │
└─────────────────────────────────────────┘
```

## Beispiel 3: Hero-Bild

```
┌─────────────────────────────────────────┐
│                                         │
│      🖼️                                │
│      Hero-Bild                         │
│                                         │
│     Titel                               │
│     Beschreibung                        │
│                                         │
└─────────────────────────────────────────┘
```

## Beispiel 4: Feed mit Bildern

```
┌─────────────────────────────────────────┐
│ 📱 Neueste Beiträge                     │
├─────────────────────────────────────────┤
│ 👤 Alice                                │
│ 🖼️                                    │
│ Sehr schönes Bild! ❤️ 23 💬 5          │
│                                         │
│ 👤 Bob                                  │
│ 🖼️  🖼️                                │
│ Urlaubserinnerungen ❤️ 45 💬 12        │
└─────────────────────────────────────────┘
```

## Beispiel 5: Card mit Bild

```
┌─────────────────────────────────────┐
│ 📝 Artikel                          │
├─────────────────────────────────────┤
│ 🖼️                                │
│                                     │
│ Titel des Artikels                  │
│ Kurze Beschreibung...               │
│                                     │
│ [Weiterlesen →]                     │
└─────────────────────────────────────┘
```

## Beispiel 6: Avatar-Grid

```
┌─────────────────────────────────────┐
│ 👥 Team                             │
├─────────────────────────────────────┤
│ 🖼️  🖼️  🖼️  🖼️                    │
│ 🖼️  🖼️  🖼️  🖼️                    │
│ 🖼️  🖼️  🖼️  🖼️                    │
└─────────────────────────────────────┘
```

## Beispiel 7: Gallery mit Lightbox

```
┌─────────────────────────────────────┐
│ 📸 Fotos                            │
├─────────────────────────────────────┤
│ ┌──────┬──────┬──────┐              │
│ │      │      │      │              │
│ │ 🖼️  │ 🖼️  │ 🖼️  │              │
│ └──────┴──────┴──────┘              │
│ [Alle 24 Fotos anzeigen]            │
└─────────────────────────────────────┘
```

## Beispiel 8: Background Image

```
┌─────────────────────────────────────┐
│                                     │
│      🖼️ (Hintergrundbild)           │
│      Text über dem Bild             │
│                                     │
└─────────────────────────────────────┘
```
