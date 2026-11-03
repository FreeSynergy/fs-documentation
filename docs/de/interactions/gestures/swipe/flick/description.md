# Flick (Schwung-Wisch)

## Beschreibung

Ein Flick ist ein schnelles Wischen, bei dem ein oder mehrere Finger **mit
Schwung abgehoben** werden. Entscheidend ist nicht die zurückgelegte Strecke, sondern
die Geschwindigkeit beim Loslassen: Der Inhalt bewegt sich nach dem Loslassen
durch die Impulskraft weiter (Momentum).

Android unterscheidet im `GestureDetector` zwischen `onScroll` (Drag,
durchgehend geführt) und `onFling` (abbrupt mit Velocity). Umgangssprachlich
werden Flick und **Fling** als Synonyme verwendet.

## Fingeranzahl

Von 1 bis zur Gerätegrenze (typisch 5–10 Finger). Mehrere gleichzeitige
Finger werden als eine Geste am Mittelpunkt aller Zeiger erkannt.

## Verwendung

- Throw-/Momentum-Scrolling in Listen
- Schnelles Blättern in Galerien und Onboarding-Seiten
- Kachel-/Carousel-Umblätterung (eine Karte weiter „schnipsen“)
- Kartenansichten: Kartenausschnitt schnell weiterschieben

## Dauer und Geschwindigkeit

- Berührungsdauer: meist unter 300ms
- Velocity-Threshold: typisch > 1000 px/s beim Loslassen
- Nachlauf: Inhalt decelariert über 300–1500ms

## Erkennung

| Methode | Beschreibung |
|---------|--------------|
| **Velocity** | Bewegungsgeschwindigkeit der letzten Events beim Up-Event |
| **Decelerate** | Nachlauf mit abnehmender Geschwindigkeit |
| **Abgrenzung Swipe** | Flick wertet Velocity, Swipe wertet Distanz |

## Unterschied zu Swipe

- **Swipe**: Distanz zählt (typisch > 50px), Inhalt folgt den Fingern 1:1
- **Flick**: Velocity zählt, Inhalt rollt nach dem Loslassen aus

## Unterschied zu Drag

- **Drag**: führend, Inhalt hängt an den Fingern, stoppt beim Loslassen
- **Flick**: impulsgebend, Inhalt bewegt sich nach dem Loslassen weiter
