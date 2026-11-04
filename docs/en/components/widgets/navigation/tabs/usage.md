# Tabs - Usage

## Einfache Tabs

```jsx
<Tabs 
  tabs={[
    { id: 'tab1', label: 'Tab 1', content: 'Content 1' },
    { id: 'tab2', label: 'Tab 2', content: 'Content 2' },
    { id: 'tab3', label: 'Tab 3', content: 'Content 3' }
  ]}
  activeTab="tab1"
  onChange={(id) => setActiveTab(id)}
/>
```

## With icons

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

## In a card

```jsx
<Card>
  <Tabs 
    tabs={tabs}
    variant="card"
    activeTab="tab1"
  />
</Card>
```

## With event handlers

```jsx
<Tabs 
  tabs={tabs}
  onSelect={(id) => console.log('Selected:', id)}
  onClose={(id) => console.log('Closed:', id)}
/>
```

## Examples

## Example 1: settings tabs

```
┌─────────────────────────────────────────┐
│ General │ Security │ Users             │
├─────────────────────────────────────────┤
│                                         │
│   Show settings                         │
│                                         │
└─────────────────────────────────────────┘
```

## Example 2: profile tabs

```
┌─────────────────────────────────────────┐
│ Overview │ Posts │ Photos │ Friends     │
├─────────────────────────────────────────┤
│                                         │
│   Profile content                       │
│                                         │
└─────────────────────────────────────────┘
```

## Example 3: Form-Tabs

```
┌─────────────────────────────────────────┐
│ Step 1 │ Step 2 │ Step 3                │
├─────────────────────────────────────────┤
│                                         │
│   Form content                          │
│                                         │
└─────────────────────────────────────────┘
```

## Example 4: chat tabs

```
┌─────────────────────────────────────────┐
│ Chat │ Groups │ Requests │ Archive      │
├─────────────────────────────────────────┤
│                                         │
│   Chat content                          │
│                                         │
└─────────────────────────────────────────┘
```

## Example 5: documentation tabs

```
┌─────────────────────────────────────────┐
│ Overview │ Installation │ Usage         │
│ API      │ Example      │               │
├─────────────────────────────────────────┤
│                                         │
│   Documentation content                 │
│                                         │
└─────────────────────────────────────────┘
```
