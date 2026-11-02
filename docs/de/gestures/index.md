# Touch-Gesten

Touch-Gesten sind Interaktionsmethoden für Touchscreen-Geräte (und verwandte
Zeiger: Maus, Stift, Sensoren). Gesten sind **Eingaben** – die visuelle
Antwort darauf ist eine [Animation](../animations/).

Die Gesten sind in vier Familien gruppiert (wie die Animationen nach
Kategorien):

## Familien

| Familie | Prinzip | Gesten |
|---------|---------|--------|
| [Ein-Finger (single)](single/) | Ein Finger/Zeiger, meist Ersatz für Klicks | 10 |
| [Mehrfinger (multi)](multi/) | Zwei+ Finger, transformieren Inhalt | 6 |
| [Gerät (device)](device/) | Bewegung des Geräts selbst (Sensoren) | 4 |
| [Kombinationen (combined)](combined/) | Zusammengesetzte Gesten mit Eigenlogik | 2 |

## Alle Gesten

| Geste | Familie | Beschreibung | Verwendung |
|-------|---------|-------------|------------|
| **Tap** | single | Kurze Berührung | Button-Klick, Item-Auswahl |
| **Double Tap** | single | Zwei schnelle Berührungen | Zoom, Öffnen |
| **Long Press** | single | Lange Berührung | Kontextmenü, Markierung |
| **Swipe** | single | Wischen in eine Richtung | Navigation, Switchen |
| **Flick** | single | Wischen mit Schwung und Abheben | Throw-Scrolling, Momentum |
| **Drag** | single | Gedrücktes Ziehen | Reorder, Scroll |
| **Edge Swipe** | single | Wischen vom Bildschirmrand | Zurück, Systemleisten |
| **Force Press** | single | Druck mit Drucksensor | Peek & Pop, Kontext |
| **Hover** | single | Zeiger über Element ohne Kontakt | Tooltip, Vorschau |
| **Draw Gesture** | single | Zeichne Form/Buchstabe | Verknüpfungen, Befehle |
| **Pinch** | multi | Zwei Finger zusammenziehen | Zoom out |
| **Spread** | multi | Zwei Finger auseinanderziehen | Zoom in |
| **Rotate** | multi | Zwei Finger drehen | Rotieren |
| **Two-Finger Tap** | multi | Tippen mit zwei Fingern | Sekundäraktion (Rechtsklick) |
| **Two-Finger Long Press** | multi | Langdruck mit zwei Fingern | Sekundär-Menü, Multiselect |
| **Three-Finger Swipe** | multi | Wischen mit drei Fingern | App-/Workspace-Wechsel |
| **Shake** | device | Schnelles Hin- und Herbewegen | Undo, Fehler-Feedback |
| **Tilt** | device | Kippen des Geräts | Steuerung, Parallax |
| **Flip** | device | Gerät umdrehen | Stummschalten, Nicht stören |
| **Wave** | device | Hand vor Sensor bewegen | Anruf annehmen, Air Gestures |
| **Pull to Refresh** | combined | Ziehen an der Listen-Obergrenze | Aktualisieren |
| **Drag and Drop** | combined | Greifen, Ziehen, Ablegen | Verschieben, Kombinieren |

## Gesten-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onTap` | function | Wird beim Tap ausgeführt |
| `onDoubleTap` | function | Wird beim Double Tap ausgeführt |
| `onLongPress` | function | Wird beim Long Press ausgeführt |
| `onSwipe` | function | Wird beim Swipe ausgeführt |
| `onFlick` | function | Wird beim Flick ausgeführt |
| `onDragStart` | function | Wird beim Drag-Start ausgeführt |
| `onDragEnd` | function | Wird beim Drag-Ende ausgeführt |
| `onEdgeSwipe` | function | Wird beim Edge Swipe ausgeführt |
| `onForcePress` | function | Wird beim Force Press ausgeführt |
| `onHoverStart` / `onHoverEnd` | function | Hover beginnt/endet |
| `onDrawGesture` | function | Wird nach erkannter Form ausgeführt |
| `onPinch` | function | Wird beim Pinch ausgeführt |
| `onSpread` | function | Wird beim Spread ausgeführt |
| `onRotate` | function | Wird beim Rotate ausgeführt |
| `onTwoFingerTap` | function | Wird beim Zwei-Finger-Tap ausgeführt |
| `onTwoFingerLongPress` | function | Wird beim Zwei-Finger-Langdruck ausgeführt |
| `onThreeFingerSwipe` | function | Wird beim Drei-Finger-Wisch ausgeführt |
| `onShake` | function | Wird beim Shake ausgeführt |
| `onTilt` | function | Wird bei Neigung ausgeführt |
| `onFlip` | function | Wird beim Umdrehen ausgeführt |
| `onWave` | function | Wird beim Winken ausgeführt |
| `onRefresh` | function | Wird bei Pull to Refresh ausgeführt |
| `onDrop` | function | Wird beim Ablegen (Drag and Drop) ausgeführt |

## Konfiguration

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `tapThreshold` | number | Zeitlimit für Tap in ms |
| `longPressThreshold` | number | Zeitlimit für Long Press in ms |
| `swipeThreshold` | number | Minimaler Abstand für Swipe |
| `velocityThreshold` | number | Mindestgeschwindigkeit für Flick in px/s |
| `edgeSize` | number | Breite der Randzone für Edge Swipe in px |
| `pointerCount` | number | Fingeranzahl für Multi-Finger-Gesten |
| `shakeThreshold` | number | Minimale Beschleunigung/Bewegung für Shake |
| `minShakes` | number | Minimale Anzahl Richtungswechsel für Shake |
| `deadZone` | number | Grad-Toleranz für Tilt |
| `matchThreshold` | number | Formähnlichkeit für Draw Gesture (0–1) |
| `enabled` | boolean | Gesten aktivieren? |

## Normen und Barrierefreiheit

| Regel | Bedeutung |
|-------|-----------|
| WCAG 2.5.1 Pointer Gestures | Mehrpunkt- und Pfadgesten brauchen Ein-Finger-Alternative |
| WCAG 2.5.2 Pointer Cancellation | Aktion erst beim Loslassen ausführen |
| WCAG 2.5.4 Motion Actuation | Sensor-Gesten (shake, tilt, flip, wave) brauchen UI-Alternative |
| WCAG 2.5.7 Dragging Movements | Drag braucht Einzelzeiger-Alternative |
| `touch-action` (CSS) | browser-eigene Gesten (pan, pinch-zoom) steuern |

Weil Gesten nie selbsterklärend sind, gilt überall: gleiche Aktion auch
über Button, Menü oder Tastatur erreichbar machen.

## Siehe auch

- Familien: [single](single/) · [multi](multi/) · [device](device/) · [combined](combined/)
- [Animationen](../animations/) - visuelle Antwort auf Gesten
- [Konventionen](../data/konventionen.md) - Datei- und Benennungsregeln
