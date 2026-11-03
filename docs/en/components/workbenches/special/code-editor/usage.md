# Code Editor (Code-Editor) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Ein Code Editor ist ein Editor für Quellcode.

- Code
- Programmierung
- Skripte

## Beispiele

### Code

```jsx
<CodeEditor value="Wert" onChange={aktion} />
```

### Programmierung

```jsx
<CodeEditor value="Wert" language="javascript" />
```

### Skripte

```jsx
<CodeEditor value="Wert" readOnly={false} />
```
