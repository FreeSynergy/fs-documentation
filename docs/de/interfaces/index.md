# Schnittstellen

**Status: Katalog-Entwurf (2026-11-06).** Das gilt für alles, auch für das, was schon gebaut ist und überarbeitet wird (ADR 0045). Die meisten Schnittstellen sind noch nicht spezifiziert; die Tabelle sagt, welche es sind.

Jedes Thema hat **eine Schnittstelle, dieselbe für jeden Anbieter**, damit ein Anbieter ausgetauscht oder ergänzt werden kann. Diese Liste beantwortet die Frage: Was gibt es zu standardisieren?

## Regeln

1. **Zuerst ein Standard.** Gibt es einen, folgt die Schnittstelle ihm. Gibt es keinen, schreiben wir einen und bieten ihn anderen an.
   **Jeder Standard hat genau ein besitzendes Programm,** den Ort der Wahrheit, und jedes andere Programm geht über dessen Schnittstelle. Kein zweites Modell derselben Sache (ADR 0050). Ein Standard mit mehreren Objektarten, wie JSCalendar, gehört pro Art: `Event` gehört `fs-calendar`, `Task` gehört `fs-tasks`.
2. **Eine Schnittstelle ist ein Ziel.** Wir legen das Ziel fest, und es darf schärfer werden, solange wir es noch nicht ganz kennen. Als Entwurf veröffentlicht, wird sie von mindestens zwei unabhängigen Nutzenden geprüft (bei einer Anbieter-Schnittstelle: zwei Anbieter), dann als Version 1.0 festgeschrieben. Danach ändert sie sich nur durch einen Sprung zu einer neuen Version, nie durch schleichendes Wachstum.
3. **Wie eine Elternklasse.** Jeder Anbieter bietet alle Methoden und Attribute seiner Schnittstelle an. Fehlt einem Anbieter etwas, suchen wir einen Weg, es trotzdem funktionieren zu lassen. Gibt es wirklich keinen, antwortet er ausdrücklich „nicht möglich“. Wir denken darüber nach, wie etwas gehen kann, bevor wir sagen, dass es nicht geht.
4. **Ein Frontend nutzt, was es will.** Die Engine darf mehr anbieten, als ein Frontend braucht.
5. **Plugins können im laufenden Betrieb hinzugefügt und entfernt werden** (Hot Plugins); siehe [Plugin-Form](#plugin-form).

## Zwei Ebenen

Wenn man diese beiden auseinanderhält, vermeidet man viel Verwirrung:

- Eine **Themen-Schnittstelle** sagt, womit Menschen arbeiten: *Nachrichten*. Programme und Frontends nutzen diese.
- Eine **Anbieter-Schnittstelle** sagt, wer es liefert: *Mail, Matrix, Telegram*. Jeder ist ein Adapter dahinter. Ein Anbieter kann zwei Rollen haben: als Client eines fremden Servers oder als der Server selbst.

## Themen: womit Menschen arbeiten

| Thema | Wofür | Standardbasis | Besitzer | Status |
|-------|----------------|---------------|---------|--------|
| Nachrichten | Jemandem etwas sagen, [KIs eingeschlossen](../programs/apps/assistant/index.md) | AS2, MIMI, JMAP Mail, MCP und ACP für Agenten | `fs-messenger` | Vertragsentwurf |
| Personen | Wissen, wer jemand ist und wie man ihn erreicht, mit [Rollen](roles.md) | JSContact | [`fs-people`](https://github.com/FreeSynergy/fs-people) | Schnittstellen-Entwurf, Anbieter vorhanden |
| Gruppen | Zusammengehören und festlegen, wer was darf | AS2 `Group`, SCIM | [`fs-groups`](../programs/platform/groups.md) | Schnittstellen-Entwurf, Code in Arbeit |
| Termine | Irgendwo zu irgendeiner Zeit sein | JSCalendar `Event` | `fs-calendar` | Kern vorhanden |
| Aufgaben | Wissen, was als Nächstes zu tun ist | JSCalendar `Task`, RFC 9253 | [`fs-tasks`](https://github.com/FreeSynergy/fs-tasks) | Kern vorhanden, Schnittstellen-Entwurf |
| Verlauf | Sich merken, was ich oder wir getan haben | AS2-Aktivitäten | [`fs-history`](https://github.com/FreeSynergy/fs-history) | vorläufiger Schnittstellen-Entwurf, Kern vorhanden |
| Ressourcen | Wissen, was wir haben und brauchen | Lücke | [`fs-resources`](https://github.com/FreeSynergy/fs-resources) | vorläufiger Schnittstellen-Entwurf, Kern vorhanden |
| Dateien | Alles behalten und wiederfinden | AS2 `Document` | [`fs-files`](../programs/apps/files/design.md) | vorläufiger Schnittstellen-Entwurf, Code in Arbeit |
| Texte | Gemeinsam schreiben und wissen | eigene Spezifikation (ADR 0031, 0033) | `fs-wiki` | Kern vorhanden |
| Orte | Wissen, wo etwas ist | GeoJSON | `fs-maps` | Kern vorhanden |
| Entscheidungen | Fragen und gemeinsam entscheiden | AS2 `Question`; darüber hinaus Lücke | [`fs-surveys`](https://github.com/FreeSynergy/fs-surveys) | vorläufiger Schnittstellen-Entwurf, Kern vorhanden |
| Boards | Visuell denken | Lücke, eigene Spezifikation | [`fs-whiteboard`](https://github.com/FreeSynergy/fs-whiteboard) | Schnittstellen-Entwurf, Kern vorhanden |
| Live-Medien | Etwas zeigen, während es passiert | WHIP, WHEP, Enhanced RTMP | [`fs-streaming`](https://github.com/FreeSynergy/fs-streaming) | Schnittstellen-Entwurf, Code in Arbeit |

## Anbieter: wer es liefert

| Schnittstelle | Wofür | Mögliche Anbieter |
|-----------|----------------|---------------------|
| Datenbank | Objekte speichern | Turso (hinter `Store` von `fs-store`, vorhanden) |
| Dateispeicher | Bytes speichern | lokaler Ordner, RustFS über S3, git, WebDAV |
| Mail | Mails senden und empfangen, als Client oder Server | JMAP-, IMAP- und SMTP-Clients; eigener Server später |
| Chat-Netzwerke | Menschen anderswo erreichen | Matrix (tuwunel), Telegram, Discord, andere |
| Identität | Anmelden, Systemzugang | Kanidm über einen [Wrapper](../programs/platform/identity.md), und unser eigener Fallback |
| Codecs | Ein Bild oder einen Ton in einen Stream und zurück umwandeln; ausgelagert, wie GStreamer | zuerst offene Codecs: AV1, Opus (ADR 0048) |
| Veröffentlichungsziel | Ein Video auf eine Plattform bringen | YouTube, Twitch, Odysee, PeerTube, andere |
| KI-Modelle | Antworten, Übersetzung, Hilfe bei Texten | llama.cpp, Anthropic API, andere |
| Kartendaten | Karten zeichnen | PMTiles (vorhanden in `fs-maps`) |

## Querschnitt: von allen genutzt

| Schnittstelle | Wofür | Standardbasis |
|-----------|----------------|---------------|
| Vertrauen | Zeigen, wann eine Person sicher ist, auch gegen Betrüger und Bots; jede Person legt ihre [eigene Stufe](../programs/apps/assistant/index.md#locking-ais-out) fest | Web of Trust; sein Nachfolger, das [Real Life Trust Protocol](https://github.com/real-life-org/trust-protocol), ist das vorgeschlagene Ziel (ADR 0052, 0054) |
| Teilen und Berechtigungen | Wer was sehen darf; Freigaben gehen an Gruppen | Lücke, eine Spezifikation für alle. Offen: [Rollen-Privatsphäre](roles.md#open) |
| Hülle und Aktivitätsprotokoll | Die äußere Form und der Verlauf jedes Objekts | AS2, vorgeschlagener Besitzer `fs-store` (ADR 0050) |
| Synchronisation | Geräte und Programme zusammenbringen | Aktivitätsprotokoll (ADR 0019) |
| Präsenz | Sehen, was andere gerade tun | Lücke; wird nie gespeichert |
| Suche | Programmübergreifend finden | Lücke |
| Benachrichtigungen | Im richtigen Moment Bescheid bekommen | Lücke |
| Metadaten-Extraktoren | Lesen, was eine Datei enthält, je nach Typ | Exif, XMP, IPTC und andere je Typ |
| Export und Import | Daten hinein- und hinausbringen | das Standardformat jedes Themas |
| Komponenten | Daten zeigen, ohne ihre Bedeutung zu kennen | unsere [Komponenten-Doku](../components/index.md) |
| Diagramme | Zeigen, was Zahlen bedeuten | Vega-Lite-Teilmenge vorgeschlagen, [Katalog](../components/charts.md) |
| Entscheidungsmethoden | Antworten in ein Ergebnis verwandeln | veröffentlichte Methodenbeschreibungen |
| Plugins, Pakete, Themes | Das System erweitern | Git als Verteilung (ADR 0036) |

Eine Komponente ist nicht die einzige Art von Schnittstelle; sie ist hier nur eine Zeile. Ein Workbench ist ebenfalls eine Komponente.

## Bekannte Grenzen vor 1.0

- **Kein erprobter Aufrufer.** Der Transport kennt nur den Systembenutzer. Jeder Name in einer Anfrage ist reiner Text, deshalb kann `fs-groups` Rechte noch nicht durchsetzen. Das ist die größte Lücke für den echten Einsatz durch mehrere Personen; sie braucht den Identitäts-Wrapper.
- **Listen ohne Cursor** in `people` und `groups` schlagen mit `too-large` fehl, wenn eine Antwort nicht mehr in eine Nachricht passt.
- **Melden, was ein Anbieter kann,** ist noch nicht einheitlich: manche Verträge haben `capabilities`, manche nur `supportReport`.

## Plugin-Form

Wir folgen dem, was [Zentinel](https://github.com/zentinelproxy/zentinel) schon macht:

- **Viele Schnittstellen sind nur Konfiguration.** Sie wird geprüft und im laufenden Betrieb atomar ausgetauscht, während alles weiterläuft.
- **Größere Plugins sind Agenten:** eigene, gegen Abstürze isolierte Prozesse über eine lokale Verbindung, die ihre Fähigkeiten melden. Unsere sprechen Cap'n Proto (ADR 0021). Ein Frontend mit eingebauten Filtern ist dieselbe Idee: ein Mini-Server auf einer Engine.
- **Wenn ein Agent zeichnen muss,** gibt er eine Szenenbeschreibung zurück, und der Host zeichnet. Wie Text vermessen wird, ist ungelöst, und es wurde noch nichts gemessen.

## Wer die Spezifikationen besitzt

Alle Schnittstellen liegen in einem öffentlichen Repository, [`fs-interfaces`](https://github.com/FreeSynergy/fs-interfaces), damit andere sie umsetzen können, ohne unsere Programme zu nutzen. Version 0.3.0 enthält die Verträge für Gemeinsames, Aufgaben, Messenger, Hub, Personen, Gruppen und Dateien als Entwürfe, erzeugt mit unserem eigenen Cap'n-Proto-Compiler. Neben den Verträgen enthält es gemeinsamen Transport-Code für Server und Clients, hinter einem Feature und ohne Geschäftslogik. Fehler reisen als RFC-9457-Problem-Details.
