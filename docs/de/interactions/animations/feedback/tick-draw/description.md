# Tick Draw

## Beschreibung

Tick Draw zeichnet ein Erfolgshäkchen als Linie: Der Strich folgt einem vorbereiteten Pfad und wird
in kurzer Zeit sichtbar, als hätte jemand es gerade gesetzt. Meist erscheint zuerst ein Kreis oder
eine Fläche, dann das Häkchen. Die Animation ersetzt einen Text wie „Gespeichert“ durch ein
eindeutiges, sprachunabhängiges Zeichen.

## Verwendung

- Bestätigung nach dem Speichern, Senden oder Synchronisieren
- eine Aufgabe in der Liste abhaken, siehe [checkbox](../../../../components/primitives/fields/checkbox/description.md)
- einen Schritt in einem Assistenten abschließen
- eine Auswahl bestätigen (Mehrfachauswahl, Filter)
- ein Häkchen auf einem Bild- oder Datei-Icon (erledigt, geprüft)
- ein kurzes Erfolgssignal nach einer gestenbasierten Bedienung

## Dauer

- Typisch: 300–500 ms für den Strich
- Anlauf (Kreis/Hintergrund erscheint): 150–250 ms
- Das Signal darf nicht länger als 600 ms dauern, sonst wirkt es träge

## Unterschied zu Ripple und Highlight

- Ripple bestätigt den Kontakt selbst und beginnt am Klickpunkt; Tick Draw bestätigt das
  Ergebnis der Aktion.
- Highlight färbt eine Fläche kurz ein und sagt „hier hat sich etwas geändert“; Tick Draw zeigt
  einen abgeschlossenen Vorgang und bleibt stehen.
