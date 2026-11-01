# Skeleton (Platzhalter) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Liste beim Laden

```jsx
<ListView>
  {[1, 2, 3].map(i => (
    <Skeleton key={i} shape="list-item" />
  ))}
</ListView>
```

## Artikeltext beim Laden

```jsx
<Skeleton shape="text" lines={5} width="100%" />
```

## Tabelle mit passenden Spaltenbreiten

```jsx
<Table columns={columns}>
  <Skeleton shape="table-row" widths={[40, 200, 90]} />
</Table>
```

## Kartenraster

```jsx
<GridView>
  {[1, 2, 3, 4].map(i => <Skeleton key={i} shape="card" />)}
</GridView>
```

## Szenarien

| Szenario | Empfehlung |
|----------|------------|
| Listen und Tabellen | `list-item` / `table-row`, max. 3 Wiederholungen |
| Textbereich | `text` mit `lines` der erwarteten Länge |
| Bild oder Diagramm | `rect` in fester Höhe |
| Inhalt vorhanden, aber leer | keine Skeletons – Meldung oder leerer Zustand |
