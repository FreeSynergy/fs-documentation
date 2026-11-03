# Slider (Schieberegler)

| Feld | Wert |
|------|------|
| **Kategorie** | `fields` |
| **Erbt von** | `base`, `number-input` |
| **Varianten** | `einfach`, `bereich` |
| **Zustände** | `dragging` |
| **Gesten** | `drag`, `tap`, `double-tap` |
| **Animationen** | `press`, `elastic` |
| **Verwandt** | `number-input`, `rating`, `progress` |
| **Status** | dokumentiert |

!!! info "Standardisierung"
    Die frühere Komponente `range-slider` ist als Variante in `slider` aufgegangen: `einfach` (ein Wert) und `bereich` (zwei Werte).

## Beschreibung
Ein Slider ist ein Wertebereich mit Schieberegler.

## Verwendungszweck

- Lautstärke
- Bewertung
- Einstellungen

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **einfach** | Ein Regler für einen Wert |
| **bereich** | Zwei Regler, wählen einen Bereich (aus `range-slider` zusammengeführt) |

## Features

- Min/Max
- Step
- Value

## Abgrenzung

- **Nicht verwechseln mit** [progress](../../feedback/progress/): der Fortschrittsbalken ist
  reine Anzeige, der Regler ist eine Eingabe.
- **Nicht verwechseln mit** [rating](../rating/): eine Skala mit Stufen, hier ist der Wert
  kontinuierlich oder fein unterteilt.
- Der Regler teilt sich die Wertlogik mit [number-input](../number-input/) (`min`, `max`, `step`);
  wo der genaue Wert zählt, gehört das Zahlenfeld hin.

## Best Practices

- Aktuellen Wert mit Einheit anzeigen, nicht nur den Knopf bewegen lassen.
- `step` so wählen, dass die Stufenzahl zwischen 5 und 20 liegt.
- Skalenenden beschriften ("leise – laut"), sonst ist die Richtung unklar.
- Tastatur bedienen: Pfeiltasten bewegen in `step`, PageUp/PageDown größer, `aria-valuenow` setzen.
- Doppelte Regler (`bereich`) dürfen sich nicht überholen; Doppeltipp setzt auf Mittelwert.

## Siehe auch

- [fields – Übersicht](../index.md)
- [Number Input](../number-input/) — genauen Wert eingeben
- [Progress](../../feedback/progress/) — Fortschritt anzeigen
- [Basiskomponente](../../basics/base/)
