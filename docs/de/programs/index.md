# Programme (Apps)

Programme sind in **Kategorien** gegliedert. Programme, deren Oberfläche in FreeSynergy nachgebildet oder angebunden wird, bekommen eine **Skin-Dokumentation**: sieben Dateien pro Programm.

## Kategorien

| Kategorie | Inhalt | Skin-Dokumentation |
|-----------|--------|--------------------|
| [Wiki](apps/wiki/) | Wiki- und Wissenssysteme | abgeschlossen (7 Programme) |
| [Messenger](apps/messenger/) | Chat, E-Mail, soziale Netzwerke | abgeschlossen (7 Programme) |
| [Desktop](platform/desktop/) | Desktop-Programme, Dashboards, Startseiten | abgeschlossen (12 Programme) |
| [Whiteboards](apps/whiteboard/) | Kollaborative Whiteboards | abgeschlossen (6 Programme) |
| [Helpdesk](apps/helpdesk/) | Tickets und Support | abgeschlossen (8 Programme) |
| [Projektmanagement](suites/projectmanagement/) | Aufgaben, Boards, Projekte | abgeschlossen (8 Programme) |
| [Kontakt](apps/people/) | Kontaktpflege | abgeschlossen (4 Programme) |
| [CRM](suites/crm/) | Kundenbeziehungen | abgeschlossen (6 Programme) |
| [Kalender](apps/calendar/) | Termine und Planung | abgeschlossen (6 Programme) |
| [Maps](apps/maps/) | Karten und Geodaten | abgeschlossen (7 Programme) |
| [ERP](suites/erp/) | Ressourcenplanung | abgeschlossen (6 Programme) |
| [Workflows](suites/workflows/) | Automatisierung und Integration | abgeschlossen (6 Programme) |
| [Demokratie](suites/democracy/) | Beteiligungsplattformen | abgeschlossen (6 Programme) |
| [Marketing](apps/marketing/) | Marketing und Analytics | abgeschlossen (6 Programme) |
| [Marktplätze](suites/marketplace/) | Marktplatz-Software und fremde Marktplätze | abgeschlossen (6 Programme) |
| [Foto-Galerien](apps/gallery/) | Bild- und Videosammlungen | abgeschlossen (8 Programme) |
| [Streaming](apps/streaming/) | Encoder, Medienserver, Multistreaming | abgeschlossen (10 Programme) |

## Skin-Schema

Jede Skin-Dokumentation liegt in `apps/<kategorie>/masks/<programm>/` und enthält:

| Datei | Inhalt |
|-------|--------|
| `index.md` | Übersicht und Links |
| `menu.md` | Menüpunkte, Kontextmenüs, Rollen-Menüs |
| `features.md` | Funktionen, Integrationen, Was es NICHT kann |
| `description.md` | Beschreibung, Vorteile, Abgrenzung, Technische Details |
| `structure.md` | Fenster-Struktur (ASCII), UI/UX, Accessibility |
| `shortcuts.md` | Alle Tastatur-Shortcuts (immer separat) |
| `api.md` | API-Art, Auth, Endpunkte, Beispiele, Rate Limits, SDKs |

Referenzbeispiele: [Wiki/Skins](apps/wiki/frontends/), [Messenger/Skins](apps/messenger/frontends/), [Desktop/Skins](platform/desktop/frontends/).

## Querverweise auf Systembereiche

| Bereich | Bezug zu Programmen |
|---------|---------------------|
| [Komponenten](../components/) | UI-Elemente, die in den Oberflächen verwendet werden |
| [Gesten](../interactions/gestures/) | Interaktionen in Touch-Oberflächen |
| [Animationen](../interactions/animations/) | Übergänge und Feedback in den Oberflächen |
| [Standardisierte Daten](../data/) | Felder, Modelle und das API-Muster aller Programme |

## Neue Programme anlegen

1. Kategorie und Ebene wählen (Levels und Beispiele siehe `conventions/doku-standard.md` im Projektstamm)
2. Verzeichnis `apps/<kategorie>/masks/<programm>/` anlegen
3. Sieben Dateien nach dem Schema oben schreiben (Deutsch zuerst)
4. `apps/<kategorie>/masks/index.md` um den Eintrag ergänzen
5. Fehlende Funktionen ausdrücklich benennen — nichts erfinden
