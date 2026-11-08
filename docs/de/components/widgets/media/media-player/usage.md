# Media Player - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden die Beispiele in `usage.md` in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Ein Media Player spielt Videos und Audio ab.

- Videos
- Audio
- Medien

## Beispiele

### Videos

```jsx
<MediaPlayer src="/example/path" controls={true} />
```

### Audio

```jsx
<MediaPlayer src="/example/path" autoplay={false} />
```

### Medien

```jsx
<MediaPlayer src="/example/path" muted={false} />
```
