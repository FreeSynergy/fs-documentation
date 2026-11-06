# Message Status (Nachrichtenstatus) - Attribute

Nur **eigene** Attribute. Alles Weitere stammt von der Basisklasse, siehe
[Basiskomponente](../../basics/base.md).

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `status` | enum | - | `sending`, `sent`, `delivered`, `read`, `failed` |
| `at` | datetime | - | Zeitpunkt der Zustandsänderung, im Tooltip angezeigt |
| `reason` | string | - | Fehlergrund für `failed` ⚠️ Textquelle offen |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `variant` | enum | `icon` | `icon`, `icon-text` |
| `showTooltip` | boolean | `true` | Tooltip bei Hover/Fokus anzeigen |

## Events

| Event | Typ | Beschreibung |
|---|---|---|
| – | - | keine Events; nur Anzeige |

Gesten (Swipe, Long-Press, Drag) sind **keine** Attribute dieser Komponente: Sie werden vom Frontend ergänzt (ADR 0037).

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|---|---|---|
| `aria-label` | string | Pflicht, z. B. „Zugestellt“ (nie nur das Symbol) |
| `role` | string | `img` oder `status`; `aria-live=polite` nur für die neueste Nachricht |

## Geerbt von

`id`, `visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onFocus`, `onBlur`, `animation`, `aria-*` → [Basiskomponente](../../basics/base.md)
