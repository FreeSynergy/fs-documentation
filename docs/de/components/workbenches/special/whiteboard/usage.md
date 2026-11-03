# Whiteboard (Whiteboard) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Ein Whiteboard ist eine Zeichenfläche für Kollaboration.

- Brainstorming
- Planung
- Kollaboration

## Beispiele

### Brainstorming

```jsx
<Whiteboard toolbar={eintraege} onChange={aktion} />
```

### Planung

```jsx
<Whiteboard toolbar={eintraege} interactive={true} />
```

### Kollaboration

```jsx
<Whiteboard toolbar={eintraege} grid={true} />
```
