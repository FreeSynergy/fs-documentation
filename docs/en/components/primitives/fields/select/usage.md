# Select - Usage

## A simple dropdown

```jsx
<Dropdown
  label="Country"
  value={country}
  onChange={setCountry}
  options={[
    { value: 'de', label: 'Germany' },
    { value: 'at', label: 'Austria' },
    { value: 'ch', label: 'Switzerland' }
  ]}
/>
```

## With search

```jsx
<Dropdown
  label="User"
  value={user}
  onChange={setUser}
  options={users}
  searchable={true}
  placeholder="Search users…"
/>
```

## Multi-select

```jsx
<Dropdown
  label="Categories"
  value={categories}
  onChange={setCategories}
  options={categoryOptions}
  multiple={true}
  showTags={true}
/>
```

## In a form

```jsx
<Form>
  <Dropdown
    label="Status"
    value={status}
    onChange={setStatus}
    options={[
      { value: 'open', label: 'Open' },
      { value: 'in-progress', label: 'In progress' },
      { value: 'done', label: 'Done' }
    ]}
  />
</Form>
```

## With event handlers

```jsx
<Dropdown
  label="Country"
  options={options}
  onSelect={(value) => console.log('Selected:', value)}
  onOpen={() => console.log('Open')}
  onClose={() => console.log('Close')}
/>
```

## Examples

## Example 1: choosing a country

```
┌─────────────────────────────────────────┐
│ Country                                 │
├─────────────────────────────────────────┤
│  Germany ▼                              │
├─────────────────────────────────────────┤
│  Austria                                │
│  Switzerland                            │
│  France                                 │
│  Italy                                  │
└─────────────────────────────────────────┘
```

## Example 2: choosing a user

```
┌─────────────────────────────────────────┐
│ Assignee                                │
├─────────────────────────────────────────┤
│  John Doe ▼                             │
├─────────────────────────────────────────┤
│  John Doe                               │
│  Jane Smith                             │
│  Bob Müller                             │
│  Alice Winter                           │
└─────────────────────────────────────────┘
```

## Example 3: categories (multi-select)

```
┌─────────────────────────────────────────┐
│ Categories                              │
├─────────────────────────────────────────┤
│  [Java] [Python] [React] ▼             │
├─────────────────────────────────────────┤
│  [✓] Java                               │
│  [✓] Python                             │
│  [ ] React                              │
│  [ ] Node.js                            │
│  [ ] Angular                            │
└─────────────────────────────────────────┘
```

## Example 4: choosing a status

```
┌─────────────────────────────────────────┐
│ Status                                  │
├─────────────────────────────────────────┤
│  🟢 Open ▼                              │
├─────────────────────────────────────────┤
│  🟢 Open                                │
│  🟡 In progress                         │
│  🟢 Done                                │
│  🔴 Rejected                            │
└─────────────────────────────────────────┘
```

## Example 5: with search

```
┌─────────────────────────────────────────┐
│ Search products…                        │
├─────────────────────────────────────────┤
│  P                                       │
├─────────────────────────────────────────┤
│  Product 1                              │
│  Product 2                              │
│  Product 3                              │
└─────────────────────────────────────────┘
```
