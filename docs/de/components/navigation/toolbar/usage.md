# Toolbar - Verwendung

## Einfache Toolbar

```jsx
<Toolbar 
  buttons={[
    { id: 'new', icon: 'plus', label: 'Neu', onClick: ... },
    { id: 'save', icon: 'save', label: 'Speichern', onClick: ... },
    { id: 'delete', icon: 'trash', label: 'Löschen', onClick: ... }
  ]}
/>
```

## Mit Separatoren

```jsx
<Toolbar 
  buttons={[
    { id: 'new', icon: 'plus', label: 'Neu' },
    { id: 'open', icon: 'folder', label: 'Öffnen' },
    { separator: true },
    { id: 'copy', icon: 'copy', label: 'Kopieren' },
    { id: 'paste', icon: 'paste', label: 'Einfügen' }
  ]}
/>
```

## Floating Toolbar

```jsx
<FloatingToolbar 
  buttons={actionButtons}
  position="bottom-right"
/>
```

## In App

```jsx
<AppShell>
  <Header />
  <Toolbar 
    buttons={toolbarButtons}
    position="top"
  />
  <Content />
</AppShell>
```

## Mit Event-Handlern

```jsx
<Toolbar 
  buttons={buttons}
  onButtonClick={(id) => console.log('Clicked:', id)}
/>
```
