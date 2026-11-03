# OTP Input (Einmalpasswort) - Attribute

Nur **eigene** Attribute. Alles andere kommt aus der Basisklasse, siehe
[base](../../basics/base/).

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `length` | number | `6` | Anzahl der Zeichen |
| `value` | string | `""` | eingegebener Code |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `digits` | number | `10`| Zeichenmenge: 10 Ziffern, 36 alphanumerisch |
| `paste` | boolean | `true` | Einfügen eines ganzen Codes erlauben |
| `autoComplete` | string | `one-time-code` | Autofill des Betriebssystems |
| `verifyOnComplete` | boolean | `true` | prüfen, wenn das letzte Zeichen gesetzt ist |
| `mask` | boolean | `false` | Zeichen verdecken |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onChange` | function | Teilwert geändert |
| `onComplete` | function | alle Zeichen gesetzt |
| `onResend` | function | neuer Code angefordert |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | `group`, einzelne Felder `textbox` |
| `aria-label` | string | je Box nötig, z. B. „Zeichen 3 von 6“ |
| `aria-describedby` | string | id des Hilfetextes unter den Boxen |

## Geerbt von

`id`, `visible`, `enabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onClick`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[Basiskomponente](../../basics/base/)
