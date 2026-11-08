# Command

| Feld | Wert |
|------|------|
| **Kategorie** | `navigation` |
| **Erbt von** | `base` |
| **Varianten** | `palette`, `inline` |
| **Zustände** | `open`, `empty` |
| **Gesten** | `tap`, `type` |
| **Animationen** | `fade-in`, `expand` |
| **Verwandt** | `search-field`, `menu`, `modal` |
| **Rolle** | `dialog` |
| **Status** | dokumentiert |

## Beschreibung

Die Befehlspalette ist ein Overlay mit einem Eingabefeld und einer Trefferliste. Sie startet
Programme, wechselt Ansichten und führt Aktionen aus — erreichbar über ein Tastenkürzel, statt
sich durch Menüs zu suchen.

## Verwendungszweck

- Schneller Zugriff auf Programme und Ansichten im Desktop-Client
- Ausführen von Aktionen, ohne den Kontext zu verlassen
- Kurze Hilfe: welche Befehle in dieser Ansicht verfügbar sind

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **palette** | zentriertes Overlay, über `Strg`/`Cmd` + `K` |
| **inline** | Palette, eingebettet in einer Seitenleiste oder Werkzeugleiste |

## Funktionen

- Suchbegriffe lassen sich auch ohne Kontext starten („neue Aufgabe“ findet das Ziel)
- Treffer gruppiert nach Programm, Ansicht und Aktion
- Zuletzt und häufig genutzte Befehle stehen auch ohne Eingabe oben
- Tastaturnavigation: `Pfeil hoch/runter`, `Enter` führt aus, `Esc` schließt

## Abgrenzung

- **Nicht verwechseln mit** [search-field](../../../primitives/fields/search-field/): die Suche findet Inhalte,
  die Palette führt Aktionen aus.
- **Nicht verwechseln mit** [menu](../menu/): Menüs zeigen das gesamte Angebot, die Palette nur
  passende Treffer.

## Best Practices

- Befehle als Verb und dann Objekt benennen („Aufgabe anlegen“, nicht „Neu“).
- Zeig pro Befehl ein Tastenkürzel, sofern es eines gibt.
- Schneide die Ergebnisse nach 50 Treffern ab und bitte den Nutzer, genauer zu werden.

## Siehe auch

- [Search Field](../../../primitives/fields/search-field/)
- [Menu](../menu/)
- [Basiskomponente](../../../primitives/basics/base.md)
