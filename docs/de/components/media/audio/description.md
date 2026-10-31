# Audio

## Beschreibung

Ein Audio-Element wiedergibt Audiodateien in verschiedenen Formaten. Es bietet Steuerungsfunktionen wie Play/Pause und Lautstärke.

## Verwendungszweck

- Podcasts wiedergeben
- Musik abspielen
- Sprachnachrichten
- Soundeffekte
- Anleitungsvideos ohne Video

## Format-Varianten

| Format | Beschreibung | Verwendung |
|--------|-------------|------------|
| **MP3** | Standard-Format, weit verbreitet | Alle Audio-Anwendungen |
| **WAV** | Unkomprimiert, hohe Qualität | Hochwertige Audio |
| **OGG** | Open Source | Web-Applikationen |
| **AAC** | Komprimiert, hohe Qualität | Streaming |

## Steuerungs-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `src` | string | Audio-URL |
| `controls` | boolean | Steuerung anzeigen? |
| `autoplay` | boolean | Auto-Wiedergabe? |
| `muted` | boolean | Stumm? |
| `loop` | boolean | Wiederholen? |
| `volume` | number | Lautstärke (0-1) |
| `currentTime` | number | Aktuelle Wiedergabeposition |
| `duration` | number | Gesamtdauer des Audios |

## Features

- Play/Pause-Button
- Lautstärkeregler
- Fortschrittsbalken
- Zeitanzeige (aktueller Zeitpunkt / Gesamtzeit)
- Timeline-Seek (klicken zum Springen)
- Wiedergabeliste

## Hover-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `zoom` | Controls vergrößern sich |
| `opacity` | Deckkraft ändert sich |
| `border` | Rand leuchtet auf |

## Usage Beispiele

### Einfaches Audio

```jsx
<Audio 
  src="/audio/podcast.mp3"
  controls={true}
  volume={0.8}
/>
```

### Autoplay mit Mute

```jsx
<Audio 
  src="/audio/intro.mp3"
  autoplay={true}
  muted={true}
  loop={true}
/>
```

### Mit Wiedergabeliste

```jsx
<Audio 
  playlist={[
    { title: "Episode 1", src: "/audio/episode1.mp3" },
    { title: "Episode 2", src: "/audio/episode2.mp3" },
    { title: "Episode 3", src: "/audio/episode3.mp3" }
  ]}
  controls={true}
/>
```

## Best Practices

- Immer `controls` anzeigen, außer bei Hintergrund-Audio
- `muted` bei `autoplay` verwenden (Browser-Anforderung)
- Alt-Text für Barrierefreiheit bereitstellen
- Verschiedene Formate für Kompatibilität bereitstellen
