# Text Input (Einzeiliges Textfeld)

| Feld | Wert |
|------|------|
| **Kategorie** | `fields` |
| **Erbt von** | `base` |
| **Varianten** | `Standard`, `Floating Label`, `Underline` |
| **Zustände** | `filled`, `error` |
| **Gesten** | `tap`, `double-tap`, `long-press` |
| **Animationen** | `highlight` |
| **Verwandt** | `textarea`, `search-field`, `number-input`, `field`, `input-group` |
| **Status** | dokumentiert |

## Beschreibung
Ein Text Input ist ein einzeiliges Eingabefeld für Text.

!!! info "Standardisierung"
    Die früheren Komponenten `email-input`, `url-input` und `phone-input` sind
    als `type`-Werte in dieser Komponente aufgegangen: `text`, `email`, `url`,
    `phone`, `password`.

## Verwendungszweck

- Namen
- Adressen
- Nachrichten

## Varianten

| Variant | Beschreibung |
|---------|--------------|
| **Standard** | Normal |
| **Floating Label** | Label schwebt über |
| **Underline** | Nur Unterstreichung |

## Features

- Placeholder
- Error-State
- Validation

## Typen (`type`)

| Typ | Beschreibung |
|-----|--------------|
| `text` | Freier Text (Standard) |
| `email` | E-Mail-Adresse mit Validierung |
| `url` | Web-Adresse mit Validierung |
| `phone` | Telefonnummer mit Ländercode |
| `password` | Maskierte Eingabe |

## Abgrenzung

- **Nicht verwechseln mit** [textarea](../textarea/): dieses Feld ist einzeilig; Absätze gehören
  ins mehrzeilige Feld.
- **Nicht verwechseln mit** [search-field](../search-field/): ein Suchfeld löst bei Eingabe etwas
  aus, dieses Feld nimmt einen Wert entgegen.
- **Nicht verwechseln mit** [number-input](../number-input/): Telefonnummern, Postleitzahlen und
  Kontonummern sind Text, keine Rechenwerte.
- Beschriftung, Hilfetext und Fehlerzeile liefert [field](../field/) – das Feld selbst ist nur
  die Eingabezeile.

## Best Practices

- Das Label bleibt sichtbar; der Placeholder ersetzt es nicht (er verschwindet beim Tippen).
- Autofill-Anworten zuordnen (`name`, `email`, `tel`), sonst funktionieren Passwörter und Adressen
  in Passwortmanagern nicht.
- Validierung erst nach dem Verlassen des Feldes, Fehler direkt unter dem Feld in Textform.
- Bei `password` Anzeige-Knopf anbieten, Anforderungen vorher nennen statt beim Absenden zeigen.
- `maxlength` nur wo nötig; dann Zähler anzeigen.

## Siehe auch

- [fields – Übersicht](../index.md)
- [Field](../field/) — Label, Hilfe und Fehlermeldung
- [Textarea](../textarea/) — mehrzeilig
- [Basiskomponente](../../basics/base/)
