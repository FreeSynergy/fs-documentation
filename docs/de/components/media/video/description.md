# Video

## Beschreibung

Ein Video-Element wiedergibt Videos in verschiedenen Formaten. Es bietet Steuerungsfunktionen wie Play/Pause, Volume und Fullscreen.

## Verwendungszweck

- Anleitungsvideos anzeigen
- Produktvideos präsentieren
- Video-Kommentare wiedergeben
- Live-Streams anzeigen
- Hintergrund-Videos

## Format-Varianten

| Format | Beschreibung | Verwendung |
|--------|-------------|------------|
| **MP4** | Standard-Format, weit verbreitet | Alle Video-Anwendungen |
| **WEBM** | Open Source, kleine Dateigröße | Web-Applikationen |
| **OGV** | Open Source-Format | Alternatives Format |
| **MKV** |容器-Format, viele Streams | Hochwertige Videos |

## Größe-Varianten

| Größe | Verwendung |
|-------|------------|
| **Small** (320px) | Inline-Videos, Kommentare |
| **Medium** (640px) | Cards, Panels |
| **Large** (1280px) | Featured-Videos |
| **Full** (1920px) | Hero-Videos, Fullscreen |

## Steuerungs-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `src` | string | Video-URL |
| `controls` | boolean | Steuerung anzeigen? |
| `autoplay` | boolean | Auto-Wiedergabe? |
| `muted` | boolean | Stumm? |
| `loop` | boolean | Wiederholen? |
| `poster` | string | Vorschaubild |
| `playsInline` | boolean | Inline-Wiedergabe (Mobile) |
| `volume` | number | Lautstärke (0-1) |

## Features

- Play/Pause-Button
- Lautstärkeregler
- Fortschrittsbalken
- Vollbild-Modus
-Untertitel
- Qualitätsauswahl
- Geschwindigkeitseinstellung

## Responsive

```jsx
<Video 
  src="/videos/demo.mp4"
  responsive={true}
  controls={true}
  poster="/images/poster.jpg"
/>
```

## autoplay mit Mute

```jsx
<Video 
  src="/videos/background.mp4"
  autoplay={true}
  muted={true}
  loop={true}
  playsInline={true}
/>
```
