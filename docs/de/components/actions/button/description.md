# Button (Schaltfläche)

| Feld | Wert |
|------|------|
| **Kategorie** | `actions` |
| **Erbt von** | `base` |
| **Varianten** | `primary`, `secondary`, `outline`, `ghost`, `danger`, `link` |
| **Zustände** | `loading` (mit Mehrfachklick-Sperre) |
| **Gesten** | `tap`, `long-press` |
| **Animationen** | `press`, `lift` |
| **Verwandt** | `link`, `switch`, `floating-action-button`, `button-group`, `spinner`, `base` |
| **Status** | dokumentiert |

## Beschreibung

Ein Button löst eine einzelne Aktion aus. Er ist die am häufigsten verwendete
Komponente überhaupt und der Ausgangspunkt fast jeder Interaktion in FreeSynergy.

## Verwendungszweck

- Aktionen bestätigen oder ausführen (Speichern, Senden, Erstellen)
- Zentrale Handlung in Dialogen, Formularen und Werkzeugleisten
- Zusammengehörige Aktionen in einer Gruppe über `button-group`

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **primary** | Hauptaktion, nur einmal pro Ansicht |
| **secondary** | Nebenaktion |
| **outline** | Rahmen ohne Füllung, schwache Betonung |
| **ghost** | ohne Rahmen, erscheint erst bei Hover |
| **danger** | zerstörerische Aktion (Löschen, Verlassen) |
| **link** | sieht aus wie ein Link, verhält sich wie ein Button |

## Features

- Icon links oder rechts, auch **icon-only** (dann mit Tooltip und `aria-label`)
- Ladezustand: ersetzt das Label durch einen Spinner und blockiert Mehrfachauslösung
- Vollbreit (`fullWidth`) für mobile Ansichten
- Aufgeteilter Button mit Dropdown-Pfeil als Variante von `button-group`

## Abgrenzung

- **Nicht verwechseln mit** [link](../../basics/link/): ein Link wechselt die Adresse
  (`href`), ein Button führt eine Aktion ohne Adresswechsel aus.

- **Nicht verwechseln mit** [switch](../../fields/switch/): ein Schalter wirkt sofort,
  ein Button löst eine Aktion aus.

- **Nicht verwechseln mit** [floating-action-button](../floating-action-button/):
  schwebende Hauptaktion in Mobile-Ansichten.

## Best Practices

- Genau **ein** `primary` pro Ansicht; Aktionen in Dialogen rechtsbündig.
- Label als Verb ("Speichern" statt "OK").
- `danger` nur mit Bestätigung (geplant: `alert-dialog`).
- Icon-only-Buttons brauchen immer `aria-label` und Tooltip.

## Siehe auch

- [Button Group](../button-group/)
- [Link](../../basics/link/)
- [Spinner](../../feedback/spinner/) (Ladezustand)
- [Basiskomponente](../../basics/base/)
