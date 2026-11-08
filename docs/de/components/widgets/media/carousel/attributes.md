# Carousel - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `images` | array[] | - | Array mit Bildern |
| `autoplay` | boolean | `false` | automatisch abspielen? |
| `interval` | number | `5000` | Intervall in ms |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `loop` | boolean | `true` | endlose Schleife? |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onSlideChange` | function | wird ausgeführt, wenn sich die Folie ändert |
| `onHover` | function | wird beim Hover ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `region` |

## Bild-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `src` | string | URL des Bildes |
| `alt` | string | Alternativtext |
| `title` | string | Titel |

## Navigations-Attribute

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `showNavigation` | boolean | `true` | Navigation anzeigen? |
| `showThumbnails` | boolean | `true` | Vorschaubilder anzeigen? |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../../primitives/basics/base.md)
