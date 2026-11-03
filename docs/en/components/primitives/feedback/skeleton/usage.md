# Skeleton - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## A list while loading

```jsx
<ListView>
  {[1, 2, 3].map(i => (
    <Skeleton key={i} shape="list-item" />
  ))}
</ListView>
```

## An article text while loading

```jsx
<Skeleton shape="text" lines={5} width="100%" />
```

## A table with matching column widths

```jsx
<Table columns={columns}>
  <Skeleton shape="table-row" widths={[40, 200, 90]} />
</Table>
```

## A grid of cards

```jsx
<GridView>
  {[1, 2, 3, 4].map(i => <Skeleton key={i} shape="card" />)}
</GridView>
```

## Scenarios

| Scenario | Recommendation |
|----------|----------------|
| Lists and tables | `list-item` / `table-row`, max. 3 repetitions |
| Text area | `text` with `lines` matching the expected length |
| Image or chart | `rect` at a fixed height |
| Content exists but is empty | no skeletons – a message or an empty state |
