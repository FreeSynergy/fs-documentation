# 0076 – Das Grundmodell: Akteure, Ressourcen, Orte, Zeit, Ziele, Abläufe, Ereignisse

Status: **akzeptiert** (Gründer, 2026-11-13) · ersetzt die Einordnung „Workflow = Facette von Tasks“ und „Store = Facette von Files“ · baut auf ADR 0020 (AS2), 0045 (Themen-Schnittstellen), 0050 (ein Programm, eine Schnittstelle), 0066 (Befehle), 0068 (Fähigkeiten), 0074 (Schichten, Programm-Manifest), 0075 (Marketplace)

## Warum

Wir haben Programme nach Bedarf angelegt. Dabei haben sich Begriffe verschoben: Ist ein Store ein Teil von Files? Ist ein Workflow eine Aufgabe? Ist ein Mensch eine Ressource? Ohne ein festes Grundmodell bauen wir dasselbe mehrfach. Dieses ADR legt das Modell fest, ordnet alle Repositories ein und sagt, was fehlt.

## 1. Das Modell

Grundlage ist **REA (Resources, Events, Agents)**, das Modell hinter ERP-Systemen, genormt als **ISO/IEC 15944-4**, und seine offene Fassung für dezentrale Netze, **ValueFlows**. Für die Daten nutzen wir **ActivityStreams 2.0** (Akteure, Aktivitäten, Orte), **schema.org**, **JSCalendar** und **Serverless Workflow**.

| Frage | Begriff | Was es ist | Standard | Programm |
|---|---|---|---|---|
| **Wer?** | **Akteur**, einzeln | Wer handeln, besitzen, zusagen, unterschreiben und verantwortlich sein kann: Mensch, KI | AS2 `Person`, `Service`/`Application`; REA Agent | **fs-people** |
| | **Akteur**, Zusammenschluss | Gruppe, Organisation, **juristische Person** (Verein, GmbH …); hat eigene Mitglieder, Rollen und Regeln und handelt als ein Akteur | AS2 `Group`, `Organization` | **fs-groups** |
| **Womit?** | **Ressource**, Information | Was es gibt und womit man etwas tun kann, als Information: Dateien, Dokumente, Medien, Daten | schema.org `CreativeWork`; REA Resource | **fs-files** (Bytes, Herkunft, Versionen) + Dokument-Programme (Inhalt) |
| | **Ressource**, Sache/Kapazität | Dinge, Räume, Material, Bestand, **Zeit und Fähigkeiten von Akteuren** | ValueFlows `EconomicResource`; schema.org `Product` | **fs-resources** |
| **Wo?** | **Ort** | physischer Ort, Route, Gebiet; Adresse im Netz (URL), Speicherort | AS2 `Place`; schema.org `Place`; URL | **fs-maps** (physisch); fs-files `storage` (Speicherorte, ADR 0070) |
| **Wann?** | **Zeit** | Termine, Wiederholungen, Verfügbarkeit | JSCalendar | **fs-calendar** |
| **Was soll geschehen?** | **Ziel / Zusage** | Was erreicht oder getan werden soll, objektiv (bis das Ziel erreicht ist) oder subjektiv (Zustand ändern) | JSCalendar Task; ValueFlows `Intent`/`Commitment` | **fs-tasks** |
| **Was wird angeboten oder gesucht?** | **Angebot / Gesuch / Katalog** | Was jemand hat oder sucht, zu welchen Bedingungen | ValueFlows `Proposal`; schema.org `Offer`/`Demand`; AS2 `Offer` | **fs-marketplace** (ADR 0075) |
| **Wie?** | **Ablauf** | Wie man etwas tut: Schritte, Aktionen der Programme, Akteur je Schritt | Serverless Workflow 1.0; ValueFlows `Recipe`/`Process` | **fs-workflows** (neu) |
| **Was ist geschehen?** | **Ereignis** | Was tatsächlich passiert ist, unveränderlich | AS2 Activity; ValueFlows `EconomicEvent` | **fs-history** |
| **Was teilen wir mit?** | **Nachricht** | Austausch zwischen Akteuren: Mail, Chat, Agenten, Neuigkeiten | AS2 `Note`/`Create`/`Announce`; JMAP | **fs-messenger** |
| **Wie entscheiden wir?** | **Abstimmung** | Fragen, Antworten, Ergebnis einer Gruppe | — | **fs-surveys** |

