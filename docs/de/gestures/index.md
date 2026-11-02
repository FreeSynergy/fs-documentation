# Touch-Gesten

Touch-Gesten sind Interaktionsmethoden für Touchscreen-Geräte (und verwandte
Zeiger: Maus, Stift, Sensoren). Gesten sind **Eingaben** – die visuelle
Antwort darauf ist eine [Animation](../animations/).

Die Gesten sind in sechs Familien gruppiert (wie die Animationen nach
Kategorien):

## Familien

| Familie | Prinzip | Gesten |
|---------|---------|--------|
| [Tippen (tap)](tap/) | Kurze Berührung ohne Weg, meist Ersatz für Klicks – ab einem Finger, multipointfähig | 6 |
| [Wischen (swipe)](swipe/) | Geführte Bewegung in eine Richtung – ab einem Finger, multipointfähig | 6 |
| [Transformation (transform)](transform/) | Zwei+ Zeiger relativ zueinander (nie einer), Anzahl ist Einstellung, transformieren Inhalt | 3 |
| [Spezielle (special)](special/) | Ohne klassisches Berührungselement: Schwebe-Geste, Biometrie-Sensor | 2 |
| [Gerät (device)](device/) | Bewegung des Geräts selbst (Sensoren, keine Zeiger) | 4 |
| [Kombinationen (combined)](combined/) | Zusammengesetzte Gesten mit Eigenlogik | 2 |

## Zeigeranzahl: Single-Point und Multipoint

Ein Touchsensor meldet jeden gleichzeitigen Kontakt; je nach Gerät werden
fünf bis zehn Finger gleichzeitig erkannt. Daraus gilt für alle Gesten:

- **Die Basisgesten sind multipointfähig.** Tap, Double Tap, Long Press,
  Force Press, Swipe, Flick, Drag, Edge Swipe und die Kombinations-Gesten
  funktionieren mit beliebig vielen Fingern bis zur Gerätegrenze – erkannt
  am Primärzeiger bzw. am Mittelpunkt aller Zeiger. „Ein Finger“ meint die
  Mindestzahl, nicht die Höchstzahl.
- **Multipoint gilt immer für alle Fingerzahlen.** Eine Geste hat kein eigenes
  Fingerlimit; oberste Grenze ist stets die Gerätegrenze.
- **Transformations- und Mehrfinger-Gesten sind im Single-Point nicht
  ausführbar.** Pinch, Spread und Rotate brauchen zwingend zwei Zeiger
  (Abstand und Winkel existieren erst ab zwei), die Multi-Finger-Varianten
  von Tap, Long Press und Swipe per Definition ebenfalls.
- **Drei Ausnahmen ohne Multipoint:** `draw-gesture` (ein Pfad ist ein
  zusammenhängender Strich – weitere Finger erzeugen eigene, getrennte Pfade),
  `hover` (ohne Kontakt; ein schwebender Mehrfinger-Zeiger existiert nicht)
  und `fingerprint` (der Sensor liest genau eine Fingerkuppe).
- **Geräte-Gesten kennen keine Zeigerzahl:** shake, tilt, flip und wave laufen
  über Sensoren, Berührungen spielen keine Rolle.

| Familie / Geste | Single-Point | Multipoint | Grundlage |
|-----------------|--------------|------------|-----------|
| tap: tap, double-tap, long-press, force-press | ✓ | ✓ bis Gerätegrenze | Primärzeiger / Zeiger-Mittelpunkt |
| tap: Multi-Finger-Varianten | ✗ | ✓ ab zwei | mindestens zwei Finger nötig |
| swipe: swipe, flick, drag, edge-swipe | ✓ | ✓ bis Gerätegrenze | Primärzeiger / Zeiger-Mittelpunkt |
| swipe: draw-gesture | ✓ | ✗ | ein Pfad = ein Strich |
| swipe: multi-finger-swipe | ✗ | ✓ ab zwei | mindestens zwei Finger nötig |
| transform (alle) | ✗ | ✓ bis Gerätegrenze | mindestens zwei Zeiger nötig |
| special: hover | ✓ | ✗ | nur ein schwebender Zeiger |
| special: fingerprint | ✓ (genau einer) | ✗ | Sensor liest eine Fingerkuppe |
| device (alle) | entfällt | entfällt | Sensorik statt Zeiger |
| combined | ✓ | ✓ | folgt den Basisgesten (Drag) |

## Alle Gesten

| Geste | Familie | Beschreibung | Verwendung |
|-------|---------|-------------|------------|
| **Tap** | tap | Kurze Berührung | Button-Klick, Item-Auswahl |
| **Double Tap** | tap | Zwei schnelle Berührungen | Zoom, Öffnen |
| **Long Press** | tap | Lange Berührung | Kontextmenü, Markierung |
| **Force Press** | tap | Druck mit Drucksensor | Peek & Pop, Kontext |
| **Multi-Finger Tap** | tap | Tippen mit mehreren Fingern | Sekundäraktion (Rechtsklick) |
| **Multi-Finger Long Press** | tap | Langdruck mit mehreren Fingern | Sekundär-Menü, Multiselect |
| **Swipe** | swipe | Wischen in eine Richtung | Navigation, Switchen |
| **Flick** | swipe | Wischen mit Schwung und Abheben | Throw-Scrolling, Momentum |
| **Drag** | swipe | Gedrücktes Ziehen | Reorder, Scroll |
| **Edge Swipe** | swipe | Wischen vom Bildschirmrand | Zurück, Systemleisten |
| **Multi-Finger Swipe** | swipe | Wischen mit mehreren Fingern | App-/Workspace-Wechsel |
| **Draw Gesture** | swipe | Zeichne Form/Buchstabe | Verknüpfungen, Befehle |
| **Pinch** | transform | Zeiger zusammenziehen (ab zwei) | Zoom out |
| **Spread** | transform | Zeiger auseinanderziehen (ab zwei) | Zoom in |
| **Rotate** | transform | Zeiger drehen (ab zwei) | Rotieren |
| **Hover** | special | Zeiger über Element ohne Kontakt | Tooltip, Vorschau |
| **Fingerprint** | special | Biometrie-Sensor berühren | Entsperren, Autorisieren |
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
| `onFingerprint` | function | Wird nach erfolgreichem Fingerprint-Scan ausgeführt |
| `onFingerprintFail` | function | Wird beim ausbleibenden Match ausgeführt |
| `onDrawGesture` | function | Wird nach erkannter Form ausgeführt |
| `onPinch` | function | Wird beim Pinch ausgeführt |
| `onSpread` | function | Wird beim Spread ausgeführt |
| `onRotate` | function | Wird beim Rotate ausgeführt |
| `onMultiFingerTap` | function | Wird beim Multi-Finger-Tap ausgeführt |
| `onMultiFingerLongPress` | function | Wird beim Multi-Finger-Langdruck ausgeführt |
| `onMultiFingerSwipe` | function | Wird beim Multi-Finger-Swipe ausgeführt |
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
| `pointerCount` | number | Mindestanzahl Zeiger der Geste (Basisgesten: 1, Transform- und Multi-Finger-Gesten: 2 oder 3 …) – nach oben durch das Gerät begrenzt |
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

- Familien: [tap](tap/) · [swipe](swipe/) · [transform](transform/) · [special](special/) · [device](device/) · [combined](combined/)
- [Animationen](../animations/) - visuelle Antwort auf Gesten
- [Konventionen](../data/konventionen.md) - Datei- und Benennungsregeln
