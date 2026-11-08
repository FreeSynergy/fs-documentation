# Number Input (Zahleneingabe)

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

- Ein Alter angeben
- Mengen
- Preise
- Werte

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **einfach** | nur ein Zahlenfeld, Tastatur ohne Schrittbuttons |
| **stepper** | Feld mit `−` und `+` daneben. Halten beschleunigt. |
| **formatiert** | Wert mit Einheit und landesüblicher Gruppierung (`1.250 g`) |

## Funktionen

- Minimal- und Maximalwerte
- Schrittweite
- Validierung
- Automatische Formatierung

## Abgrenzung

- **Nicht verwechseln mit** [slider](../slider/): Der Slider wählt grob aus und zeigt den
  Wertebereich. Dieses Feld braucht den genauen Wert. Beide nutzen dieselbe Wertelogik (`min`, `max`, `step`).
- **Nicht verwechseln mit** [text-input](../text-input/): Ziffernfolgen, die keine
  Zahlen sind (Telefonnummer, PLZ, Kontonummer), gehören in `text-input` mit `type = text`.
- **Nicht verwechseln mit** [rating](../rating/): Eine Bewertung ist eine Skala, kein Number Input.

## Best Practices

- Immer `min`, `max` und `step` setzen. Werte außerhalb als Fehler anzeigen, nicht stillschweigend begrenzen.
- Gruppierungszeichen nur in der Anzeige verwenden. Gespeichert wird die reine Zahl.
- Die Einheit als festes Suffix außerhalb des Wertes setzen, damit sie umrechenbar bleibt.
- Bei Beträgen Währung und Genauigkeit festlegen, statt freie Eingabe zu erlauben.

## Siehe auch

- [fields – Übersicht](../index.md)
- [Slider](../slider/) — Auswahl eines Werts per Schieber
- [Text Input](../text-input/) — Zeichenketten statt Zahlen
- [Base-Komponente](../../basics/base.md)
