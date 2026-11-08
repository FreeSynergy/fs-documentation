# Alert

| Feld | Wert |
|-------|-------|
| **Category** | `feedback` |
| **Inherits from** | `base` |
| **Variants** | `inline`, `banner` |
| **Types** | `info`, `success`, `warning`, `error` |
| **States** | `dismissing` |
| **Gestures** | `tap` |
| **Animations** | `fade-in`, `collapse` |
| **Related** | `toast`, `badge`, `progress` |
| **Role** | `alert` |
| **Status** | documented |

!!! info "Standardisierung"
    Die bisherige Komponente `banner` ist als Variante in `alert` aufgegangen: `inline` (innerhalb
    eines Inhalts) und `banner` (über einer Ansicht, fixiert).

## Beschreibung
Ein Alert ist eine Statusmeldung (Info, Warnung, Fehler, Erfolg).

## Zweck

- Statusmeldungen anzeigen
- Fehler anzeigen
- Erfolge anzeigen
- Warnungen anzeigen

## Varianten

| Variante | Beschreibung |
|---------|-------------|
| **inline** | Meldung innerhalb des Inhalts, dort wo sie auftritt (Standard) |
| **banner** | über die Ansicht gelegt, fixiert (`sticky`) |

## Funktionen

- Schließbar (kann geschlossen werden)
- Icon
- Titel
- Beschreibung
- Aktionsschaltfläche

## Abgrenzung

- **Nicht verwechseln mit** [toast](../toast/): ein Toast erscheint kurz und verschwindet
  von selbst, ein `alert` bleibt, bis er geschlossen oder erledigt ist.
- **Nicht verwechseln mit** [badge](../badge/): ein Badge markiert ein Element,
  eine Meldung braucht Text.

## Best Practices

- Klarer Text
- Einheitliche Farben
- Aktionsbuttons
- Barrierefreiheit

## Typen (`type`)

| Typ | Farbe | Beschreibung |
|------|--------|-------------|
| `info` | blau | Informationsmeldung |
| `success` | grün | Erfolgsmeldung |
| `warning` | orange/gelb | Warnung |
| `error` | rot | Fehlermeldung |

## Siehe auch

- [feedback – Übersicht](../index.md)
- [Basiskomponente](../../basics/base.md)
