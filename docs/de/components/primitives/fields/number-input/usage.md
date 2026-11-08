# Number Input - Verwendung

!!! note
    Die Beispiele bleiben syntaxneutral. Sobald die Umsetzung auf Rust und Blinc
    wechselt, werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Anwendung

Ein Number Input ist ein Eingabefeld für Zahlen.

- Ein Alter angeben
- Mengen
- Preise
- Werte

## Beispiele

### Ein Alter angeben

```jsx
<NumberInput onChange={action} />
```

### Mengen

```jsx
<NumberInput onChange={action} step={1} />
```

### Preise

```jsx
<NumberInput onChange={action} showStepButtons={true} />
```
