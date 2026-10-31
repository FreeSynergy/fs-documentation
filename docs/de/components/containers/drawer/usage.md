# Drawer (Seitenleiste) - Verwendung

## Einfacher Drawer

```jsx
<Drawer 
  title="Menü"
  isOpen={isOpen}
  onClose={() => setIsOpen(false)}
>
  <Menu 
    items={menuItems}
    onClick={(item) => handleNavigation(item)}
  />
</Drawer>
```

## In App

```jsx
<AppShell>
  <Header>
    <Button onClick={() => setIsOpen(true)}>
      ☰ Menü
    </Button>
  </Header>
  <Drawer 
    title="Menü"
    isOpen={isOpen}
    onClose={() => setIsOpen(false)}
  >
    <Menu items={menuItems} />
  </Drawer>
  <Content />
</AppShell>
```

## Mit Formular

```jsx
<Drawer 
  title="Filter"
  isOpen={isOpen}
  onClose={() => setIsOpen(false)}
>
  <form>
    <Select label="Status" options={statusOptions} />
    <DateInput label="Von" value={from} onChange={setFrom} />
    <DateInput label="Bis" value={to} onChange={setTo} />
  </form>
</Drawer>
```

## Mit Event-Handlern

```jsx
<Drawer 
  title="Menü"
  isOpen={isOpen}
  onOpen={() => console.log('Open')}
  onClose={() => console.log('Close')}
/>
```
