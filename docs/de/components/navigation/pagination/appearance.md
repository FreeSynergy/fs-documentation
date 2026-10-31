# Pagination - Aussehen

## Grundlayout

Pagination ist eine Navigation für große Listen, die Daten in Seiten aufteilt.

## Layout-Varianten

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

## Größe-Varianten

| Größe | Schriftgröße | Verwendung |
|-------|-------------|------------|
| Small | 12px | Inline |
| Medium | 14px | Standard |
| Large | 16px | Featured |

## Farb-Varianten

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Active** | Primärfarbe | Aktuelle Seite |
| **Inactive** | Grau | Inaktive Seiten |
| **Hover** | Heller | Hover-Zustand |
| **Disabled** | Grau | Deaktivierte Buttons |

## Features

- **Total Items**: Gesamtanzahl der Elemente
- **Current Page**: Aktuelle Seite
- **Items per Page**: Elemente pro Seite
- **Jump to Page**: Direkt zu Seite springen
- **Page Size Selector**: Anzahl pro Seite ändern

## Responsive Verhalten

| Breakpoint | Verhalten |
|------------|-----------|
| Desktop (>768px) | Volle Pagination sichtbar |
| Tablet (480-768px) | Kompakt |
| Mobile (<480px) | Previous/Next oder Load More |
