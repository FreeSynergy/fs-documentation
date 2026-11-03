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

## Beispiele

## Beispiel 1: Dateiverzeichnis

```
┌─────────────────────────────────────────┐
│ ▶ Dokumente                             │
│   └─ Projekt 1                          │
│   └─ Projekt 2                          │
├─────────────────────────────────────────┤
│ ▶ Bilder                                │
│   └─ Urlaub 2023                        │
│   └─ Veranstaltungen                    │
├─────────────────────────────────────────┤
│ ▶ Musik                                 │
│   └─ Rock                               │
│   └─ Jazz                               │
└─────────────────────────────────────────┘
```

## Beispiel 2: mit Checkboxen

```
┌─────────────────────────────────────────┐
│ [✓] Dokumente                           │
│   └─ [✓] Projekt 1                      │
│   └─ [ ] Projekt 2                      │
├─────────────────────────────────────────┤
│ [ ] Bilder                              │
│   └─ [✓] Urlaub 2023                    │
└─────────────────────────────────────────┘
```

## Beispiel 3: Kategorien

```
┌─────────────────────────────────────────┐
│ ▶ Elektronik                            │
│   └─ [✓] Smartphones                    │
│   └─ [ ] Laptops                        │
├─────────────────────────────────────────┤
│ ▶ Kleidung                              │
│   └─ [ ] Herren                         │
│   └─ [ ] Damen                          │
└─────────────────────────────────────────┘
```

## Beispiel 4: Organigramm

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

## Beispiel 5: mit Icons

```
┌─────────────────────────────────────────┐
│ 📁 Dokumente                            │
│   └─ 📄 Projekt 1                       │
│   └─ 📄 Projekt 2                       │
├─────────────────────────────────────────┤
│ 📷 Bilder                               │
│   └─ 🖼️ Urlaub 2023                    │
└─────────────────────────────────────────┘
```
