# Table - Verwendung

## Einfache Tabelle

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
    { key: 'email', title: 'E-Mail', dataIndex: 'email', sortable: true }
  ]}
  data={users}
  onSortChange={handleSortChange}
/>
```

## Mit Paginierung

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

## Mit Zeilenauswahl

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

## Mit Ereignis-Handlern

```jsx
<Table 
  columns={columns}
  data={data}
  onRowClick={(record) => console.log('Geklickt:', record)}
  onRowDoubleClick={(record) => console.log('Doppelklick:', record)}
/>
```

## Beispiele

## Beispiel 1: Benutzertabelle

```
┌─────────────────────────────────────────┐
│ ID │ Name │ Alter │ E-Mail               │
├─────────────────────────────────────────┤
│ 1  │ John │ 25    │ john@example.com     │
│ 2  │ Jane │ 30    │ jane@example.com     │
│ 3  │ Bob  │ 28    │ bob@example.com      │
└─────────────────────────────────────────┘
```

## Beispiel 2: mit Sortierung

```
┌─────────────────────────────────────────┐
│ ID │ Name ▲ │ Alter │ E-Mail             │
├─────────────────────────────────────────┤
│ 1  │ John   │ 25    │ john@example.com   │
│ 2  │ Jane   │ 30    │ jane@example.com   │
│ 3  │ Bob    │ 28    │ bob@example.com    │
└─────────────────────────────────────────┘
```

## Beispiel 3: mit Paginierung

```
┌─────────────────────────────────────────┐
│ ID │ Name │ Alter │ E-Mail               │
├─────────────────────────────────────────┤
│ 1  │ John │ 25    │ john@example.com     │
│ 2  │ Jane │ 30    │ jane@example.com     │
├─────────────────────────────────────────┤
│ [1] [2] [3] [4] [5] [Weiter →]          │
│ 1-10 von 100                            │
└─────────────────────────────────────────┘
```

## Beispiel 4: mit Zeilenauswahl

```
┌─────────────────────────────────────────┐
│ [✓] ID │ Name │ Alter │ E-Mail           │
├─────────────────────────────────────────┤
│ [✓] 1  │ John │ 25    │ john@example.com │
│ [✓] 2  │ Jane │ 30    │ jane@example.com │
│ [ ] 3  │ Bob  │ 28    │ bob@example.com  │
└─────────────────────────────────────────┘
```

## Beispiel 5: mit Aktionen

```
┌─────────────────────────────────────────┐
│ ID │ Name │ Alter │ E-Mail │ Aktion      │
├─────────────────────────────────────────┤
│ 1  │ John │ 25    │ john@example.com │ [✏️] [🗑️] │
│ 2  │ Jane │ 30    │ jane@example.com │ [✏️] [🗑️] │
└─────────────────────────────────────────┘
```
