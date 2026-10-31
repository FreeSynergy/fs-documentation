# Bild (Image) - Aussehen

## Grundlayout

Bilder werden in verschiedenen Formen und Größen angezeigt, oft mit Hover-Effekten und Loading-Zuständen.

## Form-Varianten (CSS)

```css
/* Rectangular (Rechteckig) - Standard */
.image-rectangular {
  border-radius: 4px;
}

/* Circular (Rund) */
.image-circular {
  border-radius: 50%;
}

/* Pill (Pillenform) */
.image-pill {
  border-radius: 999px;
}
```

## Größe-Varianten

| Größe | Breite/Höhe | Verwendung |
|-------|-------------|------------|
| Thumbnail | 100px | Listen, Grids |
| Small | 200px | Profile, kleine Karten |
| Medium | 400px | Cards, Panels |
| Large | 600px | Featured-Images |
| Full | 1920px+ | Hero-Sectionen, Backgrounds |

## Hover-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `zoom` | Bild vergrößert sich (1.1x) |
| `overlay` | Overlay mit Info/Icons |
| `border` | Rand leuchtet auf |
| `opacity` | Deckkraft ändert sich |

## Loading-Zustand

### Skeleton (Platzhalter)
```
┌────────────────────────┐
│ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ │
│ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ │
│ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ │
└────────────────────────┘
```

### Spinner (Ladeanimation)
```
┌────────────────────────┐
│                        │
│      🔄                │
│                        │
└────────────────────────┘
```

## Fit-Mode-Varianten

| Mode | Beschreibung | Verwendung |
|------|-------------|------------|
| `cover` | Bild füllt Container, überschüssiger Bereich abgeschnitten | Hero-Bilder |
| `contain` | Bild passt komplett in Container, eventuell Rand | Produktbilder |
| `fill` | Bild wird gestreckt, um Container zu füllen | Hintergrundbilder |

## Lazy Loading

```jsx
<Image 
  src="/images/photo.jpg" 
  size="medium" 
  loading="lazy"
  alt="Beschreibung"
/>
```

## Background-Image

```jsx
<Card 
  backgroundImage="/images/banner.jpg"
  backgroundSize="cover"
  backgroundPosition="center"
/>
```

## Responsive Images

```jsx
<Image 
  src="/images/photo.jpg"
  responsive={true}
  srcSet={[
    { size: '320w', src: '/images/photo-small.jpg' },
    { size: '640w', src: '/images/photo-medium.jpg' },
    { size: '1280w', src: '/images/photo-large.jpg' }
  ]}
/>
```

## Border & Shadow

| Variant | Beschreibung |
|---------|--------------|
| `default` | Kein Rand, leichter Schatten |
| `outlined` | Heller Rand, kein Schatten |
| `elevated` | Starkes Shadow, keine Border |
| `rounded` | Abgerundete Ecken (8px) |
