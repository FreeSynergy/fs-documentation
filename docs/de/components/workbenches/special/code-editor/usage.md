# Code-Editor – Verwendung

!!! note
    Die Beispiele bleiben syntaxneutral. Sobald die Implementierung auf Rust und
    Blinc umstellt, werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Anwendung

Ein Code-Editor ist ein Editor für Quellcode.

- Code
- Programmierung
- Skripte

## Beispiele

### Code

```jsx
<CodeEditor value="Value" onChange={action} />
```

### Programmierung

```jsx
<CodeEditor value="Value" language="javascript" />
```

### Skripte

```jsx
<CodeEditor value="Value" readOnly={false} />
```
