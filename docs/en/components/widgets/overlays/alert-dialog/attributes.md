# Alert Dialog (Bestätigungsdialog) - Attribute

Nur **eigene** Attribute. Alles andere kommt aus der Basisklasse, siehe
[base](../../../primitives/basics/base.md).

## Main attributes

| Attribute | Type | Default | Description |
| ---------- | ----- | --------- | -------------- |
| `title` | string | - | Frage als Titel |
| `message` | string | - | Auswirkung in einem Satz |
| `confirmLabel` | string | `Bestätigen` | Verb des Bestätigungs-Buttons |
| `cancelLabel` | string | `Abbrechen` | Verb des Abbrechen-Buttons |

## Behaviour

| Attribute | Type | Default | Description |
| ---------- | ----- | --------- | -------------- |
| `destructive` | boolean | `false` | zerstörerische Variante (Fehlerfarbe) |
| `confirmWord` | string | `null` | Wort, das zum Bestätigen getippt werden muss |
| `busy` | boolean | `false` | Anfrage läuft, Aktionen gesperrt |
| `closeOnEsc` | boolean | `true` | `Esc` = Abbrechen |
| `closeOnOutsideClick` | boolean | `false` | Klick außerhalb bricht nicht ab |

## Events

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `onConfirm` | function | Bestätigt |
| `onCancel` | function | Abgebrochen oder `Esc` |

## Accessibility

| Attribute | Type | Default | Description |
| ---------- | ----- | --------- | -------------- |
| `role` | string | `alertdialog` | - |
| `aria-describedby` | string | - | id des Meldungstextes |
| `initialFocus` | enum | `cancel` | zuerst fokussierter Button |

## Inherited from

`id`, `visible`, `enabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onClick`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[Base component](../../../primitives/basics/base.md)
