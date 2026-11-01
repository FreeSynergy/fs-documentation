# Tree View (Baumansicht) - Aussehen

## Grundlayout
Ein Tree View ist eine hierarchische Verzeichnisstruktur mit Ein-/Ausklappen.

```
┌─────────────────────────────────────────┐
│ ▶ Ordner 1                              │
│   └─ Datei 1                            │
│   └─ Datei 2                            │
├─────────────────────────────────────────┤
│ ▶ Ordner 2                              │
│   └─ Datei 3                            │
│   └─ Datei 4                            │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Aussehen |
|----------|----------|
| **einfach** | Dreieck und Name, Einzug pro Ebene |
| **icon** | Typsymbol zwischen Dreieck und Name |
| **kästchen** | Kästchen links, halber Haken bei Teilauswahl |
| **verschiebbar** | Cursor zum Ziehen, Ziel wird als Linie markiert |

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| Small | 200px | Inline |
| Medium | 300px | Standard |
| Large | 400px | Featured |
| Full | 100% | Volle Breite |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Default** | Hell | Standard |
| **Hover** | Heller | Hover-Zustand |
| **Active** | Primärfarbe | Aktiver Zustand |
| **Disabled** | Grau | Deaktiviert |
| **Selected** | Dunkel | Ausgewählter Knoten |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `background` | Hintergrund ändert sich |
| `border` | Rand leuchtet auf |

## Expand/Collapse

```
├─ ▼ Ordner 1
│   ├─ ▸ Unterordner
│   ├─ ─ Datei 1
│   └─ ─ Datei 2
└─ ▸ Ordner 2
```

## Reaktiv

- Der Einzug beträgt 16 px pro Ebene; auf schmalen Bildschirmen 12 px, damit auch tiefe
  Bäume ohne seitliches Scrollen lesbar bleiben.
- Zu lange Namen werden in der Mitte gekürzt, damit die Erweiterung rechts sichtbar bleibt.
- Aufklappen animiert mit `expand`; die Scrollposition des angeklickten Knotens bleibt dabei
  an derselben Stelle.
