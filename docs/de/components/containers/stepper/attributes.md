# Stepper - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `steps` | array[] | - | Array von Step-Objekten |
| `activeStep` | number | 0 | Aktueller Schritt |
| `onChange` | function | - | Event bei Schritt-Wechsel |

## Step-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `id` | string | Eindeutige ID |
| `title` | string | Titel |
| `description` | string | Beschreibung |
| `completed` | boolean | Abgeschlossen? |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `variant` | enum | `horizontal` | Stil: `horizontal`, `vertical` |
| `clickable` | boolean | `false` | Klickbar? |
| `disabled` | boolean | `false` | Deaktiviert? |

## Styling-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `size` | enum | `medium` | Größe: `small`, `medium`, `large` |
| `rounded` | boolean | `true` | Abgerundete Ecken? |
| `theme` | enum | `default` | Theme: `default`, `dark` |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-label` | string | Beschreibender Text |
| `role` | string | ARIA-Rolle: `navigation` |

## Animation-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `animate` | boolean | `true` | Animationen aktivieren? |
| `animationDuration` | number | `300` | Dauer in ms |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onStepClick` | function | Wird beim Schritt-Klick ausgeführt |
| `onComplete` | function | Wird beim Fertig-Klick ausgeführt |
