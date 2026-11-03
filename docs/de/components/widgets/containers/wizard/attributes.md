# Wizard - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `steps` | array[] | - | Array von Step-Objekten |
| `activeStep` | number | 0 | Aktueller Schritt |
| `onChange` | function | - | Event bei Schritt-Wechsel |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `validation` | boolean | `false` | Validierung pro Schritt? |
| `clickable` | boolean | `false` | Klickbar? |
| `animate` | boolean | `true` | Animationen aktivieren? |
| `animationDuration` | number | `300` | Dauer in ms |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onNext` | function | Wird beim Weiter-Klick ausgeführt |
| `onBack` | function | Wird beim Zurück-Klick ausgeführt |
| `onComplete` | function | Wird beim Fertig-Klick ausgeführt |
| `onStepClick` | function | Wird beim Schritt-Klick ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `region` |

## Step-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `id` | string | Eindeutige ID |
| `title` | string | Titel |
| `description` | string | Beschreibung |
| `content` | string/node | Inhalt |
| `completed` | boolean | Abgeschlossen? |

## Validation-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `validateStep` | function | Validierungsfunktion |
| `errorMessages` | object | Fehlermeldungen |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
