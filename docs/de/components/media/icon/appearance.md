# Icon - Aussehen

## Grundlayout

Icons sind skalierbare Grafiken, die in verschiedenen Formen und Größen angezeigt werden können.

## Form-Varianten (CSS)

```css
/* Circular (Rund) */
.icon-circular {
  border-radius: 50%;
}

/* Square (Viereckig) */
.icon-square {
  border-radius: 0;
}

/* Rectangular (Rechteckig) */
.icon-rectangular {
  border-radius: 4px;
}

/* Hexagonal (Sechseckig) */
.icon-hexagonal {
  clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
}

/* Pill (Pillenform) */
.icon-pill {
  border-radius: 999px;
}
```

## Größe-Varianten

| Größe | Breite/Höhe | Margin | Verwendung |
|-------|-------------|--------|------------|
| Small | 16px | 0 | Inline-Icons |
| Medium | 24px | 0 | Navigation, Buttons |
| Large | 32px | 0 | Cards, Panels |
| XL | 48px | 0 | Hero-Sectionen |
| XXL | 64px | 0 | Landing-Pages |

## Farb-Varianten (CSS Variables)

```css
.icon {
  color: var(--icon-color);
}

/* Variants */
.icon-primary { --icon-color: var(--primary-color); }
.icon-secondary { --icon-color: var(--secondary-color); }
.icon-success { --icon-color: var(--success-color); }
.icon-warning { --icon-color: var(--warning-color); }
.icon-error { --icon-color: var(--error-color); }
.icon-neutral { --icon-color: var(--neutral-color); }
```

## Styling-Attribute

| Attribut | Wert | Beschreibung |
|----------|------|--------------|
| `size` | `small`, `medium`, `large`, `xl`, `xxl` | Größe des Icons |
| `shape` | `circular`, `square`, `rectangular`, `hexagonal`, `pill` | Form |
| `color` | `primary`, `secondary`, `success`, `warning`, `error`, `neutral`, `#hex` | Farbe |
| `interactive` | `true`, `false` | Ist das Icon klickbar? |
| `hoverEffect` | `zoom`, `border`, `shadow`, `none` | Hover-Effekt |

## Icon-Sets (Common)

| Set | Beschreibung | Library |
|-----|-------------|---------|
| **Material Icons** | Google's Design System | material-design-icons |
| **Phosphor Icons** | Flexible SVG-Icons | @phosphor-icons/react |
| **Feather Icons** | Minimalistische Icons | feather-icons |
| **Iconify** | Unified icon framework | iconify |

## Best Practices

- Konsistente Größe innerhalb einer Komponente
- Kontrast zum Hintergrund gewährleisten
- Hover-Effekt bei interaktiven Icons
- Alt-Text für Barrierefreiheit (z.B. `aria-label="Startseite"`)
