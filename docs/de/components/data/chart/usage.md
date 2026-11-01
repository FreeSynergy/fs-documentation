# Chart (Diagramm) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Ein Chart ist eine Datenvisualisierung (Diagramme).

- Statistiken
- Diagramme
- Grafiken

## Beispiele

### Statistiken

```jsx
<Chart data={eintraege} type="line" />
```

### Diagramme

```jsx
<Chart data={eintraege} interactive={true} />
```

### Grafiken

```jsx
<Chart data={eintraege} showLegend={true} />
```

## Hinweise

- Übergänge: `highlight`
