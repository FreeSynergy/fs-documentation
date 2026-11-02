# Radial Menu (Kreismenü) - Aussehen

## Grundlayout

Ein Punkt sitzt auf dem Kreis um den Anker, nicht in einer Reihe. Der Ankerkern ist
meist inaktiv; er ist der Ausgangspunkt aller Richtungen.

```
                        ○
                   ○         ○
              ○                 ○
          ○        ◆       ◆        ○
        ○                              ○
       ○            ◆   ●   ◆          ○      ●  Anker (Mitte, inaktiv)
        ○                              ○      ◆ Punkte in Ring 1
          ○        ◆       ◆        ○          ○ Punkte in Ring 2
              ○                 ○
                   ○         ○
                        ○
```

Geometrie statt Lineal: Punkte werden über **Winkel** und **Radius** gesetzt.

| Größe | Bedeutung |
|-------|-----------|
| `radius` | Abstand Ankermitte → Punktmitte (Ring 1) |
| `ringGap` | Abstand zweier Ringe zueinander |
| `itemSize` | Durchmesser eines Punktes |
| Winkelschritt | `sweepAngle / items` — bei 6 Punkten und Vollkreis 60° |
| `startAngle` | Ausrichtung des ersten Punktes (0° = oben) |
| `coneAngle` | Winkelbereich, in dem ein Unterpunkt-Ring erscheint |

## Varianten

### ring (Standard)

```
        ◆          ◆              Punkte liegen auf einem Kreis,
            \      |              jeder Punkt ist eine eigene
             \     |              trefferbare Fläche
        ◆ ──  ●  ── ◆
                    |
        ◆          ◆
```

### sektoren (Pie-Menu)

```
   ╲   │   ╱        Segmente füllen den Ring, die Mitte bleibt
    ╲  │  ╱         leer. Getroffen ist ein Segment über seinen
  ─────●───────     Winkelbereich — nicht über die Punktmitte.
    ╱  │  ╲         Deshalb funktionieren auch kleine Zeiger-
   ╱   │   ╲        bewegungen zuverlässig.
```

### facher (Speed-Dial an Ecke oder Kante)

```
   ┌───┬──────────────          Anker oben rechts, Ring nur als
   │ ●  ╲         │             Viertel- bzw. Halbfächer nach
   │  ◆   ╲   ○   │             innen geklemmt
   │   ◆    ╲     │
   └──────────────┘
```

### launcher (Mittig, mehrere Ringe)

```
        ○   ○   ○             Ring 2 = Unterpunkte des aktiven
      ○  ◆  ●  ◆  ○           Punktes. Nur der aktive Zweig
        ○   ◆   ○             öffnet den nächsten Ring.
```

### kontext (an der Zeigerposition)

```
   Rechtsklick ──►  ● an der Zeigerstelle,
                    Ringe wachsen von dort nach außen
```

## Größen

| Größe | Anker-Ø | Punkt-Ø | Radius R1 | Radius R2 | Verwendung |
|-------|---------|---------|-----------|-----------|------------|
| `small` | 28 px | 32 px | 56 px | 96 px | dichte Flächen, Karte, Whiteboard |
| `medium` | 36 px | 40 px | 72 px | 124 px | Standard am Desktop |
| `large` | 44 px | 48 px | 88 px | 148 px | Touch, Kiosk, Controller |

`large` entspricht der Mindesttrefferfläche aus der [Basiskomponente](../../basics/base/).
Auf Touch-Oberflächen ist `small` ungeeignet, weil die Punkte im Ring einander berühren.

## Farben und Zustände

| Zustand | Aussehen | Beschreibung |
|---------|----------|--------------|
| **default** | Primärton, gesättigt | Punkt im offenen Ring |
| **hover** | heller, leicht größer | Zeiger steht auf dem Punkt |
| **active** | Akzentfarbe, gefüllter Kern | Punkt gewählt bzw. sein Zweig geöffnet |
| **focus** | 2 px Ringsichtlinie außen | Punkt über Tastatur erreicht |
| **dimmed** | gesättigt → 40 % Deckkraft | Punkt gehört nicht zum aktiven Zweig |
| **pinned** | dezenter Schattenschein | Menü bleibt nach Klick offen |
| **disabled** | ausgegraut, keine Kontur | Punkt nicht wählbar |
| **loading** | [spinner](../../feedback/spinner/) im Punkt | Ziel wird noch geladen |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `grow` | Punkt wächst auf 110 % (`scaleOnHover`) |
| `shift` | Punkt wandert 4–8 px radial nach außen (`shiftOnHover`) |
| `lift` | Schatten wächst, Punkt hebt sich vom Ring ab |
| `glow` | Leuchten um die Kontur des aktiven Punktes |
| `morph` | Form des aktiven Punktes wechselt weich (Kreis → Sechseck) |
| `ring-rotate` | ganzer Ring dreht ein Stück, damit der aktive Punkt nach oben zeigt |
| `label-reveal` | Beschriftung erscheint erst am aktivierten Punkt |
| `sector-lift` | in `sektoren`: Segment springt als Keil aus dem Ring heraus |

