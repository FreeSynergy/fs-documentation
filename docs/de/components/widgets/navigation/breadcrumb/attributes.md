# Breadcrumb - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
| ---------- | ----- | --------- | -------------- |
| `items` | array[] | - | Array mit Breadcrumb-Objekten (label, href, icon) |
| `separator` | string | `>` | Trennzeichen: `>`, `>`, `/`, `›`, `•` |
| `activeIndex` | number | - | aktueller Index (zum Hervorheben) |
| `collapsed` | boolean | `false` | eingeklappt, wenn der Platz knapp ist? |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
| ---------- | ----- | --------- | -------------- |
| `onHomeClick` | function | - | wird ausgeführt, wenn Start angeklickt wird |
| `truncate` | boolean | `false` | bei knappem Platz kürzen? |

## Darstellung
| Attribut | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `showIcons` | boolean | `false` | Icons anzeigen? |
| `color` | string | `neutral` | Farbe |

| Attribut | Typ | Beschreibung |
| ---------- | ----- | -------------- |
| `responsive` | boolean | responsives Layout? |
| `truncateBreakpoint` | number | Schwelle für das Kürzen |

## Ereignisse

| Attribut | Typ | Beschreibung |
| ---------- | ----- | -------------- |
| `onNavigate` | function | wird bei der Navigation ausgeführt |
| `onTruncate` | function | wird ausgeführt, wenn der Pfad gekürzt wird |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
| ---------- | ----- | -------------- |
| `role` | string | ARIA-Rolle: `navigation` |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../../primitives/basics/base.md)
