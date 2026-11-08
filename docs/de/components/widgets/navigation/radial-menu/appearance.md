# Radial Menu - Erscheinungsbild

## Grundlayout

Ein Eintrag sitzt auf dem Kreis um den Anker, nicht in einer Reihe. Der Ankerkern ist meist
inaktiv; er ist der Ausgangspunkt aller Richtungen.

```
                        ○
                   ○         ○
              ○                 ○
          ○        ◆       ◆        ○
        ○                              ○
       ○            ◆   ●   ◆          ○      ●  Anker (Mitte, inaktiv)
        ○                              ○      ◆ Einträge in Ring 1
          ○        ◆       ◆        ○          ○ Einträge in Ring 2
              ○                 ○
                   ○         ○
                        ○
```

Geometrie statt Lineal: Einträge werden über **Winkel** und **Radius** platziert.

| Größe | Bedeutung |
|-------|-----------|
| `radius` | Abstand Ankermitte → Eintragsmitte (Ring 1) |
| `ringGap` | Abstand zwischen zwei Ringen |
| `itemSize` | Durchmesser eines Eintrags |
| Winkelschritt | `sweepAngle / items` — bei 6 Einträgen und einem Vollkreis 60° |
| `startAngle` | Ausrichtung des ersten Eintrags (0° = oben) |
| `coneAngle` | Winkelbereich, in dem ein Ring mit Unterpunkten erscheint |

## Varianten

### ring (Standard)

```
        ◆          ◆              Einträge liegen auf einem Kreis,
            \      |              jeder Eintrag ist eine eigene
             \     |              treffbare Fläche
        ◆ ──  ●  ── ◆
                    |
        ◆          ◆
```

### sektoren (Tortenmenü)

```
   ╲   │   ╱        Segmente füllen den Ring, die Mitte bleibt
    ╲  │  ╱         frei. Ein Segment wird über seinen
  ─────●───────     Winkelbereich getroffen — nicht über die
    ╱  │  ╲         Mitte des Eintrags. Darum funktionieren
   ╱   │   ╲        auch kleine Zeigerbewegungen zuverlässig.
```

### facher (Schnellwahl an einer Ecke oder Kante)

```
   ┌───┬──────────────          Anker oben rechts, Ring nach innen
   │ ●  ╲         │             auf einen Viertel- oder Halbfächer
   │  ◆   ╲   ○   │             begrenzt
   │   ◆    ╲     │
   └──────────────┘
```

### launcher (zentriert, mehrere Ringe)

```
        ○   ○   ○             Ring 2 = Unterpunkte des aktiven
      ○  ◆  ●  ◆  ○           Eintrags. Nur der aktive Zweig
        ○   ◆   ○             öffnet den nächsten Ring.
```

### kontext (an der Zeigerposition)

```
   Rechtsklick ──►  ● an der Zeigerposition,
                    Ringe wachsen von dort nach außen
```

## Größen

| Größe | Anker Ø | Eintrag Ø | Radius R1 | Radius R2 | Verwendung |
|-------|---------|-----------|-----------|-----------|------------|
| `small` | 28 px | 32 px | 56 px | 96 px | dichte Flächen, Karte, Whiteboard |
| `medium` | 36 px | 40 px | 72 px | 124 px | Standard am Desktop |
| `large` | 44 px | 48 px | 88 px | 148 px | Touch, Kiosk, Controller |

`large` entspricht der minimalen Trefffläche aus der [Basiskomponente](../../../primitives/basics/base.md).
Auf Touch-Flächen ist `small` ungeeignet, weil sich die Einträge im Ring berühren.

## Farben und Zustände

| Zustand | Erscheinungsbild | Beschreibung |
|---------|------------------|--------------|
| **default** | Primärton, gesättigt | Eintrag in einem offenen Ring |
| **hover** | heller, etwas größer | Zeiger steht auf dem Eintrag |
| **active** | Akzentfarbe, gefüllter Kern | Eintrag gewählt oder sein Zweig geöffnet |
| **focus** | 2 px Fokusrahmen außen | Eintrag per Tastatur erreicht |
| **dimmed** | gesättigt → 40 % Deckkraft | Eintrag gehört nicht zum aktiven Zweig |
| **pinned** | dezentes Schattenleuchten | Menü bleibt nach einem Klick offen |
| **disabled** | ausgegraut, ohne Rahmen | Eintrag nicht auswählbar |
| **loading** | [spinner](../../../primitives/feedback/spinner/) im Eintrag | Ziel lädt noch |

## Effekte bei Hover und Fokus

| Effekt | Beschreibung |
|--------|--------------|
| `grow` | Eintrag wächst auf 110 % (`scaleOnHover`) |
| `shift` | Eintrag rückt 4–8 px radial nach außen (`shiftOnHover`) |
| `lift` | der Schatten wächst, der Eintrag hebt sich vom Ring ab |
| `glow` | Leuchten um den Rand des aktiven Eintrags |
| `morph` | die Form des aktiven Eintrags wechselt sanft (Kreis → Sechseck) |
| `ring-rotate` | der ganze Ring dreht sich ein Stück, damit der aktive Eintrag nach oben zeigt |
| `label-reveal` | die Beschriftung erscheint nur beim aktivierten Eintrag |
| `sector-lift` | bei `sektoren`: das Segment hebt sich als Keil aus dem Ring |

