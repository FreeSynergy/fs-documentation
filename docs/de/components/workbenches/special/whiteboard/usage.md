# Whiteboard – Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt ist, werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Anwendung

Ein Whiteboard ist eine Zeichenfläche für die Zusammenarbeit.

- Brainstorming
- Planung
- Zusammenarbeit

## Beispiele

### Brainstorming

```jsx
<Whiteboard toolbar={entries} onChange={action} />
```

### Planung

```jsx
<Whiteboard toolbar={entries} interactive={true} />
```

### Zusammenarbeit

```jsx
<Whiteboard toolbar={entries} grid={true} />
```
