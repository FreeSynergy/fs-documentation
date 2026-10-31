# Tabs - Verwendung

## Einfache Tabs

```jsx
<Tabs 
  tabs={[
    { id: 'tab1', label: 'Tab 1', content: 'Inhalt 1' },
    { id: 'tab2', label: 'Tab 2', content: 'Inhalt 2' },
    { id: 'tab3', label: 'Tab 3', content: 'Inhalt 3' }
  ]}
  activeTab="tab1"
  onChange={(id) => setActiveTab(id)}
/>
```

## Mit Icons

```jsx
<Tabs 
  tabs={[
    { id: 'tab1', label: 'Home', icon: 'home', content: '...' },
    { id: 'tab2', label: 'Profile', icon: 'user', content: '...' },
    { id: 'tab3', label: 'Settings', icon: 'settings', content: '...' }
  ]}
  showIcons={true}
/>
```

## Closable Tabs

```jsx
<Tabs 
  tabs={dynamicTabs}
  closable={true}
  onClose={(id) => removeTab(id)}
/>
```

## Vertical Tabs

```jsx
<Tabs 
  tabs={tabs}
  position="left"
  size="large"
/>
```

## In Card

```jsx
<Card>
  <Tabs 
    tabs={tabs}
    variant="card"
    activeTab="tab1"
  />
</Card>
```

## Mit Event-Handlern

```jsx
<Tabs 
  tabs={tabs}
  onSelect={(id) => console.log('Selected:', id)}
  onClose={(id) => console.log('Closed:', id)}
/>
```
