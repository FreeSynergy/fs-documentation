# Table of Contents

| Feld | Wert |
|------|------|
| **Kategorie** | `data` |
| **Erbt von** | `base` |
| **Varianten** | `randspalte`, `block`, `aufklappbar` |
| **Zustände** | `aktiv` |
| **Gesten** | `tap` |
| **Animationen** | `expand`, `collapse`, `highlight` |
| **Verwandt** | `tree-view`, `sidebar`, `breadcrumb`, `tabs` |
| **Status** | dokumentiert |

## Beschreibung
Ein Inhaltsverzeichnis ist eine Übersicht über Kapitel und Abschnitte.

## Verwendungszweck

- Dokumentation
- Bücher
- Webseiten
- Kapitelübersicht

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **randspalte** | neben dem Text, bleibt beim Scrollen stehen |
| **block** | am Anfang des Textes als Liste |
| **aufklappbar** | eingeklappter Knopf, die Liste klappt darüber auf |

## Features

- Scroll-Spy (markiert den aktuellen Abschnitt)
- Klick zum Springen (springt zu einem Abschnitt)
- Einklappbare Abschnitte (ein- und ausklappen)

## Abgrenzung

- **Nicht verwechseln mit** [tree-view](../tree-view/): die Inhaltsliste zeigt die Überschriften **eines**
  Textes mit Sprungzielen, die Tree View zeigt beliebige Datenhierarchien.
- **Nicht verwechseln mit** [sidebar](../../navigation/sidebar/): die Sidebar wechselt die
  Ansicht, diese Inhaltsliste bleibt in derselben Ansicht und scrollt darin.
- **Nicht verwechseln mit** [breadcrumb](../../navigation/breadcrumb/): der Breadcrumb zeigt, wo du
  bist; die Inhaltsliste zeigt, was es gibt.
- **Nicht verwechseln mit** [tabs](../../navigation/tabs/): Tabs tauschen Inhalte aus, hier bleibt
  alles auf einer Fläche.

## Best Practices

- Nur Überschriften ab der zweiten Ebene, höchstens drei Ebenen tief.
- Die gerade sichtbare Überschrift markieren (Scroll-Spy) und die URL mit dem Anker aktualisieren.
- Beim Springen sanft scrollen, das Ziel "Zum Abschnitt" aber gut sichtbar halten.
- Auf schmalen Bildschirmen zu `aufklappbar` wechseln, nicht die halbe Höhe belegen.
- Die Nummerierung nur übernehmen, wenn sie auch im Text sichtbar ist.

## Layout

```
┌─────────────────────────────────────────┐
│ 📚 Inhalt                               │
│                                         │
│  1. Kapitel 1                           │
│  2. Kapitel 2                           │
│  3. Kapitel 3                           │
│    3.1. Unterkapitel 1                  │
│    3.2. Unterkapitel 2                  │
└─────────────────────────────────────────┘
```

## Siehe auch

- [data – Übersicht](../index.md)
- [Tree View](../tree-view/) — Datenhierarchie
- [Sidebar](../../navigation/sidebar/) — Ansicht wechseln
- [Basiskomponente](../../../primitives/basics/base.md)
