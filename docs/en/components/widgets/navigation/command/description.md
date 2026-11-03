# Command

| Field | Value |
| ------ | ------ |
| **Category** | `navigation` |
| **Inherits from** | `base` |
| **Variants** | `palette`, `inline` |
| **States** | `open`, `empty` |
| **Gestures** | `tap`, `type` |
| **Animations** | `fade-in`, `expand` |
| **Related** | `search-field`, `menu`, `modal` |
| **Role** | `dialog` |
| **State** | documented |

## Description

Die Befehlspalette ist ein Overlay mit einem Eingabefeld und einer Trefferliste.
Sie startet Programme, wechselt Ansichten und führt Aktionen aus — erreicht durch
Tastenkürzel statt durch Menüsuche.

## Purpose

- Schneller Zugriff auf Programme und Ansichten im Desktop-Client
- Aktionen ausführen, ohne den Kontext zu verlassen
- Kurzhilfe: welche Befehle in dieser Ansicht verfügbar sind

## Variants

| Variant | Description |
| ---------- | -------------- |
| **palette** | zentriertes Overlay, per `Strg`/`Cmd` + `K` |
| **inline** | Palette eingebettet in eine Seitenleiste oder Werkzeugleiste |

## Features

- Suchbegriffe werden entkontextet gestartet („neue Aufgabe“ findet das Ziel)
- Treffer gruppiert nach Programm, Ansicht und Aktion
- Letzte und häufige Befehle stehen oben, auch ohne Eingabe
- Tastaturnavigation: `Pfeil hoch/runter`, `Enter` ausführen, `Esc` schließen

## Distinction

- **Nicht verwechseln mit** [search-field](../../../primitives/fields/search-field/): Suche findet Inhalte,
  die Palette führt Aktionen aus.
- **Nicht verwechseln mit** [menu](../menu/): Menüs zeigen das Angebot vollständig,
  die Palette nur passende Treffer.

## Best Practices

- Befehle nach Verb Objekt benennen („Aufgabe anlegen“, nicht „Neu“).
- Pro Befehl ein Kürzel anzeigen, wenn eines existiert.
- Ergebnisse nach 50 Treffern abschneiden und zum Präzisieren auffordern.

## See also

- [Search Field](../../../primitives/fields/search-field/)
- [Menu](../menu/)
- [Base component](../../../primitives/basics/base.md)
