# Karte der Programme

!!! warning "Maschinell übersetzt, noch nicht geprüft / Machine-translated, not yet reviewed"
    Diese Seite wurde maschinell aus der englischen Fassung übersetzt und noch nicht von einem Menschen geprüft.
    This page was machine-translated from the English version and has not yet been reviewed by a person.

**Status: Entwurf (2026-11-08); die Schichten und die vier Frontends sind entschieden (ADR 0066, 2026-11-09), die Programmtabelle ist noch offen.** Diese Seite stellt jedes Programm, jede Facette und jede Suite an einer Stelle dar, zusammen mit den Datentypen, die jedes besitzt, und den Frontends, die es bekommt. Sie ist der Ausgangspunkt der Runde 3: Zuerst einigen wir uns auf diese Karte, dann auf Datentypen und Schnittstellen, und erst danach bauen wir.

## Die Schichten, von unten nach oben

| Schicht | Was sie ist | Wer sie definiert |
|---------|-------------|-------------------|
| **Basistyp** | Ein kleiner Wert mit festen Regeln: E-Mail-Adresse, Telefonnummer, Name, Adresse, Datum. Überall gleich. | Einmal, für alle Programme |
| **Datentyp** | Ein Ding aus Basistypen, genau einem Programm gehörend: `Person`, `Event`, `Task`. Folgt einem Standard. | Das besitzende Programm (ADR 0050) |
| **Schnittstelle** | Was ein Programm mit seinen Datentypen tun kann: Befehle wie anlegen, ändern, finden, vorschlagen. | Das besitzende Programm |
| **Komponente** | Jeder Basistyp hat feste Komponenten: *input* (Eingabe), *display* (Anzeige), *compact* (in einer Zeile), *cell* (in einer Liste). Ein Datentyp bekommt seine Komponenten aus seinen Basistypen. | Einmal, in `fs-components` |
| **Stil** | Das Erscheinungsbild: Abstände, Ecken, Glas oder Vollfläche, Schriften, **ein eigener Icon-Satz**. Von jedem Frontend wiederverwendbar. | Einmal je Stil, 5–10 insgesamt |
| **Frontend** | Eine Art, ein Programm oder eine Facette zu nutzen, aus Komponenten in einem Stil gebaut. | Je Programm oder Facette |
| **Facette** | Ein Teil eines Programms, der wie eine eigene App aussieht (ADR 0061). | Das Programm |
| **Suite** | Mehrere Programme zusammen für einen Zweck. | Über Programme hinweg |

Das Backend meldet für jeden Datentyp seine Felder, deren Basistypen und seine Befehle. Ein Frontend entscheidet nie,
was eine E-Mail-Adresse ist; es entscheidet nur, wo es die E-Mail-Komponente zeigt.

## Vier Frontends für jedes Programm (ADR 0066)

| Frontend | Zweck | Gebaut wie |
|----------|-------|------------|
| **Admin** | Jedes Feld, jede Einstellung, jeder Befehl. Das Sicherheitsnetz. Sieht aus wie SAP Fiori (ein öffentliches Designsystem für dichte Geschäftsdaten). | Aus der Beschreibung des Datentyps generiert, derselbe Code für alle Programme |
| **Simple** | Für Menschen mit wenig Erfahrung: wenige Schaltflächen, groß, klar. | Von Hand, ein Stil für alle Programme |
| **Apple-Stil** | Nach Apples Gestaltungssprache nachgebaut, auf Maß: Abstände, Zeilenhöhen, Schriftgrößen, Ecken, Glas, Layout. | Von Hand, aus einem Messblatt |
| **Windows-Stil** | Dasselbe nach Microsofts Fluent-Design: flache Oberflächen, dessen Abstände und Ecken. | Von Hand, aus einem Messblatt |

Die Messblätter stammen aus den öffentlichen Richtlinien (Apple Human Interface Guidelines, Microsoft Fluent 2) und aus
Screenshots der eigenen Apps der Plattformen, die lokal bleiben und nie veröffentlicht werden. Der genaue Nachbau prüft
auch, was die GUI-Engine kann. Eigene Icons, Texte und offene Schriften mit ähnlichen Maßen; nichts von ihnen.

