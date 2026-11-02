# Radial Menu (Kreismenü)

| Feld | Wert |
|------|------|
| **Kategorie** | `navigation` |
| **Erbt von** | `base`, `menu` |
| **Varianten** | `ring`, `sektoren`, `facher`, `launcher`, `kontext` |
| **Zustände** | `open`, `expanded`, `dimmed`, `pinned` |
| **Gesten** | `tap`, `long-press`, `drag`, `rotate` |
| **Animationen** | `radial-out`, `radial-in`, `stagger`, `lift`, `morph` |
| **Verwandt** | `menu`, `context-menu`, `floating-action-button`, `toolbar`, `command` |
| **Rolle** | `menu` |
| **Status** | dokumentiert |

!!! info "Standardisierung"
    Der Aktionsfächer des [floating-action-button](../../actions/floating-action-button/)
    (`expanded`) und das kreisförmige Rechtsklick-Menü sind Varianten **einer**
    Komponente: `radial-menu` mit `variant: facher` bzw. `variant: kontext`. Der FAB
    bleibt die *eine* Hauptaktion der Ansicht; er verankert nur das Kreismenü
    (`anchor: "fab"`).

## Beschreibung

Ein Radial Menu (Kreismenü) ordnet Menüpunkte um einen Mittelpunkt herum an. Der Anker
sitzt in der Mitte, die Punkte liegen auf einem Ring. Hat ein Punkt Unterpunkte, erscheinen
diese im **nächsten Ring** um den ersten herum: aus zwei Ebenen werden zwei Ringe, aus drei
Ebenen drei. Der Ankerpunkt selbst ist meist inaktiv und dient nur als Ausgangspunkt.

Ausgewählt wird über die **Richtung** zum Punkt, nicht über die Strecke. Der Zeiger muss
deshalb nur kurz in die richtige Richtung wandern — der Punkt ist auch dann treffbar, wenn
er weiter weg liegt. Wiederholung führt zum Muskelgedächtnis: erfahrene Nutzer wählen den
Punkt, ohne das Menü anzusehen.

Der Anker ist frei wählbar: Ecke, Kantenmitte, Bildschirmmitte, freie Koordinaten, die
Position eines anderen Elements oder der Zeiger selbst. Dasselbe Element steht deshalb oben
rechts genauso gut wie mittig in der Fläche; am Rand wird der Vollkreis automatisch zum
Fächer geklemmt.

!!! note "Herkunft"
    Radiale Menüs sind nicht neu: der erste dokumentierte Fall ist PIXIE (1969), der erste
    Messvergleich mit linearen Menüs (1988) zeigte rund 15 % kürzere Auswahlzeit bei
    weniger Fehlern. Die bekannteste Bauform ist das **Pie Menu** mit Tortensegmenten um
    eine leere Mitte (unaktivierter Kern, Richtungsauswahl); das **Marking Menu** ist die
    verwandte Geste ohne sichtbares Menü. `sektoren` ist die Pie-Bauform, `ring` die heute
    übliche Bauform mit einzelnen Punktflächen.

## Verwendungszweck

- wiederkehrende Aktionen an fester Stelle, bedient aus dem Muskelgedächtnis
- Aktionen am Zeiger (Rechtsklick, Langdruck) als runde Variante des Kontextmenüs
- Schnellzugriff in Flächen-Programmen: [whiteboard](../../special/whiteboard/),
  [map-view](../../special/map-view/), Editoren
- Ecken- und Kantenmenüs, die bei Hover wachsen und ihre Unterpunkte nach außen schieben
- Launcher in der Bildschirmmitte auf Touch-, Kiosk- und Großbild-Oberflächen
- Menüführung auf Controllern und Stylus (Richtung statt Zielgenauigkeit)

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **ring** | Punktflächen auf einem Ring um den Anker — Standard, 3–8 Punkte |
| **sektoren** | Tortensegmente um eine leere Mitte (Pie-Menu): Auswahl nach Winkelbereich, sehr große Trefferflächen |
| **facher** | Ringstück statt Vollkreis (Halb- oder Viertelkreis) aus einer Ecke oder Kante heraus, auch als Speed-Dial |
| **launcher** | frei stehender Kreis, meist in der Bildschirmmitte, mit Unterpunkten in weiteren Ringen |
| **kontext** | erscheint an der Zeigerposition (Rechtsklick, Langdruck) |

## Features

