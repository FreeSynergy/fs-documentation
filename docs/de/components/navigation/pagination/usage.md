# Pagination - Verwendung

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

## Mit Event-Handlern

```jsx
<Pagination 
  currentPage={page}
  totalItems={total}
  onPageChange={(page) => console.log('Page:', page)}
  onPageSizeChange={(size) => console.log('Size:', size)}
/>
```
