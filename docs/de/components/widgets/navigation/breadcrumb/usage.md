# Breadcrumb - Verwendung

## Einfaches Breadcrumb

```jsx
<Breadcrumb 
  items={[
    { label: 'Home', href: '/' },
    { label: 'Wiki', href: '/wiki' },
    { label: 'Seite', href: '/wiki/seite' }
  ]}
/>
```

## Mit Icons

```jsx
<Breadcrumb 
  items={[
    { label: 'Home', icon: 'home', href: '/' },
    { label: 'Wiki', icon: 'book', href: '/wiki' },
    { label: 'Seite', icon: 'file', href: '/wiki/seite' }
  ]}
  showIcons={true}
/>
```

## Mit Separator

```jsx
<Breadcrumb 
  items={items}
  separator="›"
/>
```

## Collapsed Breadcrumb

```jsx
<Breadcrumb 
  items={longItems}
  collapsed={true}
/>
```

## In Header

```jsx
<Header>
  <Breadcrumb 
    items={breadcrumbItems}
    showIcons={true}
  />
  <h1>Aktuelle Seite</h1>
</Header>
```

## Mit Event-Handlern

```jsx
<Breadcrumb 
  items={items}
  onClick={(item, index) => navigate(item.href)}
/>
```

## Beispiele

## Beispiel 1: Wiki-Page

```
┌─────────────────────────────────────────┐
│ Home > Wiki > Dokumentation > Komponenten│
├─────────────────────────────────────────┤
│                                         │
│   Dokumentations-Inhalt                 │
│                                         │
└─────────────────────────────────────────┘
```

## Beispiel 2: Datei-Explorer

```
┌─────────────────────────────────────────┐
│ 🏠 Home > 📁 Dokumente > 📁 Projekte    │
├─────────────────────────────────────────┤
│                                         │
│   Datei-Liste                           │
│                                         │
└─────────────────────────────────────────┘
```

## Beispiel 3: E-Commerce

```
┌─────────────────────────────────────────┐
│ 🏠 Home > 🛍️ Shop > 📦 Produkte         │
├─────────────────────────────────────────┤
│                                         │
│   Produktübersicht                      │
│                                         │
└─────────────────────────────────────────┘
```

## Beispiel 4: Benutzer-Profile

```
┌─────────────────────────────────────────┐
│ 👥 Nutzer > 🧑 John Doe > 📝 Beiträge   │
├─────────────────────────────────────────┤
│                                         │
│   Beiträge anzeigen                     │
│                                         │
└─────────────────────────────────────────┘
```

## Beispiel 5: Dokument-Management

```
┌─────────────────────────────────────────┐
│ 📁 Dokumente > 📄 Verträge > 2024       │
├─────────────────────────────────────────┤
│                                         │
│   Vertrags-Übersicht                    │
│                                         │
└─────────────────────────────────────────┘
```