Der Apple-Stil nimmt Apples eigene Apps als Vorlage: zuerst 1:1 nachgebaut, dann mit Funktionen gefüllt, später bei Bedarf
geändert. Der Windows-Stil wird ebenfalls 1:1 nachgebaut, je Kategorie ein Windows-Programm, möglichst eines, das es unter
Linux nicht gibt, damit alle in der freien Software davon profitieren. Bewusst keine Linux-Programme als Vorlagen: die
haben wir schon. Später ein **FreeSynergy-Stil** eigener Art, ganz anders als alle diese (ADR 0066, Nachtrag vom 2026-11-09).

Die Analysen bekannter Programme je Kategorie (`frontends/<programm>/latest/`) bleiben die Quelle für **Funktionen**.

## Windows-Vorlagen (vom Eigentümer genehmigt, 2026-11-10)

Der Windows-Stil wird 1:1 aus je einem Windows-Programm pro Kategorie nachgebaut, möglichst eines ohne Linux-Gegenstück.
Kein Linux-Programm dient als Vorlage. Maße und Quellen: `docs/de/components/styles/windows.md`.

| Kategorie (Programm oder Facette) | Windows-Programm | Hinweise |
|-----------------------------------|------------------|----------|
| People | Outlook | Ansicht Personen der neuen Outlook-App für Windows |
| Mail (Messenger) | Outlook | Mail-Modul der neuen Outlook-App |
| Calendar | Outlook | Kalender-Modul der neuen Outlook-App |
| Groups | Microsoft Teams | |
| Tasks | Microsoft To Do | |
| Files | Datei-Explorer | |
| Gallery (Facette von Files) | Fotos | Microsoft Fotos |
| Videos | Media Player | Prüfen, welcher der beiden Player gemeint ist: die neue App Media Player oder Windows Media Player Legacy (optionale Funktion) |
| Wiki | OneNote | |
| Maps | Google Earth | Google Earth Pro für Windows. Street View bekommt kein eigenes Frontend |
| Whiteboard | Microsoft Whiteboard | **Offen:** Microsofts Support-Seite sagt, dass die eigenständigen Whiteboard-Apps für Windows am 2026-10-16 eingestellt werden (Whiteboard bleibt in Teams und im Web, für Geschäfts- und Schulkonten). Vor dem Nachbau braucht es eine Entscheidung |
| Surveys | Microsoft Forms | **Offen:** Forms ist ein Webdienst ohne Windows-App |
| Resources | Excel | |
| Streaming | YouTube Studio | **Offen:** YouTube Studio ist ein Webdienst ohne Windows-App; sein Live Control Room ist die Referenz |
| Store | Microsoft Store | |
| Start | Startmenü und Widgets | |
| Identity | Einstellungen > Konten, plus Windows Hello | Eine Einstellungsseite, kein Programm |
| History | keines | Keine Vorlage |

**Regel für Vorlagen (Eigentümer, 2026-11-10, immer gültig):** Die Vorlage einer Kategorie ist das Programm mit den besten
Funktionen, der besten Bedienbarkeit und Oberfläche, ob Open Source, nur Web oder eingestellt. Wir suchen, was Open Source
**nicht** hat; die Funktionen aus Open Source kommen obendrauf. Recherche für Whiteboard, Umfragen, Studio/Streaming und
Videos läuft (alle bekannten Programme je Kategorie, dann eine Empfehlung). **Gallery** zeigt lokale Dateien und entfernte
Quellen (YouTube, Vimeo, Odysee, PeerTube) über eine Anbieter-Schnittstelle, wie KIs bei People; **Studio** (Facette von
`fs-streaming`) ist Live-Produktion (OBS, Restream, StreamYard, vMix). ADR 0066.

## Basistypen (erste Liste)