Regeln des Modells:

1. **Menschen und KIs sind Akteure, keine Ressourcen.** Ihre Zeit, Fähigkeiten und Arbeit sind Ressourcen (fs-resources).
2. **Ort und Ding am Ort sind zwei Dinge.** Eine Website ist eine Ressource an einer Adresse. Ein Lager ist ein Ort, die Ware darin ist Ressource.
3. **Eine Sammlung ist kein Programm.** Album, Ordner, Playlist, Merkliste und Galerie sind Sammlungen (AS2 `Collection`) und in jedem Programm möglich. Ein eigenes Programm entsteht nur mit **eigenen Daten und eigenen Regeln** (Prüffrage „wessen Daten?“). Darum ist Groups ein Programm (Mitglieder, Rollen, Regeln), eine Galerie aber eine Ansicht.
4. **Angebot ≠ Ware.** Der Katalog sagt, was es gibt und wo die Ware liegt (mit Prüfsumme). Die Ware liegt in einem Lager (Speicherort). Jedes Angebot verweist auf einen **Bezugs-Workflow**: Annehmen startet ihn.
5. **Ziel ≠ Ablauf.** Tasks sagt, *was* erreicht werden soll; Workflows sagt, *wie*. Ein Ablauf kann Aufgaben anlegen (für menschliche Schritte), eine Aufgabe kann auf einen Ablauf verweisen.
6. **Geschehen ist unveränderlich.** Was passiert ist, steht in fs-history und wird nie umgeschrieben.

## 2. Ein Manifest, viele Wege

Jedes Programm veröffentlicht **ein** Manifest (ADR 0074): **Aktionen** (Funktionen), **Objekte** und **Attribute**, dazu Fähigkeiten (ADR 0068). Aus diesem einen Manifest entstehen:

- die **Menüs**, Kontextmenüs und Werkzeugleisten (Anordnungsdatei, ADR 0074);
- die **Workflow-Bausteine** in fs-workflows. **Je mehr Programme installiert sind, desto mehr Abläufe sind möglich**;
- die **REST-Schnittstelle** (als OpenAPI-Beschreibung);
- die **MCP-Werkzeuge** für KIs (Model Context Protocol);
- die Befehlszeile und die freedesktop-Aktionen (D-Bus);
- der **Katalogeintrag**, also was das Programm kann (im Store sichtbar).

Es gibt also **eine** Wahrheit darüber, was ein Programm kann. Menüs, Workflows, API und KI-Werkzeuge können nie auseinanderlaufen.

**Jedes Programm bekommt eine Workflow-Ansicht** (ein Baustein von fs-workflows): „Das kann man hier tun.“ Wer sie nicht will, blendet sie aus.

## 3. Einordnung aller Repositories

