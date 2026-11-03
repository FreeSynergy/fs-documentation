# Rich Text Editor (Rich-Text-Editor) - Usage

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Application

Ein Rich Text Editor ist ein Editor für formatierten Text.

- Dokumente
- Artikel
- Nachrichten

## Examples

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

## Notes

- Zustände: `placeholder` (zusätzlich zu den Zuständen aus `base`)
