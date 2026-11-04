# Breadcrumb - Usage

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

## With icons

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

## With separator

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

## With event handlers

```jsx
<Breadcrumb 
  items={items}
  onClick={(item, index) => navigate(item.href)}
/>
```

## Examples

## Example 1: Wiki-Page

```
┌─────────────────────────────────────────┐
│ Home > Wiki > Documentation > Components │
├─────────────────────────────────────────┤
│                                         │
│   Documentation content                 │
│                                         │
└─────────────────────────────────────────┘
```

## Example 2: Datei-Explorer

```
┌─────────────────────────────────────────┐
│ 🏠 Home > 📁 Dokumente > 📁 Projekte    │
├─────────────────────────────────────────┤
│                                         │
│   Datei-Liste                           │
│                                         │
└─────────────────────────────────────────┘
```

## Example 3: E-Commerce

```
┌─────────────────────────────────────────┐
│ 🏠 Home > 🛍️ Shop > 📦 Produkte         │
├─────────────────────────────────────────┤
│                                         │
│   Product overview                      │
│                                         │
└─────────────────────────────────────────┘
```

## Example 4: user profiles

```
┌─────────────────────────────────────────┐
│ 👥 Users > 🧑 John Doe > 📝 Posts        │
├─────────────────────────────────────────┤
│                                         │
│   Show posts                            │
│                                         │
└─────────────────────────────────────────┘
```

## Example 5: Dokument-Management

```
┌─────────────────────────────────────────┐
│ 📁 Documents > 📄 Contracts > 2024       │
├─────────────────────────────────────────┤
│                                         │
│   Contract overview                     │
│                                         │
└─────────────────────────────────────────┘
```
