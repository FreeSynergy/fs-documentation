# Alert Dialog (Bestätigungsdialog)

| Feld | Wert |
|------|------|
| **Kategorie** | `overlays` |
| **Erbt von** | `base`, `modal` |
| **Varianten** | `bestaetigung`, `zerstoererisch` |
| **Zustände** | `open`, `loading` |
| **Gesten** | `tap` |
| **Animationen** | `fade-in`, `scale-in` |
| **Verwandt** | `modal`, `alert`, `toast` |
| **Rolle** | `alertdialog` |
| **Status** | dokumentiert |

## Beschreibung

Ein Bestätigungsdialog fragt nach, bevor eine Aktion ausgeführt wird. Er ist die
Kombination aus [modal](../modal/) (eigener Fokus, blockiert dahinterliegenden Inhalt)
und [alert](../../feedback/alert/) (Meldung mit Typ und Aktion).

## Verwendungszweck

- Zerstörerische Aktionen absichern (Löschen, Verlassen, Verwerfen)
- Aktionen ohne Rückgabeweg bestätigen (Senden, Veröffentlichen)
- Shortcuts ausführen, die nicht rückgängig gemacht werden können

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **bestaetigung** | neutrale Frage, Bestätigungs- und Abbrechen-Button |
| **zerstoererisch** | Fehlerfarbe, Bestätigungs-Button erst nach Eingabe möglich |

## Features

- Fokus liegt auf der Abbrechen-Aktion, `Esc` bricht ab
- Bestätigungs-Button kann eine Tipp-Bestätigung verlangen (Name des Objekts)
- Ladezustand blockiert beide Aktionen, während die Anfrage läuft
- Kein eigenes Schließen-Symbol: entschieden wird mit einer der zwei Aktionen

## Abgrenzung

- **Nicht verwechseln mit** [modal](../modal/): ein Modal ist ein beliebiger Dialog,
  der Bestätigungsdialog hat genau zwei Auswege und blockiert `Esc`-Verlust nicht.
- **Nicht verwechseln mit** [toast](../../feedback/toast/): ein Toast meldet nach der Tat
  und bietet Rückgängig an, der Dialog fragt vorher.

## Best Practices

- Absicht im Titel nennen („Seite verwerfen?“), Auswirkung im Text.
- Bestätigungs-Button als Verb („Verwerfen“), nie „OK“.
- Rückgängige Aktionen nicht abfragen — stattdessen Toast mit Rückgängig.

## Siehe auch

- [Modal](../modal/)
- [Alert](../../feedback/alert/)
- [Basiskomponente](../../basics/base/)
