# Skeleton - Verwendung

!!! note
    Die Beispiele bleiben syntaxneutral. Sobald die Umsetzung auf Rust und Blinc
    wechselt, werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Eine Liste während des Ladens

```jsx
<ListView>
  {[1, 2, 3].map(i => (
    <Skeleton key={i} shape="list-item" />
  ))}
</ListView>
```

## Ein Artikeltext während des Ladens

```jsx
<Skeleton shape="text" lines={5} width="100%" />
```

## Eine Tabelle mit passenden Spaltenbreiten

```jsx
<Table columns={columns}>
  <Skeleton shape="table-row" widths={[40, 200, 90]} />
</Table>
```

## Ein Raster aus Cards

```jsx
<GridView>
  {[1, 2, 3, 4].map(i => <Skeleton key={i} shape="card" />)}
</GridView>
```

## Szenarien

| Szenario | Empfehlung |
|----------|------------|
| Listen und Tabellen | `list-item` / `table-row`, max. 3 Wiederholungen |
| Textbereich | `text` mit `lines` passend zur erwarteten Länge |
| Bild oder Diagramm | `rect` mit fester Höhe |
| Inhalt existiert, ist aber leer | keine Skeletons, sondern eine Meldung oder ein Empty State |