| Basistyp | Standard | Verwendet von |
|----------|----------|---------------|
| Text, mehrzeiliger Text | – | alle |
| Formatierter Text | RFC 9073 `STYLED-DESCRIPTION`, eigenes Textmodell (ADR 0031) | wiki, tasks, messages |
| E-Mail-Adresse | RFC 5322, JSContact `EmailAddress` | people, messenger, identity, groups |
| Telefonnummer | E.164, JSContact `Phone` | people |
| Online-Dienst, Benutzername | JSContact `OnlineService` | people, messenger |
| Link | RFC 3986, JSContact `Link` | alle |
| Name einer Person | JSContact `Name` mit `components[]` | people, identity |
| Postanschrift | JSContact `Address` | people, maps, resources |
| Ort | `geo:`-URI (RFC 5870), GeoJSON | maps, calendar, people, files |
| Datum, Datum und Uhrzeit, Zeitzone | RFC 3339, JSCalendar `LocalDateTime`, IANA-Zonen | calendar, tasks, history |
| Dauer, Wiederholung | JSCalendar `Duration`, `RecurrenceRule` | calendar, tasks |
| Sprache | BCP 47 (RFC 5646) | alle |
| Menge, Geld | UCUM, ISO 4217 | resources |
| Farbe | CSS Color 4 | alle |
| Bild, Ton, Video | AS2 `Image`/`Audio`/`Video`, Medientypen | people, files, messenger |
| Öffentlicher Schlüssel | OpenPGP-Fingerabdruck, JSContact `CryptoKey` | people, identity |
| Status, Priorität, Auswahl | JSCalendar-Aufzählungen, eigene Listen | tasks, surveys |
| Schlagwörter | JSContact `keywords`, JSCalendar `keywords` | alle |
| Verweis auf ein Objekt | AS2 `id` (IRI) | alle; zeigt die *compact*-Komponente des Ziels |

## Programme

| Programm | Besitzt (Standard) | Nutzt | Facetten (vorgeschlagen) | Suiten | Analysierte Programme (Funktionen) |
|----------|--------------------|-------|--------------------------|--------|------------------------------------|
| `fs-people` | `Person` (JSContact `Card`) | groups, files | Contacts, Users, AIs, Partners, Team, Members | Groupware, CRM, Democracy | GNOME Contacts, KAddressBook, Monica, Nextcloud Contacts |
| `fs-groups` | `Group`, Mitgliedschaft (AS2, SCIM) | people | Groups | alle | **keines analysiert** |
| identity (`fs-identity`) | Konto, Anmeldung (Kanidm-Hülle) | people | Users (mit people) | alle | **keines analysiert** |
| `fs-vault` | Geheimnis: Passwort, Passkey, TOTP, Schlüssel (CXF, Secret Service) | people, groups | Passwords, Keys | alle | zu recherchieren: 1Password, Apple Passwords, Bitwarden, KeePassXC (ADR 0067) |
| `fs-messenger` | `Message`, Unterhaltung (AS2, JMAP Mail, MIMI) | people, files | Mail, Chat, Assistant, evtl. Forum | Groupware, CRM, Helpdesk | Thunderbird, Element, Telegram, Kontact, Apple Mail, Outlook, Discord, Mastodon |
| `fs-calendar` | `Event` (JSCalendar) | people, maps, resources | Calendar, Booking | Groupware, Project mgmt | Merkuro, Google Calendar, Nextcloud Calendar, Outlook Calendar, Planner, DAViCal |
| `fs-tasks` | `Task` (JSCalendar, RFC 9253) | people, calendar, groups | To-dos, Tickets | Project mgmt, Helpdesk | Planka, OpenProject, Taiga, Trello, Wekan, Redmine, Jira, Asana |
| `fs-files` | `Document`, Datei (AS2) | people, groups | Files, Gallery, Music, Videos, Documents | Media, alle | Nautilus, Dolphin, Seafile, Nextcloud Files; Galerie: Immich, PhotoPrism, Lychee, Piwigo |
| `fs-wiki` | Text, Seite (eigene Spezifikation, ADR 0031) | files, people | Wiki, Notes | Groupware, Democracy | Wiki.js, MediaWiki, XWiki, Notion, Confluence |
| `fs-maps` | Ort (GeoJSON) | people, calendar | Maps | Groupware | Organic Maps, OsmAnd, uMap, QGIS |
| `fs-history` | Aktivität (AS2) | alle | Timeline | Project mgmt | **keines analysiert** |
| `fs-resources` | Ressource, Bedarf (Lücke, eigene Spezifikation) | people, calendar | Inventory, Booking (mit calendar) | ERP, Project mgmt, Democracy | ERP: Dolibarr, ERPNext, Odoo, Tryton |
| `fs-surveys` | `Question`, Stimme (AS2, Lücke) | people, groups | Polls, Votes | Democracy, Project mgmt | Decidim, Polis, LiquidFeedback, Consul, adhocracy+ |
| `fs-whiteboard` | Board (Lücke, eigene Spezifikation) | files | Whiteboard | Project mgmt | Excalidraw, tldraw, draw.io, OpenBoard |
| `fs-streaming` | Stream (WHIP/WHEP) | files | Studio (Live-Produktion und Live-Schnitt), Live | Media | OBS Studio, Restreamer, MediaMTX |
| `fs-store` (der Store) | Katalogeintrag, Paket (TUF) | – | Store | – | **keines analysiert** |
| desktop | – (Startseite, nutzt alle) | alle | Start | – | Homarr, Dashy, Homepage, Heimdall |

