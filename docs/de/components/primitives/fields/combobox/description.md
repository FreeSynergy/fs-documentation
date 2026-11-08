# Combobox

| Feld | Wert |
|-------|-------|
| **Category** | `fields` |
| **Inherits from** | `base`, `select` |
| **Variants** | `einzeln`, `freitext`, `mehrfach` |
| **States** | `open`, `loading`, `no-results` |
| **Gestures** | `tap`, `swipe` |
| **Animations** | `fade-in`, `expand`, `highlight` |
| **Related** | `select`, `search-field`, `tags-input`, `command` |
| **Status** | documented |

## Beschreibung
Eine Combobox ist ein Textfeld plus eine Auswahlliste.

## Zweck

- Adresssuche
- Kategorien
- Suchfeld

## Varianten

| Variante | Beschreibung |
|---------|-------------|
| **einzeln** | Auswahl aus Vorschlägen, eigener Text nur als Suchfilter |
| **freitext** | jeder Wert erlaubt, Vorschläge sind Angebote |
| **mehrfach** | mehrere Werte als Tags, die Vorschlagsliste bleibt offen |

## Funktionen

- Tippen
- Auswählen
- Autovervollständigung

## Abgrenzung

- **Nicht verwechseln mit** [select](../select/): `select` bietet nur vorhandene
  Optionen an und schließt sich nach der Wahl. Die Combobox ergänzt freien Text und Vorschläge
  zu einem eingegebenen Text – das ist der entscheidende Unterschied (Planabschnitt 4, Zeile 5).
- **Nicht verwechseln mit** [search-field](../search-field/): ein Suchfeld löst eine Suche aus und ändert die
  Ansicht, die Combobox schreibt einen Wert ins Formular.
- **Nicht verwechseln mit** [command](../../../widgets/navigation/command/): die Befehlspalette ist ein
  Vollbild-Overlay für Aktionen, keine Feldeingabe.

## Best Practices

- Vorschläge erst ab zwei Zeichen und mit kurzer Verzögerung laden; das Warten als
  `loading`-Zustand zeigen, nie als leere Liste.
- Freitext nur anbieten, wenn der Bereich freie Werte erlaubt; sonst `select` verwenden.
- Eine leere Vorschlagsliste als `no-results` mit einem Hinweis kennzeichnen („keine Treffer für …“).
- Vollständig per Tastatur bedienbar halten: Pfeiltasten, Enter wählt, Esc schließt, der Fokus bleibt im Feld.

## Siehe auch

- [fields – Übersicht](../index.md)
- [Select](../select/) — die reine Auswahlliste
- [Suchfeld](../search-field/) — suchen statt einen Wert wählen
- [Basiskomponente](../../basics/base.md)
