# Search Field (Suchfeld mit Filter) - Verwendung

## Einfaches Search Field

```jsx
<SearchField 
  value={searchTerm}
  onChange={setSearchTerm}
  placeholder="Suche..."
/>
```

## Mit Auto-Complete

```jsx
<SearchField 
  value={searchTerm}
  onChange={setSearchTerm}
  placeholder="Produkte suchen..."
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

## In Table

```jsx
<DataTable 
  data={data}
  columns={columns}
  search={
    <SearchField 
      value={searchTerm}
      onChange={setSearchTerm}
      placeholder="Tabelle durchsuchen..."
    />
  }
/>
```

## Mit Event-Handlern

```jsx
<SearchField 
  value={searchTerm}
  onChange={setSearchTerm}
  onSubmit={() => console.log('Search:', searchTerm)}
  onClear={() => console.log('Clear')}
/>
```

## Beispiele

## Beispiel 1: Einfache Suche

```
┌─────────────────────────────────────────┐
│ 🔍 Suche...                             │
└─────────────────────────────────────────┘
```

## Beispiel 2: mit Auto-Complete

```
┌─────────────────────────────────────────┐
│ 🔍 Suche...                             │
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
│ 🔍 Produkte...                          │
├─────────────────────────────────────────┤
│  [Kategorie] [Preis] [Status]           │
└─────────────────────────────────────────┘
```

## Beispiel 4: in Tabelle

```
┌─────────────────────────────────────────┐
│ ID │ Name │ Alter │ Aktion               │
├─────────────────────────────────────────┤
│ 🔍 Suche...                             │
├─────────────────────────────────────────┤
│ 1  │ John │ 25    │ [Bearbeiten]         │
│ 2  │ Jane │ 30    │ [Bearbeiten]         │
└─────────────────────────────────────────┘
```

## Beispiel 5: mit Clear

```
┌─────────────────────────────────────────┐
│ 🔍 Suche...                    [✕]      │
└─────────────────────────────────────────┘
```
