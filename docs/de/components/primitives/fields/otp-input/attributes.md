# OTP Input (Einmalcode) - Attribute

Nur **eigene** Attribute. Alles andere kommt aus der Basisklasse, siehe
[base](../../basics/base.md).

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `length` | number | `6` | Anzahl der Zeichen |
| `value` | string | `""` | der eingegebene Code |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `digits` | number | `10`| Zeichenvorrat: 10 Ziffern, 36 alphanumerisch |
| `paste` | boolean | `true` | Einfügen eines ganzen Codes erlauben |
| `autoComplete` | string | `one-time-code` | Autofill des Betriebssystems |
| `verifyOnComplete` | boolean | `true` | prüfen, sobald das letzte Zeichen gesetzt ist |
| `mask` | boolean | `false` | Zeichen verbergen |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onChange` | function | Teilwert hat sich geändert |
| `onComplete` | function | alle Zeichen sind gesetzt |
| `onResend` | function | neuer Code wurde angefordert |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | `group`, die einzelnen Felder `textbox` |
| `aria-label` | string | pro Kästchen nötig, z. B. „Zeichen 3 von 6“ |
| `aria-describedby` | string | ID des Hilfetexts unter den Kästchen |

## Geerbt von

`id`, `visible`, `enabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onClick`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[Base-Komponente](../../basics/base.md)
