# Encryption State (Verschlüsselungsstatus) - Attribute

Nur **eigene** Attribute. Alles Weitere stammt von der Basisklasse, siehe
[Basiskomponente](../../basics/base.md).

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `kind` | enum | - | `mls`, `openpgp`, `megolm`, `transport-only`, `none`, `unknown` |
| `guideId` | string | aus `kind` abgeleitet | Leitfaden-Seite, die der Klick öffnet ⚠️ IDs offen |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `variant` | enum | `icon` | `icon`, `icon-text`, `warning` |
| `showTooltip` | boolean | `true` | Erklärung bei Hover/Fokus anzeigen |

## Events

| Event | Typ | Beschreibung |
|---|---|---|
| `onActivate` | function | Klick oder Enter; Standard öffnet den Leitfaden |

Gesten (Swipe, Long-Press, Drag) sind **keine** Attribute dieser Komponente: Sie werden vom Frontend ergänzt (ADR 0037).

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|---|---|---|
| `aria-label` | string | Pflicht, z. B. „Ende-zu-Ende-verschlüsselt mit MLS. Leitfaden öffnen“ |
| `role` | string | `link` (es navigiert) |

## Geerbt von

`id`, `visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onFocus`, `onBlur`, `animation`, `aria-*` → [Basiskomponente](../../basics/base.md)
