# Breadcrumb

| Feld | Wert |
| ------ | ------ |
| **Kategorie** | `navigation` |
| **Erbt von** | `base` |
| **Varianten** | `pfad`, `gestutzt`, `zurueck` |
| **Zustände** | `aktiv`, `gestutzt` |
| **Gesten** | `tap`, `long-press` |
| **Animationen** | `expand`, `fade-in` |
| **Verwandt** | `menu`, `sidebar`, `tree-view`, `pagination`, `tabs` |
| **Status** | dokumentiert |

## Beschreibung
Ein Breadcrumb ist eine Pfadnavigation (Start > Wiki > Seite).

## Verwendungszweck

- Den Pfad zeigen
- Navigation
- Orientierung

## Varianten

| Variante | Beschreibung |
| ---------- | -------------- |
| **pfad** | die vollständige Folge von der Wurzel bis zum aktuellen Ort |
| **gestutzt** | lange Pfade zeigen `…` in der Mitte mit einem aufklappbaren Menü |
| **zurueck** | nur der vorherige Schritt als Knopf (schmale Bildschirme) |

Das Trennzeichen ist keine Variante, sondern das Attribut `separator` (`›`, `/`, `>`).

## Features

- Anklickbar
- Trennzeichen
- Aktiver Zustand

## Abgrenzung

- **Nicht verwechseln mit** [sidebar](../sidebar/) oder [menu](../menu/): diese zeigen, was es gibt,
  der Breadcrumb nur den Weg, der bis zum aktuellen Ort bereits gegangen wurde.
- **Nicht verwechseln mit** [pagination](../pagination/): dort blättert man durch eine Liste,
  hier wechselt man Ebenen.
- **Nicht verwechseln mit** [tabs](../tabs/): Tabs wechseln den Inhalt einer Ansicht,
  sie zeigen keine Hierarchie.

## Best Practices

- Der aktuelle Ort ist kein Link – man ist ja schon dort.
- Die Wurzel immer sichtbar halten; lange Pfade in der Mitte kürzen.
- Die Namen genau so verwenden, wie sie im Baum stehen, nicht umformulieren.
- Als eigene Landmarke kennzeichnen (`aria-label="Breadcrumb"`), den aktuellen Eintrag mit `aria-current`.
- Das Trennzeichen in der gesamten Anwendung einheitlich halten.

## Siehe auch

- [navigation – Übersicht](../index.md)
- [Tree View](../../data/tree-view/) — die Hierarchie selbst
- [Menu](../menu/) — aufklappbares Menü zwischen den Ebenen
- [Basiskomponente](../../../primitives/basics/base.md)
