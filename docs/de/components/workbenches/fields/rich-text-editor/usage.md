# Rich Text Editor - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und Blinc
    wechselt, werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Anwendung

Ein Rich-Text-Editor ist ein Editor für formatierten Text.

- Dokumente
- Artikel
- Nachrichten

## Beispiele

### Dokumente

```jsx
<RichTextEditor value="Wert" onChange={action} />
```

### Artikel

```jsx
<RichTextEditor value="Wert" placeholder="Platzhalter" />
```

### Nachrichten

```jsx
<RichTextEditor value="Wert" placeholder="Platzhalter" />
```

## Hinweise

- Zustände: `placeholder` (zusätzlich zu den Zuständen aus `base`)
