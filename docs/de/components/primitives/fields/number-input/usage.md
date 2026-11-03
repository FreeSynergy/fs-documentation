# Number Input (Nummernfeld) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Ein Number Input ist ein Eingabefeld für Zahlen.

- Altersangabe
- Mengen
- Preise
- Werte

## Beispiele

### Altersangabe

```jsx
<NumberInput onChange={aktion} />
```

### Mengen

```jsx
<NumberInput onChange={aktion} step={1} />
```

### Preise

```jsx
<NumberInput onChange={aktion} showStepButtons={true} />
```
