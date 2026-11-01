# Number Input (Nummernfeld)

| Feld | Wert |
|------|------|
| **Kategorie** | `fields` |
| **Erbt von** | `base` |
| **Varianten** | `einfach`, `stepper`, `formatiert` |
| **Zustände** | `error` |
| **Gesten** | `tap`, `long-press` |
| **Animationen** | `press`, `highlight` |
| **Verwandt** | `slider`, `rating`, `text-input`, `field` |
| **Status** | dokumentiert |

## Beschreibung
Ein Number Input ist ein Eingabefeld für Zahlen.

## Verwendungszweck

- Altersangabe
- Mengen
- Preise
- Werte

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **einfach** | Nur Zahlenfeld, Tastatur ohne Schritt-Knöpfe |
| **stepper** | Feld mit `−` und `+` daneben, Halten beschleunigt |
| **formatiert** | Wert mit Einheit und lokaler Gruppierung (`1.250 g`) |

## Features

- Min/Max-Werte
- Schrittweite
- Validierung
- Auto-formatting

## Abgrenzung

- **Nicht verwechseln mit** [slider](../slider/): der Regler wählt grob und zeigt den Wertebereich,
  dieses Feld braucht den exakten Wert. Beide teilen sich die Wertlogik (`min`, `max`, `step`).
- **Nicht verwechseln mit** [text-input](../text-input/): Zahlenfolgen, die keine Zahlen sind
  (Telefonnummer, PLZ, Kontonummer) gehören in `text-input` mit `type = text`.
- **Nicht verwechseln mit** [rating](../rating/): eine Bewertung ist eine Skala, keine Zahleneingabe.

## Best Practices

- `min`, `max` und `step` immer setzen; Werte außerhalb als Fehler zeigen, nicht still klemmen.
- Gruppierungszeichen nur in der Anzeige verwenden, gespeichert wird die nackte Zahl.
- Einheit als festes Suffix außerhalb des Wertes, damit umgerechnet werden kann.
- Für Beträge Währung und Genauigkeit vorgeben, nicht frei tippen lassen.

## Siehe auch

- [fields – Übersicht](../index.md)
- [Slider](../slider/) — gleitende Wertewahl
- [Text Input](../text-input/) — Zeichenketten statt Zahlen
- [Basiskomponente](../../basics/base/)
