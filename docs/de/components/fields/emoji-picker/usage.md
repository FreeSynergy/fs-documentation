# Emoji Picker (Emoji-Auswahl) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Ein Emoji Picker ist eine Emoji-Auswahl für Chat/Kommentare.

- Chat
- Kommentare
- Messages

## Beispiele

### Chat

```jsx
<EmojiPicker value="Wert" onChange={aktion} />
```

### Kommentare

```jsx
<EmojiPicker value="Wert" placeholder="Platzhalter" />
```

### Messages

```jsx
<EmojiPicker value="Wert" showSearch={true} />
```

## Hinweise

- Zustände: `placeholder` (zusätzlich zu den Zuständen aus `base`)
