# Architektur-Protokoll — Maske, Programm, Daten

Arbeitsdatei. **Nicht veröffentlicht** (Plan und Entwurf, siehe `conventions/CONVENTIONS.md` §1).
Zweck: Was in den Gesprächen ab dem 2026-11-03 feststeht, ist hier festgehalten, damit es nicht
wieder gefragt und wieder beantwortet werden muss. Wenn ein Punkt aus diesem Blatt in `docs/`
oder in einen ADR wandert, bleibt er hier stehen und bekommt einen Verweis.

Stand: 2026-11-03 · Quelle: Gespräch Nutzer ↔ Agent (Kalender-Fall → Masken-Modell → Datenhaltung)

Zweite Runde am selben Tag: Abgleich und Kollision, Schenken gegenüber Freigeben, „als frei
markieren", Gruppengröße. Antworten des Nutzers sind in **§15–§17** festgehalten; die daraus
entstandenen offenen Punkte stehen in §18, 11–19.

Dritte Runde, gleicher Tag: **Plan-Fragen** (Reihenfolge, Abbruchkriterium, Manifest, Register,
Code-Repos) mit nachgemessenem Ist-Zustand — **§19**.

Legende: **gesetzt** = entschieden, nicht mehr offen · **offen** = wartet auf Entscheidung ·
**Idee** = noch nicht geprüft · Belege wie in `data/standards.md` (✅ abgerufen, ⚠️ ungeprüft).

---

## 1. Status und Methode

- **Reihenfolge erst Doku, dann Programm.** Die Dokumentation ist das Mittel, um überhaupt
  herauszufinden, welche Funktionen die Programme brauchen. Deshalb werden zuerst die
  Oberflächen fremder Programme dokumentiert, nicht zuerst programmiert.
- **Alle Texte sind Platzhalter.** Was in `docs/` steht, ist eine Idee und wird mit jedem
  Durchlauf besser. Nichts davon ist verbindlich, bis es sortiert ist.
- **Skins/Schemata sind Anforderungsgewinnung**, nicht Zieloberfläche. Beim Lesen eines Skins
  werden zwei Listen gezogen: *welche Funktionen das Programm bieten muss* und *welche Daten
  es dafür braucht*. Schnittmenge aller Skins = **Pflichtmenge**, Vereinigung = **Kür**.
- **Programmiert wird erst, wenn das Bild Sinn ergibt.** Danach ggf. mit Opus, das sich die
  fertige Doku ansieht und verbessert — auch an anderen Programmen.
- **Grundmaske wird gebaut** (vom Nutzer). Sie ist die Referenzmaske: sie zeigt jede
  Fähigkeit, also ist sie der Beweis, dass eine Fähigkeit im Programm vorhanden und
  erreichbar ist. Was in der Grundmaske nicht geht, fehlt im Programm, nicht in der Maske.

## 2. Die Maske (bisher „Skin")

**gesetzt**

- Die Maske ist **pro Programm**, nicht pro Datensatz und nicht zur Laufzeit wählbar. Sie
  steht beim Start des Programms fest.
- Die Maske ist **austauschbar**. Gleiches Programm, andere Masche — „Outlook-Feel" für den
  Kalender, „Thunderbird-Feel" für Messages. Es bleibt dasselbe Programm.
- **Maske = UI/UX** (Menüs, Raumaufteilung, Interaktion, Tastenkürzel).
  **Theme = Farben, Abstände, Typografie.** Beides ist getrennt.
- Wächst einem Programm ein Feature, kann die Maske es einarbeiten — **muss aber nicht**.
- Der Begriff „Skin" trägt zu viel (wird als Farben gelesen). **Maske** für Struktur,
  **Theme** für Aussehen.

**Regeln, die daraus folgen**

- Die Maske entscheidet **nur über die Darstellung, nie über das Datenmodell.** Will eine
  Maske ein Modell, das das Programm nicht hat, ist sie kein Skin, sondern ein zweites
  Programm.
- Die Maske darf **keine Farben hartcodieren**, sie consumes Theme-Tokens. Sonst bricht das
  Theming pro Maske einzeln. (Farben stecken heute schon in `appearance.md` je Component —
  das ist die Theme-Ebene.)
- Die Maske baut aus den **Components** (primitives, widgets, workbenches) plus Blinc.
  Damit gilt: **Die Components sind die Obergrenze dessen, was jede Maske ausdrücken kann.**
  Gibt es für ein Feature keinen Baustein, kann keine Maske es zeigen. Feature-Wachstum und
  Komponenten-Wachstum sind gekoppelt — bewusst, weil es die 84 klein hält.
- Maske ↔ Programm ist ein **Build-Time-Vertrag** (Schnittstelle im Code, Version im
  Manifest), nicht Laufzeit-Aushandlung. Die Maske kann nicht in das Programm hineingreifen;
  Lücken in der Schnittstelle sind erst beim Bauen sichtbar.

**offen**

- Was passiert, wenn der **Server ein Programm hinter einer installierten Maske
  weiterentwickelt**? Das Manifest passt dann nicht mehr, ohne dass neu gebaut wurde.
  Vermutung: beim Start erneut prüfen und Update anbieten.

## 3. Programm, Modul, Server

**gesetzt**

- Ein **Programm** ist die Domänenlogik. Es **hat keine Ahnung** von einer Maske — und weiß
  auch nicht, dass es mehrere Masken gibt. Es exponiert eine Möglichkeit-Oberfläche und hört auf.
- **Das Programm ist groß, und der größte Teil davon ist nicht Logik, sondern Vertrag:**
  Versionierung, Entdeckbarkeit, Rechte, Fehlerbilder, Synchronisation.
- **Module, die auch allein arbeiten.** Installiert wird, was man braucht, statt eines großen
  Servers, der alles kann.
- **Ein Server, und er wird nur einmal installiert.** Jedes Programm bringt den Server mit;
  ist er schon da, wird er nicht nochmal installiert. Grund: man kann nie sicher sein, ob er
  schon da ist — also immer gegen den laufenden Server arbeiten.
- **Der Server hält die Vernetzung mit anderen Servern zentral.** Die Programme kümmern sich
  nicht darum. Dazu gehört auch die Datenbank, weil die Daten von diesem Server geteilt werden.
- **Bundes-/Föderationsfähig:** Programme teilen Daten und arbeiten zusammen wie in einem
  P2P-Netz, ohne fremden Server. Derselbe Rechner kann mit einer DNS als „konventioneller"
  Server betrieben werden — gleiche Software, andere Konfiguration.
- **Standardisierung macht den Speicherort gleichgültig:** ein Contact ist überall ein
  Contact — im Projektmanagement, im ERP, in der Kontakt-App. Ein Kontakt aus einer fremden
  Instanz ist in der eigenen App benutzbar, auch wenn die Gegenstelle diese App nicht hat.
- Regeln werden **gemeinsam programmiert** (Programm und Server-Seite bilden eine Einheit),
  nicht von zwei getrennten Teams gepflegt.
- **Authentifizierung ist nicht Programm.** OAuth, SCIM, Identität gehören zur Plattform
  (Ebene 6), nicht in jedes der Programme — sonst steht dieselbe Authentifizierung 84 Mal da.
  (`data/api.md` hat OAuth2 und Header-Standard auf API-Ebene, richtig so.)

**offen — Braucht der Nutzer Hilfe bei der Entscheidung**

Zwei Varianten, wie Programme an Daten kommen:

| | A · eine Zentrale Datenbank | B · jedes Programm eigene Datenbank |
|---|---|---|
| Speicher des Programms | Teil der gemeinsamen DB | eigener Speicher, **nur Cache** |
| Daten abgeben | immer möglich | erst wenn der Server installiert ist |
| Programme | größer | **schlanker**, „mal eben" installierbar |
| Ohne Netzanbindung | Daten sind trotzdem da | weniger Angriffsfläche, wenn man gar nicht online will |
| Regeln | ein Ort, alle Programme schreiben dieselbe Tabelle | Regeln pro Programm, Abgleich beim Abgeben |
| Risiko | ein Fehler in einer Migration trifft alle | dieselben Daten in mehreren Welten, Abgleich nötig |

Beides hat Vor- und Nachteile; Entscheidung steht noch aus. Klar ist in beiden Fällen:
**Es gibt immer einen Datenbank-Server.**

## 4. Datenbank-Kandidat Turso / libSQL — Belegstand 2026-11-03

Der Nutzer tendiert zu Turso und erinnerte „von Supabase". Nachstand: Turso kam **nicht** von
Supabase (der libSQL-Fork stammt von ChiselStrike); die Verbindung zu Supabase ist offenbar
die Übernahme von 2026-10-02. Nachstand:

