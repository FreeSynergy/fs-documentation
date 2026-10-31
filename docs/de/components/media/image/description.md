# Bild (Image)

## Beschreibung

Ein Bild-Element zeigt Grafiken, Fotos oder andere visuelle Inhalte an. Es ist eines der grundlegendsten Medien-Elemente in FreeSynergy.

## Verwendungszweck

- Profilfotos anzeigen
- Produktbilder in Katalogen
- Bilder in Artikeln und Dokumenten
- Background-Images
- Thumbnails

## Format-Varianten

| Format | Beschreibung | Verwendung |
|--------|-------------|------------|
| **JPEG/JPG** | Komprimiert, farbenfroh | Fotos, Bilder mit Farben |
| **PNG** | Transparenz, keine Komprimierung | Logos, Icons, Grafiken |
| **GIF** | Animation, Transparenz | Kleine Animationen |
| **WEBP** | Moderne Formate, kleine Dateigröße | Moderne Web-Applikationen |
| **SVG** | Vektorgraphik, skalierbar | Icons, Logos, Grafiken |
| **AVIF** | Neuestes Format, sehr klein | Hochwertige Bilder |

## Größe-Varianten

| Größe | Verwendung |
|-------|------------|
| **Thumbnail** (100x100) | Listen, Grids |
| **Small** (200x200) | Profile, kleine Karten |
| **Medium** (400x400) | Cards, Panels |
| **Large** (800x800) | Featured-Images |
| **Full** (1920+) | Hero-Sectionen, Backgrounds |

## Styling-Attribute

| Attribut | Wert | Beschreibung |
|----------|------|--------------|
| `src` | string | Bild-URL |
| `alt` | string | Alt-Text für Barrierefreiheit |
| `size` | enum | `thumbnail`, `small`, `medium`, `large`, `full` |
| `shape` | enum | `rectangular`, `circular`, `pill` |
| `fit` | enum | `cover`, `contain`, `fill` |
| `loading` | enum | `lazy`, `eager` |
| `interactive` | boolean | Ist das Bild klickbar? |

## Hover-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `zoom` | Bild vergrößert sich |
| `opacity` | Deckkraft ändert sich |
| `border` | Rand leuchtet auf |
| `shadow` | Schatten wird stärker |

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
