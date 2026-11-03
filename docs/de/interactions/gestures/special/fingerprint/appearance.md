# Fingerprint - Aussehen

## Grundlayout

Die Sensorzone ist markiert (Icon, Vertiefung oder leuchtender Ring beim
Display-Sensor). Die Berührung startet die Scan-Animation in der Sensorzone –
außerhalb aller UI-Elemente.

```
┌─────────────────────────────────────────┐
│                                         │
│              ╭─────────╮                │
│             (  Leisten )  Fingerkuppe   │
│              ╰─────────╯                │
│          Scan-Ring in Sensorzone        │
└─────────────────────────────────────────┘
```

## Zustände

| Zustand | Anzeige |
|---------|---------|
| **Bereit** | Sensor-Icon oder Ring statisch |
| **Scannen** | Ring pulsiert oder füllt sich |
| **Erfolg** | Häkchen, kurzes Aufleuchten |
| **Fehler** | Rot markierter Ring (Shake), Hinweis zum erneuten Versuch |

## Feedback-Optionen

| Option | Beschreibung |
|--------|--------------|
| **Haptisch** | Kurze Vibration bei Erfolg, doppelte bei Misserfolg |
| **Ring-Animation** | Pulsieren oder Fortschritts-Füllung |
| **1:1-Bewegung** | Liste bewegt sich im Swipe-Modell 1:1 mit |

## Dauer

- Scan-Animation: 100–500ms bis zum Ergebnis
- Ergebnis-Anzeige: 300–1000ms, danach schließt oder bleibt die UI offen

## Unterschied zu Tap (Aussehen)

Das Feedback erscheint immer in der Sensorzone, nie auf einem berührten
UI-Element; die Press-Animation greift hier nicht.
