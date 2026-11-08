# Tags Input - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden die Beispiele in `usage.md` in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Ein Tags Input ist eine Liste aus Tags/Labels.

- Hashtags
- Kategorien
- Schlagwörter

## Beispiele

### Hashtags

```jsx
<TagsInput tags={entries} onChange={aktion} />
```

### Kategorien

```jsx
<TagsInput tags={entries} placeholder="Platzhalter" />
```

### Schlagwörter

```jsx
<TagsInput tags={entries} showRemove={true} />
```

## Hinweise

- Zustände: `placeholder` (zusätzlich zu den Zuständen aus `base`)
