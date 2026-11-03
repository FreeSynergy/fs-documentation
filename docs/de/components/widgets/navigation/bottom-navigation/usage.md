# Bottom Navigation - Verwendung

## Einfache Bottom Navigation

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

## In App

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

## Mit Event-Handlern

```jsx
<BottomNavigation 
  items={items}
  onSelect={(id) => console.log('Selected:', id)}
  onHover={(id) => console.log('Hover:', id)}
/>
```

## Beispiele

## Beispiel 1: Mail-App

```
┌─────────────────────────────────────────┐
│ 🏠  📩  📅  👥  ⚙️                     │
│ Home Mail Cal Cont. Settings            │
└─────────────────────────────────────────┘
```

## Beispiel 2: Chat-App

```
┌─────────────────────────────────────────┐
│ 🗨️  📝  🔍  ⭐  👤                     │
│ Chat  New  Search  Favorites  Profile   │
└─────────────────────────────────────────┘
```

## Beispiel 3: E-Commerce

```
┌─────────────────────────────────────────┐
│ 🏠  🔍  📦  ⭐  👤                     │
│ Home  Search  Orders  Favorites  Profile│
└─────────────────────────────────────────┘
```

## Beispiel 4: Social Media

```
┌─────────────────────────────────────────┐
│ 🏠  🔍  📝  ❤️  👤                     │
│ Home  Search  Post  Likes  Profile      │
└─────────────────────────────────────────┘
```

## Beispiel 5: Dashboard

```
┌─────────────────────────────────────────┐
│ 📊  📈  💰  👥  ⚙️                     │
│ Stats  Analytics  Finance  Users  Settings│
└─────────────────────────────────────────┘
```
