# Farbfeld – Verwendung

!!! note
    Die Beispiele bleiben syntaxneutral. Sobald die Implementierung auf Rust und
    Blinc umstellt, werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Anwendung

Ein Farbfeld ist ein Feld zur Farbauswahl mit einem Farbwähler.

- Eine Farbe auswählen
- Farbthemen
- Farbcode

## Beispiele

### Eine Farbe auswählen

```jsx
<ColorInput value="value" onChange={action} />
```

### Farbthemen

```jsx
<ColorInput value="value" placeholder="placeholder" />
```

### Farbcode

```jsx
<ColorInput value="value" showIcon={true} />
```

## Hinweise

- Zustände: `placeholder` (zusätzlich zu den Zuständen aus `base`)
