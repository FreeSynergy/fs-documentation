# Search Field - Verwendung

## Ein einfaches Suchfeld

```jsx
<SearchField
  value={searchTerm}
  onChange={setSearchTerm}
  placeholder="Suchen…"
/>
```

## Mit Auto-complete

```jsx
<SearchField
  value={searchTerm}
  onChange={setSearchTerm}
  placeholder="Produkte suchen…"
  showSuggestions={true}
  suggestions={suggestions}
  onSelect={handleSelect}
/>
```

## Mit Filtern

```jsx
<SearchField
  value={searchTerm}
  onChange={setSearchTerm}
  showFilters={true}
  filters={filterOptions}
  onFilterChange={handleFilterChange}
/>
```

## In einer Tabelle

```jsx
<DataTable
  data={data}
  columns={columns}
  search={
    <SearchField
      value={searchTerm}
      onChange={setSearchTerm}
      placeholder="Tabelle durchsuchen…"
    />
  }
/>
```

## Mit Ereignis-Handlern

```jsx
<SearchField
  value={searchTerm}
  onChange={setSearchTerm}
  onSubmit={() => console.log('Suche:', searchTerm)}
  onClear={() => console.log('Leeren')}
/>
```

## Beispiele

## Beispiel 1: einfache Suche

```
┌─────────────────────────────────────────┐
│ 🔍 Suchen…                              │
└─────────────────────────────────────────┘
```

## Beispiel 2: mit Auto-complete

```
┌─────────────────────────────────────────┐
│ 🔍 Suchen…                              │
├─────────────────────────────────────────┤
│  Produkt 1                              │
│  Produkt 2                              │
│  Produkt 3                              │
│  +                                      │
└─────────────────────────────────────────┘
```

## Beispiel 3: mit Filtern

```
┌─────────────────────────────────────────┐
│ 🔍 Produkte…                            │
├─────────────────────────────────────────┤
│  [Kategorie] [Preis] [Status]           │
└─────────────────────────────────────────┘
```

## Beispiel 4: in einer Tabelle

```
┌─────────────────────────────────────────┐
│ ID │ Name │ Alter │ Aktion              │
├─────────────────────────────────────────┤
│ 🔍 Suchen…                              │
├─────────────────────────────────────────┤
│ 1  │ John │ 25    │ [Bearbeiten]        │
│ 2  │ Jane │ 30    │ [Bearbeiten]        │
└─────────────────────────────────────────┘
```

## Beispiel 5: mit Clear-Knopf

```
┌─────────────────────────────────────────┐
│ 🔍 Suchen…                     [✕]      │
└─────────────────────────────────────────┘
```
