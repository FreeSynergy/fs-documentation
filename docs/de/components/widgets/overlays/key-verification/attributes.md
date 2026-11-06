# Key Verification (Schlüsselprüfung) - Attribute

Nur **eigene** Attribute. Alles Weitere stammt von der Basisklasse, siehe
[base](../../../primitives/basics/base.md).

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `subject` | object | - | Person oder Gerät, die bzw. das geprüft wird |
| `fingerprint` | string | - | Fingerabdruck oder Credential-Digest |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `variant` | enum | `fingerprint` | `fingerprint`, `qr`, `device-list` |
| `open` | boolean | `false` | Sichtbarkeit (Overlay) |

## Events

| Event | Typ | Beschreibung |
|---|---|---|
| `onConfirm` | function | Person bestätigt eine Übereinstimmung |
| `onReject` | function | Person meldet eine Abweichung |
| `onClose` | function | Dialog geschlossen |

Gesten (Swipe, Long-Press, Drag) sind **keine** Attribute dieser Komponente: Sie werden vom Frontend ergänzt (ADR 0037).

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|---|---|---|
| `role` | string | `dialog` |
| `aria-describedby` | string | Erklärung, was Bestätigen bedeutet |

## Geerbt von

`id`, `visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onFocus`, `onBlur`, `animation`, `aria-*` → [Basiskomponente](../../../primitives/basics/base.md)
