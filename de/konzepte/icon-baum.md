# Icon-Baum

[← Zurück zum Index](../INDEX.md) | [Icon-System](icon-system.md) | [Themes](themes.md)

---

## Grundprinzip

Der Icon-Baum ist nach **Ontologie** organisiert — was eine Sache ist, nicht wie sie benutzt wird.
Die Verwendung (Action vs. Identity) regelt das Dual-Icon-System.

Jede Gruppe hat:
- Einen **Namen** und eine **Begründung** warum sie existiert
- Eine klare **Abgrenzung** zu anderen Gruppen
- Dokumentierte **Einzelicons** mit Bedeutung und Einzahl/Mehrzahl

---

## Baumstruktur

```
icons/
│
│  ── Digital ──────────────────────────────────────────────────
├── places/          — Orte, Standorte, Umgebungen
├── people/          — Personen, Rollen, soziale Einheiten
├── things/          — Digitale Objekte und Artefakte
├── actions/         — Was man tun kann
├── states/          — Zustände und Status
├── time/            — Zeit und Planung
├── communication/   — Austausch und Verbindung
├── data/            — Daten, Strukturen, Visualisierung
├── security/        — Schutz und Zugriffsrechte
├── media/           — Medien und Inhaltsformen
│
│  ── Realwelt ──────────────────────────────────────────────────
├── professions/     — Berufe und Tätigkeitsfelder
├── attributes/      — Qualitative Eigenschaften (selbst-deklariert)
├── certifications/  — Formale Siegel und Zertifikate (von Dritten)
├── commerce/        — Handel, Kauf und Wirtschaft
├── nature/          — Natürliche Objekte und Lebewesen
├── education/       — Lernen, Qualifikationen, Wissen
├── health/          — Gesundheit und Medizin
├── transport/       — Bewegung, Logistik, Lieferung
│
│  ── System ────────────────────────────────────────────────────
├── programs/        — FreeSynergy-Programme
└── engines/         — Konkrete Implementierungen (Drittanbieter)
```

---

## places/ — Orte und Umgebungen

**Warum diese Gruppe:** Menschen denken räumlich. Ein Ort ist etwas wo man *ist* oder *hingeht*,
kein Zustand und keine Handlung. Orte sind stabil — sie verändern sich nicht durch Interaktion.

**Abgrenzung:** `programs/` enthält Programme als Konzept; `places/` enthält Orte auch wenn
ein Programm denselben Namen hat. `home` ist ein Ort, nicht ein Programm.

| Icon | Einzahl | Mehrzahl | Bedeutung |
|---|---|---|---|
| `home` | Zuhause | — | Persönliches Home-Verzeichnis oder Startseite |
| `server` | Server | `servers` | Ein Rechner/Dienst-Host |
| `node` | Node | `nodes` | FreeSynergy-Node (Serverinstanz) |
| `network` | Netzwerk | `networks` | Verbundene Infrastruktur |
| `building` | Gebäude | `buildings` | Physischer Standort, Organisation |
| `city` | Stadt | `cities` | Geographische Ortsangabe |
| `country` | Land | `countries` | Geographische Länderangabe |
| `folder` | Ordner | `folders` | Verzeichnis im Dateisystem |
| `cloud` | Cloud | — | Entfernter Speicher oder Dienst |
| `desktop` | Desktop | — | Die Arbeitsoberfläche des Nutzers |
| `workspace` | Arbeitsbereich | `workspaces` | Virtueller Arbeitsbereich / Projekt |

---

## people/ — Personen und soziale Einheiten

**Warum diese Gruppe:** Menschen sind keine Objekte und keine Orte. Sie haben Rollen,
Berechtigungen und Identitäten. Diese Gruppe trennt klar zwischen "wer" und "was".

**Abgrenzung:** Ein Bot ist kein Mensch — Bots gehören in `programs/`. Ein Team ist eine
Sammlung von Personen, nicht ein Ort.