- ⚠️ **Supabase hat Turso gekauft**, angekündigt am 2026-10-02, zusammen mit einer
  150-Millionen-Runde; beide Seiten sagen, für Bestandsnutzer ändere sich nichts.
  **Einzelne Zweitquelle, noch nicht bei Supabase oder Turso selbst nachgelesen** — vor einer
  Infrastruktur-Entscheidung prüfen.
  <https://layerbase.com/blog/supabase-acquires-turso>
- ✅ **libSQL ist die gepflegte Gegenwart, Turso Database die Zukunft:** libSQL ist der
  SQLite-Fork mit Produktionseinsatz; Turso Database ist ein **Neuschreiben von SQLite in
  Rust** für hohe Dichte an Datenbanken **ohne Server und ohne Verbindung**. Offizielle
  Empfehlung dort: neu anfangen → Turso Database, mission-kritisch heute → libSQL.
  <https://docs.turso.tech/libsql> · <https://turso.tech/blog/we-will-rewrite-sqlite-and-we-are-going-all-in>
- ✅ **Embedded Replica:** eine lokale SQLite-Datei, **Lesezugriffe lokal in Mikrosekunden**,
  **Schreibzugriffe gehen an das Primary** und werden in die Replik zurückgespielt.
  <https://docs.turso.tech/features/embedded-replicas/introduction>
- ✅ **Offline Writes** (lokal schreiben, später synchronisieren) existieren, waren zuletzt in
  einer **privaten Beta**. <https://turso.tech/blog/introducing-offline-writes-for-turso>

**Folge für unsere Architektur** (Idee, noch nicht entschieden)

- Das „lokal lesen, entfernt schreiben" ist genau das Muster, das die Variante B stützt — aber
  die Schreib-Delegation ist der Haken: **Schreiben setzt das Primary voraus.** Wer
  Offline-Schreiben ohne Netzanbindung braucht, darf sich nicht auf die Standard-Semantik der
  Embedded Replica verlassen.
- Das „Tausende kleiner Datenbanken"-Modell von Turso Database passt gut zum Modulgedanken
  (ein Programm, ein Speicher, schlank installierbar).
- Der Satz „ohne Server und ohne Verbindung" aus der eigenen Doku ist genau der Satz, der für
  Variante B spricht. Prüfen, bevor entschieden wird.

## 5. Schreiben: Maske → Programm → Server

**gesetzt**

- Die Maske **muss Daten schreiben können**, aufgeteilt wie Frontend und Backend: kleinere
  Prüfungen darf sie selbst machen, die Daten gibt sie weiter, und die große Prüfung passiert
  dahinter. **Nichts kommt ungeprüft in die Datenbank.**
- Der große Check sitzt **da, wo die Daten liegen**. Die Maske ist per Konstruktion
  austauschbar (veraltet, falsch, bösartig); prüft nur die Maske, wird das Versprechen
  „beliebige Maske, gleiches Programm" zum Einfallstor.

**Idee — trägt die Architektur**

- **Ein geteilten Crate für die Regeln**, der sowohl ins Programm als auch in den Server
  einkompiliert wird. Kleine Prüfung und große Prüfung sind derselbe Code, an zwei Orten
  ausgeführt. Verhindert das Auseinanderdriften zweier Regelwelten.
- Wenn **mehrere Programme in dieselbe Tabelle schreiben**, können die Regeln nicht in einem
  dieser Programme wohnen. Nur zwei saubere Orte: geteilte Bibliothek, oder die Datenbank
  selbst (Constraints, Trigger). Einmal festlegen, sonst löst es jeder Modulautor anders.
- Kleine Prüfung = **gegen das publizierte Schema validieren** (Standard, nichts pro Maske
  erfinden). `data/formate.md` führt JSON Schema bereits.
- **Lokale Abkürzung verboten:** auch lokal redet jedes Programm über denselben IRI, nie über
  einen direkten internen Aufruf. Sonst funktioniert es auf einem Rechner und in der
  Föderation nicht — und bricht lautlos.

## 6. Daten überleben Module

**gesetzt** (bereits im Datenzweig angelegt, hier nur benannt)

- **Eine Tabelle pro Domäne, nicht pro Modul.** `data/events/description.md`: Aufgaben leben
  als JSCalendar-`Task` in der Termin-Domäne, **keine** eigene `aufgaben/`-Domäne. Ein
  Termin-Modul kann Aufgaben erzeugen, ohne dass es ein Projektmodul gibt.
- Regeln:
  - Modul **deinstallieren löscht keine Daten** — es nimmt Maske und Funktionen.
  - Modul **installieren** darf nicht voraussetzen, dass seine Tabellen leer sind; sie können
    voll sein mit Daten eines anderen Moduls.
  - Braucht ein Modul ein neues Feld, ergänzt es das **gemeinsame** Modell, nicht eine eigene
    Tabelle.
