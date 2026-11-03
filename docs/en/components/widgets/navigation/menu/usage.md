# Menu (Menü) - Usage

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

## With event handlers

```jsx
<Menu 
  items={items}
  onSelect={(id) => console.log('Selected:', id)}
  onOpen={(id) => console.log('Opened:', id)}
/>
```

## Examples

## Example 1: Hauptnavigation

```
┌─────────────────────────────────────────┐
│ Home │ About │ Services │ Pricing │ Blog │
└─────────────────────────────────────────┘
```

## Example 2: Sidebar-Menu

```
┌─────────┐
│ 🏠 Home │
│ 📚 Wiki │
│ 💬 Chat │
│ 📅 Kal. │
│ 👥 Prof.│
├─────────┤
│ ⚙️ Einst.│
└─────────┘
```

## Example 3: Dropdown-Menu

```
┌─────────────────────────────────────────┐
│ Home │ Produkte ▼ │ Lösungen ▼ │ Kontakt │
├─────────────────────────────────────────┤
│   Untermenü                             │
│   Untermenü 2                           │
└─────────────────────────────────────────┘
```

## Example 4: Mobile-Menu (Hamburger)

```
┌─────────────────────────────────────────┐
│ ☰ Home │ About │ Services │ Contact     │
└─────────────────────────────────────────┘
```

## Example 5: Tab-Menu

```
┌─────────────────────────────────────────┐
│ Tab 1 │ Tab 2 │ Tab 3 │ Tab 4          │
├─────────────────────────────────────────┤
│                                         │
│   Inhalt                                │
│                                         │
└─────────────────────────────────────────┘
```