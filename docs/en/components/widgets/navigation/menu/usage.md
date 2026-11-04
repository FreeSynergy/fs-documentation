# Menu - Usage

## Simple menu

```jsx
<Menu 
  items={[
    { id: 'home', label: 'Home', href: '/' },
    { id: 'about', label: 'About', href: '/about' },
    { id: 'services', label: 'Services', href: '/services' }
  ]}
  activeItem="home"
  onChange={(id) => setActiveItem(id)}
/>
```

## With dropdowns

```jsx
<Menu 
  items={[
    { id: 'home', label: 'Home', href: '/' },
    { 
      id: 'products', 
      label: 'Products', 
      dropdown: [
        { id: 'product1', label: 'Product 1' },
        { id: 'product2', label: 'Product 2' }
      ]
    }
  ]}
/>
```

## Vertical menu

```jsx
<Menu 
  items={items}
  variant="vertical"
  size="large"
/>
```

## In a header

```jsx
<Header>
  <Logo />
  <Menu 
    items={menuItems}
    variant="horizontal"
  />
</Header>
```

## With event handlers

```jsx
<Menu 
  items={items}
  onSelect={(id) => console.log('Selected:', id)}
  onOpen={(id) => console.log('Opened:', id)}
/>
```

## Examples

## Example 1: main navigation

```
┌─────────────────────────────────────────┐
│ Home │ About │ Services │ Pricing │ Blog │
└─────────────────────────────────────────┘
```

## Example 2: sidebar menu

```
┌─────────┐
│ 🏠 Home │
│ 📚 Wiki │
│ 💬 Chat │
│ 📅 Cal. │
│ 👥 Prof.│
├─────────┤
│ ⚙️ Set. │
└─────────┘
```

## Example 3: dropdown menu

```
┌─────────────────────────────────────────┐
│ Home │ Products ▼ │ Solutions ▼ │ Contact│
├─────────────────────────────────────────┤
│   Submenu                               │
│   Submenu 2                             │
└─────────────────────────────────────────┘
```

## Example 4: mobile menu (hamburger)

```
┌─────────────────────────────────────────┐
│ ☰ Home │ About │ Services │ Contact     │
└─────────────────────────────────────────┘
```

## Example 5: tab menu

```
┌─────────────────────────────────────────┐
│ Tab 1 │ Tab 2 │ Tab 3 │ Tab 4          │
├─────────────────────────────────────────┤
│                                         │
│   Content                               │
│                                         │
└─────────────────────────────────────────┘
```