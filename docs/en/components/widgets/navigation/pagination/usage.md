# Pagination - Usage

## Numerische Pagination

```jsx
<Pagination 
  currentPage={1}
  totalItems={100}
  itemsPerPage={10}
  onChange={(page) => console.log('Page:', page)}
/>
```

## Previous/Next Pagination

```jsx
<Pagination 
  variant="previous-next"
  currentPage={2}
  totalItems={50}
  onChange={(page) => console.log('Page:', page)}
/>
```

## Load More

```jsx
<List items={items}>
  <Pagination 
    variant="load-more"
    onLoadMore={() => loadMoreItems()}
  />
</List>
```

## With Page Size Selector

```jsx
<Pagination 
  showPageSizes={true}
  pageSizes={[10, 20, 50, 100]}
  onPageSizeChange={(size) => console.log('Size:', size)}
/>
```

## In Table

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

## With event handlers

```jsx
<Pagination 
  currentPage={page}
  totalItems={total}
  onPageChange={(page) => console.log('Page:', page)}
  onPageSizeChange={(size) => console.log('Size:', size)}
/>
```

## Examples

## Example 1: Tabellarische Daten

```
┌─────────────────────────────────────────┐
│ ID │ Name │ Alter │                         │
├─────────────────────────────────────────┤
│ 1  │ John │ 25    │                         │
│ 2  │ Jane │ 30    │                         │
│ 3  │ Bob  │ 28    │                         │
├─────────────────────────────────────────┤
│ [◀] 1 2 3 4 5 [▶]                       │
│ 1-10 of 100                             │
└─────────────────────────────────────────┘
```

## Example 2: Produktsuche

```
┌─────────────────────────────────────────┐
│ [◀ Back] [Next ▶]                       │
│ Page 1 of 25                            │
└─────────────────────────────────────────┘
```

## Example 3: Load More

```
┌─────────────────────────────────────────┐
│ Artikel 1                               │
│ Artikel 2                               │
│ ...                                     │
├─────────────────────────────────────────┤
│ [Load more]                             │
└─────────────────────────────────────────┘
```

## Example 4: Infinite Scroll

```
┌─────────────────────────────────────────┐
│ Artikel 1                               │
│ Artikel 2                               │
│ ...                                     │
│ (Automatisch nachladen beim Scrollen)   │
└─────────────────────────────────────────┘
```

## Example 5: With page size

```
┌─────────────────────────────────────────┐
│ [◀] 1 2 3 4 5 [▶]                       │
│ Show 10/20/50/100 entries per page      │
└─────────────────────────────────────────┘
```
