# Slider

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
    Die frühere Komponente `range-slider` ist als Variante in `slider` aufgegangen: `einfach`
    (ein Wert) und `bereich` (zwei Werte).

## Beschreibung
Ein Slider ist ein Wertebereich mit einem verschiebbaren Regler.

## Verwendungszweck

- Lautstärke
- Bewertung
- Einstellungen

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **einfach** | ein Griff für einen Wert |
| **bereich** | zwei Griffe, um einen Bereich zu wählen (zusammengeführt aus `range-slider`) |

## Features

- Min/Max
- Schritt
- Wert

## Abgrenzung

- **Nicht verwechseln mit** [progress](../../feedback/progress/): der Fortschrittsbalken dient nur
  der Anzeige, der Slider ist eine Eingabe.
- **Nicht verwechseln mit** [rating](../rating/): eine Skala mit Stufen; hier ist der Wert
  stufenlos oder fein unterteilt.
- Der Slider teilt seine Wertelogik mit [number-input](../number-input/) (`min`, `max`,
  `step`); wenn es auf den genauen Wert ankommt, ist das Zahlenfeld die richtige Wahl.

## Best Practices

- Den aktuellen Wert mit Einheit anzeigen, nicht nur den Griff verschieben lassen.
- `step` so wählen, dass die Anzahl der Schritte zwischen 5 und 20 liegt.
- Die Enden der Skala beschriften ("leise – laut"), sonst ist die Richtung unklar.
- Tastatur-Bedienung: Pfeiltasten bewegen in `step`-Schritten, Bild auf/Bild ab weiter;
  `aria-valuenow` setzen.
- Gekoppelte Griffe (`bereich`) dürfen einander nicht überholen; ein Doppeltipp setzt die Mitte.

## Siehe auch

- [fields – Übersicht](../index.md)
- [Number Input](../number-input/) — Eingabe eines genauen Wertes
- [Progress](../../feedback/progress/) — Fortschritt anzeigen
- [Basiskomponente](../../basics/base.md)
