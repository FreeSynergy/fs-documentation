# Datumsfeld

| Feld | Wert |
|-------|-------|
| **Category** | `fields` |
| **Inherits from** | `base` |
| **Variants** | `date`, `time`, `datetime` |
| **States** | `open`, `error` |
| **Gestures** | `tap`, `swipe` |
| **Animations** | `fade-in`, `slide-in` |
| **Related** | `date-picker`, `time-picker`, `range-calendar`, `calendar-view` |
| **Status** | documented |

!!! info "Standardisierung"
    Die früheren Komponenten `datetime-input` und `time-input` sind in `date-input`
    als `type`-Werte aufgegangen: `date`, `time`, `datetime`.

## Beschreibung
Ein Datumsfeld ist ein Feld zur Datumsauswahl mit einem Kalender.

## Zweck

- Geburtsdatum
- Einen Termin auswählen
- Ein Datum angeben

## Varianten

| Variante (`type`) | Beschreibung |
|------------------|-------------|
| **date** | nur Datum, ein Kalender genügt |
| **time** | nur Uhrzeit, ein Uhrzeitraster statt Kalender |
| **datetime** | Datum und Uhrzeit gemeinsam in einem Feld |

## Funktionen

- Kalender
- Formatierung
- Validierung

## Abgrenzung

- **Nicht verwechseln mit** [date-picker](../../../widgets/fields/date-picker/): das Datumsfeld nimmt auch
  getippte Werte an und ist Teil des Formulars; der Picker ist das reine Auswahl-Overlay
  ohne Texteingabe.
- **Nicht verwechseln mit** [calendar-view](../../../widgets/data/calendar-view/): die Kalenderansicht zeigt
  Termine, sie wählt kein Datum aus.
- **Nicht verwechseln mit** [range-calendar](../../../widgets/fields/range-calendar/): dort wählt man
  Anfang **und** Ende, nicht einen einzelnen Wert.

## Best Practices

- Immer im lokalen Format anzeigen, intern als ISO 8601 speichern.
- Unsinnige Werte (`min`/`max`) ablehnen, aber getippten Text nicht stillschweigend korrigieren –
  den Fehlerzustand zeigen und den Text stehen lassen.
- Bei `time` das 12-/24-Stunden-Format aus der Sprache übernehmen, nicht fest vorgeben.
- Tastaturbedienung anbieten: Pfeiltasten ändern das markierte Segment, Bild auf/ab den Monat.

## Siehe auch

- [fields – Übersicht](../index.md)
- [Date Picker](../../../widgets/fields/date-picker/) — Auswahl über ein Overlay
- [Time Picker](../../../widgets/fields/time-picker/) — Uhrzeitauswahl
- [Basiskomponente](../../basics/base.md)
