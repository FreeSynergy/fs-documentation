# Tree View (Baumansicht) - Verwendung

## Einfacher Tree View

```jsx
<TreeView 
  data={treeData}
  onClick={(node) => console.log('Clicked:', node)}
/>
```

## mit Checkboxen

```jsx
<TreeView 
  data={treeData}
  variant="with-checkboxes"
  checkedKeys={checkedKeys}
  onCheckChange={handleCheckChange}
/>
```

## Draggable

```jsx
<TreeView 
  data={treeData}
  variant="draggable"
  onDragStart={handleDragStart}
  onDragEnd={handleDragEnd}
/>
```

## In Card

```jsx
<Card title="Dateiverzeichnis">
  <TreeView 
    data={fileTree}
    onClick={handleFileClick}
    showIcons={true}
  />
</Card>
```

## Mit Event-Handlern

```jsx
<TreeView 
  data={treeData}
  onClick={(node) => console.log('Clicked:', node)}
  onExpand={(node) => console.log('Expanded:', node)}
  onCollapse={(node) => console.log('Collapsed:', node)}
/>
```
