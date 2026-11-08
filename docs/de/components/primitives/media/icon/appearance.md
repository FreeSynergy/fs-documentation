# Icon - Erscheinungsbild

## Grundlayout

Icons sind skalierbare Grafiken. Sie können in verschiedenen Formen und Größen
angezeigt werden.

## Varianten

```css
/* rund */
.icon-circular {
  border-radius: 50%;
}

/* quadratisch */
.icon-square {
  border-radius: 0;
}

/* rechteckig */
.icon-rectangular {
  border-radius: 4px;
}

/* sechseckig */
.icon-hexagonal {
  clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
}

/* Pille */
.icon-pill {
  border-radius: 999px;
}
```

## Größen

| Größe | Breite/Höhe | Abstand | Verwendung |
|-------|-------------|---------|------------|
| small | 16px | 0 | Icons im Text |
| medium | 24px | 0 | Navigation, Buttons |
| large | 32px | 0 | Cards, Panels |
| XL | 48px | 0 | Hero-Bereiche |
| XXL | 64px | 0 | Landingpages |

## Farben und Zustände

```css
.icon {
  color: var(--icon-color);
}

/* Varianten */
.icon-primary { --icon-color: var(--primary-color); }
.icon-secondary { --icon-color: var(--secondary-color); }
.icon-success { --icon-color: var(--success-color); }
.icon-warning { --icon-color: var(--warning-color); }
.icon-error { --icon-color: var(--error-color); }
.icon-neutral { --icon-color: var(--neutral-color); }
```

## Hover- und Fokuseffekte

| Effekt | Beschreibung |
|--------|--------------|
| `zoom` | das Icon wächst auf das 1,1-Fache |
| `border` | hinter dem Icon erscheint ein Kreis oder Rahmen |
| `shadow` | ein leichter Schatten hebt das Icon an |
| `ring` | Fokusring für die Tastaturnavigation |
| `none` | keine Rückmeldung (rein dekorative Icons) |

## Responsiv

- In Werkzeugleisten und auf dem Handy wird das Icon eine Stufe größer dargestellt
  (mindestens 24 px). Der Trefferbereich bleibt 44 px.
- Im Fließtext bleibt das Icon `small` (16 px) und folgt der Textzeile.
- Die Skalierung erfolgt proportional. Die Linienstärke bleibt ab 16 px gut lesbar.
  Andernfalls wird auf eine vereinfachte Form umgestellt.

## Gestaltungsattribute

| Attribut | Wert | Beschreibung |
|----------|------|--------------|
| `size` | `small`, `medium`, `large`, `xl`, `xxl` | Größe des Icons |
| `shape` | `circular`, `square`, `rectangular`, `hexagonal`, `pill` | Form |
| `color` | `primary`, `secondary`, `success`, `warning`, `error`, `neutral`, `#hex` | Farbe |
| `interactive` | `true`, `false` | ist das Icon klickbar? |
| `hoverEffect` | `zoom`, `border`, `shadow`, `none` | Hover-Effekt |

## Icon-Sets (gängig)

| Set | Beschreibung | Bibliothek |
|-----|--------------|------------|
| **Material Icons** | Googles Designsystem | material-design-icons |
| **Phosphor Icons** | flexible SVG-Icons | @phosphor-icons/react |
| **Feather Icons** | minimalistische Icons | feather-icons |
| **Iconify** | einheitliches Icon-Framework | iconify |

## Best Practices

- Innerhalb einer Komponente gleiche Größe verwenden
- Kontrast zum Hintergrund sicherstellen
- Hover-Effekt für interaktive Icons
- Alternativtext für Barrierefreiheit (z. B. `aria-label="Startseite"`)
