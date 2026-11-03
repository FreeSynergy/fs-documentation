# Bottom Navigation - Usage

## Simple bottom navigation

```jsx
<BottomNavigation 
  items={[
    { id: 'home', icon: 'home', label: 'Home' },
    { id: 'mail', icon: 'mail', label: 'Mail' },
    { id: 'calendar', icon: 'calendar', label: 'Calendar' }
  ]}
  activeItem="home"
  onChange={(id) => console.log('Selected:', id)}
/>
```

## With Text Labels

```jsx
<BottomNavigation 
  items={items}
  variant="icon-text"
/>
```

## Icon Only

```jsx
<BottomNavigation 
  items={items}
  variant="icon-only"
  showLabels={false}
/>
```

## In an app

```jsx
<AppShell>
  <Content />
  <BottomNavigation 
    items={navItems}
    activeItem={activeItem}
    onChange={handleNavChange}
  />
</AppShell>
```

## With event handlers

```jsx
<BottomNavigation 
  items={items}
  onSelect={(id) => console.log('Selected:', id)}
  onHover={(id) => console.log('Hover:', id)}
/>
```

## Examples

## Example 1: mail app

```
┌─────────────────────────────────────────┐
│ 🏠  📩  📅  👥  ⚙️                     │
│ Home Mail Cal Cont. Settings            │
└─────────────────────────────────────────┘
```

## Example 2: chat app

```
┌─────────────────────────────────────────┐
│ 🗨️  📝  🔍  ⭐  👤                     │
│ Chat  New  Search  Favorites  Profile   │
└─────────────────────────────────────────┘
```

## Example 3: E-Commerce

```
┌─────────────────────────────────────────┐
│ 🏠  🔍  📦  ⭐  👤                     │
│ Home  Search  Orders  Favorites  Profile│
└─────────────────────────────────────────┘
```

## Example 4: Social Media

```
┌─────────────────────────────────────────┐
│ 🏠  🔍  📝  ❤️  👤                     │
│ Home  Search  Post  Likes  Profile      │
└─────────────────────────────────────────┘
```

## Example 5: Dashboard

```
┌─────────────────────────────────────────┐
│ 📊  📈  💰  👥  ⚙️                     │
│ Stats  Analytics  Finance  Users  Settings│
└─────────────────────────────────────────┘
```
