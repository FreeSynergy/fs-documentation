# Heartbeat

## Beschreibung

Heartbeat imitiert einen Herzschlag: Zwei schnelle Peaks („lub-dub“) folgen direkt aufeinander, danach liegt eine deutliche Ruhephase. Der Rhythmus entspricht typischen Herzfrequenzen von etwa 60 bis 100 Schlägen pro Minute.

## Verwendung

- Gesundheits-, Fitness- und Vitalzeichen-Ansichten
- Live-Status mit „lebendiger“ Anmutung
- Emotionale Aktionen wie Favorit oder Empfehlung
- Kritischer Countdown (Abo läuft ab, Verbindung instabil)
- Visualisierung auf Wearables und Monitoren
- Vitalparameter mit erkennbarem Rhythmus

## Dauer

- Typisch: 700–1200 ms pro Zyklus, meist endlos (`iterationCount: infinite`)
- Standardwert: 1000 ms pro Zyklus

## Unterschied zu Pulse

- Pulse: Ein gleichmäßiger Peak pro Zyklus, ohne Ruhephase
- Heartbeat: Zwei Peaks unterschiedlicher Stärke pro Zyklus plus Pause - dadurch erkennbar rhythmisch
- Ripple: Welle breitet sich räumlich vom Klickpunkt aus; Heartbeat skaliert das Element selbst
