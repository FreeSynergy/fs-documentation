# GNOME Planner - Menüpunkte

## Übersicht

Planner folgt dem klassischen GTK-Anwendungsaufbau: Menüleiste oben, Umschalter für die drei Ansichten (Aufgaben / Ressourcen / Abhängigkeiten), Werkzeugleiste und rechts der Gantt- bzw. PERT-Canvas.

## Hauptmenüs

| Menü | Einträge (Auswahl) |
|------|--------------------|
| **Datei (File)** | Neu, Öffnen, Speichern, Speichern unter, Dokument drucken, Zuletzt geschlossene Dokumente, Beenden |
| **Bearbeiten (Edit)** | Rückgängig, Wiederholen, Ausschneiden/Kopieren/Einfügen, Alle auswählen |
| **Ansicht (View)** | Gantt-Ansicht, Ressourcen-Usage, Abhängigkeiten ein/aus ausblenden, Zeilenhöhen |
| **Aufgaben (Task)** | Neue Aufgabe, Teilaufgabe, Meilenstein, Aufgabe löschen, Aufgabe info (Eigenschaften), Vorgang verschieben (vor/zurück), Aufwände aktualisieren |
| **Ressourcen (Resources)** | Neue Ressource, Ressourcen löschen, Kalender-/Wochenendarstellung, Arbeitszeit |
| **Projekt (Project)** | Projektdaten (Start, Ende, Kalenderwoche), Prioritäten bearbeiten, Abhängigkeitstypen |
| **Hilfe** | Handbuch, Info |

## Ansichten-Umschalter (Tabs)

1. **Aufgaben** — Aufgabenbaum + Gantt-Balken
2. **Ressourcen** — Ressourcenliste + Balken je Ressource (Auslastung)
3. **Abhängigkeiten** — PERT-Netzwerk (Knoten = Aufgaben)

## Kontextmenü (Rechtsklick im Aufgabenbaum)

| Eintrag | Beschreibung |
|---------|--------------|
| Neue Aufgabe / Neue Teilaufgabe | Zeile anlegen |
| Neuer Meilenstein | Aufgabe mit Dauer 0 |
| Aufgabe löschen | inkl. Teilaufgaben |
| Aufgabe info | Eigenschaften: Name, Start/Ende, Aufwand (Man-hours), completion %, Priorität, Notizen, Ressourcen |
| Abhängigkeit hinzufügen | Dialog mit Typ FS/SS/FF/SF und Verzögerung (lag) |

## Menüs nach Rolle

Planner ist Einzelplatz-Software ohne Benutzerkonten — **keine rollenabhängigen Menüs**.
