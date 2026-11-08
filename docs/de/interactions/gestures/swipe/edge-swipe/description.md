# Edge Swipe (Edge Pan)

## Beschreibung

Ein Edge Swipe beginnt **am Bildschirmrand**: Ein oder mehrere Finger setzen in einer
schmalen Zone am Rand auf und wischen nach innen. Die Startposition ist entscheidend. Dieselbe
Bewegung in der Mitte des Bildschirms ist ein normaler Swipe.

iOS kennt dafür `UIScreenEdgePanGestureRecognizer`, Android hat die Systemgeste „Zurück wischen“.
Webbrowser behandeln horizontale Edge Swipes als Zurück-Geste des Browsers.

## Fingeranzahl

1 bis zur Grenze des Geräts (meist 1 pro Rand, mehrere sind möglich).
Mehrere gleichzeitige Finger werden als eine Geste erkannt, am Mittelpunkt aller Zeiger.

## Verwendung

- Zurück-Navigation (Standard unter iOS und Android)
- Ein seitliches Panel oder eine Sidebar einblenden (Desktop-Tablets, Surface)
- Kontrollzentrum oder Benachrichtigungen vom Rand heranziehen
- Radiale Menüs am Rand öffnen (Kontext)

## Randzonen

| Rand | Typische Funktion |
|------|------------------|
| Links | Zurück |
| Rechts | Zurück (bei RTL) oder seitliches Panel |
| Oben | Benachrichtigungen / Statusleiste |
| Unten | Home / App-Wechsel (Vollbild-Navigation) |

## Dauer

- Dauer des Swipes: 100–400 ms
- Startzone: 10–24 px von der Randmitte entfernt

## Erkennung

| Methode | Beschreibung |
|--------|--------|
| **Randzone** | Berührungsbeginn innerhalb der Randzone |
| **Einwärtsvektor** | Die Bewegung zeigt vom Rand weg in den Inhalt |
| **Vorhergesagter Pfad** | Die Fortsetzung des Wischpfads sagt das Ziel voraus (Android) |

## Unterschied zum Swipe

- **Swipe**: beginnt irgendwo, die Aktion gehört zum Inhalt
- **Edge Swipe**: beginnt am Rand, die Aktion gehört zur Navigation/zur App

## Siehe auch

- [Swipe](../swipe/description.md)
- [Navigation-Sidebar](../../../../components/widgets/navigation/sidebar/description.md)
