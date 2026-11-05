# Redmine - Struktur & UI/UX

## Übersicht

Redmine zeigt ein vertikales Standardlayout: schmale Kopfzeile mit Reitern und Suche, darunter Breadcrumb- und Projekt-Reiterleiste, dann der Inhaltsbereich mit Formular oder Tabelle. Rechtsrandspalten für Projektinfo und Aktionen sind modulspezifisch. Die Oberfläche folgt einem funktionalen, inhaltszentrierten Stil ohne Single-Page-Mechanik.

## Fenster-Struktur

### Hauptlayout

```
+---------------------------------------------------------------+
| Redmine | Meine Startseite | Projekte | Administration   [Suche] |
+---------------------------------------------------------------+
| Projektname > (Breadcrumb)                                    |
| [Uebersicht][Aktivitaeten][Issues][Zeiterfassung][Wiki] ...   |
+---------------------------------------------------------------+
|                                                              |
|  Inhaltsbereich (Tabelle, Formular, Issue-Ansicht)           |
|                                                              |
|  +--------------------------------------------------------+  |
|  | Filterleiste / Spaltenkoepfe                           |  |
|  | Issue-Liste mit Status, Tracker, Zugewiesene, Datum    |  |
|  +--------------------------------------------------------+  |
|  | Pagination (Seiten 1..n, Trefferzaehler)               |  |
|                                                              |
+---------------------------------------------+----------------+
|                                              | Randspalte     |
+----------------------------------------------+---------------+
| Fusszeile: Redmine-Version, Theme-Angabe                    |
+-------------------------------------------------------------+
```

### Issue-Detailansicht

```
+-------------------------------------------------------------+
| #1234 Titel des Issues          [Bearbeiten] [Loeschen]     |
+---------------------------------------------+---------------+
| Journal (Kommentare, Feldaenderungen)       | Details-Block |
| - von Anna, vor 2 Tagen: Status Neu -> In   | Tracker       |
|   Arbeit                                    | Status        |
| - Notizfeld (Textile/Markdown)              | Prioritaet    |
|                                             | Zugewiesene   |
| Notiz speichern                             | Version       |
+---------------------------------------------+---------------+
```

### Bereichs-Tabelle

| Bereich | Position | Inhalt |
|---------|----------|--------|
| Kopfzeile | oben | Hauptreiter, Benutzermenü, Suchfeld |
| Breadcrumb + Reiter | darunter | Projektpfad, Modulreiter, projektinterne Aktionen |
| Inhaltsbereich | Mitte | Listen, Formulare, Issue-Detail, Wiki-Text |
| Randspalte | rechts | Detail-Block (Issue), Projektinfo, „Verknüpfungen" |
| Fußzeile | unten | Versions- und Theme-Angabe (per Theme änderbar) |

## UI/UX

### Design-Prinzipien

- **Inhalt vor Schmuck**: tabellarische Dichte, kleine Schrift, viele Felder pro Bildschirm
- **Server-Rendered**: jede Aktion ist ein Seitenaufruf; Zustand steckt in URLs (deep-linkbar)
- **Ein Theme, viele Anpassungen**: Grundlayout stabil, Darstellung komplett per CSS austauschbar

### Farbschema und Themes

- Standardtheme „Classic" (hell, graublau), weitere Themes im Theme-Ordner (`public/themes/`)
- Kein Dark-Mode im Kern; dunkle Schemata als Theme-Plugins (versionsabhängig)
- Status-/Prioritätsfarben können über CSS oder Themes angepasst werden

### Interaktionen

- **Formulare mit Inline-Validierung**: Fehler erscheinen oben auf der Seite
- **Autocomplete** für Benutzer-/Projekt-/Versionsfelder beim Tippen
- **Kein Drag & Drop im Kern**: Sortieren über Spaltenköpfe und Formulare (Gantt-Aktionen nur als Plugin)
- **Animationen**: praktisch keine; Seitenwechsel erfolgen ohne Übergänge
- **Popups**: kleine JS-Popups für Zeiterfassungs-Schnellformular; sonst normale Seiten

### Responsive Design

- **Ab Redmine 3.x responsiv**: Viewport-Breakpoints für Listen und Formulare
- **Mobil**: Reiter brechen um, Tabellen scrollbar; Bedienung brauchbar, aber dichte Tabellen bleiben gewöhnungsbedürftig
- Eigene mobile Apps sind Plugin-/Drittanbieter-Territorium

## Zugänglichkeit

- **Skip-Link „Zum Inhalt springen"** am Seitenanfang
- **Tab-Reihenfolge** folgt der DOM-Reihenfolge; Formulare vollständig per Tastatur bedienbar
- **Keine durchgängigen ARIA-Verbesserungen**: Screenreader bekommen Tabellenstruktur, aber wenige Rollen/Labels (Nachrüstungen versionsabhängig)
- **Kontrast**: Standard-Classic schwach; für WCAG empfiehlt sich ein angepasstes Theme

## Performance

- **Serverseitige Pagination**: Standard 25/30 Zeilen je Seite, konfigurierbar über Einstellungen
- **Spalten-Auswahl** reduziert Ladezeit großer Issue-Listen
- **Caching**: Rails-Fragment-Caching; Skalierung primär über App-Server und Datenbank-Caching
- **Schwer skalierend**: projektübergreifende Abfragen und Berichte ohne restrictive Filter verlangsamen große Instanzen
