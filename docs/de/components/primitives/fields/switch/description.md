# Switch

| Feld | Wert |
|------|------|
| **Kategorie** | `fields` |
| **Erbt von** | `base` |
| **Varianten** | `standard`, `round`, `pill` |
| **Zustände** | `checked`, `loading` |
| **Gesten** | `tap`, `drag` |
| **Animationen** | `elastic`, `press` |
| **Verwandt** | `checkbox`, `button`, `field` |
| **Status** | dokumentiert |

## Beschreibung
Ein Switch ist ein Ein-/Aus-Schalter (Toggle).

## Verwendungszweck

- Einstellungen
- Funktionen
- Status

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **standard** | Rechteck |
| **round** | rund |
| **pill** | Pillenform |

## Features

- Aktiviert/deaktiviert
- Animation
- Hover-Effekt

## Abgrenzung

- **Nicht verwechseln mit** [checkbox](../checkbox/): der Switch wirkt **sofort**, die Checkbox
  bestätigt eine Auswahl, die erst beim Speichern gilt (Planabschnitt 4, Zeile 9 –
  beide bleiben getrennt, die Gemeinsamkeit ist das Boolean-Feld).
- **Nicht verwechseln mit** [button](../../actions/button/): ein Button löst eine Aktion einmalig aus,
  der Switch hält einen Zustand.
- Eine reine Statusanzeige ("online") ist kein Switch, sondern ein [badge](../../feedback/badge/).

## Best Practices

- Nur verwenden, wenn die Änderung ohne Bestätigung wirksam werden darf.
- Das Label beschreibt die Sache ("Benachrichtigungen"), nicht die Aktion;
  der Zustand ist am Switch sichtbar.
- Ist die Änderung langsam, den Griff als `loading` zeigen und wiederholtes Klicken blockieren.
- Gefährliche Schalter (Synchronisation aus, Konto löschen) zusätzlich bestätigen lassen.

## Siehe auch

- [fields – Übersicht](../index.md)
- [Checkbox](../checkbox/) — Auswahl mit Speichern
- [Badge](../../feedback/badge/) — Zustand anzeigen
- [Basiskomponente](../../basics/base.md)
