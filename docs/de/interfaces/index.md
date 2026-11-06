# Schnittstellen

**Status: Katalog-Entwurf (2026-11-06).** Das gilt für alles, auch für das, was schon gebaut ist und überarbeitet wird (ADR 0045). Die meisten Schnittstellen sind noch nicht festgelegt; die Tabelle sagt, welche es sind.

Jedes Thema hat **eine Schnittstelle, für jeden Anbieter dieselbe**, damit ein Anbieter ausgetauscht oder ergänzt werden kann. Diese Liste beantwortet die Frage: Was gibt es zu standardisieren?

## Regeln

1. **Ein Standard kommt zuerst.** Gibt es einen, folgt die Schnittstelle ihm. Gibt es keinen, schreiben wir einen und bieten ihn anderen an. **Jeder Standard hat genau ein besitzendes Programm,** den Ursprung der Wahrheit; jedes andere Programm geht über dessen Schnittstelle. Kein zweites Modell derselben Sache (ADR 0050). Ein Standard mit mehreren Objektarten, wie JSCalendar, gehört je Art: `Event` gehört `fs-calendar`, `Task` gehört `fs-tasks`.
2. **Eine Schnittstelle ist ein Ziel.** Wir definieren das Ziel, und es darf schärfer werden, solange wir es noch nicht ganz kennen. Als Entwurf veröffentlicht, wird sie von mindestens zwei unabhängigen Nutzern erprobt (bei einer Anbieter-Schnittstelle: zwei Anbieter) und danach als Version 1.0 festgelegt. Danach ändert sie sich nur durch einen Sprung zu einer neuen Version, nie durch schleichendes Wachstum.
3. **Wie eine Elternklasse.** Jeder Anbieter bietet alle Methoden und Attribute seiner Schnittstelle. Fehlt einem Anbieter etwas, suchen wir einen Weg, es trotzdem funktionieren zu lassen. Gibt es wirklich keinen, antwortet er ausdrücklich „nicht möglich“. Wir überlegen, wie etwas gehen könnte, bevor wir sagen, dass es nicht geht.
4. **Ein Frontend nutzt, was es will.** Die Engine darf mehr anbieten, als ein Frontend braucht.
5. **Plugins lassen sich im laufenden Betrieb hinzufügen und entfernen** (Hot-Plugins); siehe [Plugin-Form](#plugin-form).

## Zwei Ebenen

Sie auseinanderzuhalten verhindert viel Verwirrung:

- Eine **Themen-Schnittstelle** sagt, womit Menschen arbeiten: *Nachrichten*. Programme und Frontends nutzen sie.
- Eine **Anbieter-Schnittstelle** sagt, wer sie liefert: *Mail, Matrix, Telegram*. Jeder Anbieter ist ein Adapter dahinter. Ein Anbieter kann zwei Rollen haben: als Client eines fremden Servers oder als der Server selbst.

## Themen: womit Menschen arbeiten

| Thema | Wofür | Standard-Grundlage | Besitzer | Status |
|-------|-------|--------------------|---------|--------|
| Nachrichten | Jemandem etwas sagen | AS2, MIMI, JMAP Mail | `fs-messenger` | Vertragsentwurf |
| Personen | Wissen, wer jemand ist und wie man ihn erreicht, mit [Rollen](roles.md) | JSContact | `fs-people` | Kern vorhanden |
| Gruppen | Zusammengehören und entscheiden, wer was darf | AS2 `Group`, SCIM | `fs-groups` | Geplant |
| Ereignisse | Irgendwo zu einer Zeit sein | JSCalendar `Event` | `fs-calendar` | Kern vorhanden |
| Aufgaben | Wissen, was als Nächstes zu tun ist | JSCalendar `Task`, RFC 9253 | [`fs-tasks`](https://github.com/FreeSynergy/fs-tasks) | Kern vorhanden, Schnittstelle als Entwurf |
| Verlauf | Erinnern, was ich oder wir getan haben | AS2-Aktivitäten | `fs-history` | Geplant |
| Ressourcen | Wissen, was wir haben und brauchen | Lücke | `fs-resources` | Geplant |
| Dateien | Alles behalten und finden | AS2 `Document` | `fs-files` | Geplant |
| Texte | Gemeinsam schreiben und wissen | Eigene Spezifikation (ADR 0031, 0033) | `fs-wiki` | Kern vorhanden |
| Orte | Wissen, wo | GeoJSON | `fs-maps` | Kern vorhanden |
| Entscheidungen | Fragen und gemeinsam entscheiden | AS2 `Question`; darüber hinaus Lücke | `fs-surveys` | Geplant |
| Boards | Visuell denken | Lücke, eigene Spezifikation | `fs-whiteboard` | Geplant |
| Live-Medien | Etwas zeigen, während es passiert | WHIP, WHEP, Enhanced RTMP | `fs-streaming` | Geplant |

## Anbieter: wer sie liefert

| Schnittstelle | Wofür | Mögliche Anbieter |
|---------------|-------|-------------------|
| Datenbank | Objekte speichern | Turso (hinter `Store` von `fs-store`, vorhanden) |
| Dateispeicher | Bytes speichern | Lokaler Ordner, RustFS über S3, git, WebDAV |
| Mail | Mail senden und empfangen, als Client oder Server | JMAP-, IMAP- und SMTP-Clients; eigener Server später |
| Chat-Netzwerke | Menschen anderswo erreichen | Matrix (tuwunel), Telegram, Discord, andere |
| Identität | Anmelden, Systemzugang | Kanidm über einen [Wrapper](../programs/platform/identity.md) und unser eigener Ersatz |
| Codecs | Ein Bild oder einen Ton in einen Strom umwandeln und zurück; ausgelagert, wie bei GStreamer | Zuerst offene Codecs: AV1, Opus (ADR 0048) |
| Veröffentlichungsziel | Ein Video auf eine Plattform bringen | YouTube, Twitch, Odysee, PeerTube, andere |
| Übersetzung, KI | Lokale Hilfe bei Sprache und Text | llama.cpp, andere |
| Kartendaten | Karten zeichnen | PMTiles (vorhanden in `fs-maps`) |

## Querschnitt: von allen genutzt

| Schnittstelle | Wofür | Standard-Grundlage |
|---------------|-------|--------------------|
| Vertrauen | Zeigen, wann eine Person sicher ist, auch gegen Betrüger und Bots | Web of Trust (ADR 0052) |
| Teilen und Berechtigungen | Wer was sehen darf; Freigaben gehen an Gruppen | Lücke, eine Spezifikation für alle |
| Hülle und Aktivitätsprotokoll | Die äußere Form jedes Objekts und seine Historie | AS2, vorgeschlagener Besitzer `fs-store` (ADR 0050) |
| Sync | Geräte und Programme zusammenbringen | Aktivitätsprotokoll (ADR 0019) |
| Präsenz | Sehen, was andere gerade tun | Lücke; wird nie gespeichert |
| Suche | Über Programme hinweg finden | Lücke |
| Benachrichtigungen | Im richtigen Moment Bescheid bekommen | Lücke |
| Metadaten-Extraktoren | Lesen, was eine Datei enthält, je nach Typ | Exif, XMP, IPTC und andere je Typ |
| Export und Import | Daten hinein- und herausbringen | Standardformat jedes Themas |
| Komponenten | Daten zeigen, ohne ihre Bedeutung zu kennen | Unsere [Komponenten-Dokumentation](../components/index.md) |
| Diagramme | Zeigen, was Zahlen bedeuten | Vega-Lite-Teilmenge vorgeschlagen, [Katalog](../components/charts.md) |
| Entscheidungsmethoden | Antworten in ein Ergebnis übersetzen | Veröffentlichte Methodenbeschreibungen |
| Plugins, Pakete, Themes | Das System erweitern | Git als Verteilung (ADR 0036) |

Eine Komponente ist nicht die einzige Art von Schnittstelle; sie ist hier nur eine Zeile. Eine Workbench ist ebenfalls eine Komponente.

## Plugin-Form

Wir folgen dem, was [Zentinel](https://github.com/zentinelproxy/zentinel) bereits tut:

- **Viele Schnittstellen sind nur Konfiguration,** die geprüft und atomar ausgetauscht wird, während alles weiterläuft.
- **Größere Plugins sind Agenten:** eigene, gegen Abstürze isolierte Prozesse über eine lokale Verbindung, die ihre Fähigkeiten melden. Unsere sprechen Cap'n Proto (ADR 0021). Ein Frontend mit eingebauten Filtern ist dieselbe Idee: ein kleiner Server auf einer Engine.
- **Muss ein Agent zeichnen,** gibt er eine Szenenbeschreibung zurück, und der Host zeichnet sie. Wie Text gemessen wird, ist ungelöst, und es wurde noch nichts gemessen.

## Wer die Spezifikationen besitzt

Alle Schnittstellen gehen in ein öffentliches Repository, `fs-interfaces` (entschieden 2026-11-06, wird gerade eingerichtet), damit andere sie umsetzen können, ohne unsere Programme zu nutzen.