| Icon | Einzahl | Mehrzahl | Bedeutung |
|---|---|---|---|
| `person` | Person | `people` | Eine einzelne Person, Nutzer-Profil |
| `user` | Nutzer | `users` | Nutzer im System-Kontext (technisch) |
| `admin` | Admin | `admins` | Administrativer Nutzer |
| `guest` | Gast | `guests` | Nicht authentifizierter oder temporärer Nutzer |
| `team` | Team | `teams` | Gruppe mit gemeinsamer Aufgabe |
| `group` | Gruppe | `groups` | Sammlung von Personen (ohne feste Aufgabe) |
| `role` | Rolle | `roles` | Berechtigungs-Rolle |
| `contact` | Kontakt | `contacts` | Adressbuch-Eintrag |
| `owner` | Eigentümer | — | Wer etwas besitzt oder verantwortet |

---

## things/ — Digitale Objekte und Artefakte

**Warum diese Gruppe:** Dinge sind das was Nutzer bearbeiten, speichern und teilen.
Sie sind die Hauptobjekte der Arbeit — keine Aktionen, keine Personen, keine Orte.

**Abgrenzung:** `data/` enthält Strukturen und Visualisierungen; `things/` enthält
die Objekte selbst. Eine Datei ist ein Ding; eine Tabelle ist eine Datenstruktur.

| Icon | Einzahl | Mehrzahl | Bedeutung |
|---|---|---|---|
| `file` | Datei | `files` | Eine einzelne Datei |
| `document` | Dokument | `documents` | Textbasiertes Dokument |
| `package` | Paket | `packages` | Installiertes oder installierbares Paket |
| `container` | Container | `containers` | Laufende Container-Instanz |
| `image` | Image | `images` | Container-Image oder Disk-Image |
| `plugin` | Plugin | `plugins` | Erweiterungsmodul |
| `theme` | Theme | `themes` | Design-Paket |
| `icon-set` | Icon-Set | `icon-sets` | Sammlung von Icons |
| `cursor-set` | Cursor-Set | `cursor-sets` | Sammlung von Mauszeigern |
| `backup` | Backup | `backups` | Datensicherung |
| `link` | Link | `links` | Verweis auf eine Ressource |
| `token` | Token | `tokens` | Auth-Token, API-Key |

---

## actions/ — Was man tun kann

**Warum diese Gruppe:** Aktionen beschreiben Verben — was der Nutzer oder das System tut.
Sie sind die häufigsten Icons in Menüs und Buttons.

**Abgrenzung:** `states/` beschreibt wie etwas ist; `actions/` beschreibt was man damit tut.
"Error" ist ein Zustand; "Löschen" ist eine Aktion.

| Icon | Einzahl | Bedeutung |
|---|---|---|
| `add` | Hinzufügen | Neues Objekt erstellen oder hinzufügen |
| `edit` | Bearbeiten | Bestehendes Objekt ändern |
| `delete` | Löschen | Objekt entfernen (reversibel möglich) |
| `save` | Speichern | Zustand persistieren |
| `search` | Suchen | In Daten suchen |
| `filter` | Filtern | Ansicht einschränken |
| `sort` | Sortieren | Reihenfolge ändern |
| `refresh` | Aktualisieren | Daten neu laden |
| `sync` | Synchronisieren | Mit entferntem System abgleichen |
| `send` | Senden | Nachricht oder Daten übertragen |
| `share` | Teilen | Objekt anderen zugänglich machen |
| `copy` | Kopieren | Objekt duplizieren |
| `move` | Verschieben | Objekt an anderen Ort bringen |
| `open` | Öffnen | Programm oder Datei starten |
| `close` | Schließen | Programm oder Fenster beenden |
| `install` | Installieren | Paket einrichten |
| `uninstall` | Deinstallieren | Paket entfernen |
| `start` | Starten | Dienst oder Prozess beginnen |
| `stop` | Stoppen | Dienst oder Prozess beenden |
| `restart` | Neustarten | Dienst oder Prozess neu starten |
| `configure` | Konfigurieren | Einstellungen öffnen |
| `import` | Importieren | Externe Daten einlesen |
| `export` | Exportieren | Daten ausgeben |
| `download` | Herunterladen | Von Netz laden |
| `upload` | Hochladen | Ins Netz laden |
| `login` | Anmelden | Session starten |
| `logout` | Abmelden | Session beenden |
| `back` | Zurück | Vorherigen Schritt gehen |
| `forward` | Vorwärts | Nächsten Schritt gehen |

---

## states/ — Zustände und Status

