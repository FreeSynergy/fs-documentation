# Empty State - Attribute

Nur **eigene** Attribute. Alles andere kommt aus der Basisklasse, siehe
[base](../../basics/base.md).

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `title` | string | - | ein Satz, warum die Fläche leer ist |
| `description` | string | `null` | zusätzliche Information in einem zweiten Satz |
| `icon` | string | `null` | Name des Icons (siehe [icon](../../media/icon/)) |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `variant` | enum | `leer` | `leer`, `kein-treffer`, `fehler` |
| `actionLabel` | string | `null` | Text der Hauptaktion |
| `actionHref` | string | `null` | Ziel der Hauptaktion, falls es ein Link ist |
| `hint` | string | `null` | kurzer Text für eine Tastenkürzel- oder Hilfeangabe |
| `query` | string | `null` | Suchbegriff, angezeigt bei `kein-treffer` |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onAction` | function | Hauptaktion wurde ausgelöst |
| `onReset` | function | Filter wurde zurückgesetzt |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `role` | string | `status` | - |
| `aria-live` | enum | `polite` | damit Änderungen angekündigt werden |
| `icon` | string | - | rein dekorativ, kein `aria-label` nötig |

## Geerbt von

`id`, `visible`, `enabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onClick`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[Base-Komponente](../../basics/base.md)
