# Bottom Navigation - Verwendung

## Einfache Bottom Navigation

```jsx
<BottomNavigation 
  items={[
    { id: 'home', icon: 'home', label: 'Start' },
    { id: 'mail', icon: 'mail', label: 'Post' },
    { id: 'calendar', icon: 'calendar', label: 'Kalender' }
  ]}
  activeItem="home"
  onChange={(id) => console.log('Ausgewählt:', id)}
/>
```

## Mit Textbeschriftung

```jsx
<BottomNavigation 
  items={items}
  variant="icon-text"
/>
```

## Nur Icon

```jsx
<BottomNavigation 
  items={items}
  variant="icon-only"
  showLabels={false}
/>
```

## In einer App

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

## Mit Ereignis-Handlern

```jsx
<BottomNavigation 
  items={items}
  onSelect={(id) => console.log('Ausgewählt:', id)}
  onHover={(id) => console.log('Hover:', id)}
/>
```

## Beispiele

## Beispiel 1: Mail-App

```
┌─────────────────────────────────────────┐
│ 🏠  📩  📅  👥  ⚙️                     │
│ Start Post Kal. Kont. Einst.            │
└─────────────────────────────────────────┘
```

## Beispiel 2: Chat-App

```
┌─────────────────────────────────────────┐
│ 🗨️  📝  🔍  ⭐  👤                     │
│ Chat  Neu  Suche  Favoriten  Profil     │
└─────────────────────────────────────────┘
```

## Beispiel 3: E-Commerce

```
┌─────────────────────────────────────────┐
│ 🏠  🔍  📦  ⭐  👤                     │
│ Start  Suche  Bestellungen  Favoriten  Profil│
└─────────────────────────────────────────┘
```

## Beispiel 4: Social Media

```
┌─────────────────────────────────────────┐
│ 🏠  🔍  📝  ❤️  👤                     │
│ Start  Suche  Beitrag  Likes  Profil    │
└─────────────────────────────────────────┘
```

## Beispiel 5: Dashboard

```
┌─────────────────────────────────────────┐
│ 📊  📈  💰  👥  ⚙️                     │
│ Statistik  Analyse  Finanzen  Nutzer  Einstellungen│
└─────────────────────────────────────────┘
```
