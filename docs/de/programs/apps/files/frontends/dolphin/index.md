# Dolphin

> Kategorie: [Dateien](../../index.md) · [Frontends](../index.md)

## Was es ist

Der Dateimanager von KDE Plasma. Lokale Dateien und, über die I/O-Schicht von KDE, andere Orte. Freie Software. ⚠️ (Lizenz und I/O-Schicht wurden auf den unten genannten Seiten nicht gelesen.)

## Bemerkenswerte Ideen

- **Panels, die du ein- und verschieben kannst:** Orte, Information, Ordner, Terminal. Das Terminal folgt dem angezeigten Ordner und funktioniert nur auf lokalen Medien ✅.
- **Geteilte Ansicht:** zwei Ordner nebeneinander, um zwischen ihnen zu verschieben oder zu kopieren ✅.
- **Informations-Panel mit Bearbeitung:** Vorschau plus Bewertung, Tags und Kommentare für das ausgewählte Element ✅.
- **Gespeicherte Suchen unter Orte** ✅. Eine Suche findet Namen und Inhalte, mit Platzhaltern, und lässt sich nach Typ, Datum, Bewertung und Tag eingrenzen ✅.
- **Stapelweises Umbenennen mit `#`** als Zähler ✅.

## Gesehene Fähigkeiten

| Fähigkeit | Gesehen | Hinweis |
|-----------|---------|---------|
| Liste mit Symbolen, kompakt, Details (Baum in Details), Vorschaubilder | ✅ | Gruppierung nach Sortierart in allen Modi |
| Auswahl per Rechteck, Strg, Umschalt, Tippen zum Suchen, Strg+A | ✅ | |
| Rückgängig für Umbenennen und Verschieben in den Papierkorb (Strg+Z) | ✅ | Das Menü nennt die Aktion |
| Filterleiste nach Namensteil (Strg+I) | ✅ | |
| Suche in Namen und Inhalten (Strg+F), Suche speichern | ✅ | |
| Viele Dateien umbenennen (F2, `#`) | ✅ | |
| Lesezeichen (Orte), Geräte einbinden | ✅ | |
| Bewertung, Tags, Kommentare | ✅ | Im Informations-Panel und in den Detailspalten gezeigt |
| Zwei Dateien oder Ordner vergleichen (externes Werkzeug) | ✅ | Braucht Kompare |
| Tabs | ⚠️ | Nur eine Erwähnung auf der Ansichtsseite; ein Fehlerbericht sagt, die geteilte Ansicht gehört zu einem Tab |
| Papierkorb, Dienstmenüs | ⚠️ | Nur als Kapitelüberschriften im Inhaltsverzeichnis gesehen |
| Entfernte Orte, komprimieren | ⚠️ | Auf den gelesenen Handbuchseiten nicht gefunden |

## Namensregeln

Von Dolphin nicht dokumentiert; das Dateisystem entscheidet. ⚠️

## Was wir übernehmen

Fähigkeiten `file.search` (Namen und Inhalte), `file.tag`, Stapel-Umbenennen (im Vertrag fehlend), Rückgängig der letzten Änderung (eine Aufgabe des Frontends, der Engine muss Verschiebungen umkehrbar machen), gespeicherte Suche als Sammlung (siehe Entwurf: „ein Album kann eine gespeicherte Suche sein“).

## Quellen (gelesen 2026-11-06)

- https://docs.kde.org/stable_kf6/en/dolphin/dolphin/ (Inhalt)
- https://docs.kde.org/stable_kf6/en/dolphin/dolphin/dolphin-view.html
- https://docs.kde.org/stable_kf6/en/dolphin/dolphin/panels.html
- https://docs.kde.org/stable_kf6/en/dolphin/dolphin/quick-tips.html
- Nicht offiziell, für keine Aussage verwendet: Fehlerberichte zu geteilter Ansicht und Tabs (bugs.kde.org).
