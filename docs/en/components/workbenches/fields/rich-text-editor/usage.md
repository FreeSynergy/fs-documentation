# Rich Text Editor (Rich-Text-Editor) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Ein Rich Text Editor ist ein Editor für formatierten Text.

- Dokumente
- Artikel
- Nachrichten

## Beispiele

### Dokumente

```jsx
<RichTextEditor value="Wert" onChange={aktion} />
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
