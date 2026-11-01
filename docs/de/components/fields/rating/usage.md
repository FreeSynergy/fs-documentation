# Rating (Bewertung) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Ein Rating ist eine Sterne- oder Punktebewertung.

- Produktbewertung
- Service-Bewertung
- Sterne

## Beispiele

### Produktbewertung

```jsx
<Rating onChange={aktion} />
```

### Service-Bewertung

```jsx
<Rating onChange={aktion} readonly={false} />
```

### Sterne

```jsx
<Rating onChange={aktion} max={5} />
```
