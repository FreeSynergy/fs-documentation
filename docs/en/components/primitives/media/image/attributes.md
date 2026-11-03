# Image - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `src` | string | - | image URL |
| `alt` | string | - | alt text for accessibility |
| `shape` | enum | `rectangular` | shape: `rectangular`, `circular`, `pill` |
| `fit` | enum | `cover` | fit mode: `cover`, `contain`, `fill` |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `interactive` | boolean | `false` | is the image clickable? |
| `hoverEffect` | enum | `none` | hover effect: `zoom`, `overlay`, `border`, `shadow` |

## Presentation
| Attribute | Type | Default | Description |
|---|---|---|---|
| `roundedValue` | number | `8` | radius in px (when rounded=true) |
| `border` | enum | `none` | border: `none`, `outlined`, `elevated` |
| `shadow` | enum | `default` | shadow: `none`, `default`, `elevated` |
| Attribute | Type | Default | Description |
|---|---|---|---|
| `responsive` | boolean | `true` | responsive layout? |
| `srcSet` | array[] | - | array of srcSet objects |
| `sizes` | string | - | CSS sizes attribute |

| Attribute | Type | Default | Description |
|---|---|---|---|
| `fadeIn` | boolean | `true` | show the fade-in? |
| `fadeInDuration` | number | `300` | duration in ms |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onLoad` | function | runs when the image has loaded |
| `onError` | function | runs on error |
| `onErrorFallback` | string | fallback image URL on error |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | ARIA role: `img`, `presentation` |

## Loading attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `loading` | enum | `lazy`, `eager` | loading strategy |
| `showLoading` | boolean | `true` | show the loading state? |
| `loadingState` | enum | `skeleton` | loading status: `skeleton`, `spinner` |
| `skeletonHeight` | number | `200` | skeleton height |

## Background-image attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `backgroundSize` | enum | `cover`, `contain`, `auto` |
| `backgroundPosition` | enum | `center`, `top`, `bottom`, `left`, `right` |
| `backgroundRepeat` | enum | `no-repeat`, `repeat`, `repeat-x`, `repeat-y` |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [base component](../../basics/base.md)
