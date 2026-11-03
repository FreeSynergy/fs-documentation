# Date Input (Datumsfeld)

| Feld | Wert |
|------|------|
| **Kategorie** | `fields` |
| **Erbt von** | `base` |
| **Varianten** | `date`, `time`, `datetime` |
| **Zustände** | `open`, `error` |
| **Gesten** | `tap`, `swipe` |
| **Animationen** | `fade-in`, `slide-in` |
| **Verwandt** | `date-picker`, `time-picker`, `range-calendar`, `calendar-view` |
| **Status** | dokumentiert |

!!! info "Standardisierung"
    Die früheren Komponenten `datetime-input` und `time-input` sind als `type`-Werte in `date-input` aufgegangen: `date`, `time`, `datetime`.

## Beschreibung
Ein Date Input ist ein Datumsauswahl-Feld mit Kalender.

## Verwendungszweck

- Geburtsdatum
- Terminauswahl
- Datumsangabe

## Varianten

| Variante (`type`) | Beschreibung |
|-------------------|--------------|
| **date** | nur Datum, Kalender reicht |
| **time** | nur Uhrzeit, Uhrzeit-Raster statt Kalender |
| **datetime** | Datum und Uhrzeit gemeinsam in einem Feld |

## Features

- Kalender
- Formatierung
- Validierung

## Abgrenzung

- **Nicht verwechseln mit** [date-picker](../date-picker/): das Datumsfeld nimmt auch getippte
  Werte an und ist Teil des Formulars; der Picker ist das reine Auswahl-Overlay ohne Texteingabe.
- **Nicht verwechseln mit** [calendar-view](../../data/calendar-view/): die Kalenderansicht zeigt
  Termine, sie wählt kein Datum aus.
- **Nicht verwechseln mit** [range-calendar](../range-calendar/): hier werden Anfang **und** Ende
  gewählt, nicht ein Einzelwert.

## Best Practices

- Anzeige immer im lokalen Format (`TT.MM.JJJJ`), Speicherung intern in ISO 8601.
- Unsinnige Werte ablehnen (`min`/`max`), aber einen falsch getippten Text nicht still korrigieren –
  Fehlerzustand zeigen und den Text stehen lassen.
- Bei `time` das 12-/24-Stunden-Format aus der Sprache nehmen, nicht hart einstellen.
- Tastaturbedienung anbieten: Pfeiltasten ändern das markierte Segment, PageUp/PageDown den Monat.

## Siehe auch

- [fields – Übersicht](../index.md)
- [Date Picker](../date-picker/) — Auswahl per Overlay
- [Time Picker](../time-picker/) — Uhrzeitauswahl
- [Basiskomponente](../../basics/base/)
