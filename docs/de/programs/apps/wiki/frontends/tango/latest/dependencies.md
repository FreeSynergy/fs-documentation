# Tango: Abhängigkeiten für ein Frontend in diesem Stil

Ziel: ein Frontend im Stil von Tango (Dokumentation von der Aufnahme bis zur Anleitung mit Schrittlisten, geteilten Ansichten und einer Team-Bibliothek) auf Basis der FreeSynergy-Wiki-Engine. Vertrag: `fs-interfaces/schema/texts.capnp` (ENTWURF 0.1, 2026-11-06, bisher 0 Verbraucher).

## Benötigte UI-Komponenten

1. Schritt-Listen-Editor: geordnete Liste von Schritten, Neuanordnung per Ziehen, Schritt an einer Position hinzufügen, Titel, Beschreibung und Bild je Schritt.
2. Bildannotation: Pfeile, Rahmen, Text, Zoom, Weichzeichner-Bereich (Weichzeichnen optional, in Tango eine Pro-Funktion).
3. Anleitungsansicht: Scroll-Ansicht, Diashow-Ansicht, Einbettungs-Ansicht.
4. Geführter Durchlauf (optional): schrittweises Overlay über der Zielanwendung. Benötigt eine externe Laufzeitumgebung (Browser-Erweiterung); kein Thema für texts.capnp.
5. Freigabe- und Export-Panel: Link, HTML kopieren, Markdown/HTML/PDF exportieren.
6. Team-Bibliothek: Liste mit Mehrfachauswahl und Sammelaktionen (verschieben, duplizieren, freigeben, löschen).
7. Branding-Panel: Logo, Akzentfarbe, Badge-Umschalter.
8. Rückgängig und Wiederholen.

## texts.capnp-Operationen, die dazu passen

| Bedarf | Operation | Hinweis |
|---|---|---|
| Anleitung laden | `get`, `getByPath` | `document` ist JSON, der Inhalt ist für den Vertrag undurchsichtig |
| Listen, Ordneransicht | `list(prefix, cursor)` | pfadbasierte Ordner |
| Suche | `find(term, cursor)` | |
| Anleitung anlegen | `create(path, markdown)` | nimmt Markdown, kein Schritt-Dokument |
| Änderungen speichern | `edit(id, document)`, `editIf(id, revision, document)` | `editIf` für gleichzeitige Bearbeiter nötig (nur ein Provider-Prozess) |
| Verschieben, umbenennen | `move`, `moveFolder` | Links folgen |
| Löschen | `delete` | |
| Export | `exportText(id, mediaType)` | liefert nur Text; PDF ist binär und nicht abgedeckt |
| Import | `importText(path, mediaType, text)` | Markdown hinein |
| Links | `links`, `backlinks` | |
| Live-Aktualisierungen | `subscribe(listener)` | |

## Was texts.capnp fehlt (Lücken)

1. **Binäre Assets.** Kein Hochladen, Abrufen oder Löschen von Bildern oder Dateien. Schritte mit Screenshots brauchen einen Asset-Speicher und einen Verweis von `document` auf das Asset. Nicht im Vertrag.
2. **Schrittmodell.** Keine Definition von Schritten, Screenshots, Hervorhebungen oder Positionen. Nur „das Dokument als JSON“. Ein gemeinsames Schrittschema fehlt, wenn Anleitungen portabel sein sollen.
3. **Aufnahmesitzung.** Keine Operation zum Starten, Pausieren, Abschließen oder Verwerfen einer Aufnahme. (Die Aufnahme liegt wahrscheinlich im Client; der Vertrag müsste das Ergebnis trotzdem annehmen.)
4. **Versionsverlauf.** `revision` ist nur ein Zähler. Keine Liste früherer Revisionen, kein Lesen von Revision N, keine Wiederherstellung.
5. **Freigabe und Sichtbarkeit.** Keine Freigabe-Links, Einbettungs-Token, öffentlich/privat-Flags, Ablauf.
6. **Berechtigungen.** Keine Rollen oder Rechte je Text. Admin-Einstellungen (Branding) fehlen.
7. **Branding- und Theme-Einstellungen.** Keine Operation, um Logo oder Farben je Arbeitsbereich zu speichern.
8. **Exportformate.** `exportText` ist nur Text; kein PDF- oder HTML-Paket mit Assets.
9. **Geführter Durchlauf und Zustand.** Kein „Fortschritt des Betrachters“ und keine Ereignisse für geführte Ansichten. `events.md` ist laut ADR 0012 „bei Bedarf“.
10. **Analytik.** Keine Aufrufzahlen oder Auswertungen.
11. **Übersetzungen und Mehrpfad-Struktur (Verzweigungen).** Nicht modelliert.
12. **Vorlagen.** Keine Vorlagen-Operation.

## Tarifabhängige Funktionen

Kein Vertragsthema. Gehört in unsere Produktregeln, nicht in texts.capnp.
