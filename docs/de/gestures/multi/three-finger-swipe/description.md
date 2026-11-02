# Three-Finger Swipe (Drei-Finger-Wisch)

## Beschreibung

Ein Three-Finger Swipe ist ein Wischen mit **drei Fingern** gleichzeitig. Er
gehört zu den System- und Accessibility-Gesten: Auf macOS steuert er die
Mission-Control-Navigation, in iOS VoiceOver wechselt er Apps, und Android
nutzt Drei-Finger-Gesten in der Bedienungshilfe (Drei-Finger-Wischen für
Zurück/Home/Recents bei älteren Navigationssätzen).

## Verwendung

- App-Wechsel / Task-Wechsel (iOS VoiceOver, Android Accessibility)
- Desktop-/Workspace-Wechsel (macOS Mission Control, Linux Workspaces)
- Zurück/Forward in Dokumenten (E-Reader, Reader-Apps)
- Vollbild-Steuerung in Video-Apps (Drei-Finger-Wisch = Mini-Player)

## Richtung

| Richtung | Typische Aktion |
|----------|-----------------|
| Links/Rechts | Workspace/Seite wechseln |
| Auf | Task-Übersicht öffnen |
| Ab | Task-Übersicht schließen / Home |

## Dauer

- Wischdauer: 150–500ms
- Drei Finger müssen innerhalb von ~150ms gemeinsam unten sein

## Erkennung

| Methode | Beschreibung |
|---------|--------------|
| **Pointer Count** | Genau 3 aktive Pointer |
| **Sync-Fenster** | Gemeinsamer Down-Zeitpunkt tolerieren |
| **Richtungsvektor** | Horizontaler/vertikaler Hauptvektor wie bei Swipe |

## Unterschied zu Swipe

- **Swipe**: ein Finger, App-interne Navigation
- **Three-Finger Swipe**: drei Finger, meist System-/App-Wechsel-Ebene

## Unterschied zu Pinch

- **Pinch**: zwei Finger, zueinander bewegt, Inhalt transformieren
- **Three-Finger Swipe**: drei Finger, gleiche Richtung, Kontext wechseln
