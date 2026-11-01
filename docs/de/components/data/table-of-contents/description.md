# Table of Contents (Inhaltsverzeichnis)

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
Ein Table of Contents ist eine Übersicht über Kapitel/Sectionen.

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
| **aufklappbar** | eingeklappter Knopf, Liste klappt darüber auf |

## Features

- Scroll Spy (Markiert aktuelle Section)
- Click to Scroll (Springen zu Section)
- Collapsible Sections (Ein/Ausklappen)

## Abgrenzung

- **Nicht verwechseln mit** [tree-view](../tree-view/): das Verzeichnis zeigt Überschriften **eines**
  Textes mit Sprungzielen, die Baumansicht zeigt beliebige Datenhierarchien.
- **Nicht verwechseln mit** [sidebar](../../navigation/sidebar/): die Seitenleiste wechselt die
  Ansicht, dieses Verzeichnis bleibt in derselben und scrollt darin.
- **Nicht verwechseln mit** [breadcrumb](../../navigation/breadcrumb/): der Brotpfad zeigt, wo man
  ist; das Verzeichnis, was es alles gibt.
- **Nicht verwechseln mit** [tabs](../../navigation/tabs/): Tabs tauschen Inhalt, hier bleibt alles
  auf einer Fläche.

## Best Practices

- Nur Überschriften ab der zweiten Ebene, höchstens drei Ebenen tief.
- Die gerade sichtbare Überschrift markieren (Scroll-Spy) und die URL mit dem Anker aktualisieren.
- Sprung weich scrollen, aber `Sprung zum Abschnitt`-Ziel deutlich sichtbar machen.
- Auf schmalen Bildschirmen auf `aufklappbar` wechseln, nicht die halbe Höhe belegen.
- Nummerierung nur übernehmen, wenn der Text sie auch sichtbar trägt.

## Layout

```
┌─────────────────────────────────────────┐
│ 📚 Inhaltsverzeichnis                   │
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
- [Basiskomponente](../../basics/base/)
