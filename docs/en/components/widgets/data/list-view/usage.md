# List View - Usage

## Simple list

```jsx
<List 
  items={['Element 1', 'Element 2', 'Element 3']}
  onClick={(item, index) => console.log('Clicked:', item)}
/>
```

## With icons

```jsx
<List 
  items={files}
  showIcons={true}
  icon={(item) => getFileIcon(item)}
/>
```

## With badges

```jsx
<List 
  items={notifications}
  showBadges={true}
  badge={(item) => item.unread ? '!' : null}
/>
```

## In a card

```jsx
<Card title="Files">
  <List 
    items={files}
    onClick={handleFileClick}
    showIcons={true}
  />
</Card>
```

## With event handlers

```jsx
<List 
  items={items}
  onClick={(item) => console.log('Clicked:', item)}
  onHover={(item) => console.log('Hover:', item)}
  onActionClick={(item, action) => console.log('Action:', action)}
/>
```

## Examples

## Example 1: simple list

```
┌─────────────────────────────────────────┐
│ Element 1                               │
│ Element 2                               │
│ Element 3                               │
│ Element 4                               │
└─────────────────────────────────────────┘
```

## Example 2: with icons

```
┌─────────────────────────────────────────┐
│ 📁 File 1                               │
│ 📁 File 2                               │
│ 📁 File 3                               │
└─────────────────────────────────────────┘
```

## Example 3: with badges

```
┌─────────────────────────────────────────┐
│ Message 1      (3)                      │
│ Message 2      (1)                      │
│ Message 3                               │
└─────────────────────────────────────────┘
```

## Example 4: with actions

```
┌─────────────────────────────────────────┐
│ Element 1         [Edit] [Delete]       │
│ Element 2         [Edit] [Delete]       │
│ Element 3         [Edit] [Delete]       │
└─────────────────────────────────────────┘
```

## Example 5: with avatars

```
┌─────────────────────────────────────────┐
│ 👤 John Doe                             │
│ 👤 Jane Smith                           │
│ 👤 Bob Müller                           │
└─────────────────────────────────────────┘
```
