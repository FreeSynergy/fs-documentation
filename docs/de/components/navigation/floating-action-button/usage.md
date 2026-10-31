# Floating Action Button - Verwendung

## Standard FAB

```jsx
<FAB 
  icon="plus"
  onClick={() => console.log('Neu')}
/>
```

## Extended FAB (Mit Text)

```jsx
<FAB 
  variant="extended"
  icon="plus"
  label="Neu"
  onClick={() => console.log('Neu')}
/>
```

## Mit Badge

```jsx
<FAB 
  icon="mail"
  showBadge={true}
  badgeValue="3"
/>
```

## In App

```jsx
<AppShell>
  <Content />
  <FAB 
    icon="plus"
    position="bottom-right"
    onClick={createNewItem}
  />
</AppShell>
```

## Mit Event-Handlern

```jsx
<FAB 
  icon="plus"
  onHover={() => console.log('Hover')}
  onClick={() => console.log('Clicked')}
/>
```
