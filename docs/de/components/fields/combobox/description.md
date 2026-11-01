# Combobox (Kombinationsfeld)

| Feld | Wert |
|------|------|
| **Kategorie** | `fields` |
| **Erbt von** | `base`, `select` |
| **Varianten** | `einzeln`, `freitext`, `mehrfach` |
| **Zustände** | `open`, `loading`, `no-results` |
| **Gesten** | `tap`, `swipe` |
| **Animationen** | `fade-in`, `expand`, `highlight` |
| **Verwandt** | `select`, `search-field`, `tags-input`, `command` |
| **Status** | dokumentiert |

## Beschreibung
Ein Combobox ist ein Textfeld + Dropdown.

## Verwendungszweck

- Adresssuche
- Kategorien
- Suchfeld

## Features

- Typing
- Selection
- Auto-complete

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **einzeln** | Auswahl aus Vorschlägen, eigener Text nur als Suchfilter |
| **freitext** | beliebiger Wert erlaubt, Vorschläge sind Angebote |
| **mehrfach** | mehrere Werte als Tags, Vorschlagsliste bleibt geöffnet |

## Abgrenzung

- **Nicht verwechseln mit** [select](../select/): `select` bietet ausschließlich vorhandene
  Optionen und schließt nach der Auswahl. Die Combobox ergänzt Freitext und Vorschläge zu
  einem eingegebenen Text – das ist der entscheidende Unterschied (Plan Abschnitt 4, Zeile 5).
- **Nicht verwechseln mit** [search-field](../search-field/): ein Suchfeld löst eine Suche aus
  und verändert die Ansicht, die Combobox schreibt einen Wert ins Formular.
- **Nicht verwechseln mit** [command](../../navigation/command/): die Befehlspalette ist ein
  vollflächiges Overlay für Aktionen, keine Feld-Eingabe.

## Best Practices

- Vorschläge erst ab zwei Zeichen und mit kurzer Verzögerung laden; Warten als
  `loading`-Zustand zeigen, nie als leere Liste.
- Freitext nur anbieten, wenn die Domäne freie Werte erlaubt; sonst `select` verwenden.
- Leere Vorschlagsliste als `no-results` mit Hinweis beschriften ("keine Treffer für …").
- Tastatur durchgängig bedienen: Pfeiltasten, Enter wählt, Esc schließt, Fokus bleibt im Feld.

## Siehe auch

- [fields – Übersicht](../index.md)
- [Select (Auswahlliste)](../select/) — die reine Auswahlliste
- [Search Field](../search-field/) — Suche statt Wertauswahl
- [Basiskomponente](../../basics/base/)
