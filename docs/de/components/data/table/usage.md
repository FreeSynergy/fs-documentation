# Table (Tabelle) - Verwendung

## Einfache Table

```jsx
<Table 
  columns={[
    { key: 'id', title: 'ID', dataIndex: 'id' },
    { key: 'name', title: 'Name', dataIndex: 'name' },
    { key: 'age', title: 'Alter', dataIndex: 'age' }
  ]}
  data={users}
/>
```

## Mit Sortierung

```jsx
<Table 
  columns={[
    { key: 'name', title: 'Name', dataIndex: 'name', sortable: true },
    { key: 'email', title: 'Email', dataIndex: 'email', sortable: true }
  ]}
  data={users}
  onSortChange={handleSortChange}
/>
```

## Mit Pagination

```jsx
<Table 
  columns={columns}
  data={data}
  pagination={{
    total: total,
    pageSize: 10,
    onChange: handlePageChange
  }}
/>
```

## mit Row Selection

```jsx
<Table 
  columns={columns}
  data={data}
  rowSelection={{
    selectedRowKeys: selectedKeys,
    onChange: handleSelectionChange
  }}
/>
```

## Mit Event-Handlern

```jsx
<Table 
  columns={columns}
  data={data}
  onRowClick={(record) => console.log('Clicked:', record)}
  onRowDoubleClick={(record) => console.log('Double Clicked:', record)}
/>
```

## Beispiele

## Beispiel 1: Benutzertabelle

```
┌─────────────────────────────────────────┐
│ ID │ Name │ Alter │ E-Mail                │
├─────────────────────────────────────────┤
│ 1  │ John │ 25    │ john@example.com      │
│ 2  │ Jane │ 30    │ jane@example.com      │
│ 3  │ Bob  │ 28    │ bob@example.com       │
└─────────────────────────────────────────┘
```

## Beispiel 2: mit Sortierung

```
┌─────────────────────────────────────────┐
│ ID │ Name ▲ │ Alter │ E-Mail              │
├─────────────────────────────────────────┤
│ 1  │ John   │ 25    │ john@example.com      │
│ 2  │ Jane   │ 30    │ jane@example.com      │
│ 3  │ Bob    │ 28    │ bob@example.com       │
└─────────────────────────────────────────┘
```

## Beispiel 3: mit Pagination

```
┌─────────────────────────────────────────┐
│ ID │ Name │ Alter │ E-Mail                │
├─────────────────────────────────────────┤
│ 1  │ John │ 25    │ john@example.com      │
│ 2  │ Jane │ 30    │ jane@example.com      │
├─────────────────────────────────────────┤
│ [1] [2] [3] [4] [5] [Nächste →]         │
│ 1-10 von 100                            │
└─────────────────────────────────────────┘
```

## Beispiel 4: mit Row Selection

```
┌─────────────────────────────────────────┐
│ [✓] ID │ Name │ Alter │ E-Mail             │
├─────────────────────────────────────────┤
│ [✓] 1  │ John │ 25    │ john@example.com     │
│ [✓] 2  │ Jane │ 30    │ jane@example.com     │
│ [ ] 3  │ Bob  │ 28    │ bob@example.com      │
└─────────────────────────────────────────┘
```

## Beispiel 5: mit Actions

```
┌─────────────────────────────────────────┐
│ ID │ Name │ Alter │ E-Mail │ Aktion       │
├─────────────────────────────────────────┤
│ 1  │ John │ 25    │ john@example.com │ [✏️] [🗑️] │
│ 2  │ Jane │ 30    │ jane@example.com │ [✏️] [🗑️] │
└─────────────────────────────────────────┘
```
