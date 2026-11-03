# Architektur-Protokoll — Maske, Programm, Daten

Arbeitsdatei. **Nicht veröffentlicht** (Plan und Entwurf, siehe `conventions/CONVENTIONS.md` §1).
Zweck: Was in den Gesprächen ab dem 2026-11-03 feststeht, ist hier festgehalten, damit es nicht
wieder gefragt und wieder beantwortet werden muss. Wenn ein Punkt aus diesem Blatt in `docs/`
oder in einen ADR wandert, bleibt er hier stehen und bekommt einen Verweis.

Stand: 2026-11-03 · Quelle: Gespräch Nutzer ↔ Agent (Kalender-Fall → Masken-Modell → Datenhaltung)

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
  „Standards" und wäre gewonnen statt erfunden. **Inhaltlich noch nicht gelesen** — muss vor
  der Abbildung belegt werden.
- **Kopie oder Verweis?** Zwei mögliche Grundformen, beide brauchbar:

  | Form | Verhalten | Preis |
  |------|-----------|-------|
  | **Kopie mit Herkunft** | Arbeitskopie in der eigenen DB, offline nutzbar | kann veralten, braucht Abgleich |
  | **Live-Verweis per IRI** | immer aktuell | Gegenstelle muss erreichbar sein |

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

## 15. Offene Fragen

Nummeriert, damit Antworten hier eingetragen werden können.

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
6. **Kopie mit Herkunft** oder **Live-Verweis** als Grundform des Teilens (§8)? Wandern
  `Revision/Version` pro geteiltem Objekt mit?
7. Wird **ODRL** als Pate für Umgangsregeln angenommen? Inhaltlich noch nicht gelesen.
8. **Zeiger- und Eingabezweig** (Maus, Tastatur, Stift) neben den Touch-Gesten: eigene Familie
  oder Querschnitt durch alle Familien (§12)?
9. Gehört die **Kommandoliste** pro Programm in `docs/`? Wohin — eigene Datei neben
  `menu.md`/`features.md`, oder ein neuer Zweig?
10. **Datenanschluss pro Component** (§10): eigene Tabelle in `attributes.md` oder eigene Datei?

## Siehe auch

- `conventions/CONVENTIONS.md` §2 (sechs Ebenen), §3 (Components-Zuordnung)
- `conventions/decisions/0001` … `0005`
- `data/index.md`, `data/modelle.md`, `data/felder.md`, `data/mappings.md`, `data/api.md`,
  `data/formate.md`, `data/standards.md`
- `interactions/gestures/index.md`
- `temp/apps-plan.md`, `temp/components-konzept-und-plan.md`
