# Drawer (Seitenleiste) - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `title` | string | - | Titel |
| `isOpen` | boolean | `false` | Ist geöffnet? |
| `onClose` | function | - | Event beim Schließen |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `position` | enum | `left` | Position: `left`, `right`, `top`, `bottom` |
| `closable` | boolean | `true` | Schließbar? |
| `overlay` | boolean | `true` | Overlay anzeigen? |
| `overlayClosable` | boolean | `true` | Klick auf Overlay schließt? |

## Darstellung

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `animate` | boolean | `true` | Animationen aktivieren? |
| `animationDuration` | number | `300` | Dauer in ms |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onOpen` | function | Wird beim Öffnen ausgeführt |
| `onClose` | function | Wird beim Schließen ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `dialog` |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
