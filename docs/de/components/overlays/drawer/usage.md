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

## Beispiele

## Beispiel 1: Mobile-Menu

```
┌─────────────────────────────────────────┐
│  ☰ Menü                                 │
├─────────────────────────────────────────┤
│ 🏠 Home                                 │
│ ℹ️ About                                │
│ 🛍️ Shop                                │
│ 📝 Blog                                 │
│ 👥 Profil                               │
├─────────────────────────────────────────┤
│ ⚙️ Einstellungen                        │
│ ❓ Hilfe                                │
└─────────────────────────────────────────┘
```

## Beispiel 2: Filter-Drawer

```
┌─────────────────────────────────────────┐
│  🔍 Filter                              │
├─────────────────────────────────────────┤
│ Status:                                 │
│   [✓] Offen                             │
│   [ ] Geschlossen                       │
│                                         │
│ Priorität:                              │
│   [✓] Hoch                              │
│   [ ] Mittel                            │
│   [ ] Niedrig                           │
│                                         │
│ [Reset] [Anwenden]                      │
└─────────────────────────────────────────┘
```

## Beispiel 3: Profil-Drawer

```
┌─────────────────────────────────────────┐
│  👤 Profil                              │
├─────────────────────────────────────────┤
│  🖼️ John Doe                            │
│  Developer                             │
│  john@example.com                      │
├─────────────────────────────────────────┤
│ [Einstellungen]                         │
│ [Abmelden]                              │
└─────────────────────────────────────────┘
```

## Beispiel 4: Sidebar (Links)

```
┌─────────────────────────────────────────┐
│  📱 Menü                                │
├─────────────────────────────────────────┤
│ 🏠 Dashboard                            │
│ 📩 Nachrichten                          │
│ 📅 Kalender                             │
│ 👥 Kontakte                             │
├─────────────────────────────────────────┤
│ 📊 Reports                              │
│ ⚙️ Einstellungen                        │
└─────────────────────────────────────────┘
```

## Beispiel 5: Checkout-Drawer

```
┌─────────────────────────────────────────┐
│  🛒 Warenkorb                           │
├─────────────────────────────────────────┤
│  [✕] Produkt 1        x2  €29,99        │
│  [✕] Produkt 2        x1  €19,99        │
│                                         │
│  ─────────────────────────              │
│  Summe: €79,97                          │
│                                         │
│  [Weiter]                                │
└─────────────────────────────────────────┘
```
