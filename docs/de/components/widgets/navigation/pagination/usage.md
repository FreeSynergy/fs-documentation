# Pagination - Verwendung

## Nummerierte Pagination

```jsx
<Pagination 
  currentPage={1}
  totalItems={100}
  itemsPerPage={10}
  onChange={(page) => console.log('Page:', page)}
/>
```

## Vor/Zurück-Pagination

```jsx
<Pagination 
  variant="previous-next"
  currentPage={2}
  totalItems={50}
  onChange={(page) => console.log('Page:', page)}
/>
```

## Mehr laden

```jsx
<List items={items}>
  <Pagination 
    variant="load-more"
    onLoadMore={() => loadMoreItems()}
  />
</List>
```

## Mit Auswahl der Seitengröße

```jsx
<Pagination 
  showPageSizes={true}
  pageSizes={[10, 20, 50, 100]}
  onPageSizeChange={(size) => console.log('Size:', size)}
/>
```

## In einer Tabelle

```jsx
<Table 
  data={data}
  pagination={
    <Pagination 
      currentPage={page}
      totalItems={total}
      itemsPerPage={pageSize}
      onChange={handlePageChange}
    />
  }
/>
```

## Mit Ereignis-Handlern

```jsx
<Pagination 
  currentPage={page}
  totalItems={total}
  onPageChange={(page) => console.log('Page:', page)}
  onPageSizeChange={(size) => console.log('Size:', size)}
/>
```

## Beispiele

## Beispiel 1: Tabellarische Daten

```
┌─────────────────────────────────────────┐
│ ID │ Name │ Alter │                     │
├─────────────────────────────────────────┤
│ 1  │ John │ 25    │                     │
│ 2  │ Jane │ 30    │                     │
│ 3  │ Bob  │ 28    │                     │
├─────────────────────────────────────────┤
│ [◀] 1 2 3 4 5 [▶]                       │
│ 1-10 von 100                            │
└─────────────────────────────────────────┘
```

## Beispiel 2: Produktsuche

```
┌─────────────────────────────────────────┐
│ [◀ Zurück] [Weiter ▶]                   │
│ Seite 1 von 25                          │
└─────────────────────────────────────────┘
```

## Beispiel 3: Mehr laden

```
┌─────────────────────────────────────────┐
│ Artikel 1                               │
│ Artikel 2                               │
│ ...                                     │
├─────────────────────────────────────────┤
│ [Mehr laden]                            │
└─────────────────────────────────────────┘
```

## Beispiel 4: Endloses Scrollen

```
┌─────────────────────────────────────────┐
│ Artikel 1                               │
│ Artikel 2                               │
│ ...                                     │
│ (lädt beim Scrollen automatisch nach)   │
└─────────────────────────────────────────┘
```

## Beispiel 5: Mit Seitengröße

```
┌─────────────────────────────────────────┐
│ [◀] 1 2 3 4 5 [▶]                       │
│ 10/20/50/100 Einträge pro Seite anzeigen│
└─────────────────────────────────────────┘
```
