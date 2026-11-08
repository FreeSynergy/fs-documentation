# Breadcrumb - Verwendung

## Einfacher Breadcrumb

```jsx
<Breadcrumb 
  items={[
    { label: 'Start', href: '/' },
    { label: 'Wiki', href: '/wiki' },
    { label: 'Seite', href: '/wiki/seite' }
  ]}
/>
```

## Mit Icons

```jsx
<Breadcrumb 
  items={[
    { label: 'Start', icon: 'home', href: '/' },
    { label: 'Wiki', icon: 'book', href: '/wiki' },
    { label: 'Seite', icon: 'file', href: '/wiki/seite' }
  ]}
  showIcons={true}
/>
```

## Mit Trennzeichen

```jsx
<Breadcrumb 
  items={items}
  separator="›"
/>
```

## Eingeklappter Breadcrumb

```jsx
<Breadcrumb 
  items={longItems}
  collapsed={true}
/>
```

## Im Header

```jsx
<Header>
  <Breadcrumb 
    items={breadcrumbItems}
    showIcons={true}
  />
  <h1>Aktuelle Seite</h1>
</Header>
```

## Mit Ereignis-Handlern

```jsx
<Breadcrumb 
  items={items}
  onClick={(item, index) => navigate(item.href)}
/>
```

## Beispiele

## Beispiel 1: Wiki-Seite

```
┌─────────────────────────────────────────┐
│ Start > Wiki > Dokumentation > Komponenten │
├─────────────────────────────────────────┤
│                                         │
│   Inhalt der Dokumentation              │
│                                         │
└─────────────────────────────────────────┘
```

## Beispiel 2: Datei-Explorer

```
┌─────────────────────────────────────────┐
│ 🏠 Start > 📁 Dokumente > 📁 Projekte   │
├─────────────────────────────────────────┤
│                                         │
│   Datei-Liste                           │
│                                         │
└─────────────────────────────────────────┘
```

## Beispiel 3: E-Commerce

```
┌─────────────────────────────────────────┐
│ 🏠 Start > 🛍️ Shop > 📦 Produkte       │
├─────────────────────────────────────────┤
│                                         │
│   Produktübersicht                      │
│                                         │
└─────────────────────────────────────────┘
```

## Beispiel 4: Benutzerprofile

```
┌─────────────────────────────────────────┐
│ 👥 Nutzer > 🧑 John Doe > 📝 Beiträge   │
├─────────────────────────────────────────┤
│                                         │
│   Beiträge anzeigen                     │
│                                         │
└─────────────────────────────────────────┘
```

## Beispiel 5: Dokumentenverwaltung

```
┌─────────────────────────────────────────┐
│ 📁 Dokumente > 📄 Verträge > 2024       │
├─────────────────────────────────────────┤
│                                         │
│   Vertragsübersicht                     │
│                                         │
└─────────────────────────────────────────┘
```
