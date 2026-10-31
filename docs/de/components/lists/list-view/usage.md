# List (Aufzählung) - Verwendung

## Einfache List

```jsx
<List 
  items={['Element 1', 'Element 2', 'Element 3']}
  onClick={(item, index) => console.log('Clicked:', item)}
/>
```

## Mit Icons

```jsx
<List 
  items={files}
  showIcons={true}
  icon={(item) => getFileIcon(item)}
/>
```

## mit Badges

```jsx
<List 
  items={notifications}
  showBadges={true}
  badge={(item) => item.unread ? '!' : null}
/>
```

## In Card

```jsx
<Card title="Dateien">
  <List 
    items={files}
    onClick={handleFileClick}
    showIcons={true}
  />
</Card>
```

## Mit Event-Handlern

```jsx
<List 
  items={items}
  onClick={(item) => console.log('Clicked:', item)}
  onHover={(item) => console.log('Hover:', item)}
  onActionClick={(item, action) => console.log('Action:', action)}
/>
```