**Warum diese Gruppe:** Zustände beschreiben wie etwas ist — nicht was es ist und nicht was
man damit tut. Sie erscheinen als Status-Indikatoren, Badges und Warnungen.

| Icon | Bedeutung |
|---|---|
| `active` | Läuft, aktiv, verfügbar |
| `inactive` | Gestoppt, inaktiv |
| `loading` | Wird geladen, in Bearbeitung |
| `success` | Erfolgreich abgeschlossen |
| `warning` | Warnung, Aufmerksamkeit nötig |
| `error` | Fehler, Aktion fehlgeschlagen |
| `info` | Neutral-Information |
| `new` | Neu, noch nicht gesehen |
| `draft` | Entwurf, unveröffentlicht |
| `locked` | Gesperrt, kein Zugriff |
| `unlocked` | Entsperrt, Zugriff möglich |
| `pinned` | Angepinnt, fixiert |
| `starred` | Favorisiert, markiert |
| `hidden` | Ausgeblendet |
| `archived` | Archiviert |
| `deprecated` | Veraltet, wird entfernt |

---

## time/ — Zeit und Planung

**Warum diese Gruppe:** Zeit ist eine eigene Dimension. Zeitobjekte (Kalender, Uhr)
und zeitliche Konzepte (Verlauf, Plan) gehören zusammen.

| Icon | Einzahl | Mehrzahl | Bedeutung |
|---|---|---|---|
| `calendar` | Kalender | — | Datum-Auswahl oder Kalenderansicht |
| `clock` | Uhr | — | Uhrzeit, Timer |
| `schedule` | Zeitplan | `schedules` | Geplante Ausführungen |
| `history` | Verlauf | — | Vergangene Ereignisse |
| `deadline` | Frist | `deadlines` | Ablaufdatum |
| `duration` | Dauer | — | Zeitspanne |
| `recurrence` | Wiederholung | — | Wiederkehrende Aufgabe/Ereignis |

---

## communication/ — Austausch und Verbindung

**Warum diese Gruppe:** Kommunikation ist der Austausch zwischen Personen oder Systemen.
Diese Gruppe trennt klar von `actions/` (was man tut) und `things/` (was entsteht).

| Icon | Einzahl | Mehrzahl | Bedeutung |
|---|---|---|---|
| `message` | Nachricht | `chat` | Eine Nachricht / Konversationsverlauf |
| `email` | E-Mail | `emails` | Elektronische Post |
| `notification` | Benachrichtigung | `notifications` | System-Hinweis |
| `feed` | Feed | `feeds` | Aktivitätsstrom |
| `comment` | Kommentar | `comments` | Anmerkung zu einem Objekt |
| `mention` | Erwähnung | `mentions` | @-Erwähnung |
| `call` | Anruf | — | Sprach- oder Videoverbindung |
| `broadcast` | Broadcast | — | Nachricht an viele |
| `webhook` | Webhook | `webhooks` | Automatische HTTP-Benachrichtigung |

---

## data/ — Daten, Strukturen, Visualisierung

**Warum diese Gruppe:** Datenstrukturen und ihre Visualisierung sind keine Dinge die man
"besitzt" (wie Dateien), sondern Arten wie Information organisiert und dargestellt wird.

| Icon | Einzahl | Bedeutung |
|---|---|---|
| `database` | Datenbank | Persistenter strukturierter Speicher |
| `table` | Tabelle | Tabellarische Darstellung |
| `list` | Liste | Geordnete oder ungeordnete Auflistung |
| `tree` | Baum | Hierarchische Struktur |
| `chart` | Diagramm | Visuelle Daten-Darstellung |
| `graph` | Graph | Vernetzte Knoten-Darstellung |
| `form` | Formular | Eingabemaske für Daten |
| `field` | Feld | Einzelnes Eingabefeld |
| `tag` | Tag | Markierung/Label |
| `category` | Kategorie | Klassifizierung |
| `namespace` | Namespace | Namensraum |
| `api` | API | Programmierschnittstelle |

---

## security/ — Schutz und Zugriffsrechte

**Warum diese Gruppe:** Sicherheit ist ein eigenständiges Konzept. Alles was mit Zugang,
Schutz und Verifizierung zu tun hat, gehört hierher — nicht in `things/` oder `actions/`.

