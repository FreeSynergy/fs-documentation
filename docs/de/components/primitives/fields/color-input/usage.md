# Color Input (Farbfeld) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Ein Color Input ist ein Farbauswahl-Feld mit Farbpicker.

- Farbe wählen
- Farb-themes
- Farb-Code

## Beispiele

### Farbe wählen

```jsx
<ColorInput value="Wert" onChange={aktion} />
```

### Farb-themes

```jsx
<ColorInput value="Wert" placeholder="Platzhalter" />
```

### Farb-Code

```jsx
<ColorInput value="Wert" showIcon={true} />
```

## Hinweise

- Zustände: `placeholder` (zusätzlich zu den Zuständen aus `base`)
