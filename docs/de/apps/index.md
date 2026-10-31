# Programme (Apps)

Programme sind in **Kategorien** gegliedert. Programme, deren Oberfläche in FreeSynergy nachgebildet oder angebunden wird, bekommen eine **Skin-Dokumentation**: sieben Dateien pro Programm.

## Kategorien

| Kategorie | Inhalt | Skin-Dokumentation |
|-----------|--------|--------------------|
| [Wiki](wiki/) | Wiki- und Wissenssysteme | abgeschlossen (7 Programme) |
| [Messenger](messenger/) | Chat, E-Mail, soziale Netzwerke | teilweise (7 Programme) |
| [Desktop](desktop/) | Desktop-Programme, Dashboards, Startseiten | abgeschlossen (12 Programme) |
| [Components](components/) | UI-Bibliotheken und Frameworks | eigene Elemente-Doku: [components/](../components/) |
| [Whiteboards](whiteboards/) | Kollaborative Whiteboards | vorgesehen |
| [Helpdesk](helpdesk/) | Tickets und Support | vorgesehen |
| [Projektmanagement](projectmanagement/) | Aufgaben, Boards, Projekte | vorgesehen |
| [Kontakt](contact/) | Kontaktpflege | vorgesehen |
| [CRM](crm/) | Kundenbeziehungen | vorgesehen |
| [Kalender](calendar/) | Termine und Planung | vorgesehen |
| [Maps](maps/) | Karten und Geodaten | vorgesehen |
| [ERP](erp/) | Ressourcenplanung | vorgesehen |
| [Workflows](workflows/) | Automatisierung und Integration | vorgesehen |
| [Demokratie](democracy/) | Beteiligungsplattformen | vorgesehen |
| [Marketing](marketing/) | Marketing und Analytics | vorgesehen |

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
