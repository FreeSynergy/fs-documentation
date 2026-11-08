# Text Input (Texteingabe)

| Feld | Wert |
|------|------|
| **Kategorie** | `fields` |
| **Erbt von** | `base` |
| **Varianten** | `standard`, `floating label`, `underline` |
| **Zustände** | `filled`, `error` |
| **Gesten** | `tap`, `double-tap`, `long-press` |
| **Animationen** | `highlight` |
| **Verwandt** | `textarea`, `search-field`, `number-input`, `field`, `input-group` |
| **Status** | dokumentiert |

## Beschreibung
Ein Text Input ist ein einzeiliges Eingabefeld für Text.

!!! info "Vereinheitlichung"
    Die früheren Komponenten `email-input`, `url-input` und `phone-input` wurden in
    diese Komponente als `type`-Werte zusammengeführt: `text`, `email`, `url`, `phone`, `password`.

## Verwendungszweck

- Namen
- Adressen
- Nachrichten

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **standard** | normal |
| **floating label** | das Label schwebt oben |
| **underline** | nur eine Unterstreichung |

## Funktionen

- Platzhalter
- Fehlerzustand
- Validierung

## Abgrenzung

- **Nicht verwechseln mit** [textarea](../textarea/): Dieses Feld ist einzeilig. Absätze
  gehören in das mehrzeilige Feld.
- **Nicht verwechseln mit** [search-field](../search-field/): Ein Suchfeld löst bei der Eingabe
  etwas aus. Dieses Feld nimmt einen Wert entgegen.
- **Nicht verwechseln mit** [number-input](../number-input/): Telefonnummern, PLZ und
  Kontonummern sind Text, keine Werte für Berechnungen.
- Label, Hilfetext und Fehlerzeile kommen vom [field](../field/). Das Feld selbst ist nur
  die Eingabezeile.

## Best Practices

- Das Label bleibt sichtbar. Der Platzhalter ersetzt es nicht, er verschwindet beim Tippen.
- Autofill-Angaben setzen (`name`, `email`, `tel`). Sonst funktionieren Passwort-Manager
  und Adressvorschläge nicht.
- Erst validieren, wenn das Feld verlassen wurde. Fehlertexte direkt unter dem Feld.
- Bei `password` einen Anzeigen-Button anbieten und die Anforderungen vorab nennen,
  nicht erst beim Absenden.
- `maxlength` nur, wenn nötig. Dann einen Zähler zeigen.

## Typen (`type`)

| Typ | Beschreibung |
|-----|--------------|
| `text` | freier Text (Standard) |
| `email` | E-Mail-Adresse mit Prüfung |
| `url` | Webadresse mit Prüfung |
| `phone` | Telefonnummer mit Ländervorwahl |
| `password` | verdeckte Eingabe |

## Siehe auch

- [fields – Übersicht](../index.md)
- [Field](../field/) — Label, Hilfe und Fehlermeldung
- [Textarea](../textarea/) — mehrzeilig
- [Base-Komponente](../../basics/base.md)