Plattform ohne eigenes Frontend: `fs-objects` (Aufbewahrung von Objekten), `fs-hub` (Austausch zwischen Programmen auf einem
Gerät), `fs-interfaces` (Verträge), `fs-components` (Komponenten und Stile), `fs-release`, `fs-capnpc`.

## Suiten

| Suite | Programme |
|-------|-----------|
| Groupware | people, messenger, calendar, wiki, maps, files |
| Projektmanagement | tasks, history, resources, surveys, whiteboard, wiki, groups |
| Democracy | surveys, groups, wiki, messenger, tasks, resources |
| Helpdesk | tasks (Tickets), messenger, people, wiki — analysiert: Zammad, osTicket, GLPI, Request Tracker |
| CRM | people (Partners), messenger, tasks, calendar — analysiert: EspoCRM, SuiteCRM, CiviCRM |
| ERP | resources, people, tasks — analysiert: Dolibarr, ERPNext, Odoo |
| Media | files (Gallery), streaming |
| Marketplace | später |

## Querschnittsziele (Eigentümer, 2026-11-09)

1. **Befehlspalette** über alle Programme; die Befehle kommen aus den Typbeschreibungen (gesehen bei Raycast, Linear).
2. **Eingabe in Alltagssprache** für Termine, Aufgaben und Kontakte ("Mittagessen mit Ana Fr 13 Uhr"; Fantastical, Things, Todoist).
3. **Typisierte Notizen:** ein Schlagwort macht aus einer Notiz einen Datentyp mit Feldern (Tana-Supertags, Frappe DocTypes; bestätigt ADR 0066).
4. **Screener:** Jemand Neues erreicht dich erst, nachdem du ihn zugelassen hast, für Mail und Chat (HEY).
5. **Anleitungen als Befehle aufgezeichnet** und das **Wiki überall einbettbar** (Tango; siehe Wiki-Anforderungen).
6. **Gemeinsam entscheiden** mit den Verfahren in den Democracy-Anforderungen (Polis, Loomio, systemisches Konsensieren,
   wachsender Abstimmungsradius).

## Funktionsreferenzen (geprüft 2026-11-10, Sprint-Runde 3)

Programme, deren Macher weiter gedacht haben als die übrigen. Wir übernehmen Ideen, nie Code oder Aussehen (ADR 0025).

Von Thread F gegen Web-Quellen geprüft (Sprint-Runde 3, 2026-11-10). Die Quellen jedes Programms stehen in seiner
`index.md` (in der letzten Spalte verlinkt). ✅ an der Primärquelle bestätigt · ⚠️ nicht vollständig bestätigt (ein
Suchergebnis, Drittquelle oder nicht lesbar) · ❌ nicht mehr vorhanden. Korrekturen sind mit **Corrected** markiert. In
diesem Lauf nicht geprüft: Immich.

