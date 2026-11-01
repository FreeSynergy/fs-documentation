# Tooltip (Kurzinfo) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Icon-only-Button erklären

```jsx
<IconButton icon="settings" aria-label="Einstellungen">
  <Tooltip content="Einstellungen öffnen" placement="top" />
</IconButton>
```

## Vollständiger Text für abgeschnittenen Wert

```jsx
<TableCell value={shortTitle}>
  <Tooltip content={fullTitle} placement="top" />
</TableCell>
```

## Tastaturkürzel zeigen

```jsx
<Tooltip content="Speichern (Strg + S)" delay={0} />
```

## Mobil per Langdruck

```jsx
<ToolbarItem icon="filter">
  <Tooltip content="Filtern" trigger="longpress" />
</ToolbarItem>
```

## Szenarien

| Szenario | Empfehlung |
|----------|------------|
| Icon-only-Button | Tooltip plus `aria-label` |
| Abgeschnittener Tabellenwert | `placement="top"`, `delay={0}` |
| Erklärtext zu einem Feld | lieber [field](../../fields/field/) mit `help` |
| Inhalt mit Buttons oder Links | [popover](../popover/), kein Tooltip |