## Reaktiv

| Bereich | Verhalten |
|---------|-----------|
| Desktop | Öffnen bei Hover (`trigger: hover`), Unterpunkte im nächsten Ring |
| Tablet | Öffnen per Tipp, Unterpunkte nach zweitem Tipp |
| Mobile (< 600 px) | ein Ring, `large`, Auswahl durch Drücken–Ziehen–Loslassen |
| Schmaler Rand | `clamp`: Vollkreis wird zum Viertel- oder Halbfächer |
| `prefers-reduced-motion` | `radial-out` → `fade-in`, kein Wachstum, keine Mitrotation |
| Sehr große Flächen (Whiteboard, Karte) | bis drei Ringe, `launcher` frei positionierbar |

## Formen und Ecken

Form und Eckzahl tragen Information — sie sind nicht nur Dekoration.

| Form (`shape`) | Ecken | Beschreibung | Verwendung |
|----------------|-------|--------------|------------|
| `kreis` | – | glatte Kreisfläche | Standard in allen Ringen |
| `quadrat` | 4 | Vieleck mit `cornerRadius = 0` | eckige Oberflächen, Rasteroptik |
| `abgerundet` | 4 | Vieleck mit weich gerundeten Ecken | Brücke zwischen eckig und rund |
| `squircle` | 4 | Superellipse: durchgehend weich verrundet | Symbol-Optik, Touch-Flächen |
| `dreieck` | 3 | mit `rotation` auf eine Ecke nach außen | weist die Richtung des Punktes |
| `fuenfeck` | 5 | Fünfeck | Auszeichnung eines Sonderpunktes |
| `sechseck` | 6 | parkettierbar, Nachbarn schließen bündig | mehrere Menüs nebeneinander, Honigwaben |
| `achteck` | 8 | Vieleck mit acht Ecken | Abgrenzung ohne Kreis zu wirken |
| `vieleck` | `sides` = 3–12 | regelmäßiges Vieleck mit einstellbarer Eckzahl | Eckzahl zeigt Punkteanzahl des Ringes |
| `keil` | 2 Ecken + Bogen | Tortensegment (`sektoren`) | Richtungsauswahl, große Trefferfläche |
| `bluete` | n Wellen | welliger Rand, eine Welle je Nachbarpunkt | Rand zählt die Punkte des Ringes |
| `stern` | 2n Zacken | Zacken zeigen zu den Nachbarn | nur der aktive Punkt eines Ringes |

Regeln für die Eckzahl:

- `sides` wächst von 3 (Dreieck) über 4, 5, 6, 8 bis 12. Ab etwa 8 Ecken **und**
  `cornerRadius > 0` liest sich die Form als Kreis — für eine unterscheidbare
  Silhouette also entweder höchstens 6 Ecken oder scharfe Ecken behalten.
- `cornerRadius` steuert die Rundung unabhängig davon: `0` = scharfe Ecke,
  halbe Seitenlänge = stark verrundet, darüber wächst die Form Richtung Kreis.
  Ein Quadrat mit der halben Seitenlänge als Radius ist ein Kreis — die Rundung ist
  also ein Kontinuum, keine Umschaltung.
- Eckzahl als Information fassen: 3 Ecken = „Richtung“, 6 Ecken = „Gruppe“,
  `sides = items` = „so viele Punkte hat dieser Ring“. Sonst bleibt die Form neutral.
- Nur der **aktive** Punkt wechselt seine Form (`morph`), die übrigen bleiben konstant —
  sonst flackert der ganze Ring.
- `rotation` dreht die Form, damit eine Ecke, Zacke oder Welle nach außen zum Ring zeigt.
- Der Ankerkern (`●`) behält immer die Grundform; ändert er seine Form, wirkt das Menü
  selbst als Aktion.

## Ringe und Ebenen

| Ebene | Ring | Radius | Inhalt |
|-------|------|--------|--------|
| 1 | Ring 1 | `radius` | Hauptpunkte des Menüs |
| 2 | Ring 2 | `radius + itemSize + ringGap` | Unterpunkte des aktiven Punktes |
| 3 | Ring 3 | `radius + 2 · (itemSize + ringGap)` | Unter-Unterpunkte |

- Nur der aktive Zweig öffnet den nächsten Ring; die übrigen Punkte bleiben im bisherigen Ring.
- Die Punkte eines neuen Ringes erscheinen im **Winkelbereich** ihres Elternpunktes
  (`coneAngle`), nicht verteilt über den ganzen Kreis.
- Ein Punkt darf tiefer liegen, als der Anker weit vom Rand entfernt ist — dann greift
  `clamp` und der Ring wird zum Fächer.
- Geschwister des aktiven Punktes werden `dimmed`, ihr Winkelbereich bleibt aber trefferbar
  (direkter Wechsel ohne Umweg über den Anker).

## Siehe auch

- [Radial Menu – Beschreibung](./description.md)
- [Attribute](./attributes.md)
- [Verwendung](./usage.md)
- [radial-out](../../../animations/entrance/radial-out/) und [radial-in](../../../animations/exit/radial-in/)
