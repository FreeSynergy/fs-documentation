# Drawer - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
| ---------- | ----- | --------- | -------------- |
| `title` | string | - | Titel |
| `isOpen` | boolean | `false` | ist er geöffnet? |
| `onClose` | function | - | Ereignis beim Schließen |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `position` | enum | `left` | Position: `left`, `right`, `top`, `bottom` |
| `closable` | boolean | `true` | schließbar? |
| `overlay` | boolean | `true` | Overlay anzeigen? |
| `overlayClosable` | boolean | `true` | schließt ein Klick auf das Overlay den Drawer? |

## Darstellung

| Attribut | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `animate` | boolean | `true` | Animationen aktivieren? |
| `animationDuration` | number | `300` | Dauer in ms |

## Ereignisse

| Attribut | Typ | Beschreibung |
| ---------- | ----- | -------------- |
| `onOpen` | function | wird beim Öffnen ausgeführt |
| `onClose` | function | wird beim Schließen ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
| ---------- | ----- | -------------- |
| `role` | string | ARIA-Rolle: `dialog` |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../../primitives/basics/base.md)
