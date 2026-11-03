# Search Field - Usage

## A simple search field

```jsx
<SearchField
  value={searchTerm}
  onChange={setSearchTerm}
  placeholder="Search…"
/>
```

## With auto-complete

```jsx
<SearchField
  value={searchTerm}
  onChange={setSearchTerm}
  placeholder="Search products…"
  showSuggestions={true}
  suggestions={suggestions}
  onSelect={handleSelect}
/>
```

## With filters

```jsx
<SearchField
  value={searchTerm}
  onChange={setSearchTerm}
  showFilters={true}
  filters={filterOptions}
  onFilterChange={handleFilterChange}
/>
```

## In a table

```jsx
<DataTable
  data={data}
  columns={columns}
  search={
    <SearchField
      value={searchTerm}
      onChange={setSearchTerm}
      placeholder="Search the table…"
    />
  }
/>
```

## With event handlers

```jsx
<SearchField
  value={searchTerm}
  onChange={setSearchTerm}
  onSubmit={() => console.log('Search:', searchTerm)}
  onClear={() => console.log('Clear')}
/>
```

## Examples

## Example 1: simple search

```
┌─────────────────────────────────────────┐
│ 🔍 Search…                              │
└─────────────────────────────────────────┘
```

## Example 2: with auto-complete

```
┌─────────────────────────────────────────┐
│ 🔍 Search…                              │
├─────────────────────────────────────────┤
│  Product 1                              │
│  Product 2                              │
│  Product 3                              │
│  +                                      │
└─────────────────────────────────────────┘
```

## Example 3: with filters

```
┌─────────────────────────────────────────┐
│ 🔍 Products…                            │
├─────────────────────────────────────────┤
│  [Category] [Price] [Status]            │
└─────────────────────────────────────────┘
```

## Example 4: in a table

```
┌─────────────────────────────────────────┐
│ ID │ Name │ Age │ Action                │
├─────────────────────────────────────────┤
│ 🔍 Search…                              │
├─────────────────────────────────────────┤
│ 1  │ John │ 25  │ [Edit]                │
│ 2  │ Jane │ 30  │ [Edit]                │
└─────────────────────────────────────────┘
```

## Example 5: with clear

```
┌─────────────────────────────────────────┐
│ 🔍 Search…                     [✕]      │
└─────────────────────────────────────────┘
```
