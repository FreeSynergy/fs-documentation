# Wisch-Gesten (swipe)

Wisch-Gesten führen eine **zusammenhängende Bewegung** in eine Richtung aus –
führend, mit Impuls oder als gezeichneter Pfad. Startposition und Tempo
unterscheiden die einzelnen Gesten.

Alle Wisch-Gesten sind multipointfähig: beliebig viele Finger bis zur
Gerätegrenze werden als eine Geste am Mittelpunkt aller Zeiger erkannt. Der
Multi-Finger Swipe verlangt per Definition zwei oder mehr Finger
(`pointerCount` als Einstellung). Eine Ausnahme: draw-gesture zeichnet einen
einzelnen zusammenhängenden Strich – weitere Finger erzeugen eigene Pfade.

## Elemente

- **swipe** - Wischen in eine Richtung (Navigation, Switchen)
- **flick** - Wischen mit Schwung und Abheben (Throw-Scrolling)
- **drag** - gedrücktes Ziehen (Reorder, Scroll)
- **edge-swipe** - Wischen vom Bildschirmrand (Zurück, Systemleisten)
- **multi-finger-swipe** - Wischen mit zwei oder mehr Fingern (App-/Workspace-Wechsel)
- **draw-gesture** - gezeichnete Form/Buchstabe (Verknüpfungen, Befehle)

## Zuordnung

| Situation | Geste |
|-----------|-------|
| Richtung wechseln, Seite umblättern | swipe |
| Liste weit schleudern | flick |
| Element führen (sortieren, scrollen) | drag |
| Zurück / Systemleisten aus dem Rand | edge-swipe |
| App- oder Workspace-Wechsel | multi-finger-swipe |
| Verknüpfung durch Form/Formbuchstabe | draw-gesture |

## Barrierefreiheit

Nach WCAG 2.5.1 und 2.5.7 brauchen Wisch-Gesten Einzeiger-Alternativen
(Buttons, Schalter); der Multi-Finger Swipe zusätzlich eine Variante mit
weniger Fingern. Rand-Gesten (edge-swipe) dürfen nie die einzige Möglichkeit
sein.

## Siehe auch

- [Gesten Übersicht](../index.md)
- [Swipe](../swipe/swipe/description.md) - Basisgeste der Familie
- [Slide-Animation](../../animations/entrance/slide-in/description.md) - Antwort auf Wisch-Gesten