| Icon | Bedeutung |
|---|---|
| `lock` | Gesperrt, verschlüsselt |
| `unlock` | Entsperrt, zugänglich |
| `key` | Zugangsschlüssel, Passwort |
| `shield` | Schutz, Sicherheit allgemein |
| `fingerprint` | Biometrische Authentifizierung |
| `certificate` | TLS-Zertifikat, Signatur |
| `permission` | Berechtigung |
| `audit` | Prüfung, Log |
| `2fa` | Zwei-Faktor-Authentifizierung |
| `vpn` | Verschlüsselte Netzwerkverbindung |

---

## media/ — Medien und Inhaltsformen

**Warum diese Gruppe:** Medien sind Inhalte die angezeigt, abgespielt oder gelesen werden.
Sie sind keine generischen Dateien (`things/`) — sie haben Formatcharakter.

| Icon | Einzahl | Mehrzahl | Bedeutung |
|---|---|---|---|
| `photo` | Foto | `photos` | Bild/Foto |
| `video` | Video | `videos` | Videodatei oder -stream |
| `audio` | Audio | — | Audiodatei oder -stream |
| `document` | Dokument | `documents` | Textbasierter Inhalt |
| `code` | Code | — | Quellcode |
| `terminal` | Terminal | — | Kommandozeilen-Oberfläche |
| `markdown` | Markdown | — | Markdown-formatierter Text |
| `pdf` | PDF | `pdfs` | PDF-Dokument |
| `presentation` | Präsentation | `presentations` | Folien-Dokument |
| `spreadsheet` | Tabellenkalkulation | — | Berechnungs-Dokument |

---

## programs/ — FreeSynergy-Programme

**Warum diese Gruppe:** FreeSynergy-Programme sind konzeptuelle Werkzeuge — kein
Drittanbieter-Produkt. `browser` ist das Konzept Browser, nicht Firefox.
Drittanbieter-Icons für konkrete Implementierungen gehören in `engines/`.

| Icon | Bedeutung |
|---|---|
| `browser` | Web-Browser (Engine-unabhängig) |
| `store` | Paket-Manager/Store |
| `desktop` | Desktop-Shell |
| `terminal` | Terminal-Emulator |
| `settings` | Einstellungen eines Programms |
| `lenses` | Aggregierte Daten-Ansichten |
| `tasks` | Automatisierungs-Pipeline |
| `ai` | KI-Assistent |
| `bots` | Bot-Manager |
| `container` | Container-Manager |
| `builder` | Paket-Ersteller |
| `theme` | Theme-Manager |
| `icons` | Icon-Manager |
| `language` | Sprach-Manager |
| `auth` | Authentifizierungs-Manager |
| `node` | FreeSynergy.Node-Server |
| `inventory` | Installiertes verwalten |
| `registry` | Dienste-Verzeichnis |
| `session` | Session-Verwaltung |
| `federation` | Föderations-Verbindungen |
| `sync` | CRDT-Synchronisation |
| `search` | Suche |

---

## engines/ — Konkrete Implementierungen

**Warum diese Gruppe:** Eine Engine ist eine konkrete Drittanbieter-Technologie
die hinter einem FreeSynergy-Programm-Konzept steckt. Das Engine-Icon erscheint
als Identity-Icon wenn ein Objekt oder Programm diese Implementierung nutzt.

Das Firefox-Icon ist nicht das Browser-Icon — Firefox ist die Engine.

| Icon | Bedeutung |
|---|---|
| `firefox` | Gecko/SpiderMonkey Browser-Engine |
| `servo` | Servo Browser-Engine |
| `kanidm` | Kanidm Auth-Backend |
| `matrix` / `tuwunel` | Matrix-Homeserver |
| `stalwart` | Stalwart Mail-Server |
| `mistral` | Mistral.rs LLM-Engine |
| `ollama` | Ollama LLM-Runtime |
| `podman` | Podman Container-Engine |
| `docker` | Docker Container-Engine |
| `sqlite` | SQLite Datenbank-Engine |
| `postgres` | PostgreSQL Datenbank-Engine |

---

## professions/ — Berufe und Tätigkeitsfelder

