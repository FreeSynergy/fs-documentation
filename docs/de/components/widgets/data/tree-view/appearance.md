# Tree View - Erscheinungsbild

## Grundlayout
Eine Tree View ist eine hierarchische Verzeichnisstruktur mit Ein- und Ausklappen.

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

| Variante | Erscheinungsbild |
|----------|------------------|
| **einfach** | Dreieck und Name, eine Einrückung pro Ebene |
| **icon** | Typsymbol zwischen Dreieck und Name |
| **kästchen** | Checkbox links, halber Haken bei Teilauswahl |
| **verschiebbar** | Cursor zum Ziehen, das Ziel wird als Linie markiert |

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| small | 200px | im Text |
| medium | 300px | Standard |
| large | 400px | hervorgehoben |
| full | 100% | volle Breite |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Standard** | hell | Standard |
| **Hover** | heller | Zustand beim Überfahren |
| **Aktiv** | Primärfarbe | aktiver Zustand |
| **Deaktiviert** | Grau | deaktiviert |
| **Ausgewählt** | dunkel | ausgewählter Knoten |

## Effekte bei Hover und Fokus

| Effekt | Beschreibung |
|--------|--------------|
| `background` | der Hintergrund wechselt |
| `border` | der Rahmen leuchtet auf |

## Responsiv

- Die Einrückung beträgt 16 px pro Ebene; auf schmalen Bildschirmen 12 px, damit tiefe
  Bäume ohne seitliches Scrollen lesbar bleiben.
- Zu lange Namen werden in der Mitte gekürzt, damit die Endung rechts sichtbar bleibt.
- Das Ausklappen wird mit `expand` animiert; die Scrollposition des angeklickten Knotens bleibt
  dabei an derselben Stelle.

## Ein- und Ausklappen

```
├─ ▼ Ordner 1
│   ├─ ▸ Unterordner
│   ├─ ─ Datei 1
│   └─ ─ Datei 2
└─ ▸ Ordner 2
```