- Das ist der Grund, warum Standardisieren vor Programmieren kommt. Ein Feld, das in der
  gemeinsamen Datenbank falsch benannt oder zu arm ist, zieht sich durch alle Module.
  `data/mappings.md` benennt solche Stellen schon („Zwei-Felder-Modell ist zu arm",
  „`street`/`houseNumber` sind eine Westeuropäisierung") — das sind keine Fußnoten, das ist
  die Rechnung, die sonst mehrfach bezahlt wird.
- **IDs sind föderationsfertig**, wie sie sind: intern ULID, extern absoluter IRI
  `https://<instanz>/<domaene>/<ulid>` (`data/index.md`, Beschluss 3). Dass die **Instanz in
  der ID** steht, ist die Voraussetzung dafür, dass ein fremder Kontakt nachfragbar bleibt.

## 7. Offline ist der Regelfall, nicht der Notfall

Korrektur einer früheren Annahme des Agenten: weil alles auf dem eigenen Rechner oder Telefon
liegt, ist **lokal immer erreichbar**; das Netz ist die Ausnahme. Folge: innerhalb der eigenen
Instanz darf die Maske optimistisch reagieren. Vorsicht gilt nur bei **geteilten** Daten.
Diese Unterscheidung — **eigen** versus **geteilt** — beantworten, wie sich eine Maske bei
Fehlern verhalten darf, und gehört in die Doku.

## 8. Teilen und Rechte — „und", nicht „oder"

**gesetzt**

- Beides gleichzeitig, nicht entweder/oder:
  1. **Direkt geben** und die Daten als frei markieren.
  2. **Abo/Regel**: eine Liste von Servern, die als **Gruppe** deklariert sind; Gruppen
     schicken und empfangen Daten.
- **Ein Server kann in mehreren Gruppen sein.** Beispiel des Nutzers: die Frau steht sowohl
  auf dem Arbeits-Server als auch beim Tanzkreis. Tanzbilder gehen nur privat — sie bekommt
  sie trotzdem. Heiratet man, kann beides geteilt werden; **sie bekommt nur einen Datensatz.**
- **Umgangsregeln** an der Datenabgabe: anzeigen lassen, kopieren lassen, und so fort. Der
  Empfänger sieht, was er darf.
- **Vertrauensgrenze:** Wenn ich Daten abgebe, muss ich darauf vertrauen können, dass der
  Empfänger damit umgehen kann. Wenn nicht, ist es mein Pech — „irgendwann ist es auch mal
  gut". Die Regel endet am eigenen Server; nach der Abgabe ist die Kontrolle abgegeben.
- AS2-Struktur erlaubt dieses Modell („das ist toll"). Beleg für die AS2-Teile in
  `data/mappings.md` ✅ (Core §4.1, `name`/`nameMap`, `id` als absoluter IRI).

**Belegstand und Lücke**

- ❌ **Es gibt kein Modell dafür.** `data/modelle.md` führt fünfzehn Modelle (User, Team,
  Message, Document, Block, Event, Task, Contact, Location, File/Media, Tag/Label, Comment,
  Notification, Revision/Version, Integration/Webhook) — **keines für Teilen, Rechte oder
  Abonnements.** Das ist die einzige echte Lücke in `modelle.md`.
- `data/felder.md` deckt das nicht: `visibility` kennt nur `private`, `workspace`, `public`
  (eine Organisation, drei Stufen) und `permissions` als Array. „Diesen Kontakt habe ich dir
  gegeben, du darfst ihn in deinem PM benutzen, aber nicht weitergeben" ist damit nicht
  sagbar. Die Datei weiß es selbst, Zeile 17: für Berechtigungsfelder
  „**kein Pate gefunden**, Kandidat ODRL (Erreichbarkeit geprüft, Inhalt nicht gelesen)" ⚠️.
- **ODRL** ist deshalb kein exotischer Wunsch, sondern die W3C-Sprache dafür, welche Daten von
  wem wofür genutzt werden dürfen — inklusive der Umgangsregeln. Passt zum Maßstab
  „Standards" und wäre gewonnen statt erfunden. **Inhalt jetzt gelesen** ✅ — Klassen und die
  Unterscheidung `Offer`/`Agreement` stehen in §17.
- **Kopie oder Verweis?** Zwei mögliche Grundformen, beide brauchbar:

  | Form | Verhalten | Preis |
  |------|-----------|-------|
  | **Kopie mit Herkunft** | Arbeitskopie in der eigenen DB, offline nutzbar | kann veralten, braucht Abgleich |
  | **Live-Verweis per IRI** | immer aktuell | Gegenstelle muss erreichbar sein |

  **Stand der zweiten Runde (§16): es ist keine Wahl zwischen beiden.** Beide Formen gehören ins
  Modell, weil der Nutzer zwei verschiedene Handlungen hat — **Schenken** (Kopie, weg) und
  **Freigeben** (bleibt an mich gebunden). Die Frage aus §15, Nr. 6 ist damit beantwortet.

  Vermutung des Agenten: **Kopie mit Herkunft** plus Delta-Abgleich — dafür spricht alles
  Lokale im Modell, und `Revision / Version` in `modelle.md` ist der richtige Unterbau. Dann
  braucht ein geteiltes Objekt drei Dinge: **woher** es kommt, **welche Fassung** ich habe,
  **welche Regeln** an der Kopie kleben.
- **Der Satz „sie bekommt nur einen Datensatz"** ist eine Deduplizierungs-Anforderung: dasselbe
  Objekt, das über zwei Gruppen an denselben Empfänger kommt, darf nicht zweimal ankommen.
  Das braucht eine Identität, die über den Gruppen hinweg gleich bleibt.

## 9. Fähigkeiten, Kommandos, Masken-Abbildungen

**Idee — der Baustein, den wir noch nicht haben**

Die Maske braucht mehr als Daten-CRUD. Aus einer Maske heraus braucht man fünf Schichten:

```
Daten      · Ressourcen, Filter, Webhooks        → data/api.md hat das schon gut
Kommandos  · was darf ich hier tun?
Fähigkeiten· welche Funktionen gibt es, ab welcher Version, mit welchem Recht?
Absichten  · öffnen, exportieren, teilen
Plätze     · wo darf die Maske andocken?
```

Das mittlere Stück fehlt. Konkrete Lücke: pro Skin gibt es `menu.md`, `features.md`,
`structure.md`, `shortcuts.md`, `api.md` — aber **für unser eigenes Programm steht nirgends,
was es kann.** Die `api.md` der Skins beschreibt das **fremde** Backend, nicht unseren Vertrag.

- **Versionsprüfung wie bei der Installation, aber gegen die Schnittstellen-Version, nicht die
  Programmversion.** Die Programmversion sagt nicht, was ein Programm kann.
- Bereich statt Gleichheit prüfen („Maske braucht Form 2–4, Programm bietet 3 → passt").
  Bei Gleichheit erzwingt man Gleichschritt — genau die Kopplung, die weg soll.
- **Pflichtmenge + alles andere optional**: die Maske verlässt sich nur auf die Pflichtmenge
  (die ändert sich praktisch nie); Rest fragt sie ab und zeigt ihn, wenn er da ist. Das macht
  „kann, muss aber nicht" mechanisch funktionieren.
- **Die vier Dateien pro Skin sind vier Abbildungen derselben Kommandomenge**: `menu.md` als
  Punkte, `shortcuts.md` als Tasten, `interactions/gestures/` als Bewegungen, `structure.md`
  als Flächenknöpfe. Gibt es eine Kommandoliste pro Programm, sind das vier Spalten
  derselben Tabelle.
- **Marktboden:** In jedem dokumentierten Kalender (Google, Outlook, Nextcloud, Merkuro,
  Planner, DAViCal) tauchen dieselben Grundhandlungen auf — ansehen, anlegen, ändern,
  verschieben, löschen, suchen, exportieren, teilen. In Mail-Oberflächen ebenso, andere Form.
  Diese Konstante ist die Pflichtmenge. Eine Maske, die eine davon nicht zeigt, ist kaputt,
  nicht schlank. **Regel statt offener Suche: Pflichtmenge aus dem Markt ablesen, Kür frei,
  Grundmaske zeigt immer die Pflichtmenge.**

**Fähigkeit statt Attribut**

- Der Date Picker trägt heute `creatable`, `movable`, `editable`, `deletable`,
  `confirmDelete` — **Schreibrechte als von Hand gesetzte Maschen-Attribute.** Das ist die
  falsche Richtung: die Maske rät über die Fähigkeiten des Programms. Meldet das Programm die
  Fähigkeit, erübrigen sich diese Schalter.
- Zusätzlich nach der jetzigen Runde: **Bearbeiten gehört nicht ins Widget.** Der Picker gibt
  nur einen Wert zurück (Datum oder Datum/Zeit; Uhrzeit nie — dafür gibt es `time-picker`).
  Ein Link/Knopf öffnet das Programm, das bearbeitet. Anlegen und Löschen sind App-Gebiet.
  Das Schreiben aus dem Widget heraus (`creatable`/`editable`/`deletable`/`confirmDelete` und
  die `POST`/`PATCH`-Vermerke in `attributes.md`) muss daraus folgen und raus.
  **Noch nicht entschieden:** ob **Ziehen auf einen anderen Tag** Bearbeiten oder Auswählen
  ist — danach entscheidet sich `movable`.
- **ADR 0005** (`conventions/decisions/0005-widget-und-app-gleicher-kern.md`) hält die
  App/Widget-Grenze fest. Die ist jetzt ein Randfall des größeren Modells und muss
  überarbeitet werden, sobald die Kommandoseite steht.

## 10. Der Datenanschluss pro Component

Offen, und der Grund, warum das Einordnen der 84 Bausteine erst nutzbar wird:

> Ab dem Widget wird es schwieriger, weil ein Widget ein Datenmodell bindet. Also muss jedes
> Widget sagen können, **welchen Datenanschluss es braucht.** Nicht jedes primitive, workbench
> oder widget kann alles darstellen.

Vorgeschlagene Form (Platzhalter, noch nicht in `docs/`):

| Component | Datenanschluss | kann nicht darstellen |
|---|---|---|
| `list-view` | flache Liste von Datensätzen, ein Anzeigefeld, ein Sortierfeld | Hierarchie, Zeiträume |
| `calendar-view` | Datensätze mit Beginn (`date`/`datetime`), optional Ende oder Dauer | alles ohne Datum |
| `table` | Datensatz mit bekannten Spalten | freier Text |
| `tree-view` | Datensätze mit Eltern-Kind-Beziehung | Menge ohne Beziehung |
| `rich-text-editor` | Block-Array **oder** String — beides, aber nicht gemischt | Blöcke mit eigener Identität nur, wenn das Modell sie hat |

Damit wird „was kann was darstellen" **prüfbar** statt Prosa: ein Skript kann fragen, ob dieses
Modell zu diesem Widget passt, und die Programm-Doku kann sagen, welcher Anschluss fehlt.

## 11. Inhalt: eine Repräsentation pro Objekt

- **gesetzt:** Inhalt ist **genau eine** Sache pro Objekt — entweder Block-Array oder
  String-Format mit Markup. Wie es dargestellt wird, entscheidet das **gewählte Widget**.
  Ein Widget kann beides so darstellen, dass es wie ein Editor aussieht und anders
  funktioniert. Deshalb ist die Einordnung von primitives/widgets/workbenches und die
  Standardisierung der Daten so wichtig.
- **Warum die Wahl nicht kosmetisch ist:** ein Markup-String hat *Positionen* — „Überschrift an
  Zeichen 12" hat keine eigene Identität und ist nicht referenzierbar, nicht verschiebbar,
  nicht einzeln abfragbar. Ein Block-Array hat *Identitäten* — ein Block kann verschoben,
  verlinkt, angehängt, gefiltert werden. `modelle.md`, Modell `Block`, hat `order`, also ist
  Verschieben schon gemeint. Nicht, dass eine Notion-Maske einen String nicht rendern könnte —
  sondern dass sie dann Blöcke **erfinden** müsste, und das wäre Logik in der Maske.
- **offen und blockierend:** es gibt zwei Beschreibungen desselben Inhalts und keine
  dokumentierte Abbildung zwischen beiden — `rich-text-editor/attributes.md` (`value`, Typ
  `string`, „Wert (HTML)") und `modelle.md`/`Block` (Block-Array). Details und offene Punkte
  stehen bereits in `data/mappings.md`, Abschnitt „Überschrift im Text → `name` der Ressource".
  Der Block hat dort **kein Feld für die Überschriftenstufe** (`level`/`depth` fehlt).
  Für strukturierten Block-Inhalt wurde **kein Standard** gefunden ⚠️.

## 12. Eingaben — was an den Gesten fehlt

- **Nicht fehlend,** aber einseitig: `interactions/gestures/` hat sechs Familien und 21 Gesten,
  `hover` ist da. Der Index sagt „Touch-Gesten … und verwandte Zeiger: Maus, Stift, Sensoren".
- **Was fehlt:** die Achse ist fingerförmig. Für Maus und Tastatur gibt es in `tap`/`swipe`/
  `transform` kein Zuhause:
  - **Rechtsklick** — passt in keine Familie
  - **Scrollrad** — ebensowenig
  - **Doppelklick vs. Doppelantippen** — gleiche Geste, andere Bedeutung (Dateiliste öffnet,
    im Text markiert es ein Wort)
  - **Tastatur und Kürzel** — fehlen völlig, obwohl **jeder Skin eine `shortcuts.md` hat**
- Die halbe Antwort steckt schon in eigenen Dateien: `shake`, `flick` und `hover` haben
  `alternativeAction` bzw. `focusEquivalent` — „jede Geste braucht ein Äquivalent per
  Button/Tastatur". Das heißt: **die Geste ist nicht die Handlung, sondern ein Weg zu ihr.**

## 13. Werkzeuge, die sich daraus ergeben (Idee)

- Programme × Masken ist ein Testgitter, das niemand von Hand fährt. Zwei getrennte Prüfungen:
  eine **Programmprüfung** (erfüllt es die Vertragspflichten, meldet es alle Fähigkeiten
  korrekt?) und eine **Maskenprüfung** (nutzt sie nur Components und nur gemeldete
  Fähigkeiten?). dieselbe Sorte Werkzeug wie `scripts/check_components.py`, nur für die andere
  Seite. Zähmt das Risiko von „muss aber nicht": eine Maske, die Fähigkeiten nicht anbietet,
  wird sichtbar, statt dass Nutzer es erst beim Skin-Wechsel merken.
- **Das Register.** Wenn ohnehin eine Instanz die Datenbank hält, ist sie auch das Register:
  sie weiß, welche Schnittstellen ein Programm bietet und welche eine Maske braucht, und sie
  löst Absichten auf („wer kann diesen Termin öffnen?", „ist die App da?"). Ohne Register
  funktioniert weder die Install-Nachfrage („Programm nicht installiert → fragen, ob es
  installiert werden soll") noch der Sprung aus einem Widget in ein Programm.

## 14. Kalender-Beispiel (Einstieg in das Gespräch)

- **Das Widget hat genau eine Ausgabe: einen Wert. Das Programm besitzt die Datensätze.**
  Der Picker ist mit Datenanbindung ein kleiner Kalender; die Fläche wächst, der Vertrag bleibt.
  Die Event-Liste im Picker ist **Entscheidungshilfe** („schau, was schon verplant ist, bevor
  du den Tag wählst"), read-only.
- Drei getrennte Achsen: **Wert** (`date`, `datetime`; Uhrzeit nie) · **Darstellung**
  (Kalender, Drehregel, Dropdowns, Liste, Freitext) · **Vorschau** (Einträge als Punkte/Liste).
  Darstellung ändert nie am Wert.
- **Drehregel und Dropdowns brauchen den Kalenderkern nicht** — sie sind eigene Bausteine, die
  denselben Wertvertrag erfüllen. Sonst zwingt eine Drehregel, den ganzen Kalenderkern
  mitzukompilieren. Passt zu Rust-Feature-Flags: Schalter müssen **orthogonal** sein und einen
  **Minimal-Kern** haben. Achtung **Feature-Unifikation**: im Cargo-Graph gilt ein Feature
  crate-weit, sobald irgendwer im Abhängigkeitsgraph es einschaltet — also lieber mehrere
  kleine Bausteine als einen großen mit 40 Schaltern.
- **Größe ändert nie Funktionen.** Bringen drei Größen automatisch Menü und Export, hat man in
  drei Jahren einen Datums-Wähler mit Druckdialog.
- Wer die Daten lädt, ist die eigentliche Gabel und der eigentliche Größenhebel:
  **`entries` vom Aufrufer** (kein Datenclient, kein Filter, kein Fenster im Widget) versus
  **`sources` im Widget** (API-Client, Fensterlogik, `updatedSince`, Rechte). Beides steht
  gleichzeitig in `date-picker/attributes.md` (Zeile 13 `entries` **und** die `sources`-Gruppe) —
  das muss entschieden werden.
- Vierteilige Ordnung: **Kern** (Tageszelle, Eintragsmarke, Tagesliste, Monatsraster) →
  **Wert-Hülle** (Overlay, Rückgabe) = Picker · **Flächen-Hülle** (Wochen-/Tagesraster, Agenda,
  Zeiträume umbrechen) = Kalender-Ansicht · **Programm-Hülle** (Menü, Suche, Bearbeiten,
  Export, Einstellungen, Adresse). Der „größere Kalender" ist derselbe Kern in der Flächen-Hülle.
- „In Kalender öffnen" braucht eine **kanonische Adressform** (`fs:calendar/day/2026-11-14`,
  `fs:calendar/event/<id>`). Dieselbe Adresse ist das, was ein Programm zum Programm macht
  (adressierbar, teilbar, verlinkbar) — und sie muss definiert sein, bevor ein Widget in ein
  Programm springen kann. Das Widget darf das Programm dabei **nicht kennen**: es feuert eine
  Absicht, die Plattform löst auf.

## 15. Abgleich — Primary, Kollision, Grabstein

Die Mesh-Frage aus der ersten Runde („was ist ein Primary, wenn zwei Instanzen denselben Termin
bearbeiten?") ist beantwortet — aber die Antwort ist **nicht** „einer gewinnt automatisch".
Der Nutzer unterscheidet drei Situationen, und die dritte ist die technisch schwere.

**gesetzt — Fall 1: Server ist schon da, das Programm kommt später**

- **Wer zuerst da war, dessen Datensatz gilt.** Der Spätere wird nicht still überschrieben.
- Der Ankömmling (das Programm) bekommt eine Rückfrage: **Da ist ein Fehler — überschreiben,
  ändern oder abbrechen?** Drei Antworten, keine vierte stumm.
- Technik dahinter: das ist ein **bedingtes Schreiben**. Der Server lehnt ab, wenn die Fassung,
  die das Programm annimmt, nicht die aktuelle ist — HTTP **409 (Conflict)** bzw. **412
  (Precondition Failed)** mit `ETag`/`If-Match` ✅ (RFC 9110 §15.5.10, §13.1.1). Ohne diese
  Bedingung gewinnt immer der zuletzt Schreibende, lautlos.

**gesetzt — Fall 2: beide kommen gleichzeitig, Inhalte sind verschieden**

- Der Server meldet über **eines** der beiden Programme: derselbe Satz wird zweimal aufgespielt,
  und die beiden sind **unterschiedlich**.
- Der **Mensch** entscheidet, welche Fassung er haben will — **und was mit der anderen
  passiert**. Beides ist Teil der Frage, nicht Restmüll.
- Acceptiert: bei sehr vielen Programmen wird das Arbeit. „Wer das nicht sofort verbindet, darf
  sich nicht wundern, wenn er dann aufräumen muss." — **Aufräumen ist ein akzeptierter Preis
  für Offline**, kein Grund, das Modell zu verbiegen.

**gesetzt — Fall 3: der Server war mal da, der Datensatz ist dort gelöscht, ein Client hat ihn
noch**

- Das ist **keine sichere Sache**, deshalb: **letztes Datum prüfen** und das Programm fragt —
  gibt aber eine **Empfehlung** ab, nicht nur eine Frage.
  - Löschen ist ** später** passiert → empfohlen: hier auch löschen.
  - Anlegen/Ändern ist ** später** passiert → empfohlen: dort wieder einfügen.
- Diese Empfehlung gilt **nur, wenn der Datensatz schon mal da war.** War er nie da: einfach
  einfügen bzw. kopieren, ohne Rückfrage.

**die technische Folge, die alles trägt: der Grabstein**

„War nie da" und „war da und ist weg" sind im Moment nicht unterscheidbar — aber genau diese
Unterscheidung verlangt Fall 3. Ohne Grabstein rät das Programm in der Hälfte der Fälle falsch.

- ✅ AS2 hat den Typ **`Tombstone`** mit `formerType` und `deleted` (Vocabulary, Object Types,
  Beispiel 60): „a content object that has been deleted … signify that there used to be an object at this
  position". <https://www.w3.org/TR/activitystreams-vocabulary/>
- ✅ ActivityPub §6.4: beim `Delete` **MAY** der Server das Objekt durch einen Grabstein
  ersetzen; wird das gelöschte Objekt angefordert, **SHOULD** er **410 Gone** mit Grabstein
  antworten, sonst 404. <https://www.w3.org/TR/activitypub/>
- **Idee:** Grabsteine sind keine Nebennotiz, sondern eine eigene Tabelle pro Domäne (oder eine
  gemeinsame pro Instanz) mit `id`, `formerType`, `deleted`, `deletedBy`. Löschen wird sonst zu
  „Zeile fehlt", und „fehlt" ist mehrdeutig.

**Idee — Kollision ist ein Zustand, kein Dialog**

Eine Rückfrage, die niemand beantwortet, ist keine Entscheidung. Wenn die Frage nur in einem
Modal hängt, ist der Konflikt beim nächsten Neustart weg und die Daten still gemischt.
Vermutung: ein Konflikt ist ein **Zustand am Datensatz** (Konflikt-Markierung plus eigene Liste,
in der man sie sammelt) — damit „nicht sofort" legal ist und „später aufräumen" (Fall 2) ein
Ziel hat statt einer Lücke.

**Belegstand für Fassungszähler — das kann man erben statt erfinden**

- ✅ **JSCalendar `sequence`** (RFC 8984 §4.1.7): anfangs 0, **MUST bei jeder Änderung um eins
  hoch**, außer bei `participants`. <https://www.rfc-editor.org/rfc/rfc8984>
- ✅ **iTIP RFC 5546 §5.3** regelt dasselbe für Kalender: Folge 5 gegen vorhandene Folge 2 →
  **aktualisieren**; Folge 2 gegen vorhandene Folge 5 → **MUST NOT überschreiben**. Das ist ein
  fertiges Regelwerk für „welche Fassung gewinnt", für das wir nichts erfinden müssen.
  <https://www.rfc-editor.org/rfc/rfc5546>
- ✅ **JMAP RFC 8620**: `state` pro Datensatz, `ifInState` beim Ändern, Fehler **`stateMismatch`**,
  und `updatedSince`/`oldState`/`newState` beim Nachziehen. Genau das Muster „welche Fassung habe
  ich, und hat sich die Welt seitdem bewegt". <https://www.rfc-editor.org/rfc/rfc8620>

**offen — Punkte, die die Antwort nicht auflöst**

1. **„ändern" ist unklar.** Überschreiben · zusammenführen · eigene Fassung als Zweig
   behalten? Drei verschiedene Dinge, und die Auswahl entscheidet, ob `Revision/Version`
   pro geteiltem Objekt mitwandern muss (vgl. §18, Nr. 6).
2. **Wo wohnt die Rückfrage — Server oder Maske?** Vermutung: **Server** entscheidet, Maske
   zeigt. Sonst löst jedes der 84 Programme dieselbe Kollision anders, und eine Maske könnte
   Konflikte einfach unterdrücken (widerspricht §5: große Prüfung da, wo die Daten liegen).
3. **„letztes Datum" ist auf zwei Rechnern nicht sicher.** Uhren laufen auseinander, und ein
   zurückgestelltes Handy lügt. Entweder akzeptiert man das (mit Rückfrage als Netz) oder der
   Vergleich bekommt einen **Zähler pro Datensatz** (`sequence`) und die Frage „kennt diese
   Fassung meine Fassung?" — nicht nur ein Zeitstempel. **Das ist der Punkt, den ich beim
   nächsten Mal zuerst klären möchte.**
4. **Wie lange bleiben Grabsteine?** Für immer frisst Platz, ein Verfallsdatum bricht die
   Unterscheidung aus Fall 3 wieder auf. Braucht eine Regel (z. B. so lang wie die längste
   Offline-Zeit, die man versprechen will).
5. **Fall „Server ist ganz weg"** (nicht nur ein Datensatz) ist damit noch nicht behandelt.
   Die Instanz steht in der ID (§6, Beschluss 3), also sind die Daten noch zuordenbar — aber
   ob man einer wiedergekehrten Instanz ihre alten Datensatz-Identitäten noch glaubt, ist eine
   Vertrauensfrage (siehe `data/identity/`, WoT).

**Was das für „Primary" heißt**

Der Begriff ist in zwei Bedeutungen aufgetaucht und muss getrennt werden:

| Bedeutung | Quelle | Antwort dieser Runde |
|---|---|---|
| **Schreibprimär** (wo schreibt die Replik hin) | Turso/libSQL, §4 | bleibt eine Technikfrage (§18, Nr. 2) |
| **Wer hat recht** | Mesh-Frage | **kein automatischer Gewinner** außer Reihenfolge in Fall 1; sonst fragt das Programm |

Der Satz „Schreiben setzt das Primary voraus" aus §4 gilt also nur für die Technik-Ebene. Für die
Wahrheit gilt: **Reihenfolge entscheidet einmal, danach entscheidet der Mensch.**

## 16. Schenken und Freigeben — zwei Grundformen; Gruppe = Liste

Die Frage „Kopie mit Herkunft oder Live-Verweis?" (§8, §18 Nr. 6) war falsch gestellt. Der
Nutzer hat **zwei Handlungen**, und sie verhalten sich gegenteilig:

| | **Schenken / Geschenk** | **Freigeben** |
|---|---|---|
| was passiert | eine Kopie geht zum Empfänger, die Nachricht mailt man an eine Person oder eine Gruppe | wie im Messenger: bleibt an den Geber gebunden |
| weitergeben | der Empfänger darf, er hat eine eigene Kopie | hat er kopiert und weitergeleitet, ist sie außer Reichweite |
| zurücknehmen | **nicht möglich** — „ich habe meine Daten abgegeben" | **ja**: lösche ich sie, ist sie auch beim anderen weg |
| Grundform | **Kopie mit Herkunft** | **Verweis mit Bindung** (Löschen pflanzt sich fort) |

**gesetzt — Freigaben können Abgabe verlangen**

Bei Umfrage und Buchhaltung kann man Leute **verpflichten, etwas abzugeben**. Dann wird eine
Kopie von der Person gemacht — **nicht alles, sondern alles, was man dafür braucht.** Und es gibt
die Achse **anonym oder nicht**.

- Das ist ein dritter Fall neben Schenken und Freigeben: eine **Forderung** (der Geber ist der
  Empfänger). AS2-Muster dafür: `Invite`/`Question`/`Offer` mit `target` ✅ (Vocabulary, Beispiele
  23–24), Annahme mit `Accept`, Ablehnung mit `Reject`.
- „nicht alles, nur was man dafür braucht" braucht eine **Teilmenge pro Anfrage** — nicht
  „Kontakt ja/nein", sondern „diese Felder". Das ist ein Feld-Modell-Thema, kein Rechte-Thema,
  und es berührt `data/felder.md`.

**gesetzt — Gruppe ist eine Liste, wie bei E-Mail**

Ich schreibe Leute an oder Gruppen; die Gruppe ist **nichts anderes als eine Liste**.

- ✅ AS2 `Group` („formal or informal collective of Actors"), `audience` = „total population of
  entities for which the object can be considered to be relevant", `to/cc/bto/bcc` steuern, wo
  Kopien landen (Vocabulary §3.3, §4) ✅.
- ✅ ActivityPub: die **Followers-Collection** ist ein üblicher Ziel-Korb beim Senden; Server
  liefern nur an die Adressen in `to/bto/cc/bcc/audience` ✅. Die Liste lebt also als Collection
  am Server, nicht als Attribut am Datensatz.
- **Folge, noch nicht ausgesprochen:** bei einer **Schenkung** gilt die Liste **im Augenblick des
  Sendens**. Ändert sich die Mitgliedschaft danach, ändert das an den verteilten Kopien nichts —
  das ist korrekt und billig: eine Gruppe muss nicht weiterexistieren, damit ihre Gaben stimmen.
- **Bei Freigaben ist es umgekehrt**: dort muss eine Mitgliedschaftsänderung **sofort** wirken
  (wer aus der Tanzgruppe austritt, darf den Termin nicht weiter sehen). Genau hier entscheidet
  sich, ob Gruppen **gezählt** werden müssen oder als Liste genügen: **zum Schicken reicht die
  Liste, zum Widerruf braucht man die Zugehörigkeit.**
- Der Dedup-Satz aus §8 („sie bekommt nur einen Datensatz") bleibt davon unberührt und bleibt
  eine Anforderung an die Objektidentität über mehrere Gruppen hinweg.

**offen — Gruppengröße (die Frage ist offen geblieben)**

Klar ist nur der trivialste Fall (die Frau in zwei Gruppen). Offen: Tanzgruppe 40, Verein 400,
Firma 2000. Konkret hängen davon drei Dinge ab:

1. **Widerruf.** „Alle Freigaben einer Gruppe neu schreiben" ist bei 2000 Leuten und 50 000
   Objekten nicht machbar. Lösung kann nur sein: **Freigabe zeigt auf die Gruppe**, und die
   Zugehörigkeit wird bei der Prüfung nachgeschlagen — nicht in die Freigabe ausgeschrieben.
2. **Abzählen** („wer hat das gesehen?") geht nur, wenn die Freigabe ein eigenes Objekt ist.
   Eine Zeile „geteilt mit Gruppe Y" an meinem Kontakt kann man nicht abzählen.
3. **Rechtlich/sozial:** braucht eine Gruppenmitgliedschaft Zustimmung, Sichtbarkeit, Verwaltung
   durch jemand anderen als den Gruppeninhaber?

**offen — Attribut oder eigene Domäne?** Die Frage aus der ersten Runde ist damit nicht
entschieden, aber die Antwort neigt sich klar: **eigenes Modell**, denn Abzählen, Widerrufen und
Gruppieren (Punkt 1 und 2) sind mit einem Attribut nicht machbar. Ein Kandidatenname für
`data/modelle.md` wäre `Share`/`Grant` plus `Group`/`Membership`. Das schließt die in §8
benannte **einzige echte Lücke** in `modelle.md`.

## 17. „Als frei markieren" — Ansage, nicht Regel

Antwort des Nutzers: **„Wenn ich meine Daten abgebe, dann gebe ich sie ab. Der Serverbetreiber
kann damit machen, was er möchte. Er sollte nur vorher sagen, was er damit vorhat. Das kann man
mit AS2 abbilden."** Das ist die konsequente Fortsetzung der Vertrauensgrenze aus §8: die Regel
endet am eigenen Server.

**gesetzt**

- Nach der Abgabe gibt es **keine durchsetzbare Regel mehr**, nur Vertrauen.
- Was es gibt, ist eine **vorherige Ansage** der Absicht. Eine Ansage ist kein Zwang.

**die Unterscheidung, die man daraus machen muss — drei Zustände, kein Boolesch**

§8 sagt „Direkt geben **und** die Daten als frei markieren". „Frei" deckt drei verschiedene
Dinge ab, und sie sind getrennt speicherbar:

| Zustand | heißt | fehlt dann |
|---|---|---|
| **kein Kanal** | kein Abo, keine Regelbeziehung — nur dieser einen Stelle gegeben | die Beziehung |
| **keine Umgangsregel** | keine Regel an der Kopie; jeder darf weitergeben | die Regel |
| **kein Anspruch** | Public Domain / gemeinfrei — auch rechtlich nichts vorzubehalten | der Anspruch |

„Kein Kanal" und „keine Regel" sind verschieden: ein einzelnes Geschenk ohne Regel ist **nicht**
daselbe wie gemeinfrei.

**wie man es abbildet — zwei Ebenen, nicht eine**

- **Ansage (menschenlesbar, am Angebot):** AS2 `Offer`/`Announce` mit `name`/`summary`/`content`
  (und `*Map` für Sprachen), `audience` für den angesprochenen Kreis ✅. Das ist die
  Absichts-Erklärung, die der Nutzer fordert. **Nicht durchsetzbar** — genau richtig.
- **Regel (maschinenlesbar, an der Kopie, solange ich sie halte):** **ODRL**. Beleg jetzt
  gelesen (zuvor ⚠️): ODRL Information Model kennt `Permission` (Fähigkeit, eine `Action` auf
  einem `Asset` auszuüben), `Prohibition` (Unfähigkeit), **`Duty`** (Pflicht als Vorbedingung
  einer Erlaubnis), `Constraint`, `Party` und **`PartyCollection`**, `assigner`/`assignee`, und
  die Unterklasse **`Agreement`** = „Regeln, die vom `assigner` an `assignee`-Parteien
  **gewährt** werden" ✅.
  <https://www.w3.org/TR/odrl-model/>
- ✅ Der feine Unterschied passt exakt auf unsere zwei Handlungen: ODRL **`Offer`** stellt Regeln
  für einen weiteren Kreis **bereit, gewährt aber keine Regeln**; **`Agreement`** gewährt sie.
  Übersetzt: **Angebot mit Ansage** gegenüber **tatsächlicher Abgabe**.

**offen**

1. Wird ODRL als Pate angenommen (Nr. 7 bleibt)? Jetzt mit Inhalt gelesen, also entscheidbar; die
   Frage ist nur noch, wie viel der ODRL-Klassen wir wirklich brauchen — vermutlich
   `Policy`/`Agreement`/`Offer` + `Permission`/`Prohibition`/`Duty`, nicht den ganzen Kern.
2. **Wer sagt die Absicht?** Die Ansage ist eine Erklärung des Gebers. Ob der Betreiber sie
   beantworten muss („ich tue X damit"), ist eine Produktfrage, keine Datenfrage.
3. **Pate für „kein Anspruch"** (Public Domain) ist nicht gesucht — Kandidaten (Lizenz-Kenn-
   zeichnung) sind **nicht geprüft** ⚠️.

## 18. Offene Fragen

Nummeriert, damit Antworten hier eingetragen werden können. Nr. 1–10 aus der ersten Runde,
Nr. 11–19 aus der zweiten (Abgleich, Teilen, Gruppen, „frei").

1. **Variante A oder B** (§3): eine Zentrale Datenbank, oder eigene Datenbank je Programm mit
  dem Server als Abgabestelle? Wer ist Herr über das Schema, wenn zwei Programme beim Start
  beide eine Migration wollen?
2. **Zieht Turso Database (Rust-Neuschreiben, „ohne Server, ohne Verbindung") oder libSQL**
  (§4)? Und: brauche ich echtes Offline-Schreiben (private Beta) statt Schreib-Delegation?
  Vorab die Übernahme durch Supabase und der Reifegrad direkt bei Turso prüfen (beides ⚠️).
3. Bleibt **`movable`** im Widget — ist Ziehen auf einen anderen Tag Bearbeiten oder Auswählen?
4. Wer meldet Fähigkeiten: **Programm bei jeder Anfrage** mit, oder **Maske fragt beim Start
  ab** und merkt sie sich? (Nach §2 eher zweiteres, weil Build-Time-Vertrag.)
5. Was ist die **eine Inhaltsrepräsentation** für Texte — Block-Array oder String mit Markup?
  Inklusive Überschriftenstufe und der Abbildung zwischen beiden (§11).
6. ~~Kopie mit Herkunft oder Live-Verweis?~~ → **erledigt, beide** (§16): Schenken = Kopie,
  Freigeben = Verweis mit Bindung. **Offen bleibt der Rest der Nummer:** wandert
  `Revision/Version` pro geteiltem Objekt mit (hängt an Nr. 12)?
7. Wird **ODRL** als Pate für Umgangsregeln angenommen? Inhalt ist gelesen (§17) — es fehlt nur
  noch die Ja/Nein-Entscheidung und der Umfang (welche Klassen).
8. **Zeiger- und Eingabezweig** (Maus, Tastatur, Stift) neben den Touch-Gesten: eigene Familie
  oder Querschnitt durch alle Familien (§12)?
9. Gehört die **Kommandoliste** pro Programm in `docs/`? Wohin — eigene Datei neben
  `menu.md`/`features.md`, oder ein neuer Zweig?
10. **Datenanschluss pro Component** (§10): eigene Tabelle in `attributes.md` oder eigene Datei?

**aus der zweiten Runde (Abgleich, Teilen, Gruppen, „frei")**

11. **Woran erkennt das Programm, ob es eine Fassung schon mal gesehen hat** — Zeitstempel oder
    Zähler? Uhren sind über zwei Rechner unsicher (§15, offen 3). Meine Empfehlung: pro
    geteiltem Objekt `sequence` (JSCalendar) oder `state` (JMAP), der Zeitstempel wird nur die
    **Empfehlung**, nicht die Entscheidung.
12. Was heißen die drei Antworten aus Fall 1 genau: **überschreiben · zusammenführen · eigene
    Fassung behalten**? Und was heißt „ändern" in Fall 2 — dieselben drei, oder mehr?
13. **Wie lange bleiben Grabsteine**, und liegen sie pro Domäne oder pro Instanz (§15, offen 4)?
14. Ist ein **Konflikt ein Zustand am Datensatz** mit eigener Liste, oder nur ein Dialog
    (§15, Idee)? Wenn Zustand: welches Widget zeigt ihn (`alert`? `list-view`? beides?).
15. **Fall „Server ist ganz weg"** statt einzelner Datensatz: glaubt man einer wiedergekehrten
    Instanz ihre alten IDs (§15, offen 5)? Hat das etwas mit `data/identity/` (WoT) zu tun oder
    ist es bewusst Plattform-Ebene 6?
16. **Wie groß kann eine Gruppe werden**, und **braucht Mitgliedschaft Zustimmung** (§16)?
    Entscheidend für die Frage, ob Freigaben auf Gruppen **zeigen** (billig, sofort widerrufbar)
    oder Mitgliedschaften **ausgeschrieben** werden (abzählbar, teuer beim Widerruf).
17. **Eigenes Modell für Freigaben** (`Share`/`Grant` + `Group`/`Membership`) — Name und
    Aufnahme in `data/modelle.md`? Das wäre das **sechzehnte** Modell und schließt die Lücke
    aus §8.
18. Bei der **Abgabepflicht** (Umfrage, Buchhaltung): wie beschreibt man die **Teilmenge** der
    Felder, die man verlangt, und was heißt **anonym** technisch (Kopie ohne
    `attributedTo`/`actor`)?
19. Drei Zustände des **Frei-Markierens** (§17): werden sie als **drei Felder**, ein Enum, oder
    als ODRL-Policy mit leerem Inhalt gespeichert?

## 19. Plan-Fragen — dritte Runde (2026-11-03)

Kein Datenmodell, sondern **der Plan selbst**: Reihenfolge, Aufwand, Abbruchkriterium, Werkzeuge.
Vorher der Stand, wie er auf der Festplatte wirklich ist — gemessen, nicht geschätzt.

**Ist-Zustand (2026-11-03 nachgemessen)**

| Bereich | Ist |
|---|---|
| Skin-Doku in `de/` | 562 Dateien unter `programs/apps/` (11 Kategorien), 220 unter `programs/suites/` (5), 87 unter `programs/platform/` |
| Abgearbeitet laut `temp/apps-plan.md` | **42 von 869** Zeilen mit `[x]` — das ist genau calendar (6 Masken × 7 Dateien) |
| Dateien vorhanden, **ohne** Haken | **520** — nach der Vorlage heißt das: geschrieben, aber **nicht an Primärquellen verifiziert** |
| `temp/apps-plan.md` selbst | veraltet: alle 869 Zeilen zeigen auf `apps/…`; die Dateien liegen seit dem `programs/`-Umzug unter `programs/…`. Zeile 8 (`apps/index.md`) fehlt **an jedem** Ort |
| `temp/apps-prompt-vorlage.md` | verweist auf `docs/de/apps/plan.md` und `docs/de/apps/PROMPT-VORLAGE.md` — **beide Pfade existieren nicht mehr** |
| `de/` gegen `en/` | 1491 Dateien `de`, 478 `en`; `docs/en/components/` (355 Dateien) ist **uncommitted** (`??` in git) |
| Prüfer | `check_components.py` ✅ bestanden (84 Komponenten), `gen_component_indexes.py --check` ✅; für `data/` gibt es **keinen** Prüfer, und in CI laufen nur diese beiden |
| Ableitungslisten aus §1 (Pflichtmenge / Kür) | **existieren nicht.** „Pflichtmenge" kommt im ganzen Repo nur in diesem Blatt vor |

**die Fragen — P1 bis P4 entscheiden, ob der Plan tragfähig ist; P5 bis P8 sind die fehlenden
Stücke daran**

**P1 — Was bedeutet der Haken im Plan?**
42 Zeilen sind `[x]`, aber 520 Dateien sind geschrieben und stehen ohne Haken. Wenn `[x]`
**verifiziert** heißt (die Vorlage verlangt Primärquellen, und sie warnt ausdrücklich vor
fabriziertem Bestand — davical war mit Baïkal vermischt), dann sind 520 geschriebene Dateien
unverifiziert und der Plan ist ehrlich. Wenn `[x]` **geschrieben** heißt, ist der Plan kaputt.
Das muss zuerst geklärt werden, weil es die Menge der Restarbeit um Faktor 10 ändert.

**P2 — Wie viele Masken braucht die Pflichtmenge wirklich?**
§1 sagt: Schnittmenge aller Skins = Pflichtmenge, Vereinigung = Kür. Bei 119 Masken ist die
Schnittmenge nach wenigen Masken pro Kategorie praktisch eingefroren — die 827 restlichen Dateien
bringen dann fast keine neuen Anforderungen mehr. **Vorschlag des Agenten:** Abbruchkriterium
pro Kategorie (z. B. 3–5 Masken, dann Schnittmenge einfrieren, Rest nur als Stichprobe oder
beim konkreten Bedarf). Ohne dieses Kriterium sind 827 Dateien das Ziel statt das Mittel — und
das wäre der Hauptgrund, warum der Plan nie fertig wird.

**P3 — Wo landen Pflichtmenge und Kür?**
Sie sind der Input für §9 (Fähigkeiten) und §10 (Datenanschluss pro Component), und es gibt
keinen Ort für sie. Kandidaten: `data/anforderungen.md` wächst mit, oder ein eigener Zweig
(`requirements/`). **Solange der Ort fehlt, ist jede weitere Skin-Datei Arbeit ohne Ergebnis.**

**P4 — Was ist die kleinste Scheibe, bevor die Grundmaske anfangen kann?**
§1 setzt: die Grundmaske wird vom Nutzer gebaut und ist die Referenz. Vier Dinge muss er dafür
in der Hand haben: **Manifest** (P5), **Fähigkeitenliste** (P6), **Adressform** (P7),
**Datenanschluss** (§10 / §18 Nr. 10). Alles andere (Abgleich, Rechte, Grabsteine) kann später
kommen — ohne diese vier ist die erste Maske eine Vermutung.

**P5 — Das Manifest ist unbeschrieben.**
§2 benutzt es zweimal („Version im Manifest", „Build-Time-Vertrag"), aber keine Datei im Repo
beschreibt es (nachgesehen: „Manifest" kommt nur hier und in fremden Skin-Dokus vor). Welche
Felder? Programm-ID, Programm-Version, Masken-ID, benötigte Komponenten, benötigte Fähigkeiten,
zulässige Fassungs-Spanne. Ohne Manifest hat die Grundmaske **keine Schnittstelle**, und die
offene Frage aus §2 (Server entwickelt das Programm hinter einer installierten Maske weiter) ist
nicht entscheidbar, weil nicht definiert ist, was verglichen wird.

**P6 — Was ist eine Fähigkeit, und ist die Liste geschlossen?**
Vor §18 Nr. 4 (wer meldet Fähigkeiten) kommt diese Frage. Eine **geschlossene, zentrale** Liste
(„Objekt öffnen", „Datensatz bearbeiten", „Termin auswählen" …) ist die Bedingung dafür, dass das
Register auflösen und der Masken-Prüfer aus §13 feststellen kann, dass eine Maske eine Fähigkeit
nicht anbietet. Eine freie Liste pro Programm macht beides unprüfbar.

**P7 — Adressform: zwei Ebenen oder eine?**
§14 will `fs:calendar/day/2026-11-14`, §6 (Beschluss 3) hat `https://<instanz>/<domaene>/<ulid>`.
Vermutung des Agenten: bewusst **zwei** Ebenen — Absichtsadresse intern, IRI nach außen. Dann
fehlt die Abbildung zwischen beiden, und das Register braucht den einen Schlüssel. Kleine Frage,
blockiert aber Register und Sprung aus dem Widget.

**P8 — Register: Plattform oder Server?**
§13 macht es zur Voraussetzung für Install-Nachfrage und für den Sprung aus einem Widget ins
Programm; beschrieben ist es nirgends. Ebene 6 (Plattform) oder Teil des Servers (§3)?

**P9 — Der Datenzweig hat eine unbeantwortete Bitte von 2026-11-02.**
`data/anforderungen.md` §6 Nr. 4: „**bitte bestätigen oder verwerfen**" für *kein eigenes
`person/`-Verzeichnis* (Begründung: JSContact-Card mit Rolle `individual` + `sub` aus `login/` +
`profile/` decken die Person ab, `person/` wäre eine Projektion ohne eigene Daten). Dazu zwei
offene Haken in §7: **App-Dateninventur → Zuordnung in Domänen** und **`identity/mapping.md`**.
Alle drei sind billig und sind direkter Zulauf zu P3.

**P10 — Braucht `data/` einen Prüfer?**
Komponenten haben einen (`check_components.py`, läuft in CI), der Datenzweig nicht. Muster:
`scripts/data/check_data.py` zählt und meldet — Felder ohne Pate (heute: `visibility`, `roles`,
`permissions`, `scopes` in `felder.md` Zeile 17, ⚠️), Modelle, die nicht in der `index.md`-Tabelle
stehen, Domänen ohne Pflichtdateien. Damit wird „kein Pate gefunden" eine **Zahl, die sinken
muss**, statt eines Satzes.

**P11 — `en/`: Beschluss 5 oder Bestand?**
Komponenten-Plan, Beschluss 5: „englische Spiegelung erst nach Abschluss der deutschen Version".
`docs/en/components/` mit 355 Dateien liegt trotzdem schon da und ist **nicht committet**.
Dazu die 9 defekten Links in `en/` aus `todo/qwen.md`. Drei Möglichkeiten: committen und
mitpflegen, weg und am Ende neu, oder als Stand der Dinge committet lassen. Entschieden werden
muss es, sonst übersetzt der Übersetzer gegen eine Wand.

**P12 — Wo entsteht der Code?**
In `temp/` steht nichts über Code-Repos (nachgesehen). CONVENTIONS §1 sagt nur: gleiche Schale in
jedem Repo, Code-Repos ohne Doku. §3 („ein Server, einmal installiert") und §5 („ein geteilter
Crate für die Regeln") deuten auf mindestens zwei Repos: einer für Server/Plattform-Crates, einer
für die Grundmaske. Namen und Grenze wären vor der Grundmaske zu nennen — sonst entsteht das
dritte Repo nebenbei.

**Reihenfolge, die der Agent vorschlagen würde** (nur Vorschlag, Entscheidung liegt beim Nutzer)

1. P1 klären (eine Zeile), dann P2 — ohne Abbruchkriterium ist der Rest des Plans nicht
   bezahlbar.
2. P4 und P5–P7: Manifest, Fähigkeitenliste, Adressform. Das ist der engste Pfad zur
   Grundmaske und unabhängig von Variante A/B (§18 Nr. 1) und von Turso (Nr. 2).
3. P3 und P9: Ort für die abgeleiteten Listen, dazu die drei billigen Datenzweig-Erledigungen.
4. Der Datenzweig-Kram (§18 Nr. 16–19, Grabsteine, `sequence`) kann bis nach der Grundmaske
   warten — **außer** P7, weil die Adresse in der Maske schon benutzt wird.

## 20. Antworten des Nutzers auf §19 (vierte Runde, 2026-11-03)

Der Nutzer hat P1–P6 beantwortet; P8–P12 bleiben offen. Die Antworten sind hier
festgehalten, das Beschlossene steht als ADR in `conventions/decisions/`.

**P1 — der Haken** ✅ geklärt: `[x]` heißt **verifiziert** — die Programme wurden noch mal
überprüft und das Projekt ist dadurch konkreter geworden (Beispiel: Google arbeitet kaum nach
Standards, macht sein eigenes Ding; OSS versucht Standards zu stützen, die großen proprietären
kaum oder dagegen — OOXML). Die Skin-Dokus sind kein Selbstzweck, sondern ein **Spiegel**: wer
macht was, wie, und wo liegt das gesellschaftliche Problem. `[x]` heißt: nicht nur eben etwas
gemacht, sondern die Daten besser überprüft. → ADR 0006; Plan-Legende in `temp/apps-plan.md`
(komplette Pfade, 520 erhaltene Dateien als `[~]` markiert).

**P2 — Abbruchkriterium** ✅: **mindestens 3 Projekte/Masken** pro Kategorie, dann reicht die
Datenbasis, um anzufangen. Ablauf pro Kategorie: Daten sammeln → **zuerst Standards suchen, die
das Bild abbilden (Muss, absolute Priorität)** → dann Crates suchen, die das tragen → dann 3
Programme zum Nachbauen aussuchen: **2 nicht-OSS, 1 OSS** (kann variieren). Begründung: Für OSS
gibt es schon genug; nachgebaut werden die Programme, die **Standards setzen und nicht offen für
OSS sind**. Suiten und Plattformen werden vorab auf Apps heruntergerechnet (stabile Basis), dann
wird aus Apps der Baukasten nach oben zusammengesetzt. → ADR 0006

**P3 — Ort der Pflichtmenge** ✅: **pro Programmkategorie eine fast leere Datei** — dort landet
später, was unser Programm kann und braucht (Beispiel messages). Reihenfolge bis zum Programm:
UI-Härtung über Blinc (erste visuelle Anlaufstelle) → Daten + Standards (erste Anlaufstelle für
„was brauchen wir") → Crates → erst dann am Programm arbeiten. → Ort: `requirements.md` pro
Kategorie unter `programs/<ebene>/<kategorie>/`; Muster vorgearbeitet in
`temp/ableitungen/calendar-requirements.md`.

**P4 — Brückenprinzip** ✅: von **zwei Seiten** bauen — Aussehen/Ideen von oben (vorhandene
Programme kopieren), Daten + Standardisierung von unten; in der Mitte treffen sich
Toleranzen und Erweiterungen (das Mehr, das ein einzelnes Programm nicht hat). Umwerfen und
Verändern ist bei der Planung erlaubt. → Vorgehen steht in ADR 0006.

**P5 — Manifest:** vom Nutzer abgeleitet aus dem Gesamtanliegen, hier festgehalten (dem Manifest
vorangestellt als Erklärung):

> Die Idee ist, eine Software zu schreiben, die frei ist, sehr viele Möglichkeiten schafft, schnell
> ist (Rust), und die Menschen dort abholt, wo sie sind. Menschen interessiert nicht, ob es eine
> API gibt oder ob OOXML oder ODF gespeichert wird — sie wollen das, was sie gelernt haben,
> dorthin klicken, wo sie wollen, und ein Ergebnis haben. Wenn wir Standards setzen, die andere
> nachprogrammieren können, ist es gleich, ob mein Programm oder ein anderes benutzt wird. Es muss
> weder auf Geld noch auf Downloads programmiert werden: Es kann Software geben, bei der egal ist,
> ob sie benutzt wird — aber Menschen können sich, wenn sie wollen, selbst einbringen. Die Großen
> haben viele Möglichkeiten, Menschen auszubeuten, Armut und Diskriminierung auszunutzen, und Macht
> und Geld immer im Vorteil; Menschen, die ausgegrenzt werden, sollen ebenso sicher, schnell und
> anständig arbeiten können. Kleine Vereine können mitmachen und aus Kleinem etwas Großes machen.
> Einfachheit stellt den Menschen in den Vordergrund, nicht umgekehrt. Niemand sollte darüber
> nachdenken müssen, ob es klappt, ob Software zu teuer ist oder in welchem Format gespeichert
> wird: Wenn ich eine Datei erstelle, gebe ich sie dem Programm direkt — statt „wird in ODF
> wird“, oder „für Word geschrieben“ zu schreiben, sage ich, für welches Programm sie ist.
> Entlastung der KIs: das Rad nicht neu erfinden — einmal gemacht, können alle es sofort nutzen.
> Deshalb freie Lizenz. Mir ist egal, wer weiterentwickelt: Software, KI, Menschen sind frei, es zu
> nutzen — und wiederzuverwenden. Macht es jemand besser? Ein Baustein wird verändert, alles
> funktioniert besser.

⚠️ **Konflikt, Entscheidung nötig:** Dieser Text sagt **MIT** („Deshalb MIT Lizenz“), repo und
Website sagen **Apache 2.0** (`LICENSE`, README-Badge, `docs/de/index.md`). Beide sind
permissiv; Apache 2.0 bringt eine ausdrückliche Patenterteilung und Namensschutz, MIT ist kürzer.
Eine Zeile reicht: MIT **oder** Apache 2.0.

**P6 — Fähigkeitenliste: beides** ✅: die Liste wird **zentral dokumentiert** (geschlossen als
Kern, erweiterbar) und ist **abfragbar über API, CLI, MCP** — Standard versteht sich. Damit kann
das Register auflösen und der Masken-Prüfer (§13) feststellen, dass eine Maske eine Fähigkeit
nicht anbietet. → Muster vorgearbeitet in `temp/ableitungen/faehigkeiten.md` (Begriffsschicht +
Ablauf + offene Punkte; keine fertige Liste).

**Aus der Antwort P2 neu — Umbau der Doku (2026-11-03):**

- **`skins/` → `masks/`** (Unterordner unter `programs/<ebene>/<kategorie>/`). Der Begriff
  „Maske" (§2) trägt die Doku; Skin bleibt nur als historische Notiz in Altdaten.
- **Englisch zuerst**: `en/` ist die erste Sprache der Doku (Weitergabe an Dritte), `de/` zweite.
  Der Textverkehr bleibt deutsch. `de/`-Bestand wird mitgezogen, beide Sprachen möglichst gleich
  halten. Das
  kehrt `data/anforderungen.md` §1 und ADR-0002-Folge um; die 355 uncommitteten `en/components/`-
  Dateien (P11) sind damit Bestand, nicht Ballast — **empfohlen: committen**.
- **Blinc ist gesetzt** (GUI.md-Fazit „Hauptfavorit" + Nutzerentscheid): jetzt abgleichen, was die
  84 Komponenten in Blinc können und wie das echte Usage aussieht. → neue Dokuseite
  `programs/platform/crates/blinc.md` + Todo-Liste.
- **Mehr Programme** werden gebraucht — der Plan ist offen, Kategorien wachsen.

## Siehe auch

- `conventions/CONVENTIONS.md` §2 (sechs Ebenen), §3 (Components-Zuordnung)
- `conventions/decisions/0001` … `0005`
- `data/index.md`, `data/modelle.md`, `data/felder.md`, `data/mappings.md`, `data/api.md`,
  `data/formate.md`, `data/standards.md`
- `interactions/gestures/index.md`
- `temp/apps-plan.md`, `temp/components-konzept-und-plan.md`, `temp/apps-prompt-vorlage.md`
- `todo/qwen.md` (offene Struktur-Aufgaben, u. a. defekte Links in `en/`)

Normen, die in §15–§17 neu belegt wurden (noch nicht in `data/standards.md` eingetragen —
nachziehen, wenn ein Punkt daraus in `docs/` wandert): RFC 9110 (409/412, `If-Match`),
RFC 5546 iTIP §5.3 (Fassungszähler), RFC 8620 JMAP (`state`, `ifInState`, `stateMismatch`),
AS2 `Tombstone`/`Group`/`Offer`/`audience`, ActivityPub §6.4 (Grabstein, 410 Gone),
ODRL Information Model.