## Responsiv

| Haltepunkt | Verhalten |
|------------|-----------|
| Desktop | öffnet beim Überfahren (`trigger: hover`), Unterpunkte im nächsten Ring |
| Tablet | öffnet per Tippen, Unterpunkte nach einem zweiten Tippen |
| Mobil (< 600 px) | ein Ring, `large`, Auswahl per Drücken–Ziehen–Loslassen |
| schmaler Rand | `clamp`: der volle Kreis wird zu einem Viertel- oder Halbfächer |
| `prefers-reduced-motion` | `radial-out` → `fade-in`, kein Wachsen, keine Mitdrehung |
| sehr große Flächen (Whiteboard, Karte) | bis zu drei Ringe, `launcher` frei positionierbar |

## Formen und Ecken

Form und Anzahl der Ecken tragen Information — sie sind nicht nur Dekoration.

| Form (`shape`) | Ecken | Beschreibung | Verwendung |
|----------------|-------|--------------|------------|
| `kreis` | – | glatte runde Fläche | Standard in allen Ringen |
| `quadrat` | 4 | Vieleck mit `cornerRadius = 0` | kantige Flächen, Rasteroptik |
| `abgerundet` | 4 | Vieleck mit leicht abgerundeten Ecken | Brücke zwischen kantig und rund |
| `squircle` | 4 | Superellipse: durchgehend sanft gerundet | Icon-Optik, Touch-Flächen |
| `dreieck` | 3 | mit `rotation`, sodass eine Ecke nach außen zeigt | zeigt die Richtung des Eintrags an |
| `fuenfeck` | 5 | Fünfeck | Markierung eines besonderen Eintrags |
| `sechseck` | 6 | kachelbar, Nachbarn schließen bündig an | mehrere Menüs nebeneinander, Waben |
| `achteck` | 8 | Vieleck mit acht Ecken | unterscheidbar, ohne wie ein Kreis zu wirken |
| `vieleck` | `sides` = 3–12 | regelmäßiges Vieleck mit einstellbarer Eckenzahl | die Eckenzahl zeigt die Anzahl der Einträge im Ring |
| `keil` | 2 Ecken + Bogen | Tortenstück (`sektoren`) | Richtungswahl, große Trefffläche |
| `bluete` | n Wellen | gewellter Rand, eine Welle pro Nachbareintrag | der Rand zählt die Einträge im Ring |
| `stern` | 2n Spitzen | Spitzen zeigen zu den Nachbarn | nur der aktive Eintrag eines Rings |

Regeln für die Eckenzahl:

- `sides` steigt von 3 (Dreieck) über 4, 5, 6, 8 bis 12. Ab etwa 8 Ecken **und**
  `cornerRadius > 0` wirkt die Form wie ein Kreis — für eine unterscheidbare Silhouette
  daher höchstens 6 Ecken oder scharfe Ecken behalten.
- `cornerRadius` steuert die Rundung unabhängig davon: `0` = scharfe Ecke, halbe Seitenlänge =
  stark gerundet, darüber wächst die Form zum Kreis. Ein Quadrat mit halber Seitenlänge als Radius
  ist ein Kreis — die Rundung ist ein Kontinuum, kein Schalter.
- Lies die Eckenzahl als Information: 3 Ecken = „Richtung“, 6 Ecken = „Gruppe“,
  `sides = items` = „so viele Einträge hat der Ring“. Sonst bleibt die Form neutral.
- Nur der **aktive** Eintrag ändert seine Form (`morph`), die übrigen bleiben konstant —
  sonst flackert der ganze Ring.
- `rotation` dreht die Form, sodass eine Ecke, Spitze oder Welle nach außen zum Ring zeigt.
- Der Ankerkern (`●`) behält immer die Grundform; ändert er seine Form, liest sich das Menü
  selbst als Aktion.

## Ringe und Ebenen

| Ebene | Ring | Radius | Inhalt |
|-------|------|--------|--------|
| 1 | Ring 1 | `radius` | Haupteinträge des Menüs |
| 2 | Ring 2 | `radius + itemSize + ringGap` | Unterpunkte des aktiven Eintrags |
| 3 | Ring 3 | `radius + 2 · (itemSize + ringGap)` | Unter-Unterpunkte |

- Nur der aktive Zweig öffnet den nächsten Ring; die übrigen Einträge bleiben im vorherigen Ring.
- Die Einträge eines neuen Rings erscheinen im **Winkelbereich** ihres übergeordneten Eintrags
  (`coneAngle`), nicht verteilt über den ganzen Kreis.
- Ein Eintrag darf nicht tiefer liegen, als der Anker vom Rand entfernt ist — dann greift `clamp`
  und der Ring wird zum Fächer.
- Geschwister des aktiven Eintrags werden `dimmed`, ihr Winkelbereich bleibt aber treffbar
  (direkter Wechsel ohne Umweg über den Anker).

## Siehe auch

- [Radial Menu – Beschreibung](./description.md)
- [Attribute](./attributes.md)
- [Verwendung](./usage.md)
- [radial-out](../../../../interactions/animations/entrance/radial-out/) und [radial-in](../../../../interactions/animations/exit/radial-in/)
