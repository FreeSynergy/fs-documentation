# Hover (Schwebe-Geste)

## Beschreibung

Hover beschreibt das **Positionieren des Zeigers über einem Element ohne
Kontakt**. Klassisch mit Maus, auf Tablets mit Präzisionszeiger (Apple Pencil
Hover über iPad, iPadOS Cursor) und Stiften mit Hover-Erkennung; auf reinen
Touchscreens gibt es Hover nicht – dort ist der erste Touch zugleich die
Aktion.

iOS stellt dafür die `UIHoverGestureRecognizer` bereit, Web:
`pointerover`/`pointerenter` mit `pointerType`.

## Verwendung

- Tooltip / Hilfetext anzeigen
- Vorschau-Menu unter Menüpunkten öffnen
- Hover-Lift: Element anheben, Fokus sichtbar machen
- Präzise Auswahl in dichten Oberflächen (Tabellen, CAD, Karten)
- Stift-Vorschau: Werkzeug-Größe zeigen, bevor gezeichnet wird

## Dauer

- Ein-/Ausblenden: 100–300ms mit Delay (meist 300–700ms gegen versehentliches Triggern)
- Solange Zeiger über Element: unbegrenzt aktiv

## Erkennung

| Methode | Beschreibung |
|---------|--------------|
| **Mouse** | `pointermove` ohne gedrückte Taste |
| **Stift-Hover** | Sensor erkennt Stift vor Aufsetzen |
| **Touch-Pointer** | verbundener Bluetooth-/Trackpad-Zeiger |

## Unterschied zu Tap

- **Tap**: Kontakt + Auslösung
- **Hover**: kein Kontakt, nur Vorbereitung der Aktion

## Unterschied zu Force Press (Stift)

- **Hover**: Abstand > 0, keine Kraft
- **Force Press**: Kontakt mit Kraft

## Barrierefreiheit

Hover-Inhalte müssen auch per Tastatur-Fokus erreichbar und per Tap/Escape
schließbar sein (WCAG 1.4.13 Content on Hover or Focus). Auf Touch ist ein
erstes Tippen zum Aufklappen, ein zweites zum Ausführen erlaubt.
