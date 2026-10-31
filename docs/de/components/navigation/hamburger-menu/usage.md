# Hamburger Menu - Verwendung

## Einfaches Hamburger Menu

```jsx
<HamburgerMenu 
  isOpen={isOpen}
  onToggle={() => setIsOpen(!isOpen)}
/>
```

## In Header

```jsx
<Header>
  <HamburgerMenu 
    isOpen={isOpen}
    onToggle={() => setIsOpen(!isOpen)}
    items={menuItems}
  />
  <Logo />
</Header>
```

## In Drawer

```jsx
<Drawer 
  isOpen={isOpen}
  onClose={() => setIsOpen(false)}
>
  <HamburgerMenu 
    isOpen={isOpen}
    items={menuItems}
  />
</Drawer>
```

## Mit Event-Handlern

```jsx
<HamburgerMenu 
  isOpen={isOpen}
  onOpen={() => console.log('Open')}
  onClose={() => console.log('Close')}
  onClick={() => console.log('Clicked')}
/>
```
