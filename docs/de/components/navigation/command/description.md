# Command (Befehlspalette)

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

Die Befehlspalette ist ein Overlay mit einem Eingabefeld und einer Trefferliste.
Sie startet Programme, wechselt Ansichten und führt Aktionen aus — erreicht durch
Tastenkürzel statt durch Menüsuche.

## Verwendungszweck

- Schneller Zugriff auf Programme und Ansichten im Desktop-Client
- Aktionen ausführen, ohne den Kontext zu verlassen
- Kurzhilfe: welche Befehle in dieser Ansicht verfügbar sind

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **palette** | zentriertes Overlay, per `Strg`/`Cmd` + `K` |
| **inline** | Palette eingebettet in eine Seitenleiste oder Werkzeugleiste |

## Features

- Suchbegriffe werden entkontextet gestartet („neue Aufgabe“ findet das Ziel)
- Treffer gruppiert nach Programm, Ansicht und Aktion
- Letzte und häufige Befehle stehen oben, auch ohne Eingabe
- Tastaturnavigation: `Pfeil hoch/runter`, `Enter` ausführen, `Esc` schließen

## Abgrenzung

- **Nicht verwechseln mit** [search-field](../../fields/search-field/): Suche findet Inhalte,
  die Palette führt Aktionen aus.
- **Nicht verwechseln mit** [menu](../menu/): Menüs zeigen das Angebot vollständig,
  die Palette nur passende Treffer.

## Best Practices

- Befehle nach Verb Objekt benennen („Aufgabe anlegen“, nicht „Neu“).
- Pro Befehl ein Kürzel anzeigen, wenn eines existiert.
- Ergebnisse nach 50 Treffern abschneiden und zum Präzisieren auffordern.

## Siehe auch

- [Search Field](../../fields/search-field/)
- [Menu](../menu/)
- [Basiskomponente](../../basics/base/)
