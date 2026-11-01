# Input Group (Feldgruppe)

| Feld | Wert |
|------|------|
| **Kategorie** | `fields` |
| **Erbt von** | `base` |
| **Varianten** | `praefix`, `suffix`, `beides` |
| **Zustände** | - |
| **Gesten** | - |
| **Animationen** | - |
| **Verwandt** | `text-input`, `button-group`, `field`, `button`, `base` |
| **Status** | dokumentiert |

## Beschreibung

Eine Input Group verbindet ein Eingabefeld mit vor- oder nachgestellten
Elementen: Icon, statischer Text (z. B. `https://` oder `€`), Länderauswahl
oder ein Action-Button. Optisch und bedienmäßig entsteht ein gemeinsames Feld.

## Verwendungszweck

- Währung, Einheit oder Protokoll vor dem Feld (`€`, `kg`, `https://`)
- Such-Icon im Feld, Clear- oder Action-Button dahinter
- Ländercode-Dropdown vor dem Telefonfeld (Nachfolger von `phone-input`)

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **praefix** | Vorangestelltes Element links im Feld |
| **suffix** | Nachgestelltes Element rechts im Feld |
| **beides** | Präfix und Suffix gleichzeitig |

## Features

- Fokus-Ring und Hover gelten für die gesamte Gruppe
- Innen-Elemente können statisch (Text), dekorativ (Icon) oder interaktiv
  (Button, Select) sein

- Mehrere Gruppen-Elemente hintereinander möglich

## Abgrenzung

- **Nicht verwechseln mit** [text-input](../text-input/): das Feld
  allein hat keine angebauten Elemente.

- **Nicht verwechseln mit** [button-group](../../actions/button-group/): dort
  stehen mehrere Aktionsbuttons nebeneinander, kein Eingabefeld.

- **Nicht verwechseln mit** [field](../field/): der Wrapper beschriftet von
  außen, die Gruppe gestaltet das Feld selbst.

## Best Practices

- Präfix-Text nicht als Ersatz für ein Label verwenden.
- Interaktive Gruppen-Elemente brauchen eigene Beschriftung (`aria-label`).
- Höchstens zwei Elemente pro Seite der Gruppe.

## Siehe auch

- [Text Input](../text-input/)
- [Field](../field/)
- [Button](../../actions/button/)
- [Basiskomponente](../../basics/base/)
