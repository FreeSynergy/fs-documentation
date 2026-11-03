# Icon - Appearance

## Base layout

Icons are scalable graphics that can be shown in different shapes and sizes.

## Variants

```css
/* circular */
.icon-circular {
  border-radius: 50%;
}

/* square */
.icon-square {
  border-radius: 0;
}

/* rectangular */
.icon-rectangular {
  border-radius: 4px;
}

/* hexagonal */
.icon-hexagonal {
  clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
}

/* pill */
.icon-pill {
  border-radius: 999px;
}
```

## Sizes

| Size | Width/height | Margin | Use |
|------|--------------|--------|-----|
| small | 16px | 0 | inline icons |
| medium | 24px | 0 | navigation, buttons |
| large | 32px | 0 | cards, panels |
| XL | 48px | 0 | hero sections |
| XXL | 64px | 0 | landing pages |

## Colours and states

```css
.icon {
  color: var(--icon-color);
}

/* variants */
.icon-primary { --icon-color: var(--primary-color); }
.icon-secondary { --icon-color: var(--secondary-color); }
.icon-success { --icon-color: var(--success-color); }
.icon-warning { --icon-color: var(--warning-color); }
.icon-error { --icon-color: var(--error-color); }
.icon-neutral { --icon-color: var(--neutral-color); }
```

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `zoom` | the icon grows to 1.1 times |
| `border` | a circle or frame appears behind the icon |
| `shadow` | a light shadow lifts the icon |
| `ring` | focus ring for keyboard navigation |
| `none` | no feedback (purely decorative icons) |

## Responsive

- In toolbars and on mobile the icon is shown one step larger
  (at least 24 px), the hit area stays 44 px.
- In running text the icon stays `small` (16 px) and follows the text line.
- Scaling happens proportionally; the line weight stays readable from 16 px up,
  otherwise switch to a simplified shape.

## Styling attributes

| Attribute | Value | Description |
|-----------|-------|-------------|
| `size` | `small`, `medium`, `large`, `xl`, `xxl` | size of the icon |
| `shape` | `circular`, `square`, `rectangular`, `hexagonal`, `pill` | shape |
| `color` | `primary`, `secondary`, `success`, `warning`, `error`, `neutral`, `#hex` | colour |
| `interactive` | `true`, `false` | is the icon clickable? |
| `hoverEffect` | `zoom`, `border`, `shadow`, `none` | hover effect |

## Icon sets (common)

| Set | Description | Library |
|-----|-------------|---------|
| **Material Icons** | Google's design system | material-design-icons |
| **Phosphor Icons** | flexible SVG icons | @phosphor-icons/react |
| **Feather Icons** | minimalist icons | feather-icons |
| **Iconify** | unified icon framework | iconify |

## Best Practices

- Consistent size within one component
- Ensure contrast against the background
- Hover effect for interactive icons
- Alt text for accessibility (e.g. `aria-label="Home"`)
