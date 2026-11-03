# Grid View (Rasteransicht) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Grid View ist eine Karten/Raster-Darstellung von Elementen.

- Bildergalerien
- Produktkataloge
- Kartenansichten
- Dateiverzeichnisse

## Beispiele

### Bildergalerien

```jsx
<GridView items={eintraege} columns={3} />
```

### Produktkataloge

```jsx
<GridView items={eintraege} interactive={false} />
```

### Kartenansichten

```jsx
<GridView items={eintraege} gap={16} />
```
