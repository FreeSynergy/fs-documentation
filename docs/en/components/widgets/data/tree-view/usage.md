# Tree View - Usage

## Simple tree view

```jsx
<TreeView 
  data={treeData}
  onClick={(node) => console.log('Clicked:', node)}
/>
```

## With checkboxes

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

## In a card

```jsx
<Card title="File directory">
  <TreeView 
    data={fileTree}
    onClick={handleFileClick}
    showIcons={true}
  />
</Card>
```

## With event handlers

```jsx
<TreeView 
  data={treeData}
  onClick={(node) => console.log('Clicked:', node)}
  onExpand={(node) => console.log('Expanded:', node)}
  onCollapse={(node) => console.log('Collapsed:', node)}
/>
```

## Examples

## Example 1: file directory

```
┌─────────────────────────────────────────┐
│ ▶ Documents                             │
│   └─ Project 1                          │
│   └─ Project 2                          │
├─────────────────────────────────────────┤
│ ▶ Images                                │
│   └─ Vacation 2023                      │
│   └─ Events                             │
├─────────────────────────────────────────┤
│ ▶ Music                                 │
│   └─ Rock                               │
│   └─ Jazz                               │
└─────────────────────────────────────────┘
```

## Example 2: with checkboxes

```
┌─────────────────────────────────────────┐
│ [✓] Documents                           │
│   └─ [✓] Project 1                      │
│   └─ [ ] Project 2                      │
├─────────────────────────────────────────┤
│ [ ] Images                              │
│   └─ [✓] Vacation 2023                  │
└─────────────────────────────────────────┘
```

## Example 3: categories

```
┌─────────────────────────────────────────┐
│ ▶ Electronics                           │
│   └─ [✓] Smartphones                    │
│   └─ [ ] Laptops                        │
├─────────────────────────────────────────┤
│ ▶ Clothing                              │
│   └─ [ ] Men                            │
│   └─ [ ] Women                          │
└─────────────────────────────────────────┘
```

## Example 4: org chart

```
┌─────────────────────────────────────────┐
│ CEO                                     │
│   └─ CTO                                │
│       └─ Dev Team                       │
│           └─ Frontend                   │
│           └─ Backend                    │
│   └─ CFO                                │
│       └─ Finance                        │
└─────────────────────────────────────────┘
```

## Example 5: with icons

```
┌─────────────────────────────────────────┐
│ 📁 Documents                            │
│   └─ 📄 Project 1                       │
│   └─ 📄 Project 2                       │
├─────────────────────────────────────────┤
│ 📷 Images                               │
│   └─ 🖼️ Vacation 2023                   │
└─────────────────────────────────────────┘
```
