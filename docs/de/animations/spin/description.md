# Spin

## Beschreibung

Spin dreht ein Element dauerhaft in gleichmäßigem Takt – ohne definierten Endwinkel. Die Animation läuft als Endlosschleife und signalisiert Aktivität, solange eine Aufgabe (Laden, Sync, Verarbeitung) noch nicht abgeschlossen ist.

## Verwendung

- Lade-Spinner beim Abrufen von Daten
- Synchronisierungs- und Aktualisierungsstatus
- Verarbeitung oder Upload mit unbekanntem Fortschritt
- Aufnahme- bzw. Live-Indikator in Werkzeugleisten
- Play-Status: rotierendes Icon während des Abspielens
- Fortschrittsrad neben Texten wie „Wird gespeichert …“

## Dauer

- Pro Umdrehung: 800–1500ms
- `iterationCount: infinite` – die Gesamtdauer endet mit der Aufgabe
- Unter 800ms pro Umdrehung wirkt unruhig, über 1500ms träge

## Unterschied zu Rotate

- Spin: Endlose Drehung ohne Endwinkel; beendet erst, wenn die Arbeit fertig ist
- Rotate: Definierte, einmalige Drehung auf einen festen Winkel mit dauerhaftem Endzustand
