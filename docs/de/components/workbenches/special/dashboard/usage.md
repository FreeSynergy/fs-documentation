# Dashboard – Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt ist, werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Anwendung

Ein Dashboard ist eine Übersichtsseite mit Widgets.

- Überblick
- Auswertung
- Projekt

## Beispiele

### Überblick

```jsx
<Dashboard widgets={items} />
```

### Auswertung

```jsx
<Dashboard widgets={items} dragAndDrop={true} />
```

### Projekt

```jsx
<Dashboard widgets={items} responsive={true} />
```

## Hinweise

- Gesten: `drag`
