# Switch (Schalter)

| Feld | Wert |
|------|------|
| **Kategorie** | `fields` |
| **Erbt von** | `base` |
| **Varianten** | `Standard`, `Round`, `Pill` |
| **Zustände** | `checked`, `loading` |
| **Gesten** | `tap`, `drag` |
| **Animationen** | `elastic`, `press` |
| **Verwandt** | `checkbox`, `button`, `field` |
| **Status** | dokumentiert |

## Beschreibung
Ein Switch ist ein Ein/Aus-Schalter (Toggle).

## Verwendungszweck

- Einstellungen
- Features
- Status

## Varianten

| Variant | Beschreibung |
|---------|--------------|
| **Standard** | Rechteck |
| **Round** | Rund |
| **Pill** | Pillenform |

## Features

- Checked/Unchecked
- Animation
- Hover-Effect

## Abgrenzung

- **Nicht verwechseln mit** [checkbox](../checkbox/): der Schalter wirkt **sofort**, die Checkbox
  bestätigt eine Auswahl, die erst beim Speichern gilt (Plan Abschnitt 4, Zeile 9 — beide bleiben
  eigen, gemeinsame Basis ist das boolesche Feld).
- **Nicht verwechseln mit** [button](../../actions/button/): ein Knopf löst einmal eine Aktion aus,
  der Schalter hält einen Zustand.
- Reine Statusanzeige ("online") ist kein Schalter, sondern ein [badge](../../feedback/badge/).

## Best Practices

- Nur verwenden, wenn die Änderung ohne Bestätigung wirksam werden darf.
- Die Beschriftung beschreibt den Sachverhalt ("Benachrichtigungen"), nicht die Aktion;
  der Zustand sieht man am Schalter.
- Wirkt die Änderung langsam, den Knopf als `loading` zeigen und mehrfachklicken sperren.
- Gefährliche Schalter (Synchronisation aus, Konto löschen) zusätzlich bestätigen lassen.

## Siehe auch

- [fields – Übersicht](../index.md)
- [Checkbox](../checkbox/) — Auswahl mit Speichern
- [Badge](../../feedback/badge/) — Zustand anzeigen
- [Basiskomponente](../../basics/base/)
