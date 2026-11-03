# Audio - Usage

## Simple audio

```jsx
import { AudioPlayer } from '@freesynergy/ui';

<AudioPlayer 
  src="/audio/podcast.mp3"
  controls={true}
  volume={0.8}
/>
```

## Autoplay with mute

```jsx
<AudioPlayer 
  src="/audio/intro.mp3"
  autoplay={true}
  muted={true}
  loop={true}
/>
```

## With a playlist

```jsx
<AudioPlayer 
  playlist={[
    { title: "Episode 1", src: "/audio/episode1.mp3" },
    { title: "Episode 2", src: "/audio/episode2.mp3" },
    { title: "Episode 3", src: "/audio/episode3.mp3" }
  ]}
  controls={true}
  shuffle={true}
/>
```

## With event handlers

```jsx
<AudioPlayer 
  src="/audio/song.mp3"
  onPlay={() => console.log('Start')}
  onPause={() => console.log('Pause')}
  onEnded={() => console.log('End')}
  onTimeUpdate={(time) => console.log(time)}
/>
```

## In chat

```jsx
<Message>
  <Avatar name={sender} />
  <div>
    <AudioPlayer src={audioUrl} size="compact" />
    <span>Voice message</span>
  </div>
</Message>
```

## In a podcast app

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

## Audio list

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

## Examples

## Example 1: podcast app

```
┌─────────────────────────────────────────┐
│ 🎙️ My podcasts                         │
├─────────────────────────────────────────┤
│                                         │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │
│ [▶] Episode 42: AI in the future       │
│     45:30 / 1:23:45                     │
│                                         │
└─────────────────────────────────────────┘
```

## Example 2: music player

```
┌─────────────────────────────────────────┐
│ 🎵 Song Title                          │
│ 🎸 Artist Name                         │
├─────────────────────────────────────────┤
│ [⏮] [◀] [▶] [▶] [⏭]                   │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │
│ 0:00                                      3:45 │
│ [🔊 80%]                               🎵  │
└─────────────────────────────────────────┘
```

## Example 3: voice messages (chat)

```
┌─────────────────────────────────────────┐
│ John:                                   │
│  [▶] 0:15                               │
│                                         │
│ Jane:                                   │
│  [▶] 0:08                               │
└─────────────────────────────────────────┘
```

## Example 4: audio list

```
┌─────────────────────────────────────────┐
│ 📽️ My videos                            │
├─────────────────────────────────────────┤
│ [▶] Tutorial #1  10:30  👁️ 1.2k        │
│ [▶] Tutorial #2  15:45  👁️ 856         │
│ [▶] Tutorial #3  08:20  👁️ 2.3k        │
└─────────────────────────────────────────┘
```

## Example 5: audio player with a playlist

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

## Example 6: audio visualizer

```
┌─────────────────────────────────────────┐
│ 🎵 Live audio                           │
├─────────────────────────────────────────┤
│  ──  ─────  ─  ─────  ───               │
│  ─────  ─  ─────  ─────  ─              │
│  ─  ─────  ─────  ─  ─────              │
│  ─────  ───  ─  ─────  ─                │
├─────────────────────────────────────────┤
│ [⏸] 1:23 / 3:45                        │
└─────────────────────────────────────────┘
```

## Example 7: audio in a list item

```
┌─────────────────────────────────────────┐
│ 📁 Files                                │
├─────────────────────────────────────────┤
│ [🎵] podcast.mp3  45:30                 │
│ [🎵] song.mp3  3:45                     │
│ [🎵] recording.mp3  12:00               │
└─────────────────────────────────────────┘
```

## Example 8: audio with progress

```
┌─────────────────────────────────────────┐
│ 🎧 Audioplay                            │
├─────────────────────────────────────────┤
│ Chapter 1: The beginning               │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │
│ 0:00                                      30:00 │
│ [🔊] [⏮] [◀] [▶] [⏭] [Loop]           │
└─────────────────────────────────────────┘
```
