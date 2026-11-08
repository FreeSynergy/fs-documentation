# 0005 – App und Widget: derselbe Kern, unterschiedliche Ebene

## Kontext
Zwei Kalender-Bausteine werden leicht verwechselt: `date-picker` (Auswahl-Overlay, liefert
ein Datum in ein Feld) und `calendar-view` (Planungsfläche in der Kalender-App). Seit der
Date Picker Einträge liest und schreibt (Punkte, Tagesliste, Schnellaufnahme), steckt
bereits Kalenderfunktionalität darin — er ist ein kleiner Kalender. Offen war, wo ein
Baustein aufhört, Widget zu sein, wo die App anfängt, und was passiert, wenn ein Widget
anwächst.

## Entscheidung
Der **darstellende Kern ist identisch**. Die App bettet das Widget ganzzahlig und baut keine
zweite Kalenderdarstellung. Der Unterschied ist ausschließlich die Hülle.

- **Widget (Ebene 2, `components/`)** — eingebettete Fläche. Bindet ein beim Bauen bekanntes
  Datenmodell, zeigt Einträge, liefert als Ergebnis einen **Wert**: Tag, Zeitraum, Auswahl —
  für ein Eingabefeld, einen Filter, eine Leiste. Kein Menü, keine eigene Fenster- und
  Adressführung, kein Export, kein Druck, keine Einstellungen, keine Benachrichtigungen.
  Ändern von Daten ist erlaubt (`POST`/`PATCH` über die Daten-API), aber immer im Dienst
  des Wertes, nur bei Schreibrecht, und ohne eigene Bearbeitungsfläche.
- **App (Ebene 4, `programs/`)** — dieselbe Fläche im ganzen Bildschirm **plus** Laufebene:
  Menü und Toolbar, eigenes Fenster mit eigener Adresse, Umschalten der Sichten,
  Bearbeiten in eigenen Flächen, **Export und Ausgabeformate** (ICS, CSV, Drucklayout),
  Einstellungen, Weckrufe, Teilen und Freigabe, Führung der Datenführung.

Faustregel: **Alles, was das Widget zeigt, kann die App größer.** Alles, was ein Menü, eine
Adresse, eine Datei oder eine Einstellung braucht, ist App.

## Folgen
- Wächst einem Widget Menü, Export oder eigene Adresse, verlässt es die Bauebene: offen und
  lauffähig → `workbenches/` (Ebene 3); mit Menü, Fenster und Speichern → `programs/apps/`
  (Ebene 4). Der Baustein zieht um, die Darstellung bleibt dieselbe.
- Was in `appearance.md` und `attributes.md` eines Widgets steht, gilt damit auch für die
  App: Marken, Farben, Eintragstypen und Datenfenster werden **nicht** zweimal beschrieben.
  Die App-Doku (`menu.md`, `features.md`, `structure.md`) hält nur die Hülle fest.
- Neue Widgets nehmen keine App-Features in den Steckbrief auf. Umgekehrt gilt: Wo die App
  etwas anzeigt, verweist sie auf das Widget, statt die Ansicht neu zu erklären.
- Betroffene Doku: `components/fields/date-picker/`, `components/data/calendar-view/`,
  `programs/apps/calendar/`. Zuordnung der Bausteine bleibt `conventions/CONVENTIONS.md` §3.