- **Ringe pro Ebene** — Unterpunkte eines Punktes erscheinen im nächsten Ring (`levels`, höchstens drei)
- **Freier Anker** — neun Rand- und Eckenpositionen, Bildschirmmitte, freie Koordinaten, `anchor` auf ein anderes Element, oder Zeigerposition
- **Klemmung am Rand** — `clamp` macht aus dem Vollkreis an Ecke oder Kante einen Viertel- bzw. Halbfächer; der ganze Ring bleibt sichtbar
- **Hover** — Punkt wächst, wandert ein Stück nach außen und wirft Schatten; seine Unterpunkte fächern sich gestaffelt nach außen auf
- **Wegfahr-Toleranz** — `closeDelay` lässt den Zeiger zwischen den Ringen wandern, ohne dass das Menü schließen würde
- **Formen** — Kreis, Vieleck mit 3–12 Ecken, Squircle, Keil, Blüte (siehe [Formen und Ecken](./appearance.md#formen-und-ecken))
- **Richtungsselektion** — in `sektoren` gilt der Punkt als getroffen, sobald der Zeiger in seinem Winkelbereich ist
- **Tastatur** — Pfeiltasten gehen im Ring herum, `Enter` eine Ebene hinein, `Esc` zurück; 4er- und 8er-Ringe liegen auf den Pfeiltasten
- **Anheftbar** — Klick hält das Menü offen (`pinned`), sonst schließt es beim Verlassen des Bereichs
- **Ring-Hervorhebung** — `dimInactive` dämpft alle Ringe außer dem aktiven

## Abgrenzung

- **Nicht verwechseln mit** [menu](../menu/): das lineare Menü folgt der Lese-Reihenfolge und
  eignet sich für lange und dynamische Listen; das Kreismenü folgt **Richtungen** und lebt von
  einer kleinen, immer gleichen Punktezahl.
- **Nicht verwechseln mit** [context-menu](../../overlays/context-menu/): beide erscheinen am
  Zeiger und tragen dieselben Aktionen — das Kontextmenü als Liste, das Kreismenü im Kreis.
  Beide haben die Rolle `menu`.
- **Nicht verwechseln mit** [floating-action-button](../../actions/floating-action-button/):
  der FAB trägt die *eine* Hauptaktion, das Kreismenü mehrere gleichrangige. Der Fächer des
  FABs ist die Variante `facher`.
- **Nicht verwechseln mit** [toolbar](../toolbar/): die Toolbar ist dauerhaft sichtbar,
  das Kreismenü kommt auf Zuruf (Hover, Tipp, Rechtsklick) und verschwindet wieder.
- **Nicht verwechseln mit** [command](../command/): die Befehlspalette sucht aus vielen
  Befehlen; das Kreismenü zeigt eine feste, gelernte Auswahl ohne Suche.

## Best Practices

- 3–12 Punkte pro Ring; über 8 Punkte lieber Sektoren oder einen zweiten Ring.
- Höchstens drei Ringe: jeder Ring vergrößert Fläche und Zeigerweg.
- Richtungen programmweit gleich halten (z. B. oben = Neu, rechts = Teilen) — darauf beruht
  der ganze Vorteil; eine umgestellte Reihenfolge kostet die Nutzer ihre Geschwindigkeit.
- `hoverDelay` 80–150 ms, `closeDelay` 150–250 ms — ohne Toleranz schließt das Menü,
  sobald der Zeiger zum Unterpunkt wandert.
- Auf Touch: **drücken – ziehen – loslassen** statt Hover; Hover-Menüs brauchen dort
  `trigger: tap`.
- Kein Kreismenü für lange, dynamische oder unbekannte Listen — dafür lineare Menüs oder
  [command](../command/).
- Beschriftung erst im aktiven Segment oder als [tooltip](../../overlays/tooltip/);
  ein Vollkreis mit dauerhaften Labels wird unlesbar.
- Bei `prefers-reduced-motion`: `radial-out` → `fade-in`, Wachstum und Mitrotation abschalten.

## Siehe auch

- [navigation – Übersicht](../index.md)
- [Menu](../menu/) — Elternklasse
- [Context Menu](../../overlays/context-menu/) — dieselben Punkte, linear
- [Floating Action Button](../../actions/floating-action-button/) — Anker für `facher`
- [radial-out](../../../animations/entrance/radial-out/) und [radial-in](../../../animations/exit/radial-in/)
- [Basiskomponente](../../basics/base/)
