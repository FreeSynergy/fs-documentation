# Breadcrumb (Brotkrümel)

| Feld | Wert |
|------|------|
| **Kategorie** | `navigation` |
| **Erbt von** | `base` |
| **Varianten** | `pfad`, `gestutzt`, `zurueck` |
| **Zustände** | `aktiv`, `gestutzt` |
| **Gesten** | `tap`, `long-press` |
| **Animationen** | `expand`, `fade-in` |
| **Verwandt** | `menu`, `sidebar`, `tree-view`, `pagination`, `tabs` |
| **Status** | dokumentiert |

## Beschreibung
Ein Breadcrumb ist eine Pfadnavigation (Home > Wiki > Seite).

## Verwendungszweck

- Pfad anzeigen
- Navigation
- Orientierung

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **pfad** | vollständige Folge von der Wurzel bis zum aktuellen Ort |
| **gestutzt** | lange Pfade zeigen in der Mitte `…` mit Aufklappmenü |
| **zurueck** | nur der vorherige Schritt als Knopf (schmale Bildschirme) |

Das Trennzeichen ist keine Variante, sondern das Attribut `separator` (`›`, `/`, `>`).

## Features

- Clickable
- Separator
- Active State

## Abgrenzung

- **Nicht verwechseln mit** [sidebar](../sidebar/) oder [menu](../menu/): die zeigen, was es gibt,
  der Brotpfad nur den zurückgelegten Weg zum aktuellen Ort.
- **Nicht verwechseln mit** [pagination](../pagination/): dort blättert man in einer Liste,
  hier wechselt man Ebenen.
- **Nicht verwechseln mit** [tabs](../tabs/): Tabs wechseln den Inhalt einer Ansicht,
  sie zeigen keine Hierarchie.

## Best Practices

- Der aktuelle Ort ist kein Link — er ist schon da.
- Wurzel immer sichtbar lassen, lange Wege in der Mitte kürzen.
- Namen genau wie im Baum verwenden, nicht umformulieren.
- Als eigenes Landmark beschriften (`aria-label="Brotpfad"`), aktueller Punkt mit `aria-current`.
- Trennzeichen in der ganzen Anwendung einheitlich halten.

## Siehe auch

- [navigation – Übersicht](../index.md)
- [Tree View](../../data/tree-view/) — die Hierarchie selbst
- [Menu](../menu/) — Aufklappmenü zwischen den Ebenen
- [Basiskomponente](../../basics/base/)
