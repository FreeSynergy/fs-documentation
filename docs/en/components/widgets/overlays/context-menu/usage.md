# Context Menu - Usage

## Simple context menu

```jsx
<ContextMenu
  items={[
    { id: 'edit', label: 'Edit', icon: 'pencil' },
    { id: 'copy', label: 'Copy', icon: 'copy' },
    { id: 'delete', label: 'Delete', icon: 'trash', danger: true }
  ]}
  onSelect={(id) => console.log('Selected:', id)}
/>
```

## With separator

```jsx
<ContextMenu
  items={[
    { id: 'edit', label: 'Edit' },
    { id: 'copy', label: 'Copy' },
    { separator: true },
    { id: 'delete', label: 'Delete', danger: true }
  ]}
/>
```

## In a list item

```jsx
<ListItem onContextMenu={showContextMenu}>
  <ContextMenu
    items={itemMenu}
    anchorEl={anchor}
    position={position}
  />
</ListItem>
```

## With icons

```jsx
<ContextMenu
  items={[
    { id: 'edit', label: 'Edit', icon: 'pencil' },
    { id: 'delete', label: 'Delete', icon: 'trash', danger: true }
  ]}
  showIcons={true}
/>
```

## With event handlers

```jsx
<ContextMenu
  items={items}
  onOpen={() => console.log('Open')}
  onClose={() => console.log('Close')}
  onSelect={(id) => console.log('Selected:', id)}
/>
```

## Examples

## Example 1: file explorer

```
└─ right-click on file ─────────────────┐
   📋 Edit                               │
   📄 Copy                               │
   📄 Paste                              │
   ─────────────────────                 │
   🗑️ Delete                             │
   ℹ️ Properties                          │
└────────────────────────────────────────┘
```

## Example 2: chat context

```
└─ right-click on message ──────────────┐
   📋 Reply                              │
   📄 Forward                            │
   ⭐ Star                                │
   ─────────────────────                 │
   🗑️ Delete (only for me)               │
   🚫 Report                             │
└────────────────────────────────────────┘
```

## Example 3: tab context

```
└─ right-click on tab ──────────────────┐
   🔄 Refresh                            │
   📄 Copy                               │
   ─────────────────────                 │
   🗑️ Close                              │
   📤 Open in new tab                    │
└────────────────────────────────────────┘
```

## Example 4: list item context

```
└─ right-click on list item ────────────┐
   📋 Edit                               │
   📄 Copy                               │
   ─────────────────────                 │
   🗑️ Delete                             │
   📧 Send e-mail                        │
└────────────────────────────────────────┘
```

## Example 5: dashboard context

```
└─ right-click on widget ───────────────┐
   📋 Edit                               │
   📄 Copy                               │
   ─────────────────────                 │
   🗑️ Delete                             │
   ⚙️ Settings                           │
└────────────────────────────────────────┘
```
