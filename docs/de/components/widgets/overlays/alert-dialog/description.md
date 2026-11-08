# Alert Dialog

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

Ein Bestätigungsdialog fragt nach, bevor eine Aktion ausgeführt wird. Er ist die Verbindung aus
[modal](../modal/) (eigener Fokus, blockiert den Inhalt dahinter) und
[alert](../../../primitives/feedback/alert/) (eine Meldung mit Typ und Aktion).

## Verwendungszweck

- Absicherung zerstörerischer Aktionen (löschen, verlassen, verwerfen)
- Bestätigung von Aktionen ohne Rückweg (senden, veröffentlichen)
- Ausführung von Abkürzungen, die sich nicht rückgängig machen lassen

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **bestaetigung** | neutrale Frage, Bestätigen- und Abbrechen-Button |
| **zerstoererisch** | Fehlerfarbe, der Bestätigungsbutton wird erst nach einer Eingabe möglich |

## Funktionen

- Der Fokus liegt auf der Abbrechen-Aktion, `Esc` bricht ab
- Der Bestätigungsbutton kann eine getippte Bestätigung verlangen (den Namen des Objekts)
- Der Ladezustand sperrt beide Aktionen, solange die Anfrage läuft
- Kein eigenes Schließen-Symbol: die Entscheidung fällt über eine der beiden Aktionen

## Abgrenzung

- **Nicht verwechseln mit** [modal](../modal/): ein Modal ist ein beliebiger Dialog, der
  Bestätigungsdialog hat genau zwei Ausgänge und blockiert nicht ohne `Esc` zu verlieren.
- **Nicht verwechseln mit** [toast](../../../primitives/feedback/toast/): ein Toast meldet nachträglich
  und bietet Rückgängig an, der Dialog fragt vorab.

## Best Practices

- Benenne die Absicht im Titel („Seite verwerfen?“), die Wirkung im Text.
- Bestätigungsbutton als Verb („Verwerfen“), nie „OK“.
- Frage nicht bei umkehrbaren Aktionen nach — nimm stattdessen einen Toast mit Rückgängig.

## Siehe auch

- [Modal](../modal/)
- [Alert](../../../primitives/feedback/alert/)
- [Basiskomponente](../../../primitives/basics/base.md)
