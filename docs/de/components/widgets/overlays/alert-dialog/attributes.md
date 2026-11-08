# Alert Dialog - Attribute

Nur **eigene** Attribute. Alles Übrige kommt von der Basisklasse, siehe
[base](../../../primitives/basics/base.md).

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `title` | string | - | die Frage als Titel |
| `message` | string | - | die Wirkung in einem Satz |
| `confirmLabel` | string | `Confirm` | Verb des Bestätigungsbuttons |
| `cancelLabel` | string | `Cancel` | Verb des Abbrechen-Buttons |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `destructive` | boolean | `false` | zerstörerische Variante (Fehlerfarbe) |
| `confirmWord` | string | `null` | Wort, das zur Bestätigung eingegeben werden muss |
| `busy` | boolean | `false` | Anfrage läuft, Aktionen gesperrt |
| `closeOnEsc` | boolean | `true` | `Esc` = Abbrechen |
| `closeOnOutsideClick` | boolean | `false` | ein Klick außerhalb bricht nicht ab |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onConfirm` | function | bestätigt |
| `onCancel` | function | abgebrochen oder `Esc` |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `role` | string | `alertdialog` | - |
| `aria-describedby` | string | - | ID des Nachrichtentextes |
| `initialFocus` | enum | `cancel` | Button, der zuerst den Fokus erhält |

## Geerbt von

`id`, `visible`, `enabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onClick`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[Basiskomponente](../../../primitives/basics/base.md)