| Repository | Art | Rolle im Modell | Änderung |
|---|---|---|---|
| fs-people | Programm | Akteure, einzeln (Mensch, KI) | Facetten Contacts, Users, AIs, Partners bleiben |
| fs-groups | Programm | Akteure, Zusammenschluss, inkl. juristischer Personen | Gruppentyp „juristische Person“ ergänzen |
| fs-files | Programm | Ressourcen (Information): Bytes, Herkunft, Versionen, Speicherorte, Installieren als Aktion | Galerie und Desktop sind Facetten bzw. Frontends |
| fs-resources | Programm | Ressourcen (Sache/Kapazität): Dinge, Räume, Bestand, Zeit von Akteuren | — |
| fs-maps | Programm | Orte | — |
| fs-calendar | Programm | Zeit | — |
| fs-tasks | Programm | Ziele, Zusagen | Workflow ist **keine** Facette mehr |
| fs-history | Programm | Ereignisse | — |
| fs-messenger | Programm | Nachrichten | Facetten Mail, Chat, **News** (`Announce`, einer an viele) |
| fs-surveys | Programm | Abstimmungen | — |
| fs-streaming | Programm | Verteilung von Live-Medien | später prüfen, ob Facette eines Medien-Programms |
| fs-wiki | **wird Facette von fs-text** | — | Wiki-Code wird der Kern von fs-text (Umbenennung, Schritt 3) |
| fs-whiteboard | **wird Facette von fs-draw** | — | Code wird Kern von fs-draw (Umbenennung, Schritt 3) |
| fs-store | **Facette von fs-marketplace** | Laden-Ansicht | Logik wandert nach fs-marketplace (ADR 0075) |
| fs-catalog | Format + Daten | Kataloge (Angebote) | wird Katalog-Format von fs-marketplace |
| fs-identity | Baustein / Brücke | Anmeldung (Kanidm) | — |
| fs-hub | Baustein | Programme finden einander | — |
| fs-objects | Baustein | Objektspeicher jedes Programms | — |
| fs-interfaces | Baustein | Schnittstellen aller Themen | neue Themen `marketplace`, `workflows`, Dokument-Themen |
| fs-components | Baustein | Bausteine und Theme-Vertrag | — |
| fs-jscalendar | Baustein | gemeinsame Zeitlogik | — |
| fs-capnpc | Werkzeug | Schema-Compiler | — |
| fs-icons | Inhalt | Icon-Sets | — |
| fs-release | Werkzeug | Release-Kette | ihre Abläufe werden Workflows (fs-workflows) |
| fs-documentation | Inhalt | Doku, Website | wird mit fs-text/Wiki dargestellt |
| fs-kanidm, fs-zentinel, fs-tuwunel | Server | Anmeldung, Proxy, Matrix | in den Katalog als Art `server` |
| **fs-workflows** | **neu: Programm** | Abläufe | Repository anlegen |
| **fs-marketplace** | **neu: Programm** | Angebote, Gesuche, Kataloge | Repository anlegen |
| **fs-text** | **neu: Programm** | Dokumente aus Text (ODF `.odt`); Facette Wiki | Repository anlegen |
| **fs-data** | **neu: Programm** | strukturierte Dokumente, Tabellen (ODF `.ods`) | Repository anlegen |
| **fs-draw** | **neu: Programm** | Zeichnungen, Vektor, Präsentation (ODF `.odg`/`.odp`); Facette Whiteboard | Repository anlegen |
| **fs-paint** | **neu: Programm** | Raster und Foto; Facette Foto | Repository anlegen |

## 4. Ziel für jedes Programm

Jedes Programm soll:

1. **im Store sein.** Was noch nicht installierbar ist, steht dort ehrlich als „in Arbeit“ (Feld `unavailable` mit Grund);
2. **mindestens vier Frontends haben**: Standard, Admin (angelehnt an SAP Fiori) und zwei nach Vorbildern (ADR 0074);
3. mit **mehreren Icon-Sets, Themes, Animationsprofilen und Klang-Themes** nutzbar sein. Sie kommen nicht alle von uns, sind aber frei und im Store.

Dazu sind die **Server im Store** (Art `server`), und **Kataloge sind Git-Repositories**.

Fremde, freie Pakete (Icon-Sets, Farbpaletten, Klang-Themes) stehen im Store **als eigene Pakete mit ihrer eigenen Lizenz**. In unsere MIT-Repositories mischen wir nur Lizenzen, die dazu passen.

## 5. Weg dorthin

1. **Jetzt:** dieses ADR; Repositories der sechs neuen Programme mit README, DESIGN (Einordnung nach diesem ADR) und Lizenz, noch ohne Code; alle Programme mit Katalogeintrag (installierbar oder „in Arbeit“); Server in den Katalog; freie Icon-Sets, Themes, Klang-Themes als Pakete.
2. **Meilenstein „Wir benutzen es selbst“** läuft weiter; nichts davon hält ihn auf.
3. **Danach:** Umbenennungen (fs-wiki → Kern von fs-text, fs-whiteboard → Kern von fs-draw, fs-store → Facette auf fs-marketplace) als eigene, geprüfte Schritte, mit Weiterleitung, Katalog und Paketnamen; fs-workflows mit Programm-Manifest und Workflow-Ansicht; Frontends je Programm auf vier.
