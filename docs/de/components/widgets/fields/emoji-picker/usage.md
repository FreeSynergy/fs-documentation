# Emoji Picker - Verwendung

!!! note
    Die Beispiele bleiben syntaxneutral. Sobald die Umsetzung zu Rust und Blinc wechselt,
    werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Anwendung

Ein Emoji Picker ist eine Emoji-Auswahl für Chat und Kommentare.

- Chat
- Kommentare
- Nachrichten

## Beispiele

### Chat

```jsx
<EmojiPicker value="value" onChange={action} />
```

### Kommentare

```jsx
<EmojiPicker value="value" placeholder="Platzhalter" />
```

### Nachrichten

```jsx
<EmojiPicker value="value" showSearch={true} />
```

## Hinweise

- Zustände: `placeholder` (zusätzlich zu den Zuständen aus `base`)
