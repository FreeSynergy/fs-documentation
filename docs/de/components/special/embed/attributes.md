# Embed (Einbettung) - Attribute

Nur **eigene** Attribute. Alles andere kommt aus der Basisklasse, siehe
[base](../../basics/base/).

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `source` | enum | `iframe` | Art der Einbettung: `app`, `widget`, `iframe` |
| `src` | string | - | Quell-URL (nur `source = iframe`) |
| `appId` | string | - | Programm-id (nur `source = app`) |
| `config` | object | - | Konfiguration des eingebetteten Inhalts |
| `title` | string | - | Titel der Kopfzeile |
| `showBorder` | boolean | `true` | Rand anzeigen? |
| `borderColor` | string | `#ccc` | Rand-Farbe |
| `widgetId` | string | - | Widget-ID |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `responsive` | boolean | `true` | Fläche passt sich der Breite an |
| `interactive` | boolean | `true` | Eingaben im eingebetteten Inhalt erlauben |
| `ratio` | enum | `auto` | Seitenverhältnis: `auto`, `16:9`, `4:3`, `1:1` |
| `allowFullscreen` | boolean | `true` | Vollbild erlauben |
| `sandbox` | string | `null` | Sandbox-Vorgaben, nur `source = iframe` |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onLoad` | function | Inhalt ist bereit |
| `onError` | function | Inhalt konnte nicht geladen werden |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | `region` bei `app` und `widget`, `iframe` bei `iframe` |
| `title` | string | dient zugleich als benennender Text für Hilfstechnologien |

## Kommunikation

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `postMessage` | boolean | `false` | Nachrichtenaustausch mit dem Inhalt |
| `origin` | string | - | erlaubte Herkunft, Pflicht bei `postMessage` |

## Geerbt von

`id`, `visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[Basiskomponente](../../basics/base/)
