# Menu (Menü) - Verwendung

## Einfaches Menu

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

## Mit Dropdowns

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

## Vertical Menu

```jsx
<Menu 
  items={items}
  variant="vertical"
  size="large"
/>
```

## In Header

```jsx
<Header>
  <Logo />
  <Menu 
    items={menuItems}
    variant="horizontal"
  />
</Header>
```

## Mit Event-Handlern

```jsx
<Menu 
  items={items}
  onSelect={(id) => console.log('Selected:', id)}
  onOpen={(id) => console.log('Opened:', id)}
/>
```
