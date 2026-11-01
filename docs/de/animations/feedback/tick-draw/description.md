# Tick Draw

## Beschreibung

Tick Draw zeichnet ein Erfolgshäkchen als Linie: Der Strich folgt einem vorbereiteten Pfad und wird in kurzer Zeit sichtbar, als hätte ihn jemand gesetzt. Meist erscheint zuerst ein Kreis oder eine Fläche, dann der Haken. Die Animation ersetzt einen Text wie „Gespeichert“ durch ein eindeutiges, sprachunabhängiges Zeichen.

## Verwendung

- Bestätigung nach dem Speichern, Senden oder Synchronisieren
- Abhaken einer Aufgabe in der Liste, siehe [checkbox](../../../components/fields/checkbox/description.md)
- Abschluss eines Schritts in einem Assistenten
- Auswahl bestätigen (Mehrfachauswahl, Filter)
- Häkchen auf einem Bild oder Dateisymbol (erledigt, geprüft)
- Kurzes Erfolgssignal nach einer Gestenbedienung

## Dauer

- Typisch: 300–500 ms für den Strich
- Vorlauf (Kreis/Hintergrund erscheint): 150–250 ms
- Signal darf nicht länger als 600 ms brauchen, sonst wirkt es träge

## Unterschied zu Ripple und Highlight

- Ripple bestätigt die Berührung an sich und startet am Klickpunkt; Tick Draw bestätigt das Ergebnis der Aktion.
- Highlight färbt eine Fläche kurz ein und sagt „hier hat sich etwas geändert“; Tick Draw zeigt einen abgeschlossenen Vorgang und bleibt stehen.
