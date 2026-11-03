# Popover (Inhaltspopover)

| Feld | Wert |
|------|------|
| **Kategorie** | `overlays` |
| **Erbt von** | `base` |
| **Varianten** | `inhalt`, `aktionen`, `formular` |
| **Zustände** | `open` |
| **Gesten** | `tap` |
| **Animationen** | `expand`, `fade-in` |
| **Verwandt** | `tooltip`, `modal`, `select`, `context-menu`, `base` |
| **Status** | dokumentiert |

## Beschreibung

Ein Popover ist ein kleines Overlay mit interaktivem Inhalt: Aktionen, eine
Vorschau oder ein kurzes Formular. Es ist an ein Auslöser-Element gedockt,
übernimmt aber – anders als ein Modal – nicht den ganzen Bildschirm.

## Verwendungszweck

- Sekundäraktionen an einem Eintrag (mehr-Menü mit Buttons)
- Schnelleingaben ohne Seitenwechsel (Datum setzen, Label zuweisen)
- Detailvorschau zu einem Eintrag (Kurzfassung vor dem Öffnen)

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **inhalt** | Text, Bilder oder Vorschau, keine Formulareingabe |
| **aktionen** | Liste von Aktionen (Abgrenzung zu context-menu: fester Auslöser) |
| **formular** | kleines Formular, z. B. Datum oder Farbe setzen |

## Features

- Fokus wandert in das Popover und nach dem Schließen zum Auslöser zurück
- Schließen per Klick außerhalb, Escape oder Aktion im Popover
- Andockposition wie beim [tooltip](../tooltip/)

## Abgrenzung

- **Nicht verwechseln mit** [tooltip](../tooltip/): Tooltip = nur Text, nie
  interaktiv.

- **Nicht verwechseln mit** [modal](../modal/): ein Modal blockiert
  und zentriert; ein Popover bleibt am Auslöser und lässt das Übrige bedienbar.

- **Nicht verwechseln mit** [dropdown](../../fields/select/): ein Dropdown
  wählt einen Wert aus einer Liste, ein Popover trägt beliebigen Inhalt.

- **Nicht verwechseln mit** [context-menu](../context-menu/): das
  Kontextmenü folgt dem Rechtsklick, ein Popover einem festen Auslöser.

## Best Practices

- Escape und Klick außerhalb müssen schließen; Fokus kehrt zum Auslöser zurück.
- `aria-expanded` am Auslöser ist Pflicht.
- Kein voller Dialog-Ersatz: für mehr als ~5 Eingabefelder ein `modal` verwenden.

## Siehe auch

- [Tooltip](../tooltip/)
- [Modal](../modal/)
- [Context Menu](../context-menu/)
- [Basiskomponente](../../basics/base/)
