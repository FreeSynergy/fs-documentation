# Menu - Verwendung

## Einfaches Menü

```jsx
<Menu 
  items={[
    { id: 'home', label: 'Start', href: '/' },
    { id: 'about', label: 'Über uns', href: '/about' },
    { id: 'services', label: 'Leistungen', href: '/services' }
  ]}
  activeItem="home"
  onChange={(id) => setActiveItem(id)}
/>
```

## Mit Aufklappmenüs

```jsx
<Menu 
  items={[
    { id: 'home', label: 'Start', href: '/' },
    { 
      id: 'products', 
      label: 'Produkte', 
      dropdown: [
        { id: 'product1', label: 'Produkt 1' },
        { id: 'product2', label: 'Produkt 2' }
      ]
    }
  ]}
/>
```

## Vertikales Menü

```jsx
<Menu 
  items={items}
  variant="vertical"
  size="large"
/>
```

## In einer Kopfleiste

```jsx
<Header>
  <Logo />
  <Menu 
    items={menuItems}
    variant="horizontal"
  />
</Header>
```

## Mit Ereignis-Handlern

```jsx
<Menu 
  items={items}
  onSelect={(id) => console.log('Selected:', id)}
  onOpen={(id) => console.log('Opened:', id)}
/>
```

## Beispiele

## Beispiel 1: Hauptnavigation

```
┌─────────────────────────────────────────┐
│ Start │ Über uns │ Leistungen │ Preise │ Blog │
└─────────────────────────────────────────┘
```

## Beispiel 2: Seitenleisten-Menü

```
┌─────────┐
│ 🏠 Start│
│ 📚 Wiki │
│ 💬 Chat │
│ 📅 Kal. │
│ 👥 Prof.│
├─────────┤
│ ⚙️ Einst.│
└─────────┘
```

## Beispiel 3: Aufklappmenü

```
┌─────────────────────────────────────────┐
│ Start │ Produkte ▼ │ Lösungen ▼ │ Kontakt │
├─────────────────────────────────────────┤
│   Untermenü                             │
│   Untermenü 2                           │
└─────────────────────────────────────────┘
```

## Beispiel 4: Mobil-Menü (Hamburger)

```
┌─────────────────────────────────────────┐
│ ☰ Start │ Über uns │ Leistungen │ Kontakt │
└─────────────────────────────────────────┘
```

## Beispiel 5: Tab-Menü

```
┌─────────────────────────────────────────┐
│ Tab 1 │ Tab 2 │ Tab 3 │ Tab 4          │
├─────────────────────────────────────────┤
│                                         │
│   Inhalt                                │
│                                         │
└─────────────────────────────────────────┘
