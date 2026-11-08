# Spin

## Beschreibung

Spin dreht ein Element dauerhaft in gleichmäßigem Takt – ohne festgelegten Endwinkel. Die Animation läuft als endlose Schleife und zeigt Aktivität, solange eine Aufgabe (Laden, Synchronisieren, Verarbeiten) noch nicht fertig ist.

## Verwendung

- Ladespinner, während Daten abgerufen werden
- Synchronisations- und Aktualisierungsstatus
- Verarbeitung oder Upload mit unbekanntem Fortschritt
- Aufnahme- oder Live-Indikator in Werkzeugleisten
- Abspielstatus: ein drehendes Icon während der Wiedergabe
- ein Fortschrittsrad neben Texten wie "Speichern …"

## Dauer

- Pro Umdrehung: 800–1500 ms
- `iterationCount: infinite` – die Gesamtdauer endet mit der Aufgabe
- Unter 800 ms pro Umdrehung wirkt unruhig, über 1500 ms träge

## Unterschied zu Rotate

- Spin: eine endlose Drehung ohne Endwinkel; sie stoppt erst, wenn die Arbeit erledigt ist
- Rotate: eine festgelegte, einmalige Drehung auf einen festen Winkel mit einem bleibenden Endzustand
