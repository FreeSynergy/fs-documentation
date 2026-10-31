# Wizard - Attribute

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
| `content` | string/node | Inhalt |
| `completed` | boolean | Abgeschlossen? |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `variant` | enum | `horizontal` | Stil: `horizontal`, `vertical`, `stepper` |
| `disabled` | boolean | `false` | Deaktiviert? |
| `validation` | boolean | `false` | Validierung pro Schritt? |

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
| `role` | string | ARIA-Rolle: `region` |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onNext` | function | Wird beim Weiter-Klick ausgeführt |
| `onBack` | function | Wird beim Zurück-Klick ausgeführt |
| `onComplete` | function | Wird beim Fertig-Klick ausgeführt |

## Validation-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `validateStep` | function | Validierungsfunktion |
| `errorMessages` | object | Fehlermeldungen |
