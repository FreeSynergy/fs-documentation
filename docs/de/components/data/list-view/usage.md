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

## Beispiele

## Beispiel 1: Einfache Liste

```
┌─────────────────────────────────────────┐
│ Element 1                               │
│ Element 2                               │
│ Element 3                               │
│ Element 4                               │
└─────────────────────────────────────────┘
```

## Beispiel 2: mit Icons

```
┌─────────────────────────────────────────┐
│ 📁 Datei 1                              │
│ 📁 Datei 2                              │
│ 📁 Datei 3                              │
└─────────────────────────────────────────┘
```

## Beispiel 3: mit Badges

```
┌─────────────────────────────────────────┐
│ Nachricht 1    (3)                      │
│ Nachricht 2    (1)                      │
│ Nachricht 3                             │
└─────────────────────────────────────────┘
```

## Beispiel 4: mit Aktionen

```
┌─────────────────────────────────────────┐
│ Element 1         [Bearbeiten] [Löschen]│
│ Element 2         [Bearbeiten] [Löschen]│
│ Element 3         [Bearbeiten] [Löschen]│
└─────────────────────────────────────────┘
```

## Beispiel 5: mit Avataren

```
┌─────────────────────────────────────────┐
│ 👤 John Doe                             │
│ 👤 Jane Smith                           │
│ 👤 Bob Müller                           │
└─────────────────────────────────────────┘
```
