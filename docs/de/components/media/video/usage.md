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

## Autoplay mit Mute

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

## Responsive Video

```jsx
<Video 
  src="/videos/demo.mp4"
  responsive={true}
  aspectRatio="16/9"
  controls={true}
/>
```

## In Card

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

## mit Event-Handlern

```jsx
<Video 
  src="/videos/speech.mp4"
  onPlay={() => console.log('Start')}
  onPause={() => console.log('Pause')}
  onEnded={() => console.log('Ende')}
  onTimeUpdate={(time) => console.log(time)}
/>
```

## In Modal

```jsx
<Modal>
  <Video 
    src="/videos/presentation.mp4"
    controls={true}
    autoplay={true}
  />
</Modal>
```