**Warum diese Gruppe:** Ein Beruf ist weder eine Person noch ein Ort — er beschreibt die
gesellschaftliche oder wirtschaftliche Rolle einer Person oder Organisation.
Berufe sind fast immer **Identity-Icons**: sie sagen wer jemand ist, nicht was er gerade tut.

**Abgrenzung:** `people/` enthält die Person selbst (`person`, `user`); `professions/` enthält
die Rolle die sie ausübt. Ein Arzt ist `person` + `doctor`. Eine Arztpraxis ist `building` + `doctor`.

| Icon | Einzahl | Bedeutung |
|---|---|---|
| `baker` | Bäcker | Bäckerei, Bäcker-Beruf, Backwaren-Anbieter |
| `butcher` | Metzger | Fleischerei, Fleischer-Beruf |
| `farmer` | Bauer | Landwirt, Bauernhof |
| `chef` | Koch | Gastronomie, Restaurant, Caterer |
| `doctor` | Arzt | Medizinischer Beruf, Praxis, Klinik |
| `pharmacist` | Apotheker | Apotheke, Arzneimittel-Anbieter |
| `teacher` | Lehrer | Bildungseinrichtung, Lehrperson |
| `lawyer` | Anwalt | Rechtsberatung, Kanzlei |
| `engineer` | Ingenieur | Technischer Beruf, Konstruktion |
| `artist` | Künstler | Kreativberuf, Atelier, Galerie |
| `musician` | Musiker | Musik-Dienstleistung, Studio |
| `photographer` | Fotograf | Fotostudio, Bildproduktion |
| `developer` | Entwickler | Software-Entwicklung, IT-Dienstleistung |
| `designer` | Designer | Gestaltung, Agentur |
| `accountant` | Buchhalter | Steuerberatung, Finanzdienstleistung |
| `therapist` | Therapeut | Heilpraktiker, Therapieangebot |
| `trainer` | Trainer | Sport, Coaching, Fitness |
| `cleaner` | Reiniger | Reinigungsservice |
| `carpenter` | Schreiner | Handwerk, Holzverarbeitung |
| `electrician` | Elektriker | Elektroinstallation, Handwerk |
| `plumber` | Klempner | Sanitärinstallation, Handwerk |
| `tailor` | Schneider | Bekleidung, Maßanfertigung |
| `florist` | Florist | Blumengeschäft, Pflanzenbetrieb |
| `veterinarian` | Tierarzt | Tierklinik, Tiermedizin |

---

## attributes/ — Qualitative Eigenschaften

**Warum diese Gruppe:** Attribute beschreiben wie etwas ist — nicht was es ist und nicht was
man damit tut. Sie sind selbst-deklariert: ein Anbieter oder Produzent behauptet diese
Eigenschaft von seinem Produkt oder Betrieb, ohne dass ein Dritter sie bestätigt hat.

**Abgrenzung:** `certifications/` enthält formal bestätigte Siegel von Drittorganisationen.
`states/` enthält System-Zustände (`active`, `error`). `attributes/` ist für qualitative,
inhaltliche Beschreibungen der Realwelt.

| Icon | Einzahl | Bedeutung |
|---|---|---|
| `organic` | Bio | Biologisch angebaut / hergestellt, ohne Pestizide |
| `handmade` | Handgemacht | Manuell gefertigt, keine Massenproduktion |
| `local` | Lokal | Aus der Region, kurze Lieferwege |
| `seasonal` | Saisonal | Nur zur Saison verfügbar, keine Lagerware |
| `vegan` | Vegan | Keine tierischen Produkte oder Nebenprodukte |
| `vegetarian` | Vegetarisch | Kein Fleisch, aber tierische Nebenprodukte möglich |
| `gluten-free` | Glutenfrei | Ohne Gluten hergestellt |
| `lactose-free` | Laktosefrei | Ohne Laktose hergestellt |
| `sustainable` | Nachhaltig | Ressourcenschonend, zukunftsorientiert |
| `recycled` | Recycelt | Aus Recycling-Material hergestellt |
| `vinted` | Second-Hand | Gebraucht, wiederverwendet |
| `premium` | Premium | Hohe Qualitätsstufe (selbst-deklariert) |
| `fresh` | Frisch | Nicht gelagert, tagesfrisch |
| `raw` | Roh | Unverarbeitet, naturbelassen |
| `spicy` | Scharf | Enthält scharfe Zutaten |
| `allergen` | Allergen | Enthält bekannte Allergene |
| `limited` | Limitiert | Begrenzte Verfügbarkeit |
| `exclusive` | Exklusiv | Nur bei diesem Anbieter erhältlich |

