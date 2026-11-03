# Video - Usage

## Simple video

```jsx
<Video 
  src="/videos/demo.mp4"
  controls={true}
  poster="/images/poster.jpg"
  alt="Demo video"
/>
```

## Autoplay with mute

```jsx
<Video 
  src="/videos/background.mp4"
  autoplay={true}
  muted={true}
  loop={true}
  playsInline={true}
/>
```

## With subtitles

```jsx
<Video 
  src="/videos/lecture.mp4"
  controls={true}
  captions="/subtitles/de.srt"
/>
```

## With a playlist

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

## Responsive video

```jsx
<Video 
  src="/videos/demo.mp4"
  responsive={true}
  aspectRatio="16/9"
  controls={true}
/>
```

## In a card

```jsx
<Card>
  <Video 
    src="/videos/product-demo.mp4"
    size="small"
    controls={true}
  />
  <h3>Product demo</h3>
  <p>Description</p>
</Card>
```

## With event handlers

```jsx
<Video 
  src="/videos/speech.mp4"
  onPlay={() => console.log('Start')}
  onPause={() => console.log('Pause')}
  onEnded={() => console.log('End')}
  onTimeUpdate={(time) => console.log(time)}
/>
```

## In a modal

```jsx
<Modal>
  <Video 
    src="/videos/presentation.mp4"
    controls={true}
    autoplay={true}
  />
</Modal>
```

## Examples

## Example 1: video player

```
┌─────────────────────────────────────────┐
│ 🎬 Video title                          │
├─────────────────────────────────────────┤
│                                         │
│      🖼️                                │
│      (video display)                    │
│                                         │
│ [⏮] [◀] [▶] [▶] [⏭]                   │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │
│ [🔊 80%]  0:00                3:45      │
└─────────────────────────────────────────┘
```

## Example 2: video feed

```
┌─────────────────────────────────────────┐
│ 📽️ Latest videos                        │
├─────────────────────────────────────────┤
│ 🖼️ Video 1  10:30  👁️ 1.2k            │
│ 🖼️ Video 2  15:45  👁️ 856             │
│ 🖼️ Video 3  08:20  👁️ 2.3k            │
└─────────────────────────────────────────┘
```

## Example 3: video in a card

```
┌─────────────────────────────────────┐
│ 🎥 Tutorial                         │
├─────────────────────────────────────┤
│                                     │
│      🖼️                           │
│      (video)                        │
│                                     │
│ Title of the tutorial               │
│ Description...                      │
│                                     │
│ [▶] Play                            │
└─────────────────────────────────────┘
```

## Example 4: video gallery

```
┌─────────────────────────────────────┐
│ 📺 My videos                        │
├─────────────────────────────────────┤
│ ┌──────┬──────┬──────┐              │
│ │[▶]   │ │[▶]   │ │[▶]   │          │
│ │ 🖼️  │ │ 🖼️  │ │ 🖼️  │          │
│ └──────┘ └──────┘ └──────┘          │
│ Video 1  Video 2  Video 3           │
└─────────────────────────────────────┘
```

## Example 5: hero video

```
┌─────────────────────────────────────┐
│                                     │
│      🖼️ (background video)          │
│                                     │
│      Title                          │
│      Description                    │
│                                     │
│      [▶] Play                       │
│                                     │
└─────────────────────────────────────┘
```

## Example 6: video with subtitles

```
┌─────────────────────────────────────┐
│ 📺 Video with subtitles             │
├─────────────────────────────────────┤
│                                     │
│      🖼️                           │
│      [German]                       │
│                                     │
│ [▶]  ━━━━━━━━━━━━━━━━━  0:00 / 10:00│
└─────────────────────────────────────┘
```

## Example 7: video playlist

```
┌─────────────────────────────────────┐
│ 🎬 Playlist                         │
├─────────────────────────────────────┤
│ 1. [▶] Video 1  5:30  (current)     │
│ 2. [⏸] Video 2  7:15                │
│ 3. [⏸] Video 3  4:20                │
│ 4. [⏸] Video 4  8:45                │
├─────────────────────────────────────┤
│ [🔄] [🔀] [🔊 75%] 0:00 / 5:30      │
└─────────────────────────────────────┘
```

## Example 8: video in chat

```
┌─────────────────────────────────────┐
│ John:                               │
│ [▶] 0:15                            │
│                                     │
│ Jane:                               │
│ [▶] 0:08                            │
└─────────────────────────────────────┘
```
