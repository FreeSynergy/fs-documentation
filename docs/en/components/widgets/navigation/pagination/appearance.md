# Pagination - Appearance

## Base layout

Pagination ist eine Navigation für große Listen, die Daten in Seiten aufteilt.

## Variants

### Numeric (Numerisch)

```
┌─────────────────────────────────────────┐
│ [◀] 1 2 3 4 5 [▶]                       │
└─────────────────────────────────────────┘
```

### Previous/Next

```
┌─────────────────────────────────────────┐
│ [◀ Zurück] [Weiter ▶]                   │
└─────────────────────────────────────────┘
```

### Load More

```
┌─────────────────────────────────────────┐
│ [Mehr laden]                            │
└─────────────────────────────────────────┘
```

### Infinite Scroll

```
┌─────────────────────────────────────────┐
│ (Automatisch nachladen beim Scrollen)   │
└─────────────────────────────────────────┘
```

## Sizes

| Size | Font size | Use |
| ------- | ------------- | ------------ |
| Small | 12px | Inline |
| Medium | 14px | Standard |
| Large | 16px | Featured |

## Colours and states

| State | Colour | Description |
| -------- | ------- | -------------- |
| **Active** | Primärfarbe | Aktuelle Seite |
| **Inactive** | Grau | Inaktive Seiten |
| **Hover** | Heller | hover state |
| **Disabled** | Grau | Deaktivierte Buttons |

## Hover and focus effects

| Effect | Description |
| -------- | -------------- |
| `background` | Seitenzahl bekommt eine Fläche |
| `ring` | Fokus-Ring bei Tastaturnavigation |
| `underline` | Unterstrich beim aktiven Eintrag |
| `none` | deaktivierte Pfeile ohne Rückmeldung |

## Responsive

| Breakpoint | Behaviour |
| ------------ | ----------- |
| Desktop (>768px) | Volle Pagination sichtbar |
| Tablet (480-768px) | Kompakt |
| Mobile (<480px) | Previous/Next oder Load More |

## Features

- **Total Items**: Gesamtanzahl der Elemente
- **Current Page**: Aktuelle Seite
- **Items per Page**: Elemente pro Seite
- **Jump to Page**: Direkt zu Seite springen
- **Page Size Selector**: Anzahl pro Seite ändern
