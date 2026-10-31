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

## Autoplay mit Mute

```jsx
<AudioPlayer 
  src="/audio/intro.mp3"
  autoplay={true}
  muted={true}
  loop={true}
/>
```

## Mit Wiedergabeliste

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

## Mit Event-Handlern

```jsx
<AudioPlayer 
  src="/audio/song.mp3"
  onPlay={() => console.log('Start')}
  onPause={() => console.log('Pause')}
  onEnded={() => console.log('Ende')}
  onTimeUpdate={(time) => console.log(time)}
/>
```

## In Chat

```jsx
<Message>
  <Avatar name={sender} />
  <div>
    <AudioPlayer src={audioUrl} size="compact" />
    <span>Audio-Nachricht</span>
  </div>
</Message>
```

## In Podcast-App

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

## Audio-Liste

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
