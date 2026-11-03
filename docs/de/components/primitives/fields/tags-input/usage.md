# Tags Input (Tags-Feld) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Ein Tags Input ist eine Liste von Tags/Etiketten.

- Hashtags
- Kategorien
- Schlagworte

## Beispiele

### Hashtags

```jsx
<TagsInput tags={eintraege} onChange={aktion} />
```

### Kategorien

```jsx
<TagsInput tags={eintraege} placeholder="Platzhalter" />
```

### Schlagworte

```jsx
<TagsInput tags={eintraege} showRemove={true} />
```

## Hinweise

- Zustände: `placeholder` (zusätzlich zu den Zuständen aus `base`)
