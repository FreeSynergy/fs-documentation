# Multi-Finger Swipe (Mehrfinger-Wisch)

## Beschreibung

Ein Multi-Finger Swipe ist ein Wischen mit **zwei oder mehr Fingern**
gleichzeitig (klassisch drei). Er gehört zu den System- und Accessibility-
Gesten: Auf macOS steuert er die Mission-Control-Navigation, in iOS VoiceOver
wechselt er Apps, und Android nutzt Mehrfinger-Wische in der Bedienungshilfe
(Drei-Finger-Wischen für Zurück/Home/Recents bei älteren Navigationssätzen).

Ob mit zwei, drei oder vier Fingern gewischt wird, ist eine Einstellung
(`pointerCount`) – die Geste bleibt dieselbe.

## Fingeranzahl

Genau `pointerCount` (Standard 3) bis zur Gerätegrenze.

## Verwendung

- App-Wechsel / Task-Wechsel (iOS VoiceOver, Android Accessibility)
- Desktop-/Workspace-Wechsel (macOS Mission Control, Linux Workspaces)
- Zurück/Forward in Dokumenten (E-Reader, Reader-Apps)
- Vollbild-Steuerung in Video-Apps (Mehrfinger-Wisch = Mini-Player)

## Richtung

| Richtung | Typische Aktion |
|----------|-----------------|
| Links/Rechts | Workspace/Seite wechseln |
| Auf | Task-Übersicht öffnen |
| Ab | Task-Übersicht schließen / Home |

## Dauer

- Wischdauer: 150–500ms
- Alle Finger müssen innerhalb von ~150ms gemeinsam unten sein

## Erkennung

| Methode | Beschreibung |
|---------|--------------|
| **Pointer Count** | Genau `pointerCount` aktive Pointer (Standard 3) |
| **Sync-Fenster** | Gemeinsamer Down-Zeitpunkt tolerieren |
| **Richtungsvektor** | Horizontaler/vertikaler Hauptvektor wie bei Swipe |

## Unterschied zu Swipe

- **Swipe**: mit einem oder mehreren Fingern, App-interne Navigation
- **Multi-Finger Swipe**: verlangt mindestens zwei Finger (`pointerCount`), meist System-/App-Wechsel-Ebene

## Unterschied zu Pinch

- **Pinch**: Zeiger bewegen sich zueinander, Inhalt transformieren
- **Multi-Finger Swipe**: alle Zeiger in gleiche Richtung, Kontext wechseln
