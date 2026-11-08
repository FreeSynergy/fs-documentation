# Grid View - Verwendung

!!! note
    Die Beispiele bleiben syntaxneutral. Sobald die Umsetzung zu Rust und Blinc wechselt,
    werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Anwendung

Eine Grid View ist eine Karten- bzw. Rasteransicht von Elementen.

- Bildergalerien
- Produktkataloge
- Kartenansichten
- Dateiverzeichnisse

## Beispiele

### Bildergalerien

```jsx
<GridView items={entries} columns={3} />
```

### Produktkataloge

```jsx
<GridView items={entries} interactive={false} />
```

### Kartenansichten

```jsx
<GridView items={entries} gap={16} />
```
