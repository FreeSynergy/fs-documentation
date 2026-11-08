# Heartbeat

## Beschreibung

Heartbeat ahmt einen Herzschlag nach: Zwei schnelle Spitzen ("lub-dub") folgen direkt aufeinander, danach kommt eine deutliche Ruhephase. Der Rhythmus entspricht typischen Herzfrequenzen von etwa 60 bis 100 Schlägen pro Minute.

## Verwendung

- Gesundheits-, Fitness- und Vitalwert-Ansichten
- Live-Status mit einem "lebendigen" Eindruck
- emotionale Aktionen wie Favorit oder Empfehlung
- ein kritischer Countdown (Abo läuft ab, Verbindung instabil)
- Visualisierung auf Wearables und Monitoren
- Vitalparameter mit einem erkennbaren Rhythmus

## Dauer

- Typisch: 700–1200 ms pro Zyklus, meist endlos (`iterationCount: infinite`)
- Standardwert: 1000 ms pro Zyklus

## Unterschied zu Pulse

- Pulse: eine gleichmäßige Spitze pro Zyklus, ohne Ruhephase
- Heartbeat: zwei unterschiedlich starke Spitzen pro Zyklus plus eine Pause, dadurch klar rhythmisch
- Ripple: eine Welle breitet sich räumlich vom Klickpunkt aus. Heartbeat skaliert das Element selbst.
