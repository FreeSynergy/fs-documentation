# Alert (Warnung)

| Feld | Wert |
|------|------|
| **Kategorie** | `feedback` |
| **Erbt von** | `base` |
| **Varianten** | `inline`, `banner` |
| **Typen** | `info`, `success`, `warning`, `error` |
| **Zustände** | `dismissing` |
| **Gesten** | `tap` |
| **Animationen** | `fade-in`, `collapse` |
| **Verwandt** | `toast`, `badge`, `progress` |
| **Rolle** | `alert` |
| **Status** | dokumentiert |

!!! info "Standardisierung"
    Die frühere Komponente `banner` ist als Variante in `alert` aufgegangen: `inline` (in einem Inhalt) und `banner` (über einer Ansicht, fixiert).

## Beschreibung
Ein Alert ist eine Status-Meldung (Info, Warning, Error, Success).

## Verwendungszweck

- Status-Meldungen anzeigen
- Fehler anzeigen
- Erfolge anzeigen
- Warnungen anzeigen

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **inline** | Meldung im Inhalt, dort wo sie auftritt (Standard) |
| **banner** | quer über einer Ansicht, fixiert (`sticky`) |

## Features

- Dismissible (Schließbar)
- Icon
- Title
- Description
- Action Button

## Abgrenzung

- **Nicht verwechseln mit** [toast](../toast/): ein Toast erscheint kurz und verschwindet
  von selbst, ein `alert` bleibt stehen, bis er geschlossen oder behoben ist.
- **Nicht verwechseln mit** [badge](../badge/): ein Badge kennzeichnet ein Element,
  eine Meldung braucht Text.

## Best Practices

- Klarer Text
- Konsistente Farben
- Action-Buttons
- Accessibility

## Typen (`type`)

| Typ | Farbe | Beschreibung |
|-----|-------|--------------|
| `info` | Blau | Informationsmeldung |
| `success` | Grün | Erfolgsmeldung |
| `warning` | Orange/Gelb | Warnmeldung |
| `error` | Rot | Fehlermeldung |

## Siehe auch

- [feedback – Übersicht](../index.md)
- [Basiskomponente](../../basics/base/)