---

## certifications/ — Formale Siegel und Zertifikate

**Warum diese Gruppe:** Zertifikate sind extern bestätigt — eine unabhängige Stelle hat die
Eigenschaft geprüft und offiziell vergeben. Das unterscheidet sie klar von `attributes/`.
Ein "Bio"-Siegel von Demeter ist etwas anderes als das Wort "Bio" auf einem Etikett.

**Abgrenzung:** `attributes/` = selbst-deklariert; `certifications/` = extern vergeben.
`security/` enthält technische Zertifikate (TLS, Signaturen); `certifications/` enthält
gesellschaftliche und wirtschaftliche Zertifikate.

| Icon | Einzahl | Bedeutung |
|---|---|---|
| `verified` | Verifiziert | Allgemeines Verifiziert-Siegel (von FreeSynergy oder Plattform) |
| `certified` | Zertifiziert | Allgemeines Zertifikat (ohne spezifische Stelle) |
| `official` | Offiziell | Staatlich oder behördlich anerkannt |
| `awarded` | Ausgezeichnet | Hat einen Preis oder eine Auszeichnung erhalten |
| `demeter` | Demeter | Biodynamische Landwirtschaft (Demeter e.V.) |
| `fairtrade` | Fairtrade | Fairer Handel, soziale Standards (Fairtrade International) |
| `iso` | ISO | ISO-Norm-Zertifizierung (Qualitätsmanagement etc.) |
| `gdpr` | DSGVO-konform | Datenschutz nach EU-Grundverordnung bestätigt |
| `accessibility` | Barrierefrei | Zugänglich für Menschen mit Einschränkungen |
| `press` | Presse | Akkreditierter Pressevertreter |
| `government` | Behörde | Staatliche Institution |
| `nonprofit` | Gemeinnützig | Als gemeinnützig anerkannte Organisation |

---

## commerce/ — Handel und Wirtschaft

**Warum diese Gruppe:** Handel ist ein eigenes Konzeptfeld — weder reine Aktion noch reines Objekt.
Kauf, Preis, Bestellung und Rechnung haben eine eigene Semantik die in Marktplätzen,
Organisationsprofilen und Produktdaten durchgängig auftaucht.

**Abgrenzung:** `actions/` enthält generische Aktionen (`add`, `delete`); `commerce/` enthält
wirtschaftliche Konzepte die immer mit Geld oder Tausch verbunden sind.

| Icon | Einzahl | Mehrzahl | Bedeutung |
|---|---|---|---|
| `price` | Preis | `prices` | Geldwert eines Produkts oder Angebots |
| `discount` | Rabatt | `discounts` | Preisreduktion |
| `offer` | Angebot | `offers` | Zeitlich oder mengenmäßig begrenzte Kondition |
| `cart` | Warenkorb | — | Aktiver Einkaufsvorgang |
| `order` | Bestellung | `orders` | Abgeschlossener Kaufvorgang |
| `invoice` | Rechnung | `invoices` | Zahlungsaufforderung |
| `receipt` | Quittung | `receipts` | Zahlungsbestätigung |
| `payment` | Zahlung | `payments` | Geldtransfer |
| `subscription` | Abo | `subscriptions` | Wiederkehrende Zahlung |
| `refund` | Erstattung | `refunds` | Rückzahlung |
| `store-front` | Laden | `stores` | Physisches oder digitales Geschäft |
| `market` | Markt | `markets` | Marktplatz (physisch oder digital) |
| `inventory-item` | Lagerbestand | — | Verfügbare Menge eines Produkts |
| `shipping` | Versand | — | Lieferung einer Bestellung |
| `tax` | Steuer | `taxes` | Abgabe auf Transaktion |
| `currency` | Währung | `currencies` | Geldeinheit |
| `review` | Bewertung | `reviews` | Nutzerbewertung eines Produkts oder Anbieters |

---

## nature/ — Natürliche Objekte und Lebewesen

