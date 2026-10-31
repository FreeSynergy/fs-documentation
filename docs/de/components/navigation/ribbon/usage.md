# Ribbon - Verwendung

## Einfaches Ribbon

```jsx
<Ribbon 
  tabs={[
    { id: 'home', label: 'Home', groups: [...] },
    { id: 'insert', label: 'Insert', groups: [...] },
    { id: 'design', label: 'Design', groups: [...] }
  ]}
  activeTab="home"
  onChange={(id) => setActiveTab(id)}
/>
```

## Mit Groups und Commands

```jsx
<Ribbon 
  tabs={[{
    id: 'home',
    label: 'Home',
    groups: [
      {
        label: 'Schrift',
        commands: [
          { id: 'bold', icon: 'bold', onClick: ... },
          { id: 'italic', icon: 'italic', onClick: ... }
        ]
      }
    ]
  }]}
/>
```

## Minimized Ribbon

```jsx
<Ribbon 
  tabs={tabs}
  minimized={true}
  collapsible={true}
/>
```

## In App

```jsx
<AppShell>
  <Ribbon 
    tabs={ribbonTabs}
    activeTab="home"
  />
  <Content />
</AppShell>
```

## Mit Event-Handlern

```jsx
<Ribbon 
  tabs={tabs}
  onSelect={(tabId, commandId) => console.log('Command:', commandId)}
/>
```
