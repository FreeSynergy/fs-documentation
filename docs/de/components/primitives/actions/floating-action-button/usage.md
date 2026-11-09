# Floating Action Button – Verwendung

## Standard-FAB

```jsx
<FAB 
  icon="plus"
  onClick={() => console.log('New')}
/>
```

## Erweiterter FAB (mit Text)

```jsx
<FAB 
  variant="extended"
  icon="plus"
  label="New"
  onClick={() => console.log('New')}
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

## In einer App

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

## Mit Ereignis-Handlern

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

## Beispiel 2: Aufgaben-App

```
                    ┌──────────────┐
                    │   +  Task    │
                    └──────────────┘
```

## Beispiel 3: Chat-App

```
                    ┌─────────┐
                    │   +     │
                    │ (5)     │
                    └─────────┘
```

## Beispiel 4: Galerie-App

```
                    ┌──────────────┐
                    │  📷  New     │
                    └──────────────┘
```

## Beispiel 5: Dashboard

```
                    ┌─────────┐
                    │   +     │
                    └─────────┘
```
