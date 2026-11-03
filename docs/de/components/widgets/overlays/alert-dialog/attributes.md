# Alert Dialog (Bestätigungsdialog) - Attribute

Nur **eigene** Attribute. Alles andere kommt aus der Basisklasse, siehe
[base](../../basics/base/).

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `title` | string | - | Frage als Titel |
| `message` | string | - | Auswirkung in einem Satz |
| `confirmLabel` | string | `Bestätigen` | Verb des Bestätigungs-Buttons |
| `cancelLabel` | string | `Abbrechen` | Verb des Abbrechen-Buttons |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `destructive` | boolean | `false` | zerstörerische Variante (Fehlerfarbe) |
| `confirmWord` | string | `null` | Wort, das zum Bestätigen getippt werden muss |
| `busy` | boolean | `false` | Anfrage läuft, Aktionen gesperrt |
| `closeOnEsc` | boolean | `true` | `Esc` = Abbrechen |
| `closeOnOutsideClick` | boolean | `false` | Klick außerhalb bricht nicht ab |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onConfirm` | function | Bestätigt |
| `onCancel` | function | Abgebrochen oder `Esc` |

## Barrierefreiheit

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `role` | string | `alertdialog` | - |
| `aria-describedby` | string | - | id des Meldungstextes |
| `initialFocus` | enum | `cancel` | zuerst fokussierter Button |

## Geerbt von

`id`, `visible`, `enabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onClick`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[Basiskomponente](../../basics/base/)
