# Drawer - Usage

## Simple drawer

```jsx
<Drawer 
  title="Menu"
  isOpen={isOpen}
  onClose={() => setIsOpen(false)}
>
  <Menu 
    items={menuItems}
    onClick={(item) => handleNavigation(item)}
  />
</Drawer>
```

## In an app

```jsx
<AppShell>
  <Header>
    <Button onClick={() => setIsOpen(true)}>
      ☰ Menu
    </Button>
  </Header>
  <Drawer 
    title="Menu"
    isOpen={isOpen}
    onClose={() => setIsOpen(false)}
  >
    <Menu items={menuItems} />
  </Drawer>
  <Content />
</AppShell>
```

## With form

```jsx
<Drawer 
  title="Filter"
  isOpen={isOpen}
  onClose={() => setIsOpen(false)}
>
  <form>
    <Select label="Status" options={statusOptions} />
    <DateInput label="From" value={from} onChange={setFrom} />
    <DateInput label="To" value={to} onChange={setTo} />
  </form>
</Drawer>
```

## With event handlers

```jsx
<Drawer 
  title="Menu"
  isOpen={isOpen}
  onOpen={() => console.log('Open')}
  onClose={() => console.log('Close')}
/>
```

## Examples

## Example 1: Mobile menu

```
┌─────────────────────────────────────────┐
│  ☰ Menu                                 │
├─────────────────────────────────────────┤
│ 🏠 Home                                 │
│ ℹ️ About                                │
│ 🛍️ Shop                                │
│ 📝 Blog                                 │
│ 👥 Profile                              │
├─────────────────────────────────────────┤
│ ⚙️ Settings                             │
│ ❓ Help                                 │
└─────────────────────────────────────────┘
```

## Example 2: Filter-Drawer

```
┌─────────────────────────────────────────┐
│  🔍 Filter                              │
├─────────────────────────────────────────┤
│ Status:                                 │
│   [✓] Open                              │
│   [ ] Closed                            │
│                                         │
│ Priority:                               │
│   [✓] High                              │
│   [ ] Medium                            │
│   [ ] Low                               │
│                                         │
│ [Reset] [Apply]                         │
└─────────────────────────────────────────┘
```

## Example 3: Profile drawer

```
┌─────────────────────────────────────────┐
│  👤 Profile                             │
├─────────────────────────────────────────┤
│  🖼️ John Doe                            │
│  Developer                             │
│  john@example.com                      │
├─────────────────────────────────────────┤
│ [Settings]                              │
│ [Sign out]                              │
└─────────────────────────────────────────┘
```

## Example 4: Sidebar (left)

```
┌─────────────────────────────────────────┐
│  📱 Menu                                │
├─────────────────────────────────────────┤
│ 🏠 Dashboard                            │
│ 📩 Messages                             │
│ 📅 Calendar                             │
│ 👥 Contacts                             │
├─────────────────────────────────────────┤
│ 📊 Reports                              │
│ ⚙️ Settings                             │
└─────────────────────────────────────────┘
```

## Example 5: Checkout-Drawer

```
┌─────────────────────────────────────────┐
│  🛒 Cart                                │
├─────────────────────────────────────────┤
│  [✕] Product 1        x2  €29,99        │
│  [✕] Product 2        x1  €19,99        │
│                                         │
│  ─────────────────────────              │
│  Total: €79.97                          │
│                                         │
│  [Continue]                              │
└─────────────────────────────────────────┘
```
