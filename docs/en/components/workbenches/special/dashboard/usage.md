# Dashboard (Dashboard) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Ein Dashboard ist eine Übersichtsseite mit Widgets.

- Übersicht
- Analytics
- Project

## Beispiele

### Übersicht

```jsx
<Dashboard widgets={eintraege} />
```

### Analytics

```jsx
<Dashboard widgets={eintraege} dragAndDrop={true} />
```

### Project

```jsx
<Dashboard widgets={eintraege} responsive={true} />
```

## Hinweise

- Gesten: `drag`
