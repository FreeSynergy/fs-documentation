# Button

| Feld | Wert |
|-------|-------|
| **Kategorie** | `actions` |
| **Erbt von** | `base` |
| **Varianten** | `primary`, `secondary`, `outline`, `ghost`, `danger`, `link` |
| **Zustände** | `loading` (mit Sperre gegen Doppelklick) |
| **Gesten** | `tap`, `long-press` |
| **Animationen** | `press`, `lift` |
| **Verwandt** | `link`, `switch`, `floating-action-button`, `button-group`, `spinner`, `base` |
| **Status** | dokumentiert |

## Beschreibung

Ein Button löst eine einzelne Aktion aus. Er ist die meistgenutzte Komponente überhaupt und der
Ausgangspunkt fast jeder Interaktion in FreeSynergy.

## Verwendungszweck
- Aktionen bestätigen oder ausführen (speichern, senden, anlegen)
- Zentrale Aktion in Dialogen, Formularen und Werkzeugleisten
- Zusammengehörige Aktionen werden über `button-group` gruppiert

## Varianten

| Variante | Beschreibung |
|---------|-------------|
| **primary** | Hauptaktion, nur einmal pro Ansicht |
| **secondary** | Nebenaktion |
| **outline** | Rahmen ohne Füllung, schwache Betonung |
| **ghost** | kein Rahmen, erscheint erst bei Hover |
| **danger** | zerstörerische Aktion (löschen, verlassen) |
| **link** | sieht aus wie ein Link, verhält sich wie ein Button |

## Funktionen

- Icon links oder rechts, auch **nur Icon** (dann mit Tooltip und `aria-label`)
- Ladezustand: ersetzt die Beschriftung durch einen Spinner und blockiert wiederholtes Auslösen
- Volle Breite (`fullWidth`) für mobile Ansichten
- Split-Button mit Pfeil für die Auswahlliste als Variante von `button-group`

## Abgrenzung

- **Nicht verwechseln mit** [link](../../basics/link/): ein Link ändert die Adresse
  (`href`), ein Button führt eine Aktion aus, ohne die Adresse zu ändern.

- **Nicht verwechseln mit** [switch](../../fields/switch/): ein Schalter wirkt
  sofort, ein Button löst eine Aktion aus.

- **Nicht verwechseln mit** [floating-action-button](../floating-action-button/):
  schwebende Hauptaktion in mobilen Ansichten.

## Best Practices

- Genau **einen** `primary` pro Ansicht; Aktionen in Dialogen rechts ausrichten.
- Beschriftung als Verb („Speichern“ statt „OK“).
- `danger` nur mit Bestätigung, z. B. über [alert-dialog](../../../widgets/overlays/alert-dialog/).
- Buttons nur mit Icon brauchen immer `aria-label` und einen Tooltip.

## Siehe auch

- [Button-Gruppe](../button-group/)
- [Link](../../basics/link/)
- [Spinner](../../feedback/spinner/) (Ladezustand)
- [Basiskomponente](../../basics/base.md)
