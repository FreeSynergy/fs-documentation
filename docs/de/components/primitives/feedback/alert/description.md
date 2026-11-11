# Alert

| Feld | Wert |
|-------|-------|
| **Kategorie** | `feedback` |
| **Erbt von** | `base` |
| **Varianten** | `inline`, `banner` |
| **Types** | `info`, `success`, `warning`, `error` |
| **Zustände** | `dismissing` |
| **Gesten** | `tap` |
| **Animationen** | `fade-in`, `collapse` |
| **Verwandt** | `toast`, `badge`, `progress` |
| **Role** | `alert` |
| **Status** | dokumentiert |

!!! info "Standardisierung"
    Die bisherige Komponente `banner` ist als Variante in `alert` aufgegangen: `inline` (innerhalb
    eines Inhalts) und `banner` (über einer Ansicht, fixiert).

## Beschreibung
Ein Alert ist eine Statusmeldung (Info, Warnung, Fehler, Erfolg).

## Verwendungszweck
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
