# Table - Usage

## Simple table

```jsx
<Table 
  columns={[
    { key: 'id', title: 'ID', dataIndex: 'id' },
    { key: 'name', title: 'Name', dataIndex: 'name' },
    { key: 'age', title: 'Age', dataIndex: 'age' }
  ]}
  data={users}
/>
```

## With sorting

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

## With pagination

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

## With row selection

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

## With event handlers

```jsx
<Table 
  columns={columns}
  data={data}
  onRowClick={(record) => console.log('Clicked:', record)}
  onRowDoubleClick={(record) => console.log('Double Clicked:', record)}
/>
```

## Examples

## Example 1: user table

```
┌─────────────────────────────────────────┐
│ ID │ Name │ Age │ Email                   │
├─────────────────────────────────────────┤
│ 1  │ John │ 25  │ john@example.com        │
│ 2  │ Jane │ 30  │ jane@example.com        │
│ 3  │ Bob  │ 28  │ bob@example.com         │
└─────────────────────────────────────────┘
```

## Example 2: with sorting

```
┌─────────────────────────────────────────┐
│ ID │ Name ▲ │ Age │ Email                 │
├─────────────────────────────────────────┤
│ 1  │ John   │ 25  │ john@example.com        │
│ 2  │ Jane   │ 30  │ jane@example.com        │
│ 3  │ Bob    │ 28  │ bob@example.com         │
└─────────────────────────────────────────┘
```

## Example 3: with pagination

```
┌─────────────────────────────────────────┐
│ ID │ Name │ Age │ Email                   │
├─────────────────────────────────────────┤
│ 1  │ John │ 25  │ john@example.com        │
│ 2  │ Jane │ 30  │ jane@example.com        │
├─────────────────────────────────────────┤
│ [1] [2] [3] [4] [5] [Next →]            │
│ 1-10 of 100                             │
└─────────────────────────────────────────┘
```

## Example 4: with row selection

```
┌─────────────────────────────────────────┐
│ [✓] ID │ Name │ Age │ Email                │
├─────────────────────────────────────────┤
│ [✓] 1  │ John │ 25  │ john@example.com      │
│ [✓] 2  │ Jane │ 30  │ jane@example.com      │
│ [ ] 3  │ Bob  │ 28  │ bob@example.com       │
└─────────────────────────────────────────┘
```

## Example 5: with actions

```
┌─────────────────────────────────────────┐
│ ID │ Name │ Age │ Email │ Action           │
├─────────────────────────────────────────┤
│ 1  │ John │ 25  │ john@example.com │ [✏️] [🗑️] │
│ 2  │ Jane │ 30  │ jane@example.com │ [✏️] [🗑️] │
└─────────────────────────────────────────┘
```
