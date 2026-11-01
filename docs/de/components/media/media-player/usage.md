# Media Player (Medienwiedergabe) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Ein Media Player wiedergibt Videos und Audios.

- Videos
- Audios
- Medien

## Beispiele

### Videos

```jsx
<MediaPlayer src="/beispiel/pfad" controls={true} />
```

### Audios

```jsx
<MediaPlayer src="/beispiel/pfad" autoplay={false} />
```

### Medien

```jsx
<MediaPlayer src="/beispiel/pfad" muted={false} />
```
