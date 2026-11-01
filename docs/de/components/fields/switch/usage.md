# Switch (Schalter) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Ein Switch ist ein Ein/Aus-Schalter (Toggle).

- Einstellungen
- Features
- Status

## Beispiele

### Einstellungen

```jsx
<Switch checked={false} onChange={aktion} />
```

### Features

```jsx
<Switch checked={false} animate={true} />
```

### Status

```jsx
<Switch checked={false} animationDuration={300} />
```

## Hinweise

- Zustände: `checked` (zusätzlich zu den Zuständen aus `base`)
