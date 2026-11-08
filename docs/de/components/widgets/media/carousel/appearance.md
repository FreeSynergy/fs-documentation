# Carousel - Erscheinungsbild

## Grundlayout
Eine Folie ist sichtbar, links und rechts Pfeile, darunter eine Reihe Punkte.

```
┌─────────────────────────────────────────┐
│ [◀]   🖼️   [▶]                          │
│      Bild 1                             │
│  ● ○ ○ ○                                │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Erscheinungsbild |
|----------|------------------|
| **automatik** | Pause-Knopf erscheint über der Folie |
| **manuell** | nur Pfeile und Punkte |
| **miniaturen** | Streifen mit kleinen Vorschaubildern unter der Folie |
| **überblenden** | keine Schiebebewegung, sondern ein weiches Überblenden |

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| Small | 300px | kleine Diashows |
| Medium | 500px | Standard |
| Large | 700px | große Diashows |
| Full | 100% | volle Breite |

## Farben und Zustände

| Zustand | Farbe | Beschreibung |
|---------|-------|--------------|
| **Active Dot** | Primärfarbe | aktiver Punkt |
| **Inactive Dot** | grau | inaktive Punkte |
| **Hover** | heller | Hover-Zustand |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `zoom` | das Bild wird größer |
| `overlay` | Overlay mit Informationen |

## Responsiv

- Der Carousel behält sein Seitenverhältnis; unterhalb einer kleinen Bildschirmbreite (`small`)
  wird er volle Breite und die Pfeile werden durch Wischen ersetzt.
- Der Miniaturstreifen scrollt seitlich und zentriert die aktive Vorschau; auf schmalen
  Bildschirmen entfällt er zugunsten der Punkte-Reihe.
- Der Übergang ist `cross-slide` (Schieben) oder `cross-fade` (Variante `überblenden`);
  bei reduzierter Bewegung werden die Folien ohne Effekt getauscht.
