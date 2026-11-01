# Context Menu - Verwendung

## Einfaches Context Menu

```jsx
<ContextMenu 
  items={[
    { id: 'edit', label: 'Bearbeiten', icon: 'pencil' },
    { id: 'copy', label: 'Kopieren', icon: 'copy' },
    { id: 'delete', label: 'Löschen', icon: 'trash', danger: true }
  ]}
  onSelect={(id) => console.log('Selected:', id)}
/>
```

## Mit Separator

```jsx
<ContextMenu 
  items={[
    { id: 'edit', label: 'Bearbeiten' },
    { id: 'copy', label: 'Kopieren' },
    { separator: true },
    { id: 'delete', label: 'Löschen', danger: true }
  ]}
/>
```

## In List-Item

```jsx
<ListItem onContextMenu={showContextMenu}>
  <ContextMenu 
    items={itemMenu}
    anchorEl={anchor}
    position={position}
  />
</ListItem>
```

## Mit Icons

```jsx
<ContextMenu 
  items={[
    { id: 'edit', label: 'Bearbeiten', icon: 'pencil' },
    { id: 'delete', label: 'Löschen', icon: 'trash', danger: true }
  ]}
  showIcons={true}
/>
```

## Mit Event-Handlern

```jsx
<ContextMenu 
  items={items}
  onOpen={() => console.log('Open')}
  onClose={() => console.log('Close')}
  onSelect={(id) => console.log('Selected:', id)}
/>
```

## Beispiele

## Beispiel 1: Datei-Explorer

```
└─ Rechtsklick auf Datei ───────────────┐
   📋 Bearbeiten                          │
   📄 Kopieren                            │
   📄 Einfügen                            │
   ─────────────────────                   │
   🗑️ Löschen                             │
   ℹ️ Eigenschaften                        │
└─────────────────────────────────────────┘
```

## Beispiel 2: Chat-Kontext

```
└─ Rechtsklick auf Nachricht ───────────┐
   📋 Antworten                            │
   📄 Weiterleiten                         │
   ⭐ Markieren                            │
   ─────────────────────                   │
   🗑️ Löschen (nur für mich)              │
   🚫 melden                              │
└─────────────────────────────────────────┘
```

## Beispiel 3: Tab-Kontext

```
└─ Rechtsklick auf Tab ─────────────────┐
   🔄 Aktualisieren                       │
   📄 Kopieren                            │
   ─────────────────────                   │
   🗑️ Schließen                          │
   📤 In neuem Tab öffnen                 │
└─────────────────────────────────────────┘
```

## Beispiel 4: List-Item-Kontext

```
└─ Rechtsklick auf List-Item ───────────┐
   📋 Bearbeiten                          │
   📄 Kopieren                            │
   ─────────────────────                   │
   🗑️ Löschen                             │
   📧 E-Mail senden                       │
└─────────────────────────────────────────┘
```

## Beispiel 5: Dashboard-Kontext

```
└─ Rechtsklick auf Widget ──────────────┐
   📋 Bearbeiten                          │
   📄 Kopieren                            │
   ─────────────────────                   │
   🗑️ Löschen                             │
   ⚙️ Einstellungen                       │
└─────────────────────────────────────────┘
```