**Warum diese Gruppe:** Mit der Realwelt kommen natürliche Objekte in die Plattform —
Zutaten, Pflanzen, Tiere, Terrain. Sie sind keine digitalen Artefakte (`things/`)
und keine Orte (`places/`), auch wenn Natur an Orten vorkommt.

**Abgrenzung:** `places/` enthält geographische Orte (`city`, `country`); `nature/` enthält
natürliche Objekte die an diesen Orten existieren. Ein Wald ist `nature/forest`;
ein Waldgebiet auf einer Karte könnte `places/` sein.

| Icon | Einzahl | Mehrzahl | Bedeutung |
|---|---|---|---|
| `plant` | Pflanze | `plants` | Allgemeine Pflanze, Gewächs |
| `tree` | Baum | `trees` | Baum (nicht Datenstruktur — Kontext entscheidet) |
| `flower` | Blume | `flowers` | Blütenpflanze |
| `herb` | Kraut | `herbs` | Küchen- oder Heilkraut |
| `animal` | Tier | `animals` | Allgemeines Tier |
| `pet` | Haustier | `pets` | Domestiziertes Tier |
| `fish` | Fisch | — | Fisch als Tier oder Lebensmittel |
| `ingredient` | Zutat | `ingredients` | Bestandteil eines Rezepts oder Produkts |
| `grain` | Getreide | — | Korn, Mehl, Getreideprodukte |
| `fruit` | Obst | — | Fruchterzeugnis |
| `vegetable` | Gemüse | — | Gemüseerzeugnis |
| `meat` | Fleisch | — | Fleischprodukt |
| `dairy` | Milchprodukt | `dairy-products` | Milch, Käse, Butter etc. |
| `water` | Wasser | — | Wasserquelle oder -produkt |
| `soil` | Boden | — | Erde, Ackerboden, Substrat |
| `weather` | Wetter | — | Wetterlage, Klimabedingung |
| `season` | Jahreszeit | `seasons` | Frühling, Sommer, Herbst, Winter |
| `forest` | Wald | `forests` | Waldgebiet |
| `field` | Feld | `fields` | Acker, Wiese (nicht Formularfeld — Kontext entscheidet) |
| `mountain` | Berg | `mountains` | Gebirge, Erhebung |
| `river` | Fluss | `rivers` | Fließgewässer |
| `ocean` | Meer | — | Meeresgebiet |

---

## education/ — Lernen, Qualifikationen und Wissen

**Warum diese Gruppe:** Bildung ist ein eigenständiges Themenfeld sobald Organisationen
(Schulen, Akademien, Kursanbieter) oder Personen (Lehrer, Schüler) in der Plattform auftauchen.
Lerninhalt, Abschluss und Institution sind konzeptuell verschieden.

**Abgrenzung:** `professions/` enthält den Beruf `teacher`; `education/` enthält das
was gelehrt oder gelernt wird und die Strukturen dafür. `certifications/` enthält Abschlüsse
die als Siegel gelten; `education/` enthält den Weg dorthin.

| Icon | Einzahl | Mehrzahl | Bedeutung |
|---|---|---|---|
| `course` | Kurs | `courses` | Lerneinheit, Kursangebot |
| `lesson` | Lektion | `lessons` | Einzelne Unterrichtseinheit |
| `curriculum` | Lehrplan | `curricula` | Gesamter Lehrinhalt eines Angebots |
| `qualification` | Qualifikation | `qualifications` | Nachgewiesene Fähigkeit |
| `degree` | Abschluss | `degrees` | Formaler Bildungsabschluss |
| `skill` | Fähigkeit | `skills` | Konkrete Fertigkeit |
| `school` | Schule | `schools` | Bildungseinrichtung allgemein |
| `university` | Universität | `universities` | Hochschuleinrichtung |
| `library` | Bibliothek | `libraries` | Wissenssammlung (physisch oder digital) |
| `book` | Buch | `books` | Lektüre, Lehrbuch |
| `quiz` | Quiz | `quizzes` | Lernkontrolle, Prüfungsfrage |
| `exam` | Prüfung | `exams` | Formale Leistungskontrolle |
| `student` | Schüler | `students` | Lernende Person |

---

## health/ — Gesundheit und Medizin

