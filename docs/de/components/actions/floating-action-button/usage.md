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

## Beispiele

## Beispiel 1: Mail-App

```
                    ┌─────────┐
                    │   +     │
                    │ (2)     │
                    └─────────┘
```

## Beispiel 2: Todo-App

```
                    ┌──────────────┐
                    │   +  Aufgabe │
                    └──────────────┘
```

## Beispiel 3: Chat-App

```
                    ┌─────────┐
                    │   +     │
                    │ (5)     │
                    └─────────┘
```

## Beispiel 4: Gallery-App

```
                    ┌──────────────┐
                    │  📷  Neues  │
                    └──────────────┘
```

## Beispiel 5: Dashboard

```
                    ┌─────────┐
                    │   +     │
                    └─────────┘
```
