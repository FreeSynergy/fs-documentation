# Wizard - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `steps` | array[] | - | Array mit Schritt-Objekten |
| `activeStep` | number | 0 | aktueller Schritt |
| `onChange` | function | - | Ereignis beim Schrittwechsel |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `validation` | boolean | `false` | pro Schritt prüfen? |
| `clickable` | boolean | `false` | anklickbar? |
| `animate` | boolean | `true` | Animationen aktivieren? |
| `animationDuration` | number | `300` | Dauer in ms |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onNext` | function | wird beim Klick auf "Weiter" ausgeführt |
| `onBack` | function | wird beim Klick auf "Zurück" ausgeführt |
| `onComplete` | function | wird beim Klick auf "Fertigstellen" ausgeführt |
| `onStepClick` | function | wird beim Klick auf einen Schritt ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `region` |

## Schritt-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `id` | string | eindeutige ID |
| `title` | string | Titel |
| `description` | string | Beschreibung |
| `content` | string/node | Inhalt |
| `completed` | boolean | abgeschlossen? |

## Validierungs-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `validateStep` | function | Validierungsfunktion |
| `errorMessages` | object | Fehlermeldungen |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../../primitives/basics/base.md)
