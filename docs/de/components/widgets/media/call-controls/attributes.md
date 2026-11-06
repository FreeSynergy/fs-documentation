# Call Controls (Anrufsteuerung) - Attribute

Nur **eigene** Attribute. Alles Weitere stammt von der Basisklasse, siehe
[base](../../../primitives/basics/base.md).

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `session` | object | - | Anrufsitzung (Zustand, Geräte) |
| `controls` | array | all | welche Bedienelemente angezeigt werden |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `variant` | enum | `bar` | `bar`, `compact` |
| `muted` | boolean | `false` | Mikrofon stummgeschaltet |
| `cameraOn` | boolean | `true` | Kamera an |

## Events

| Event | Typ | Beschreibung |
|---|---|---|
| `onToggleMic` | function | Mikrofon umgeschaltet |
| `onToggleCamera` | function | Kamera umgeschaltet |
| `onShareScreen` | function | Bildschirmfreigabe gestartet oder beendet |
| `onHangUp` | function | Anruf beendet |

Gesten (Swipe, Long-Press, Drag) sind **keine** Attribute dieser Komponente: Sie werden vom Frontend ergänzt (ADR 0037).

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|---|---|---|
| `role` | string | `toolbar` |
| `aria-pressed` | boolean | bei Umschaltern |

## Geerbt von

`id`, `visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onFocus`, `onBlur`, `animation`, `aria-*` → [Basiskomponente](../../../primitives/basics/base.md)
