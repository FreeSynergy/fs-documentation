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
