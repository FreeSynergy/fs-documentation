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
    Der Aktionsfächer des [floating-action-button](../../../primitives/actions/floating-action-button/)
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
deshalb nur kurz in die richtige Richtung wandern. Der Punkt bleibt auch dann treffbar, wenn
er weiter entfernt liegt. Wiederholung führt zu Muskelgedächtnis: Erfahrene Nutzer wählen den
Punkt, ohne auf das Menü zu schauen.

Der Anker ist frei wählbar: Ecke, Mitte einer Kante, Bildschirmmitte, freie Koordinaten, die
Position eines anderen Elements oder der Zeiger selbst. Dasselbe Element funktioniert damit
oben rechts genauso gut wie in der Mitte der Fläche. Am Rand wird der volle Kreis automatisch
zu einem Fächer beschnitten.

!!! note "Herkunft"
    Kreismenüs sind nichts Neues: Der erste dokumentierte Fall ist PIXIE (1969). Der erste
    gemessene Vergleich mit linearen Menüs (1988) zeigte rund 15 % kürzere Auswahlzeit bei
    weniger Fehlern. Die bekannteste Form ist das **Pie Menu** mit Tortenstücken um eine leere
    Mitte (inaktiver Kern, Auswahl per Richtung). Das **Marking Menu** ist die verwandte Geste
    ohne sichtbares Menü. `sektoren` ist die Tortenform, `ring` die heute übliche Form mit
    einzelnen Punktflächen.

## Zweck

- wiederkehrende Aktionen an einer festen Stelle, aus dem Muskelgedächtnis heraus bedient
- Aktionen am Zeiger (Rechtsklick, Long-Press) als runde Variante des Kontextmenüs
- schneller Zugriff in flächenbasierten Programmen: [whiteboard](../../../workbenches/special/whiteboard/),
  [map-view](../../special/map-view/), Editoren
- Ecken- und Kantenmenüs, die beim Überfahren wachsen und ihre Unterpunkte nach außen schieben
- Launcher in der Bildschirmmitte auf Touch-, Kiosk- und Großbildflächen
- Menünavigation mit Controller und Stift (Richtung statt Zielgenauigkeit)

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **ring** | Punktflächen auf einem Ring um den Anker — Standard, 3–8 Punkte |
| **sektoren** | Tortenstücke um eine leere Mitte (Pie Menu): Auswahl über den Winkelbereich, sehr große Trefferflächen |
| **facher** | Ringsegment statt Vollkreis (Halb- oder Viertelkreis), das aus einer Ecke oder Kante heraustritt, auch als Speed Dial |
| **launcher** | freistehender Kreis, meist in der Bildschirmmitte, mit Unterpunkten in weiteren Ringen |
| **kontext** | erscheint an der Zeigerposition (Rechtsklick, Long-Press) |

## Funktionen

- **Ein Ring pro Ebene** — die Unterpunkte eines Punktes erscheinen im nächsten Ring (`levels`, höchstens drei)
- **Freier Anker** — neun Positionen an Kanten und Ecken, Bildschirmmitte, freie Koordinaten, `anchor` mit Verweis auf ein anderes Element oder die Zeigerposition
- **Randbeschnitt** — `clamp` macht aus dem Vollkreis an einer Ecke oder Kante einen Viertel- oder Halbfächer; der gesamte Ring bleibt sichtbar
- **Hover** — der Punkt wird größer, rückt etwas nach außen und wirft einen Schatten; seine Unterpunkte fächern gestaffelt nach außen auf
- **Wegtoleranz** — `closeDelay` erlaubt dem Zeiger, zwischen den Ringen zu wechseln, ohne dass sich das Menü schließt
- **Formen** — Kreis, Polygon mit 3–12 Ecken, Squircle, Keil, Blüte (siehe [Formen und Ecken](./appearance.md#formen-und-ecken))
- **Richtungsauswahl** — bei `sektoren` gilt ein Punkt als getroffen, sobald der Zeiger in seinem Winkelbereich liegt
- **Tastatur** — Pfeiltasten bewegen sich im Ring, `Enter` geht eine Ebene tiefer, `Esc` geht zurück; bei 4- und 8-Punkt-Ringen liegen die Punkte auf den Pfeiltasten
- **Fixierbar** — ein Klick hält das Menü offen (`pinned`), sonst schließt es sich, wenn der Bereich verlassen wird
- **Ring-Hervorhebung** — `dimInactive` blendet alle Ringe außer dem aktiven aus

## Abgrenzung

- **Nicht verwechseln mit** [menu](../menu/): Das lineare Menü folgt der Leserichtung und eignet sich für lange und dynamische Listen. Das Kreismenü folgt **Richtungen** und setzt auf eine kleine, immer gleiche Anzahl an Punkten.
- **Nicht verwechseln mit** [context-menu](../../overlays/context-menu/): Beide erscheinen am Zeiger und enthalten dieselben Aktionen — das Kontextmenü als Liste, das Kreismenü im Kreis. Beide haben die Rolle `menu`.
- **Nicht verwechseln mit** [floating-action-button](../../../primitives/actions/floating-action-button/): Der FAB trägt die *eine* Hauptaktion, das Kreismenü mehrere gleichwertige. Der Fächer des FAB ist die Variante `facher`.
- **Nicht verwechseln mit** [toolbar](../toolbar/): Die Toolbar ist dauerhaft sichtbar, das Kreismenü erscheint bei Bedarf (Hover, Tippen, Rechtsklick) und verschwindet wieder.
- **Nicht verwechseln mit** [command](../command/): Die Befehlspalette sucht unter vielen Befehlen; das Kreismenü zeigt eine feste, gelernte Auswahl ohne Suche.

## Best Practices

- 3–12 Punkte pro Ring; über 8 Punkten lieber Sektoren oder einen zweiten Ring nehmen.
- Höchstens drei Ringe: Jeder Ring vergrößert sowohl die Fläche als auch den Weg des Zeigers.
- Richtungen im ganzen Programm gleich halten (z. B. oben = Neu, rechts = Teilen). Der gesamte Vorteil beruht darauf; eine umsortierte Anordnung kostet die Nutzer ihre Geschwindigkeit.
- `hoverDelay` 80–150 ms, `closeDelay` 150–250 ms. Ohne Toleranz schließt sich das Menü, sobald der Zeiger zum Unterpunkt wandert.
- Auf Touch gilt **drücken – ziehen – loslassen** statt Hover; Hover-Menüs brauchen dort `trigger: tap`.
- Kein Kreismenü für lange, dynamische oder unbekannte Listen. Dafür lineare Menüs oder [command](../command/) nehmen.
- Beschriftungen nur im aktiven Segment oder als [tooltip](../../overlays/tooltip/). Ein voller Kreis mit dauerhaften Beschriftungen wird unlesbar.
- Bei `prefers-reduced-motion`: `radial-out` → `fade-in`, Wachstum und Mitdrehen abschalten.

## Siehe auch

- [navigation – Übersicht](../index.md)
- [Menu](../menu/) — übergeordnete Klasse
- [Context Menu](../../overlays/context-menu/) — dieselben Punkte, linear
- [Floating Action Button](../../../primitives/actions/floating-action-button/) — Anker für `facher`
- [radial-out](../../../../interactions/animations/entrance/radial-out/) und [radial-in](../../../../interactions/animations/exit/radial-in/)
- [Base-Komponente](../../../primitives/basics/base.md)
