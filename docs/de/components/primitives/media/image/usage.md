# Image - Verwendung

## Ein einfaches Bild

```jsx
<Image
  src="/images/photo.jpg"
  size="medium"
  alt="Beschreibung"
/>
```

## Rundes Bild

```jsx
<Image
  src="/images/profile.jpg"
  shape="circular"
  size="large"
  alt="Profilbild"
/>
```

## Mit Hover-Effekt

```jsx
<Image
  src="/images/product.jpg"
  interactive={true}
  hoverEffect="zoom"
  onClick={() => openProductDetails()}
/>
```

## Verzögertes Laden

```jsx
<Image
  src="/images/large-photo.jpg"
  size="full"
  loading="lazy"
  alt="Großes Foto"
/>
```

## Hintergrundbild

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

## Responsives Bild

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

## Mit Ersatzbild

```jsx
<Image
  src="/images/optional.jpg"
  alt="Optional"
  onErrorFallback="/images/default.jpg"
/>
```

## In einem Listenelement

```jsx
<ListItem>
  <Image src={item.image} shape="circular" size="small" />
  <span>{item.title}</span>
</ListItem>
```

## Rasteranordnung

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

## Beispiel 1: Profilbilder in einer Liste

```
┌─────────────────────────────────────────┐
│ 🧑‍🤝‍🧑 Teilnehmende                       │
├─────────────────────────────────────────┤
│ 🖼️ Alice                              │
│ 🖼️ Bob                                │
│ 🖼️ Carol                              │
│ 🖼️ Dave                               │
└─────────────────────────────────────────┘
```

## Beispiel 2: Produktgalerie

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
│      Hero-Bild                          │
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
│ Sehr schönes Foto! ❤️ 23 💬 5          │
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

## Beispiel 6: Avatar-Raster

```
┌─────────────────────────────────────┐
│ 👥 Team                             │
├─────────────────────────────────────┤
│ 🖼️  🖼️  🖼️  🖼️                    │
│ 🖼️  🖼️  🖼️  🖼️                    │
│ 🖼️  🖼️  🖼️  🖼️                    │
└─────────────────────────────────────┘
```

## Beispiel 7: Galerie mit Lightbox

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

## Beispiel 8: Hintergrundbild

```
┌─────────────────────────────────────┐
│                                     │
│      🖼️ (Hintergrundbild)           │
│      Text über dem Bild            │
│                                     │
└─────────────────────────────────────┘
```
