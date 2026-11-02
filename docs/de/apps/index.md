# Programme (Apps)

Programme sind in **Kategorien** gegliedert. Programme, deren Oberfläche in FreeSynergy nachgebildet oder angebunden wird, bekommen eine **Skin-Dokumentation**: sieben Dateien pro Programm.

## Kategorien

| Kategorie | Inhalt | Skin-Dokumentation |
|-----------|--------|--------------------|
| [Wiki](wiki/) | Wiki- und Wissenssysteme | abgeschlossen (7 Programme) |
| [Messenger](messenger/) | Chat, E-Mail, soziale Netzwerke | abgeschlossen (7 Programme) |
| [Desktop](desktop/) | Desktop-Programme, Dashboards, Startseiten | abgeschlossen (12 Programme) |
| [Whiteboards](whiteboards/) | Kollaborative Whiteboards | abgeschlossen (6 Programme) |
| [Helpdesk](helpdesk/) | Tickets und Support | abgeschlossen (8 Programme) |
| [Projektmanagement](projectmanagement/) | Aufgaben, Boards, Projekte | abgeschlossen (8 Programme) |
| [Kontakt](contact/) | Kontaktpflege | abgeschlossen (4 Programme) |
| [CRM](crm/) | Kundenbeziehungen | abgeschlossen (6 Programme) |
| [Kalender](calendar/) | Termine und Planung | abgeschlossen (6 Programme) |
| [Maps](maps/) | Karten und Geodaten | abgeschlossen (7 Programme) |
| [ERP](erp/) | Ressourcenplanung | abgeschlossen (6 Programme) |
| [Workflows](workflows/) | Automatisierung und Integration | abgeschlossen (6 Programme) |
| [Demokratie](democracy/) | Beteiligungsplattformen | abgeschlossen (6 Programme) |
| [Marketing](marketing/) | Marketing und Analytics | abgeschlossen (6 Programme) |
| [Marktplätze](marketplace/) | Marktplatz-Software und fremde Marktplätze | abgeschlossen (6 Programme) |
| [Foto-Galerien](gallery/) | Bild- und Videosammlungen | abgeschlossen (8 Programme) |
| [Streaming](streaming/) | Encoder, Medienserver, Multistreaming | abgeschlossen (10 Programme) |

## Skin-Schema

Jede Skin-Dokumentation liegt in `apps/<kategorie>/skins/<programm>/` und enthält:

| Datei | Inhalt |
|-------|--------|
| `index.md` | Übersicht und Links |
| `menu.md` | Menüpunkte, Kontextmenüs, Rollen-Menüs |
| `features.md` | Funktionen, Integrationen, Was es NICHT kann |
| `description.md` | Beschreibung, Vorteile, Abgrenzung, Technische Details |
| `structure.md` | Fenster-Struktur (ASCII), UI/UX, Accessibility |
| `shortcuts.md` | Alle Tastatur-Shortcuts (immer separat) |
| `api.md` | API-Art, Auth, Endpunkte, Beispiele, Rate Limits, SDKs |

Referenzbeispiele: [Wiki/Skins](wiki/skins/), [Messenger/Skins](messenger/skins/), [Desktop/Skins](desktop/skins/).

## Querverweise auf Systembereiche

| Bereich | Bezug zu Programmen |
|---------|---------------------|
| [Komponenten](../components/) | UI-Elemente, die in den Oberflächen verwendet werden |
| [Gesten](../gestures/) | Interaktionen in Touch-Oberflächen |
| [Animationen](../animations/) | Übergänge und Feedback in den Oberflächen |
| [Standardisierte Daten](../data/) | Felder, Modelle und das API-Muster aller Programme |

## Neue Programme anlegen

1. Kategorie wählen (Kategorien und Beispiele sind in `SYSTEM.md` im Projektstamm beschrieben)
2. Verzeichnis `apps/<kategorie>/skins/<programm>/` anlegen
3. Sieben Dateien nach dem Schema oben schreiben (Deutsch zuerst)
4. `apps/<kategorie>/skins/index.md` um den Eintrag ergänzen
5. Fehlende Funktionen ausdrücklich benennen — nichts erfinden
