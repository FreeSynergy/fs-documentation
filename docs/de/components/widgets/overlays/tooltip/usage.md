# Tooltip - Verwendung

!!! note
    Die Beispiele bleiben syntaxneutral. Sobald die Umsetzung zu Rust und Blinc wechselt,
    werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Erklären einer Schaltfläche nur mit Icon

```jsx
<IconButton icon="settings" aria-label="Einstellungen">
  <Tooltip content="Einstellungen öffnen" placement="top" />
</IconButton>
```

## Vollständiger Text für einen gekürzten Wert

```jsx
<TableCell value={shortTitle}>
  <Tooltip content={fullTitle} placement="top" />
</TableCell>
```

## Anzeige eines Tastenkürzels

```jsx
<Tooltip content="Speichern (Strg + S)" delay={0} />
```

## Mobil per langem Drücken

```jsx
<ToolbarItem icon="filter">
  <Tooltip content="Filter" trigger="longpress" />
</ToolbarItem>
```

## Szenarien

| Szenario | Empfehlung |
|----------|------------|
| Schaltfläche nur mit Icon | Tooltip plus `aria-label` |
| gekürzter Tabellenwert | `placement="top"`, `delay={0}` |
| erklärender Text zu einem Feld | besser [field](../../../primitives/fields/field/) mit `help` |
| Inhalt mit Schaltflächen oder Links | [popover](../popover/), kein Tooltip |
