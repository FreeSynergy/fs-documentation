# Icon - Aussehen

## Grundlayout

Icons sind skalierbare Grafiken, die in verschiedenen Formen und Größen angezeigt werden können.

## Varianten

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

## Größen

| Größe | Breite/Höhe | Margin | Verwendung |
|-------|-------------|--------|------------|
| Small | 16px | 0 | Inline-Icons |
| Medium | 24px | 0 | Navigation, Buttons |
| Large | 32px | 0 | Cards, Panels |
| XL | 48px | 0 | Hero-Sectionen |
| XXL | 64px | 0 | Landing-Pages |

## Farben und Zustände

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

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `zoom` | Icon wächst auf das 1,1-fache |
| `border` | Kreis oder Rahmen erscheint hinter dem Icon |
| `shadow` | leichter Schatten hebt das Icon an |
| `ring` | Fokus-Ring bei Tastaturnavigation |
| `none` | keine Rückmeldung (rein dekorative Icons) |

## Reaktiv

- In Werkzeugleisten und auf Mobil wird das Icon eine Stufe größer dargestellt
  (mindestens 24 px), die Trefferfläche bleibt 44 px.
- In Fließtext bleibt das Icon auf `small` (16 px) und folgt der Schriftzeile.
- Skalierung erfolgt proportional; die Konturstärke bleibt ab 16 px lesbar,
  sonst auf eine vereinfachte Form wechseln.

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
