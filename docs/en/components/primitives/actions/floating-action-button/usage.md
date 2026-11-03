# Floating Action Button - Usage

## Standard FAB

```jsx
<FAB 
  icon="plus"
  onClick={() => console.log('New')}
/>
```

## Extended FAB (with text)

```jsx
<FAB 
  variant="extended"
  icon="plus"
  label="New"
  onClick={() => console.log('New')}
/>
```

## With a badge

```jsx
<FAB 
  icon="mail"
  showBadge={true}
  badgeValue="3"
/>
```

## In an app

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

## With event handlers

```jsx
<FAB 
  icon="plus"
  onHover={() => console.log('Hover')}
  onClick={() => console.log('Clicked')}
/>
```

## Examples

## Example 1: mail app

```
                    ┌─────────┐
                    │   +     │
                    │ (2)     │
                    └─────────┘
```

## Example 2: todo app

```
                    ┌──────────────┐
                    │   +  Task    │
                    └──────────────┘
```

## Example 3: chat app

```
                    ┌─────────┐
                    │   +     │
                    │ (5)     │
                    └─────────┘
```

## Example 4: gallery app

```
                    ┌──────────────┐
                    │  📷  New     │
                    └──────────────┘
```

## Example 5: dashboard

```
                    ┌─────────┐
                    │   +     │
                    └─────────┘
```
