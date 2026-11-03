# Input Group (Feldgruppe)

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

Eine Input Group fügt ein Eingabefeld und die Teile, die unmittelbar dazugehören, zu
einer zusammenhängenden Fläche zusammen: ein Vorsatz-Zeichen, eine Einheit, ein Dropdown
für die Landesvorwahl oder eine Schaltfläche direkt am Feld. Es bleibt ein Wert; die
Nachbarteile erklären oder begrenzen ihn.

## Verwendungszweck

- Einheiten und Vorzeichen anzeigen (`€`, `kg`, `https://`)
- Eine passende Aktion direkt ans Feld setzen (Suchen, Kopieren, Anmelden)
- Kurze Voreinstellung am Feld (Landesvorwahl, Protokoll)
- Passwörter mit Umschalt-Icon absichern

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **praefix** | fester Vorsatz links im Feld (Icon, Einheit, Vorzeichen) |
| **suffix** | fester Nachsatz rechts im Feld (Einheit, Status-Icon) |
| **aktion** | Schaltfläche am Feld, meist rechts |
| **auswahl** | kleines Dropdown als Vorsatz, z. B. Landesvorwahl |

## Features

- Gemeinsame Höhe, Kante und Radius wie das Feld selbst
- Fokus liegt weiter beim Feld; die Gruppe markiert ihn mit
- Vorsatz und Nachsatz sind reine Anzeige, die Aktion ist ein richtbarer Button
- Links und rechts kombinierbar, je Seite höchstens ein Teil

## Abgrenzung

- **Nicht verwechseln mit** [field](../field/): der Wrapper gehört *um* das Feld herum
  (Beschriftung, Hilfetext, Fehlermeldung), die Gruppe sitzt *im* Feld neben dem Wert.
  Beide werden kombiniert, nicht ersetzt.
- **Nicht verwechseln mit** [button-group](../../actions/button-group/): dort sind alle
  Teile gleichwertige Aktionen; hier trägt ein Teil den Wert, die anderen erklären ihn.
- **Nicht verwechseln mit** [search-field](../search-field/): das Suchfeld bringt
  Suchlogik mit (Vorschläge, Leeren, Tastatur). Die Gruppe ist nur die Bauform aus
  Icon, Feld und Knopf.
- **Nicht verwechseln mit** [tags-input](../tags-input/): hier entsteht ein Wert mit
  Dekoration, dort eine Menge von Werten.

## Best Practices

- Nur eine Tabulator-Reihenfolge: Gruppe und Vorsatz bekommen keinen eigenen Fokus.
- Entscheidende Information gehört in das [label](../../basics/label/), nie in einen
  Vorsatz — Vorsätze sind für Screenreader Zusatztext.
- Die Schaltfläche in der Gruppe wirkt auf den Feldwert, nicht auf die Seite.
- Bei mehr als zwei Zusatzteilen lieber zwei Felder in einer Zeile.

## Siehe auch

- [fields – Übersicht](../index.md)
- [Text Input](../text-input/) — das Feld in der Gruppe
- [Field](../field/) — Beschriftung und Fehlermeldung außerhalb
- [Basiskomponente](../../basics/base/)
