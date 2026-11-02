# Edge Swipe (Rand-Wisch)

## Beschreibung

Ein Edge Swipe startet **am Bildschirmrand**: Ein oder mehrere Finger setzen
in einer schmalen Zone am Rand an und wischen nach innen. Die Startposition ist
entscheidend – dieselbe Bewegung mitten auf dem Bildschirm ist ein normaler
Swipe.

iOS kennt dafür die `UIScreenEdgePanGestureRecognizer`, Android die
System-Geste „Zurück wischen“; Web-Browser behandeln horizontale Rand-Wische
als Zurück-Geste des Browsers.

## Fingeranzahl

Von 1 bis zur Gerätegrenze (üblich 1 pro Kante, mehrere sind möglich).
Mehrere gleichzeitige Finger werden als eine Geste am Mittelpunkt aller
Zeiger erkannt.

## Verwendung

- Zurück-Navigation (iOS und Android Standard)
- Side-Panel / Seitenleiste einblenden (Desktop-Tablets, Surface)
- Control Center / Benachrichtigungen aus dem Rand ziehen
- Radiale Menüs am Rand öffnen (Kontext)

## Randzonen

| Rand | Typische Funktion |
|------|-------------------|
| Links | Zurück |
| Rechts | Zurück (bei RTL) oder Seitenpanel |
| Oben | Benachrichtigungen / Statusleiste |
| Unten | Home / App-Wechsel (Full-Screen-Navigation) |

## Dauer

- Wischdauer: 100–400ms
- Anlaufzone: 10–24px ab Randmitte

## Erkennung

| Methode | Beschreibung |
|---------|--------------|
| **Edge Zone** | Touch-start innerhalb der Randzone |
| **Einwärts-Vektor** | Bewegung zeigt vom Rand weg in den Inhalt |
| **Prädiktiver Pfad** | Fortsetzung des Wischpfads sagt Ziel voraus (Android) |

## Unterschied zu Swipe

- **Swipe**: startet überall, Aktion gehört zum Inhalt
- **Edge Swipe**: startet am Rand, Aktion gehört zur Navigation/App

## Siehe auch

- [Swipe](../swipe/description.md)
- [Navigation Sidebar](../../../components/navigation/sidebar/description.md)
