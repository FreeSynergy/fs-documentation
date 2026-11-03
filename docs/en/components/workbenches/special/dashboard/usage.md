# Dashboard (Dashboard) - Usage

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Application

Ein Dashboard ist eine Übersichtsseite mit Widgets.

- Übersicht
- Analytics
- Project

## Examples

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

## Notes

- Gesten: `drag`