**Warum diese Gruppe:** Gesundheit ist ein Kernthema sobald medizinische Berufe,
Apotheken, Heilpraktiker oder gesundheitsbezogene Produkte in der Plattform erscheinen.
Die Konzepte (Diagnose, Therapie, Medikament) haben eine eigene Semantik.

**Abgrenzung:** `professions/` enthält `doctor`, `pharmacist`, `therapist` (die Person/Rolle);
`health/` enthält was diese Personen tun und womit sie arbeiten.
`attributes/` enthält Gesundheits-Eigenschaften wie `gluten-free`, `vegan`.

| Icon | Einzahl | Mehrzahl | Bedeutung |
|---|---|---|---|
| `medical` | Medizin | — | Allgemeines Medizin-Symbol (Kreuz) |
| `medication` | Medikament | `medications` | Arzneimittel, Präparat |
| `prescription` | Rezept | `prescriptions` | Ärztliche Verordnung |
| `diagnosis` | Diagnose | `diagnoses` | Festgestellte Erkrankung |
| `therapy` | Therapie | `therapies` | Behandlungsmaßnahme |
| `appointment` | Termin | `appointments` | Arzt- oder Behandlungstermin |
| `allergy` | Allergie | `allergies` | Bekannte Unverträglichkeit |
| `vaccination` | Impfung | `vaccinations` | Schutzimpfung |
| `wellness` | Wellness | — | Wohlbefinden, Prävention |
| `fitness` | Fitness | — | Körperliche Aktivität, Sport |
| `nutrition` | Ernährung | — | Ernährungsplan, Diät |
| `emergency` | Notfall | `emergencies` | Akuter medizinischer Notfall |
| `hospital` | Krankenhaus | `hospitals` | Medizinische Einrichtung (stationär) |
| `clinic` | Klinik | `clinics` | Medizinische Einrichtung (ambulant) |

---

## transport/ — Bewegung, Logistik und Lieferung

**Warum diese Gruppe:** Sobald physische Produkte gehandelt oder Dienstleistungen
vor Ort angeboten werden, spielt Transport eine Rolle. Lieferwege, Fahrzeuge,
Routen und Verfügbarkeit sind eigenständige Konzepte.

**Abgrenzung:** `commerce/shipping` beschreibt den Versandvorgang; `transport/` beschreibt
die Mittel und Strukturen dahinter. `places/` enthält Orte; `transport/` die Verbindungen
zwischen Orten.

| Icon | Einzahl | Mehrzahl | Bedeutung |
|---|---|---|---|
| `delivery` | Lieferung | `deliveries` | Physische Zustellung eines Produkts |
| `pickup` | Abholung | `pickups` | Selbstabholung beim Anbieter |
| `route` | Route | `routes` | Lieferpfad, Fahrweg |
| `vehicle` | Fahrzeug | `vehicles` | Allgemeines Transportmittel |
| `truck` | Lastwagen | `trucks` | Liefer-Fahrzeug |
| `bike` | Fahrrad | `bikes` | Fahrrad-Kurier, Lastenrad |
| `car` | Auto | `cars` | PKW, Personenbeförderung |
| `train` | Zug | `trains` | Schienen-Transport |
| `ship` | Schiff | `ships` | See-Transport |
| `plane` | Flugzeug | `planes` | Luft-Transport |
| `warehouse` | Lager | `warehouses` | Physisches Lagergebäude |
| `tracking` | Sendungsverfolgung | — | Status-Tracking einer Lieferung |
| `distance` | Entfernung | — | Räumlicher Abstand zwischen zwei Punkten |
| `radius` | Lieferradius | — | Maximale Lieferdistanz eines Anbieters |

---

## Regeln für neue Icons

1. **Gruppe zuerst** — zu welcher ontologischen Kategorie gehört das neue Konzept?
2. **Einzahl/Mehrzahl prüfen** — macht ein Plural-Icon semantisch Sinn?
3. **Begründung dokumentieren** — warum heißt es so? Was grenzt es ab?
4. **Kein Duplikat** — gibt es schon ein Icon das dieselbe Bedeutung hat?
5. **Kein Verwendungs-Icon** — Icons beschreiben was etwas ist, nicht wie es benutzt wird

---

Weiter: [Icon-System](icon-system.md) | [Themes](themes.md) | [Icon Manager](../programme/icons/README.md)
