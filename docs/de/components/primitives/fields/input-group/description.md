# Input Group (Eingabegruppe)

| Feld | Wert |
|------|------|
| **Kategorie** | `fields` |
| **Erbt von** | `base` |
| **Varianten** | `praefix`, `suffix`, `aktion`, `auswahl` |
| **Zustände** | `focus-within`, `filled` |
| **Gesten** | `tap`, `type` |
| **Animationen** | `highlight`, `expand` |
| **Verwandt** | `text-input`, `field`, `button`, `button-group`, `search-field` |
| **Rolle** | `group` |
| **Status** | dokumentiert |

## Beschreibung

Eine Input Group verbindet ein Eingabefeld mit den Teilen, die direkt dazugehören,
zu einer zusammenhängenden Fläche. Das sind ein Präfixzeichen, eine Einheit, eine
Auswahl für die Ländervorwahl oder ein Button direkt am Feld. Sie bleibt ein
einziger Wert. Die angrenzenden Teile erklären oder begrenzen ihn.

## Verwendungszweck

- Einheiten und Vorzeichen anzeigen (`€`, `kg`, `https://`)
- Eine passende Aktion direkt am Feld platzieren (Suche, Kopieren, Anmelden)
- Eine kurze Vorauswahl am Feld (Ländervorwahl, Protokoll)
- Passwörter mit einem Umschalt-Icon absichern

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **praefix** | fester Präfix links im Feld (Icon, Einheit, Zeichen) |
| **suffix** | fester Suffix rechts im Feld (Einheit, Status-Icon) |
| **aktion** | Button am Feld, meist rechts |
| **auswahl** | kleine Auswahlliste als Präfix, z. B. für die Ländervorwahl |

## Funktionen

- Gleiche Höhe, Kante und Rundung wie das Feld selbst
- Der Fokus liegt weiter beim Feld. Die Gruppe zeigt ihn nur an.
- Präfix und Suffix sind nur Anzeige. Die Aktion ist ein fokussierbarer Button.
- Links und rechts kombinierbar, pro Seite höchstens ein Teil

## Abgrenzung

- **Nicht verwechseln mit** [field](../field/): Der Wrapper liegt *um* das Feld
  (Label, Hilfetext, Fehlermeldung). Die Gruppe liegt *im* Feld neben dem
  Wert. Beide werden kombiniert, sie ersetzen sich nicht.
- **Nicht verwechseln mit** [button-group](../../actions/button-group/): Dort sind alle
  Teile gleichrangige Aktionen. Hier trägt ein Teil den Wert, die anderen erklären ihn.
- **Nicht verwechseln mit** [search-field](../search-field/): Das Suchfeld bringt
  Suchlogik mit (Vorschläge, Leeren, Tastatur). Die Gruppe ist nur der Aufbau aus
  Icon, Feld und Button.
- **Nicht verwechseln mit** [tags-input](../tags-input/): Hier entsteht ein einzelner
  Wert mit Zierelementen, dort eine Menge von Werten.

## Best Practices

- Nur eine Tab-Reihenfolge: Die Gruppe und das Präfix bekommen keinen eigenen Fokus.
- Wichtige Information gehört in das [Label](../../basics/label/), nie in ein
  Präfix. Präfixe sind nur zusätzlicher Text für Screenreader.
- Der Button in der Gruppe wirkt auf den Feldwert, nicht auf die ganze Seite.
- Bei mehr als zwei zusätzlichen Teilen lieber zwei Felder in einer Zeile nutzen.

## Siehe auch

- [fields – Übersicht](../index.md)
- [Text Input](../text-input/) — das Feld in der Gruppe
- [Field](../field/) — Label und Fehlermeldung außen
- [Base-Komponente](../../basics/base.md)
