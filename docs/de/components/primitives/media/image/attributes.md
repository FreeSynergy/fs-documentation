# Image - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `src` | string | - | URL des Bildes |
| `alt` | string | - | Alternativtext für Barrierefreiheit |
| `shape` | enum | `rectangular` | Form: `rectangular`, `circular`, `pill` |
| `fit` | enum | `cover` | Einpassung: `cover`, `contain`, `fill` |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `interactive` | boolean | `false` | ist das Bild klickbar? |
| `hoverEffect` | enum | `none` | Hover-Effekt: `zoom`, `overlay`, `border`, `shadow` |

## Darstellung
| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `roundedValue` | number | `8` | Radius in px (bei rounded=true) |
| `border` | enum | `none` | Rahmen: `none`, `outlined`, `elevated` |
| `shadow` | enum | `default` | Schatten: `none`, `default`, `elevated` |
| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `responsive` | boolean | `true` | responsives Layout? |
| `srcSet` | array[] | - | Liste der srcSet-Objekte |
| `sizes` | string | - | CSS-Attribut `sizes` |

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `fadeIn` | boolean | `true` | Einblendung anzeigen? |
| `fadeInDuration` | number | `300` | Dauer in ms |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onLoad` | function | wird ausgeführt, wenn das Bild geladen ist |
| `onError` | function | wird bei einem Fehler ausgeführt |
| `onErrorFallback` | string | URL des Ersatzbildes bei einem Fehler |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `img`, `presentation` |

## Lade-Attribute

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `loading` | enum | `lazy`, `eager` | Ladestrategie |
| `showLoading` | boolean | `true` | Ladezustand anzeigen? |
| `loadingState` | enum | `skeleton` | Ladeanzeige: `skeleton`, `spinner` |
| `skeletonHeight` | number | `200` | Höhe des Skeletons |

## Attribute für Hintergrundbilder

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `backgroundSize` | enum | `cover`, `contain`, `auto` |
| `backgroundPosition` | enum | `center`, `top`, `bottom`, `left`, `right` |
| `backgroundRepeat` | enum | `no-repeat`, `repeat`, `repeat-x`, `repeat-y` |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base-Komponente](../../basics/base.md)
