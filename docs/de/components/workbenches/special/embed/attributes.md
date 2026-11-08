# Embed – Attribute

Nur **eigene** Attribute. Alles Weitere kommt von der Basisklasse, siehe
[base](../../../primitives/basics/base.md).

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `source` | enum | `iframe` | Art der Einbettung: `app`, `widget`, `iframe` |
| `src` | string | - | Quell-URL (nur `source = iframe`) |
| `appId` | string | - | Programm-ID (nur `source = app`) |
| `config` | object | - | Konfiguration des eingebetteten Inhalts |
| `title` | string | - | Titel der Kopfzeile |
| `showBorder` | boolean | `true` | Rahmen anzeigen? |
| `borderColor` | string | `#ccc` | Rahmenfarbe |
| `widgetId` | string | - | Widget-ID |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `responsive` | boolean | `true` | die Fläche passt sich der Breite an |
| `interactive` | boolean | `true` | Eingaben im eingebetteten Inhalt erlauben |
| `ratio` | enum | `auto` | Seitenverhältnis: `auto`, `16:9`, `4:3`, `1:1` |
| `allowFullscreen` | boolean | `true` | Vollbild erlauben |
| `sandbox` | string | `null` | Sandbox-Einstellungen, nur `source = iframe` |

## Ereignisse

| Attribut | Typ | Beschreibung |
|-----------|------|-------------|
| `onLoad` | function | der Inhalt ist bereit |
| `onError` | function | der Inhalt konnte nicht geladen werden |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|-----------|------|-------------|
| `role` | string | `region` für `app` und `widget`, `iframe` für `iframe` |
| `title` | string | dient zugleich als Name für unterstützende Technik |

## Kommunikation

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `postMessage` | boolean | `false` | Nachrichtenaustausch mit dem Inhalt |
| `origin` | string | - | erlaubter Ursprung, bei `postMessage` erforderlich |

## Geerbt von

`id`, `visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[Basiskomponente](../../../primitives/basics/base.md)
