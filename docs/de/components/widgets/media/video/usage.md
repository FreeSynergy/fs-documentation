# Video - Verwendung

## Einfaches Video

```jsx
<Video 
  src="/videos/demo.mp4"
  controls={true}
  poster="/images/poster.jpg"
  alt="Demo-Video"
/>
```

## Automatisch abspielen, stumm

```jsx
<Video 
  src="/videos/background.mp4"
  autoplay={true}
  muted={true}
  loop={true}
  playsInline={true}
/>
```

## Mit Untertiteln

```jsx
<Video 
  src="/videos/lecture.mp4"
  controls={true}
  captions="/subtitles/de.srt"
/>
```

## Mit Playlist

```jsx
<Video 
  playlist={[
    { title: "Video 1", src: "/videos/video1.mp4" },
    { title: "Video 2", src: "/videos/video2.mp4" },
    { title: "Video 3", src: "/videos/video3.mp4" }
  ]}
  controls={true}
  shuffle={true}
/>
```

## Responsives Video

```jsx
<Video 
  src="/videos/demo.mp4"
  responsive={true}
  aspectRatio="16/9"
  controls={true}
/>
```

## In einer Karte

```jsx
<Card>
  <Video 
    src="/videos/product-demo.mp4"
    size="small"
    controls={true}
  />
  <h3>Produkt-Demo</h3>
  <p>Beschreibung</p>
</Card>
```

## Mit Ereignis-Handlern

```jsx
<Video 
  src="/videos/speech.mp4"
  onPlay={() => console.log('Start')}
  onPause={() => console.log('Pause')}
  onEnded={() => console.log('Ende')}
  onTimeUpdate={(time) => console.log(time)}
/>
```

## In einem Modal

```jsx
<Modal>
  <Video 
    src="/videos/presentation.mp4"
    controls={true}
    autoplay={true}
  />
</Modal>
```

## Beispiele

## Beispiel 1: Videoplayer

```
┌─────────────────────────────────────────┐
│ 🎬 Videotitel                           │
├─────────────────────────────────────────┤
│                                         │
│      🖼️                                │
│      (Videoanzeige)                     │
│                                         │
│ [⏮] [◀] [▶] [▶] [⏭]                   │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │
│ [🔊 80%]  0:00                3:45      │
└─────────────────────────────────────────┘
```

## Beispiel 2: Video-Feed

```
┌─────────────────────────────────────────┐
│ 📽️ Neueste Videos                       │
├─────────────────────────────────────────┤
│ 🖼️ Video 1  10:30  👁️ 1.2k            │
│ 🖼️ Video 2  15:45  👁️ 856             │
│ 🖼️ Video 3  08:20  👁️ 2.3k            │
└─────────────────────────────────────────┘
```

## Beispiel 3: Video in einer Karte

```
┌─────────────────────────────────────┐
│ 🎥 Tutorial                         │
├─────────────────────────────────────┤
│                                     │
│      🖼️                            │
│      (Video)                        │
│                                     │
│ Titel des Tutorials                 │
│ Beschreibung...                     │
│                                     │
│ [▶] Abspielen                       │
└─────────────────────────────────────┘
```

## Beispiel 4: Videogalerie

```
┌─────────────────────────────────────┐
│ 📺 Meine Videos                     │
├─────────────────────────────────────┤
│ ┌──────┬──────┬──────┐              │
│ │[▶]   │ │[▶]   │ │[▶]   │          │
│ │ 🖼️  │ │ 🖼️  │ │ 🖼️  │          │
│ └──────┘ └──────┘ └──────┘          │
│ Video 1  Video 2  Video 3           │
└─────────────────────────────────────┘
```

## Beispiel 5: Hero-Video

```
┌─────────────────────────────────────┐
│                                     │
│      🖼️ (Hintergrundvideo)          │
│                                     │
│      Titel                          │
│      Beschreibung                   │
│                                     │
│      [▶] Abspielen                  │
│                                     │
└─────────────────────────────────────┘
```

## Beispiel 6: Video mit Untertiteln

```
┌─────────────────────────────────────┐
│ 📺 Video mit Untertiteln            │
├─────────────────────────────────────┤
│                                     │
│      🖼️                            │
│      [Deutsch]                      │
│                                     │
│ [▶]  ━━━━━━━━━━━━━━━━━  0:00 / 10:00│
└─────────────────────────────────────┘
```

## Beispiel 7: Video-Playlist

```
┌─────────────────────────────────────┐
│ 🎬 Playlist                         │
├─────────────────────────────────────┤
│ 1. [▶] Video 1  5:30  (aktuell)     │
│ 2. [⏸] Video 2  7:15                │
│ 3. [⏸] Video 3  4:20                │
│ 4. [⏸] Video 4  8:45                │
├─────────────────────────────────────┤
│ [🔄] [🔀] [🔊 75%] 0:00 / 5:30      │
└─────────────────────────────────────┘
```

## Beispiel 8: Video im Chat

```
┌─────────────────────────────────────┐
│ John:                               │
│ [▶] 0:15                            │
│                                     │
│ Jane:                               │
│ [▶] 0:08                            │
└─────────────────────────────────────┘
```