| Bereich | Programme und ihre herausragende Idee | Prüfung (2026-11-10) |
|---------|---------------------------------------|----------------------|
| People | Monica: Erinnerungen, "last spoke", Aktivitäten; ein Tagebuch für Lebensereignisse; v3 für 2026 angekündigt · Google Contacts: Zusammenführungsvorschläge ("Merge & fix", innerhalb eines Kontos) · **Corrected:** Apple Contacts: NameDrop (iOS 17) | ✅ [people](apps/people/frontends/index.md) · Monica ⚠️ Lebensereignisse (nur README) |
| Mail | HEY: Screener, Imbox/Feed/Paper Trail · Superhuman Mail: Tastatur, geteilter Posteingang (eine geteilte Liste, kein gemeinsamer Posteingang) · Spark: Team-Kommentare zu einer Mail · Fastmail: maskierte Adressen · Delta Chat: Chat über E-Mail | ✅ [messenger](apps/messenger/frontends/index.md) · Superhuman ⚠️ **Corrected:** Grammarly hat Superhuman Mail 2025 übernommen und die Firma in Superhuman umbenannt (ein Suchergebnis) |
| Chat | Zulip: ein Thema für jede Nachricht · Signal: keine herausragende Funktion genannt; Protokolldokumente (PQXDH, Double Ratchet) · Telegram: Themen, geplante Nachrichten · Discord: Rollen je Kanal; spontane Sprachräume ⚠️ (nicht geprüft) · Element: Spaces, Brücken | ✅ [messenger](apps/messenger/frontends/index.md) · Discord ⚠️ Sprachräume |
| Calendar | Fantastical: Eingabe in Alltagssprache ⚠️ (Details aus einem Drittanbieter-Leitfaden von 2019) · Notion Calendar: Zeitzonen nebeneinander, freie Zeitfenster teilen · Cal.com: Buchungsseiten · Reclaim, Motion: Aufgaben in freie Zeit gelegt | ✅ [calendar](apps/calendar/frontends/index.md) · Fantastical ⚠️ |
| Tasks | Things 3: Heute / Heute Abend / Irgendwann, schnelle Eingabe (⚠️ Tastenkürzel nicht geprüft) · OmniFocus: Perspektiven, Überprüfung (v4) · Todoist: Filtersprache · Linear: Triage, Zyklen; ⚠️ "Geschwindigkeit" nicht geprüft · Taskwarrior: berechnete Dringlichkeit (v3.5.0) | ✅ [tasks](apps/tasks/frontends/index.md) · Linear ⚠️ Geschwindigkeit |
| Files | Dolphin: geteilte Ansicht, Terminal-Bereich, Orte · **Corrected:** Dienstmenüs nur in den KDE-Entwicklerdokumenten, nicht im Handbuch · Finder: Quick Look · Everything: sofortige Namenssuche (NTFS-Journal, nur Windows) · Dropbox: Dateianfragen (Absender braucht kein Konto) · Seafile: clientseitig verschlüsselte Bibliotheken ⚠️ (nur Desktop-Client; Dateinamen nicht verschlüsselt) · Syncthing: Gerät-zu-Gerät-Synchronisation | ✅ [files](apps/files/frontends/index.md) · Dolphin ⚠️ Dienstmenüs · Seafile ⚠️ |
| Gallery | Immich: Suche in Alltagssprache, Gesichter, Karte, Teilen mit Partnern (noch nicht geprüft) · Apple Fotos: Duplikate (Album ab macOS Ventura) · **Corrected:** Text in Bildern nicht bestätigt (⚠️) | ✅ [gallery](apps/gallery/frontends/index.md) · Immich offen · Apple Fotos ⚠️ Text |
| Wiki, Notizen | Tango: Anleitungen aus Klicks (**Corrected:** das Produkt ist tango.ai) · Tana: Supertags mit Vererbung und Tabellenansicht · Obsidian: Rückverweise, Canvas · Logseq: Blockverweise ⚠️ (nur Forenquelle) · Notion: Datenbanken in Seiten | ✅ [wiki](apps/wiki/frontends/index.md) · Logseq ⚠️ |
| Maps | Google Earth: 3D-Globus; Projekte (eigene, teilbare Karten), Messen, Höhenprofil (2026) · geführte Touren ⚠️ (nur für den Start 2017 bestätigt) · **Corrected:** Street View ist eine Funktion von Google Maps/Earth, kein Programm (Entscheidung offen) · OsmAnd: offline; Höhenlinien nur mit kostenpflichtigem Plugin · Organic Maps · uMap · Felt: gleichzeitiges Bearbeiten | ✅ [maps](apps/maps/frontends/index.md) · Google Earth ⚠️ Touren · OsmAnd ⚠️ Höhenlinien |
| History | Day One: Ort und Wetter, "An diesem Tag" (auch im Web seit 2025-09) · ActivityWatch: automatisch, lokal (v0.14.1) · Exist.io: Zusammenhänge; Dienst noch online | ✅ [history](apps/history/frontends/index.md) |
| Resources, ERP | ERPNext/Frappe: DocTypes erzeugen Liste und Formular · **Corrected:** SAP Fiori ist ein Designsystem, kein Programm (nicht analysiert) · Odoo: verknüpfte Module ⚠️ (indirekter Beleg) · Grocy: Haushaltsbestand · Snipe-IT: Ausgabe und Rücknahme (Verbrauchsgüter kommen nie zurück) | ✅ [resources](apps/resources/frontends/index.md) · Odoo ⚠️ |
| Decisions | Polis: aktiv (Commits Nov 2026) · Loomio: aktiv (v3.15.0) · LiquidFeedback: Delegation ✅, **Corrected:** kein Release seit Core 4.2.2 (2021), es stockt · Decidim: Beteiligungsräume mit Komponenten (v0.32.2) · Consul: 2.6.1 · dieBasis-Verfahren sind Verfahren, keine Software (siehe Democracy-Anforderungen) | ✅ [surveys](apps/surveys/frontends/index.md) · LiquidFeedback stockt |
| Whiteboard | tldraw ⚠️ "Gefühl" ist subjektiv; Fakten: React-SDK, unendliche Fläche · Excalidraw: handgezeichnet; **Corrected:** Ende-zu-Ende-Verschlüsselung nur in der gehosteten App, nicht im npm-Paket · FigJam: Sticker, Timer, Abstimmung mit Stimmen erst am Ende sichtbar | ✅ [whiteboard](apps/whiteboard/frontends/index.md) · tldraw ⚠️ |
| Streaming | OBS Studio: Szenen · YouTube Studio: Live-Kontrollraum, Auswertung danach · StreamYard: Gäste im Browser · Ecamm Live: nur Mac ⚠️ (Drittquelle) · Owncast: ActivityPub · PeerTube: AGPL-3.0, ActivityPub, P2P-Live | ✅ [streaming](apps/streaming/frontends/index.md) · Ecamm Live ⚠️ |
| Store | F-Droid: Anti-Feature-Kennzeichen, reproduzierbare Builds · Obtainium: Installation direkt aus Git-Releases · Flathub: verifizierte Herausgeber (Prüfung des App-ID-Besitzes) | ✅ [store](apps/store/frontends/index.md) |
| Start | Raycast: eine Palette für alles · Alfred: Palette, Workflows (⚠️ nur macOS nicht ausdrücklich genannt) · KDE Plasma: Aktivitäten mit eigenen Favoriten, Widgets, Hintergrund, Fensterregeln; Energie und Leisten gelten für alle (informelle Quellen ⚠️) | ✅ [desktop](platform/desktop/frontends/index.md) · Alfred ⚠️ |
| Helpdesk | Chatwoot: alle Kanäle in einem Posteingang, Website-Widget · **Corrected:** Zammad hat ein CTI-Anrufprotokoll (Placetel, sipgate, generische CTI-API), kein eigenes SIP; Warnung bei Bearbeitungskonflikten · Help Scout: Kundenseitenleiste | ✅ [helpdesk](apps/helpdesk/frontends/index.md) · Zammad korrigiert |
| CRM | Twenty: eigene Objekte und Felder (Lizenz aus einer Drittquelle ⚠️) · Attio: Anreicherung | ✅ [crm](suites/crm/frontends/index.md) · Twenty Lizenz ⚠️ |
| Workflows | n8n: Knoten-Leinwand, Code-Knoten (Anzahl der Integrationen widersprüchlich: 400+ vs. 1500+) · Huginn: Agenten und Ereignisse · Windmill: Skripte werden zu Formularen, Endpunkten und Jobs · Apple Kurzbefehle: persönliches Gerätewerkzeug · Power Automate: gehostetes Produkt | ✅ [workflows](suites/workflows/frontends/index.md) · n8n-Anzahl offen |
| Marketing | Plausible: ohne Cookies, Trichter, Statistik-API · Umami: ohne Cookies, Trichter, Verweildauer, Reisen · Listmonk: Newsletter-Verwaltung (AGPL-3.0) | ✅ [marketing](apps/marketing/frontends/index.md) |

## Offene Punkte dieses Entwurfs

1. **Marketing** (analysiert: Matomo, Plausible, Mautic): eigenes Programm mit eigenen Daten, oder eine Suite über messenger und people?
2. **Workflows** (analysiert: n8n, Node-RED): ein Programm, das Workflow-Definitionen besitzt (Standardkandidat: CNCF
   Serverless Workflow, BPMN), oder später?
3. **Helpdesk**: Suite wie oben vorgeschlagen, oder eigenes Programm?
4. **Groups, identity**: noch keine Referenzprogramme analysiert; Haiku recherchiert Kandidaten. History und Store haben ihre ersten Analysen (2026-11-10).
5. **Stile**: die ersten vier sind durch die Frontends festgelegt: *Admin* (dicht), *Simple* (groß), *Apple* (runde Ecken,
   Glas), *Windows* (flach, Fluent-Abstände). Jeder mit einem eigenen Icon-Satz. Weitere können folgen.
