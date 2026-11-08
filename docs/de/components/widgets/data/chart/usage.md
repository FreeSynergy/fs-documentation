# Chart - Verwendung

!!! note
    Die Beispiele bleiben syntaxneutral. Sobald die Umsetzung zu Rust und Blinc wechselt,
    werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Anwendung

Ein Chart ist eine Datenvisualisierung (Diagramme).

- Statistiken
- Diagramme
- Grafiken

## Beispiele

### Statistiken

```jsx
<Chart data={entries} type="line" />
```

### Diagramme

```jsx
<Chart data={entries} interactive={true} />
```

### Grafiken

```jsx
<Chart data={entries} showLegend={true} />
```

## Hinweise

- Übergänge: `highlight`
