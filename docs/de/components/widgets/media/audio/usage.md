# Audio - Verwendung

## Einfaches Audio

```jsx
import { AudioPlayer } from '@freesynergy/ui';

<AudioPlayer 
  src="/audio/podcast.mp3"
  controls={true}
  volume={0.8}
/>
```

## Automatisch abspielen, stumm

```jsx
<AudioPlayer 
  src="/audio/intro.mp3"
  autoplay={true}
  muted={true}
  loop={true}
/>
```

## Mit Playlist

```jsx
<AudioPlayer 
  playlist={[
    { title: "Folge 1", src: "/audio/episode1.mp3" },
    { title: "Folge 2", src: "/audio/episode2.mp3" },
    { title: "Folge 3", src: "/audio/episode3.mp3" }
  ]}
  controls={true}
  shuffle={true}
/>
```

## Mit Ereignis-Handlern

```jsx
<AudioPlayer 
  src="/audio/song.mp3"
  onPlay={() => console.log('Start')}
  onPause={() => console.log('Pause')}
  onEnded={() => console.log('Ende')}
  onTimeUpdate={(time) => console.log(time)}
/>
```

## Im Chat

```jsx
<Message>
  <Avatar name={sender} />
  <div>
    <AudioPlayer src={audioUrl} size="compact" />
    <span>Sprachnachricht</span>
  </div>
</Message>
```

## In einer Podcast-App

```jsx
<PodcastEpisode episode={currentEpisode}>
  <AudioPlayer 
    src={episode.audioUrl}
    controls={true}
    showVisualizer={true}
    visualizerStyle="waves"
  />
</PodcastEpisode>
```

## Audioliste

```jsx
<AudioList>
  {audios.map((audio, index) => (
    <AudioItem 
      key={index}
      title={audio.title}
      artist={audio.artist}
      cover={audio.cover}
      isActive={index === currentIndex}
      onClick={() => playAudio(index)}
    />
  ))}
</AudioList>
```

## Beispiele

## Beispiel 1: Podcast-App

```
┌─────────────────────────────────────────┐
│ 🎙️ Meine Podcasts                      │
├─────────────────────────────────────────┤
│                                         │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │
│ [▶] Folge 42: KI in der Zukunft        │
│     45:30 / 1:23:45                     │
│                                         │
└─────────────────────────────────────────┘
```

## Beispiel 2: Musikplayer

```
┌─────────────────────────────────────────┐
│ 🎵 Titel des Songs                      │
│ 🎸 Name des Künstlers                   │
├─────────────────────────────────────────┤
│ [⏮] [◀] [▶] [▶] [⏭]                   │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │
│ 0:00                                      3:45 │
│ [🔊 80%]                               🎵  │
└─────────────────────────────────────────┘
```

## Beispiel 3: Sprachnachrichten (Chat)

```
┌─────────────────────────────────────────┐
│ John:                                   │
│  [▶] 0:15                               │
│                                         │
│ Jane:                                   │
│  [▶] 0:08                               │
└─────────────────────────────────────────┘
```

## Beispiel 4: Audioliste

```
┌─────────────────────────────────────────┐
│ 📽️ Meine Videos                         │
├─────────────────────────────────────────┤
│ [▶] Tutorial #1  10:30  👁️ 1.2k        │
│ [▶] Tutorial #2  15:45  👁️ 856         │
│ [▶] Tutorial #3  08:20  👁️ 2.3k        │
└─────────────────────────────────────────┘
```

## Beispiel 5: Audioplayer mit Playlist

```
┌─────────────────────────────────────────┐
│ 🎵 Playlist                             │
├─────────────────────────────────────────┤
│ 1. Song A  [▶]                          │
│ 2. Song B  [⏸]                          │
│ 3. Song C  [⏸]                          │
│ 4. Song D  [⏸]                          │
│ 5. Song E  [⏸]                          │
├─────────────────────────────────────────┤
│ [🔄] [🔀] [🔊 75%] 0:00 / 3:45         │
└─────────────────────────────────────────┘
```

## Beispiel 6: Audio-Visualisierung

```
┌─────────────────────────────────────────┐
│ 🎵 Live-Audio                           │
├─────────────────────────────────────────┤
│  ──  ─────  ─  ─────  ───               │
│  ─────  ─  ─────  ─────  ─              │
│  ─  ─────  ─────  ─  ─────              │
│  ─────  ───  ─  ─────  ─                │
├─────────────────────────────────────────┤
│ [⏸] 1:23 / 3:45                        │
└─────────────────────────────────────────┘
```

## Beispiel 7: Audio in einem Listeneintrag

```
┌─────────────────────────────────────────┐
│ 📁 Dateien                              │
├─────────────────────────────────────────┤
│ [🎵] podcast.mp3  45:30                 │
│ [🎵] song.mp3  3:45                     │
│ [🎵] recording.mp3  12:00               │
└─────────────────────────────────────────┘
```

## Beispiel 8: Audio mit Fortschritt

```
┌─────────────────────────────────────────┐
│ 🎧 Audiowiedergabe                      │
├─────────────────────────────────────────┤
│ Kapitel 1: Der Anfang                   │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │
│ 0:00                                      30:00 │
│ [🔊] [⏮] [◀] [▶] [⏭] [Loop]           │
└─────────────────────────────────────────┘
```
