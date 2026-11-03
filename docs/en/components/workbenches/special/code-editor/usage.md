# Code Editor (Code-Editor) - Usage

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Application

Ein Code Editor ist ein Editor für Quellcode.

- Code
- Programmierung
- Skripte

## Examples

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
