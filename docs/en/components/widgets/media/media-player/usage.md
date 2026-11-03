# Media Player - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## Application

A media player plays videos and audio.

- Videos
- Audio
- Media

## Examples

### Videos

```jsx
<MediaPlayer src="/example/path" controls={true} />
```

### Audio

```jsx
<MediaPlayer src="/example/path" autoplay={false} />
```

### Media

```jsx
<MediaPlayer src="/example/path" muted={false} />
```
