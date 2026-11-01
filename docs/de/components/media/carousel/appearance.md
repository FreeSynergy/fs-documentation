# Carousel (Karussell) - Aussehen

## Grundlayout
Eine Folie sichtbar, Pfeile links und rechts, Punktreihe darunter.

```
┌─────────────────────────────────────────┐
│ [◀]   🖼️   [▶]                         │
│      Bild 1                             │
│  ● ○ ○ ○                                │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Aussehen |
|----------|----------|
| **automatik** | Pause-Knopf erscheint über der Folie |
| **manuell** | nur Pfeile und Punkte |
| **miniaturen** | Streifen kleiner Vorschaubilder unter der Folie |
| **überblenden** | keine Schiebebewegung, weicher Farbwechsel |

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| Small | 300px | Kleine Slideshows |
| Medium | 500px | Standard |
| Large | 700px | Große Slideshows |
| Full | 100% | Volle Breite |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Active Dot** | Primärfarbe | Aktiver Punkt |
| **Inactive Dot** | Grau | Inaktive Punkte |
| **Hover** | Heller | Hover-Zustand |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `zoom` | Bild vergrößert sich |
| `overlay` | Overlay mit Info |

## Reaktiv

- Das Karussell behält sein Seitenverhältnis; unter `small` Bildschirmbreite wird es vollbreit
  und die Pfeile werden durch Wischen ersetzt.
- Die Miniaturen-Leiste scrollt seitlich und zentriert die aktive Vorschau; auf schmalen
  Bildschirmen entfällt sie zugunsten der Punktreihe.
- Der Übergang ist `cross-slide` (Schieben) bzw. `cross-fade` (Variante `überblenden`);
  bei reduzierter Bewegung wird ersatzlos getauscht.
